"""Clean Chinese UI over the existing, unchanged SDK control sequence."""
from pathlib import Path
import sys
for _stream in (sys.stdin,sys.stdout,sys.stderr):
    if hasattr(_stream,'reconfigure'):
        _stream.reconfigure(encoding='utf-8')
if __package__ in (None,''):
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
sys.dont_write_bytecode=True

import argparse
import contextlib
from dataclasses import replace
import json
import os
import traceback

from app import bootstrap
from app.runtime import DemoRecorder, DiagnosticStream, hidden_logs
from app.setup_check import check_environment
from controller import angle_cli as angle, coordinated_live as session, safety
from dh116_dev.cli import _lhandpro_running
from dh116_dev.models import DeviceConfig
from dh116_dev.sdk_reader import VendorBackend

NAMES={1:'拇指侧摆',2:'拇指屈曲',3:'食指屈曲',4:'中指屈曲',5:'无名指屈曲',6:'小指屈曲'}
_DLL_DIRECTORIES=[]


class LocalConfigurationError(ValueError):
    pass


def load_device_configuration(root,*,mock=False):
    """Public example contains no device serial; real settings stay ignored."""
    root=Path(root)
    path=root/'config'/('device.example.json' if mock else 'device.local.json')
    if not path.is_file():
        raise LocalConfigurationError('请将 config/device.example.json 复制为 config/device.local.json，填写本机适配器序列号后再运行；此本地文件不会上传GitHub。')
    try:
        values=json.loads(path.read_text(encoding='utf-8'))
        if mock:values['adapter_serial']='MOCK-ADAPTER'
        serial=values.get('adapter_serial')
        if not isinstance(serial,str) or not serial.strip() or (not mock and serial.startswith(('SET_','CONFIGURE_','MOCK-'))):
            raise ValueError('adapter serial has not been configured')
        return DeviceConfig(**values)
    except (ValueError,TypeError,KeyError) as error:
        raise LocalConfigurationError('config/device.local.json 配置未完成或格式不正确，请按README填写本机参数；未连接设备。') from error


def configure_vendor(root):
    """Library search paths only; never loads the SDK or opens an adapter."""
    folders=[root/'vendor/sdk/bin']
    try:
        import libusb_package
        library=libusb_package.get_library_path()
        if library:folders.append(Path(library).parent)
    except ImportError:pass
    for folder in folders:
        os.environ['PATH']=str(folder)+os.pathsep+os.environ.get('PATH','')
        if os.name=='nt' and folder.is_dir():_DLL_DIRECTORIES.append(os.add_dll_directory(str(folder)))


def friendly_error(error):
    if isinstance(error,LocalConfigurationError):return str(error)
    text=str(error).lower()
    if any(token in text for token in ('alarm','报警')):return '电机报警，后续动作已取消。'
    if any(token in text for token in ('timeout','feedback','fresh','communication','通讯','connectionerror')):return '设备通信或反馈异常，动作未确认完成。'
    if any(token in text for token in ('adapter','usb','device not found')):return '未找到可用CANFD适配器，或适配器被占用；请检查供电、接线和WinUSB驱动。'
    if any(token in text for token in ('dll','winerror 126','vcruntime','msvcp')):return 'SDK或运行库不可用，请检查厂家SDK及Microsoft x64运行库。'
    if 'approval' in text:return '未输入YES，本次操作已取消，未授权连接和运动。'
    if 'lhandpro' in text:return '请完全退出LHandPro后再启动，当前未继续连接。'
    if 'stopiteration' in text or 'eoferror' in text:return '输入已结束。'
    return '控制流程未完成，后续动作已取消；请查看内部诊断记录。'


class DemoConsole(angle.AngleConsole):
    def __init__(self,*args,notify,**kwargs):
        super().__init__(*args,**kwargs);self.notify=notify
    def initialize_limits(self,motion):
        super().initialize_limits(motion)
        self.notify('设备连接成功，初始化完成。正在准备六轴HOME，请留意活动空间。')
    def help(self):
        self.notify('\n========================================\n           角度控制菜单\n========================================')
        for axis,name in NAMES.items():self.notify(f'M{axis}  {name}')
        self.notify('输入示例：M3 30、M4 20、M1 15\nSPEED 300  修改后续运动速度\nPOSE M1=20 M3=30  多轴不同角度，逐轴执行\nALL 10     六轴统一角度，逐轴执行\nRETURN     六轴依次返回零角度目标\nSTATUS     六轴状态\nHELP       帮助\nSTOP       软件停止并退出\nEXIT       停止、断使能、关闭并退出')
        self.notify(f'当前速度：{self.velocity} {angle.SDK_POSITION_VELOCITY_UNIT}')
    def status(self,sample):
        self.notify(f'当前速度：{self.velocity} {angle.SDK_POSITION_VELOCITY_UNIT}')
        for motor in sample.motors:
            self.notify(f'M{motor.motor_id} {NAMES[motor.motor_id]}：角度 {motor.now_angle_deg:.3f}°，位置 {motor.now_position}，目标 {motor.target_position}，状态 {motor.status}，报警 {motor.alarm}')
    def _read(self,capture):
        while True:
            line,sample=super()._read(capture)
            fields=line.strip().upper().split()
            if fields and fields[0]=='SPEED':
                if len(fields)!=2:
                    self.notify('修改速度请输入 SPEED 300（正整数，位置计数/秒）。');continue
                try:speed=angle.parse_speed(fields[1])
                except ValueError as error:
                    self.notify('速度未修改：'+str(error));continue
                old=self.velocity
                # This executes in the monitoring/control thread, not the
                # keyboard thread. Only later stages consult this value.
                self.recorder.event('session_speed_changed',before=old,after=speed,
                    unit=angle.SDK_POSITION_VELOCITY_UNIT,affects='SUBSEQUENT_COMMANDS_ONLY')
                self.velocity=speed
                self.notify(f'当前速度：{speed} {angle.SDK_POSITION_VELOCITY_UNIT}')
                continue
            return line,sample
    def stages(self,capture,baseline):
        self.notify('\n当前六轴角度控制已就绪。输入 HELP 可查看用法。')
        yield from super().stages(capture,baseline)


def main(argv=None,*,input_fn=input,output=None,root=None,backend_factory=None):
    parser=argparse.ArgumentParser(description='DH116右手简洁控制台；默认真机，连接与HOME前必须输入YES')
    parser.add_argument('--mock',action='store_true',help='纯模拟，不加载SDK、不连接USB')
    parser.add_argument('--debug',action='store_true',help='额外显示内部诊断输出')
    parser.add_argument('--check',action='store_true',help='仅做安装静态检查，不连接设备')
    args=parser.parse_args(argv)
    root=Path(root or bootstrap.ROOT).resolve();output=output or sys.stdout
    def notify(text):output.write(str(text)+'\n');output.flush()
    notify('========================================\n       DH116 灵巧手控制系统\n========================================\n设备：DH116 Right Hand\n控制方式：六轴自定义角度与速度')
    if args.mock:notify('【模拟模式】所有范围和反馈均为合成数据，不连接真实设备。')
    if args.check or not args.mock:
        errors=check_environment(root)
        if errors:
            for error in errors:notify(error)
            notify('请先按README补齐文件并执行“首次安装.bat”；未连接设备。')
            return 2
        if args.check:
            notify('文件与Python环境静态检查通过，未连接设备。');return 0
    if backend_factory is not None and not args.mock:
        notify('外部测试后端仅用于 --mock。');return 2
    def read(prompt):
        if 'Type YES' in prompt or 'authorize' in prompt:
            prompt='六轴HOME可能经过较大行程；请确认空间、供电和独立停机条件。会话允许修改SPEED。输入 YES 开始：'
        elif 'angle>' in prompt:prompt='DH116 > '
        output.write(prompt);output.flush()
        return input_fn('' if input_fn is input else prompt)
    recorder=None;diagnostic=None
    try:
        logs=hidden_logs(root)
        diagnostic=DiagnosticStream(logs/'diagnostic.log',output,debug=args.debug,notice=notify)
        with contextlib.redirect_stdout(diagnostic),contextlib.redirect_stderr(diagnostic):
            mapping=angle.load_mapping(root/'config/angle_control.json')
            config=load_device_configuration(root,mock=args.mock)
            notify('\n请输入运动速度 SPEED：')
            while True:
                try:text=read('SPEED: ')
                except (EOFError,StopIteration):notify('已取消，未连接设备。');return 2
                try:speed=angle.parse_speed(text);break
                except ValueError as error:notify('速度输入无效：'+str(error))
            notify(f'当前速度：{speed} {angle.SDK_POSITION_VELOCITY_UNIT}')
            if not args.mock and _lhandpro_running():raise RuntimeError('LHandPro is running')
            plan=angle.build_angle_plan(mapping,velocity=speed)
            plan=replace(plan,amplitude_context=dict(plan.amplitude_context,interactive_speed_updates=True))
            def event_notice(name,fields):
                if name=='sdk_command_started' and fields.get('command')=='home_all':notify('正在执行六轴HOME回零...')
                if name=='angle_axis_dispatch_requested':
                    axis=fields['motor_id'];notify(f'\nM{axis} {NAMES[axis]}\n目标角度：{fields["requested_angle"]:g}°\n当前速度：{console.velocity}\n正在运动...')
                if name=='angle_sequence_started' and len(fields.get('motor_order',[]))>1:notify('按电机编号逐轴执行，每轴等待反馈；不是同步运动。')
                if name=='angle_feedback_complete':
                    for motor in fields['motors']:notify(f'完成（SDK反馈）：M{motor["motor_id"]} 当前角度 {motor["now_angle_deg"]:.3f}°')
            dll=root/'vendor/sdk/bin/LHandProLib.dll'
            recorder=DemoRecorder(root,config,dll,notice=event_notice)
            recorder.set_experiment_metadata(mode='MOCK' if args.mock else 'LIVE',synthetic=args.mock,
                initial_session_speed=speed,position_velocity_policy=angle.SPEED_POLICY,
                application='DH116_Controller_Demo',evidence_scope='SDK_FEEDBACK_ONLY_NOT_PHYSICAL_CALIBRATION')
            approval=safety.collect_motion_session_approval(config,recorder.run_id,plan.as_dict(),input_fn=read)
            console=DemoConsole(mapping,recorder,velocity=speed,input_fn=read,notify=notify)
            if args.mock:
                from app.mock_backend import DemoMockBackend
                factory=backend_factory or DemoMockBackend
            else:
                configure_vendor(root)
                def factory():return VendorBackend(root/'vendor/sdk/python',dll,capture_echo=True)
            notify('正在连接灵巧手...' if not args.mock else '正在建立模拟控制会话...')
            result=session.run_session(config,factory,recorder,plan,approval=approval,
                on_initialized=console.initialize_limits,stage_source=console.stages,
                session_velocity_source=lambda:console.velocity,
                **({'minimum_wait':.5,'home_timeout':3,'move_timeout':3} if args.mock else {}))
            # The original runner has finished/closed its recorder and attempts
            # stop/disable independently even if capture/logging failed.
            recorder=None
            if result.result!='SESSION_COMPLETE_SDK_FEEDBACK_ONLY':
                notify('操作未完成：'+friendly_error(result.error or result.cleanup))
                if any(str(result.cleanup.get(k,'')).startswith(('FAILED','UNCONFIRMED')) for k in ('stop_all','disable_all','stop_confirmation')):
                    notify('停止未确认；请现场确认手部状态，必要时立即使用独立断电。')
                elif result.cleanup.get('stop_all')=='COMPLETED':notify('已执行软件停止、断使能及关闭请求；物理停止仍需现场确认。')
                notify('详细信息已保存在内部诊断记录 .runtime/logs/ 中。')
                return 1
            notify('会话结束，软件停止、断使能与关闭请求已完成；请现场确认机械停止。')
            return 0
    except BaseException as error:
        saved=False
        if diagnostic:
            try:diagnostic.write(traceback.format_exc()+'\n');saved=True
            except OSError:pass
        notify('操作未完成：'+friendly_error(error))
        if saved:notify('详细信息已保存在内部诊断记录 .runtime/logs/ 中。')
        else:notify('诊断记录无法写入；请检查目录权限和磁盘空间。')
        return 2
    finally:
        if recorder:
            try:recorder.finish('CANCELLED_BEFORE_ADAPTER',['No device session was started.'])
            except Exception as error:notify('诊断记录写入失败，请检查目录权限或磁盘空间。')
        if diagnostic:
            try:diagnostic.close()
            except OSError:notify('诊断记录关闭失败，请检查磁盘。')


if __name__=='__main__':raise SystemExit(main())
