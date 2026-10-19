"""Native SDK angle REPL. Default/preview never load a DLL or access a device."""
from __future__ import annotations
import argparse
from ctypes import c_float
from dataclasses import dataclass,field
import hashlib
import json
import math
from pathlib import Path
from queue import Empty,Queue
import re
import sys
from threading import Thread
import time
from typing import Callable

from dh116_dev.logging import RunRecorder
from dh116_dev.state import FeedbackSample
from dh116_dev.motion import (is_sdk_position_velocity, SDK_POSITION_VELOCITY_UNIT,
    SDK_POSITION_VELOCITY_C_INT_MAX, SDK_POSITION_VELOCITY_REPRESENTATION_MAX)
from controller import coordinated_live as live,safety

DEFAULT_MAPPING=live.PROJECT_ROOT/'config/exp05_angle_mapping.json'

SPEED_POLICY={
    'api':'set_position_velocity(id, int velocity)',
    'unit':SDK_POSITION_VELOCITY_UNIT,
    'representation_range':[1,SDK_POSITION_VELOCITY_REPRESENTATION_MAX],
    'c_int_max':SDK_POSITION_VELOCITY_C_INT_MAX,
    'representation_basis':'C int and CANFD two-byte field capacity; not a proven SDK/firmware maximum',
    'actual_device_maximum':'UNKNOWN_NOT_DOCUMENTED',
    'sdk_to_wire_scaling':'NOT_ESTABLISHED_BY_LOCAL_SOURCES',
    'sdk_validation':'Checked setter plus get_position_velocity readback before each MOVE; not physical acceptance',
}


def parse_speed(text):
    value=text.strip()
    if not re.fullmatch(r'[+]?[0-9]+',value):
        raise ValueError('SPEED 必须为正整数，SDK 参数为 int；不接受空值、小数、NaN 或 Infinity')
    try:speed=int(value)
    except ValueError as error:raise ValueError('SPEED 超出可解析整数范围') from error
    if not is_sdk_position_velocity(speed):
        raise ValueError(f'SPEED 必须为 1–{SDK_POSITION_VELOCITY_REPRESENTATION_MAX} 的整数（参数/报文容量保护，非设备已验证范围）')
    return speed


def request_session_speed(input_fn):
    print('请输入本次控制会话的运动速度 SPEED：',flush=True)
    print(f'单位：{SDK_POSITION_VELOCITY_UNIT}；SDK/固件最大速度未明确记载，参数可表示不等于设备已支持。',flush=True)
    while True:
        try:text=input_fn('SPEED: ')
        except (EOFError,StopIteration) as error:raise ValueError('速度输入已取消；未连接设备') from error
        try:speed=parse_speed(text)
        except ValueError as error:print(f'SPEED_REJECTED: {error}',flush=True);continue
        print(f'当前会话速度：{speed} {SDK_POSITION_VELOCITY_UNIT}',flush=True)
        print('速度设置完成，可以输入手指和角度。',flush=True)
        return speed

@dataclass
class AngleMapping:
    data:dict
    runtime_limits:dict=field(default_factory=dict)
    @property
    def enabled(self):return tuple(axis for axis in range(1,7) if self.data['motors'][str(axis)]['enabled'])
    def motor(self,axis):
        if axis not in self.enabled:
            raise ValueError(f'M{axis} 未在本角度会话中启用；不派发运动')
        return self.data['motors'][str(axis)]
    def set_runtime_limits(self,limits):
        if set(limits)!=set(self.enabled):raise ValueError('SDK limits must cover every enabled motor')
        checked={}
        for axis,bounds in limits.items():
            if (not isinstance(bounds,(list,tuple)) or len(bounds)!=2 or
                    any(type(v) not in (int,float) or not math.isfinite(v) for v in bounds) or
                    not bounds[0]<=0<bounds[1]):
                raise ValueError(f'M{axis} SDK limits missing/invalid or incompatible with zero reference: {bounds}')
            checked[axis]=(float(bounds[0]),float(bounds[1]))
        self.runtime_limits=checked
    def angle_range(self,axis):
        self.motor(axis)
        bounds=self.runtime_limits.get(axis)
        return (max(0.,bounds[0]),bounds[1]) if bounds else None
    def assess(self,axis,angle,*,check_limits=True):
        self.motor(axis)
        if not math.isfinite(angle) or not math.isfinite(c_float(angle).value):
            raise ValueError('SDK angle must be finite and representable as C float')
        if angle<0:raise ValueError(f'M{axis} 负角度语义未由本机资料证实，当前不接受负角度')
        bounds=self.angle_range(axis) if check_limits else None
        if bounds is not None and not bounds[0]<=angle<=bounds[1]:
            raise ValueError(f'M{axis} requested={angle:g} deg exceeds SDK get_limit_target_angle range {bounds}; no setter/MOVE sent')
        return {'requested_angle':angle,'sdk_command':f'set_target_angle({axis}, {angle:g})',
                'raw_target':None,'raw_target_source':'SDK_GET_TARGET_POSITION_AFTER_NATIVE_SETTER',
                'live_allowed':True if bounds is not None else None,
                'live_command_range':bounds,'sdk_reported_angle_range':self.runtime_limits.get(axis),
                'reason':'SDK_RUNTIME_LIMITS_CHECKED' if bounds is not None else 'SDK_LIMITS_QUERY_REQUIRED_BEFORE_MOTION'}
    def ranges(self):
        return {f'M{axis}':{'name':m['name'],'enabled':m['enabled'],
            'input_angle_range':'finite nonnegative C float' if m['enabled'] else None,
            'live_command_range':self.angle_range(axis) if m['enabled'] else None,
            'sdk_reported_angle_range':self.runtime_limits.get(axis),
            'range_source':'SDK_RUNTIME_QUERY_REQUIRED' if m['enabled'] else 'DISABLED_PENDING_VALIDATION',
            'historical_feedback_range_not_a_limit':m.get('historical_feedback_range')}
            for axis in range(1,7) for m in [self.data['motors'][str(axis)]]}

def load_mapping(path):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    if (d.get('schema_version')!=3 or d.get('control_mode')!='SDK_NATIVE_ANGLE' or
            d.get('sdk_raw_api_domain')!=[0,10000] or
            set(d.get('motors',{}))!={str(i) for i in range(1,7)} or
            not is_sdk_position_velocity(d.get('velocity_raw_per_second')) or d.get('current_raw')!=1000 or
            type(d.get('angle_feedback_timeout_seconds')) not in (int,float) or
            not math.isfinite(d['angle_feedback_timeout_seconds']) or
            not 0<d['angle_feedback_timeout_seconds']<=2 or not d.get('evidence')):
        raise ValueError('invalid native angle configuration, SDK domain, velocity/current or feedback policy')
    for axis in range(1,7):
        m=d['motors'][str(axis)];enabled=True
        if (type(m.get('enabled')) is not bool or m['enabled']!=enabled or
                not m.get('name') or not m.get('evidence') or
                m.get('input_angle_range') is not None or m.get('negative_angle_supported') is not False or
                m.get('live_command_range')!=('SDK_QUERY' if enabled else None)):
            raise ValueError(f'M{axis} requires native SDK range query; negative-angle control stays disabled')
        if enabled and (type(m.get('sdk_angle_tolerance_deg')) not in (int,float) or
                not math.isfinite(m['sdk_angle_tolerance_deg']) or not 0<m['sdk_angle_tolerance_deg']<=.1):
            raise ValueError(f'M{axis} invalid SDK angle feedback tolerance')
    return AngleMapping(d)

@dataclass(frozen=True)
class Command:
    kind:str
    angles:dict|None=None
    raw_targets:dict|None=None
    assessments:dict|None=None
    sequence:str='SINGLE'

def parse_command(line,mapping,*,check_limits=True):
    fields=line.strip().upper().split()
    if len(fields)==1 and fields[0] in ('RETURN','STATUS','HELP','STOP','EXIT'):return Command(fields[0])
    if fields and fields[0]=='POSE':
        angles={}
        if len(fields)<2:raise ValueError('usage: POSE M1=30 M2=15 M3=45 M4=40 M5=25 M6=20')
        for field in fields[1:]:
            match=re.fullmatch(r'M([1-6])=([^=]+)',field)
            if not match:raise ValueError(f'invalid POSE field: {field}; expected M1=15')
            axis=int(match[1])
            if axis in angles:raise ValueError(f'duplicate POSE motor M{axis}')
            try:angles[axis]=float(match[2])
            except ValueError as error:raise ValueError(f'M{axis} angle must be numeric') from error
        angles=dict(sorted(angles.items()))
        assessments={axis:mapping.assess(axis,value,check_limits=check_limits) for axis,value in angles.items()}
        return Command('ANGLE',angles,None,assessments,'POSE')
    if len(fields)!=2 or (fields[0]!='ALL' and not re.fullmatch(r'M[1-6]',fields[0])):
        raise ValueError('usage: M3 45 | POSE M3=10 M4=8 | ALL 10 | RETURN | STATUS | HELP | STOP | EXIT')
    try:angle=float(fields[1])
    except ValueError as error:raise ValueError('angle must be numeric') from error
    axes=mapping.enabled if fields[0]=='ALL' else (int(fields[0][1:]),)
    assessments={axis:mapping.assess(axis,angle,check_limits=check_limits) for axis in axes}
    return Command('ANGLE',{axis:angle for axis in axes},None,assessments,'ALL' if fields[0]=='ALL' else 'SINGLE')

def display_assessment(command,sample=None):
    states={m.motor_id:m for m in sample.motors} if sample else {}
    for axis,info in command.assessments.items():
        actual=states[axis].now_angle_deg if axis in states else 'UNKNOWN_NOT_CONNECTED'
        eligibility='YES' if info['live_allowed'] else 'UNKNOWN_SDK_QUERY_REQUIRED'
        print(f'M{axis} requested_sdk_angle={info["requested_angle"]:g} sdk_parameter={info["sdk_command"]} '
              f'raw_target=SDK_NATIVE_READBACK actual_sdk_angle={actual} '
              f'live_allowed={eligibility} SDK_ACCEPTED=NOT_YET TARGET_REACHED=UNCONFIRMED',flush=True)

def build_angle_plan(mapping,*,velocity=None):
    axes=mapping.enabled
    domain={axis:10000 if axis in axes else 0 for axis in range(1,7)}
    plan=live.SessionPlan('angle',(
        live.Stage('ANGLE_SESSION_LIMITS',domain,axes),
        live.Stage('CONTROLLED_OPEN_RETURN',dict.fromkeys(range(1,7),0),axes)),
        mapping.data['velocity_raw_per_second'] if velocity is None else velocity,mapping.data['current_raw'],10000,
        requires_step_advance=False,amplitude_context={
            'native_sdk_angle_control':True,
            'position_velocity_policy':SPEED_POLICY,
            'angle_tolerances_deg':{axis:mapping.motor(axis)['sdk_angle_tolerance_deg'] for axis in axes},
            'authorization_scope':'NATIVE_ANGLES_WITHIN_SDK_RUNTIME_LIMITS; NO_AUTOMATIC_CURL',
            'raw_domain_is_not_a_mechanical_limit':True,'configuration':mapping.data})
    live.validate_session_plan(plan);return plan

class AngleConsole:
    def __init__(self,mapping,recorder,*,velocity=None,input_fn:Callable[[str],str]=input):
        self.mapping,self.recorder,self.input_fn=mapping,recorder,input_fn;self.exit_reason=None
        self.velocity=mapping.data['velocity_raw_per_second'] if velocity is None else velocity
        if not is_sdk_position_velocity(self.velocity):raise ValueError('invalid session SPEED')
    def initialize_limits(self,motion):
        self.motion=motion
        limits=motion.read_angle_limits(self.mapping.enabled)
        self.mapping.set_runtime_limits(limits)
        self.recorder.set_experiment_metadata(native_angle_limits=limits,
            native_angle_limits_source='SDK get_limit_target_angle; not independent mechanical certification')
        print('SDK_ANGLE_LIMITS '+json.dumps(self.mapping.ranges(),ensure_ascii=False),flush=True)
    def preflight(self,command):
        """Query every requested limit BEFORE any setter or single-axis MOVE.

        Syntax-only parsing deliberately ignores stale startup limits. Hardware
        errors/invalid SDK limits abort the session; invalid user targets only
        reject this command. Per-axis dispatch rechecks limits again in backend.
        """
        axes=tuple(sorted(command.angles))
        started=time.monotonic()
        limits=self.motion.read_angle_limits(axes)
        if set(limits)!=set(axes):raise RuntimeError('SDK preflight limits incomplete; no command dispatched')
        try:self.mapping.set_runtime_limits(self.mapping.runtime_limits|limits)
        except ValueError as error:raise RuntimeError(f'invalid SDK preflight limits; no command dispatched: {error}') from error
        self.recorder.event('angle_command_limits_queried',motor_order=axes,sdk_limits=limits,
            getter_started_monotonic=started,getter_finished_monotonic=time.monotonic(),
            before_any_setter_or_move=True)
        return Command('ANGLE',command.angles,None,
            {axis:self.mapping.assess(axis,angle) for axis,angle in command.angles.items()},command.sequence)
    def help(self):
        print(f'本会话 SPEED={self.velocity} {SDK_POSITION_VELOCITY_UNIT}；单轴/POSE/ALL/RETURN 共用，HOME速度由原有厂家流程决定。')
        print('M1 30 | M2 15 | M3 45 | M4 40 | M5 25 | M6 20 | M3 7.5 | POSE M3=10 M4=8 | ALL 10 | RETURN | STATUS | HELP | STOP | EXIT')
        print('Native SDK limits govern execution. No historical angle/raw cap or local angle/raw extrapolation.')
        print('POSE/ALL: query ALL requested SDK limits first, then M1 -> M6 in order; wait feedback per motor; NOT synchronous.')
        print('RETURN: M1-M6 individually return to zero; axes already at SDK zero are skipped. Unspecified POSE axes retain targets.')
        print('STOP/EXIT stop, disable, close; no implicit RETURN. SDK internal wire-axis isolation is not proven.')
        for key,info in self.mapping.ranges().items():print(f'{key} {info["name"]}: live SDK range={info["live_command_range"]}; source={info["range_source"]}')
        print('Negative angles remain disabled. SDK angle ranges are not calibrated mechanical safety limits.',flush=True)
    def status(self,sample):
        print(f'STATUS SPEED={self.velocity} {SDK_POSITION_VELOCITY_UNIT} timestamp={sample.timestamp_utc} position_frames={sample.position_frame_count}')
        for m in sample.motors:print(f'M{m.motor_id} now_position={m.now_position} actual_sdk_angle={m.now_angle_deg:.6f} target_position={m.target_position} status={m.status} alarm={m.alarm}')
        print(flush=True)
    def _read(self,capture):
        answers=Queue(maxsize=1)
        def keyboard():
            try:answers.put((True,self.input_fn('DH116 angle> ')))
            except (EOFError,StopIteration):answers.put((True,'EXIT'))
            except BaseException as error:answers.put((False,error))
        Thread(target=keyboard,name='exp05-angle-input',daemon=True).start()
        while True:
            sample=capture()
            try:ok,answer=answers.get_nowait()
            except Empty:time.sleep(.1);continue
            if not ok:raise answer
            return answer,sample
    def _confirm_angles(self,command,capture):
        deadline=time.monotonic()+self.mapping.data['angle_feedback_timeout_seconds']
        while True:
            sample=capture();states={m.motor_id:m for m in sample.motors};missing={}
            for axis,angle in command.angles.items():
                tolerance=self.mapping.motor(axis)['sdk_angle_tolerance_deg']
                actual=states[axis].now_angle_deg
                if not math.isfinite(actual) or abs(actual-angle)>tolerance:
                    missing[axis]={'requested':angle,'actual_sdk_angle':actual,'tolerance':tolerance}
            if not missing:
                for axis,angle in command.angles.items():
                    m=states[axis]
                    print(f'M{axis} requested_sdk_angle={angle:g} sdk_target_raw={m.target_position} actual_raw={m.now_position} '
                          f'actual_sdk_angle={m.now_angle_deg:.6f} SDK_ACCEPTED=YES TARGET_REACHED=YES (SDK_FEEDBACK_ONLY)',flush=True)
                self.recorder.event('angle_feedback_complete',requested_angles=command.angles,
                    raw_source='SDK_NATIVE',sample_utc=sample.timestamp_utc,
                    motors=[vars(states[axis]) for axis in command.angles],physical_angle_calibrated=False)
                return
            if time.monotonic()>=deadline:raise TimeoutError(f'angle feedback mismatch: {missing}')
            time.sleep(.05)
    def stages(self,capture,baseline):
        if not self.mapping.runtime_limits:raise RuntimeError('SDK angle limits must be read before interactive motion')
        self.help();self.status(baseline)
        while True:
            line,sample=self._read(capture);self.recorder.event('angle_console_input',text=line)
            try:cmd=parse_command(line,self.mapping,check_limits=False)
            except ValueError as error:
                print(f'INPUT_REJECTED: {error}',flush=True)
                self.recorder.event('angle_input_rejected',text=line,error=str(error));continue
            if cmd.kind=='HELP':self.help();continue
            if cmd.kind=='STATUS':self.status(sample);continue
            if cmd.kind in ('STOP','EXIT'):
                self.exit_reason=cmd.kind;self.recorder.event('angle_console_exit',reason=cmd.kind,implicit_return=False);return
            returning=cmd.kind=='RETURN'
            if returning:
                cmd=parse_command('ALL 0',self.mapping,check_limits=False)
            try:cmd=self.preflight(cmd)
            except ValueError as error:
                print(f'INPUT_REJECTED: {error}',flush=True)
                self.recorder.event('angle_input_rejected',text=line,error=str(error));continue
            sequence='RETURN' if returning else cmd.sequence
            order=sorted(cmd.angles)
            self.recorder.event('angle_sequence_started',sequence=sequence,motor_order=order,
                requested_angles=cmd.angles,dispatch='PER_AXIS_WAIT_FOR_FEEDBACK_NOT_SYNCHRONOUS',
                requested_motor_ids=order,wire_axis_scope='SDK_MANAGED_NOT_PROVEN_ISOLATED')
            # ALL is a high-level sequence, never move_motors(0). Each axis is
            # confirmed before the next setter/dispatch; an error aborts the rest.
            for ordinal,axis in enumerate(order,1):
                sample=capture();states={m.motor_id:m for m in sample.motors}
                state=states[axis]
                if (returning and state.target_position==0 and abs(state.now_position)<=1 and
                        abs(state.now_angle_deg)<=self.mapping.motor(axis)['sdk_angle_tolerance_deg'] and state.status==0):
                    self.recorder.event('angle_return_no_command',motor_id=axis,reason='SDK_FEEDBACK_ALREADY_AT_ZERO')
                    continue
                angle=cmd.angles[axis]
                single=Command('ANGLE',{axis:angle},None,{axis:cmd.assessments[axis]})
                display_assessment(single,sample)
                held_targets={m.motor_id:m.target_position for m in sample.motors}
                self.recorder.event('angle_command_requested',requested_angles=single.angles,
                    raw_source='SDK_NATIVE_NO_LOCAL_CONVERSION',held_targets_snapshot=held_targets)
                self.recorder.event('angle_axis_dispatch_requested',sequence=sequence,
                    ordinal=ordinal,motor_id=axis,sdk_move_id=axis,requested_angle=angle,
                    dispatch_order=order,physical_synchronization_verified=False)
                yield live.Stage('ANGLE_RETURN' if returning else 'ANGLE_COMMAND',held_targets,
                                 (axis,),angle_targets=single.angles)
                self._confirm_angles(single,capture)
            self.recorder.event('angle_sequence_completed',sequence=sequence,motor_order=order)
            if returning:self.status(capture())
