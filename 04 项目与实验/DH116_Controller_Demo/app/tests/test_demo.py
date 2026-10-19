"""Offline distribution tests. No vendor DLL or USB is ever loaded."""
import contextlib
import csv
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from app import main as demo
from app.mock_backend import DemoMockBackend
from app.runtime import RollingText, DemoRecorder
from app.setup_check import check_environment


class Clock:
    def __init__(self):self.now=0.
    def monotonic(self):return self.now
    def sleep(self,value):self.now+=max(.001,value)


class DemoTests(unittest.TestCase):
    def execute(self,lines,*,fault=None,debug=False):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup)
        root=Path(temp.name)
        shutil.copytree(ROOT/'config',root/'config')
        answers=iter(lines);prompts=[];output=io.StringIO();backend=DemoMockBackend(fault)
        def answer(prompt):prompts.append(prompt);return next(answers)
        clock=Clock()
        with patch('time.monotonic',clock.monotonic),patch('time.sleep',clock.sleep):
            result=demo.main(['--mock']+(['--debug'] if debug else []),input_fn=answer,
                             output=output,root=root,backend_factory=lambda:backend)
        return result,output.getvalue(),prompts,backend,root

    def test_all_commands_one_session_dynamic_speed_and_cleanup(self):
        lines=['500','YES','HELP','M1 5','M2 3','M3 10','M4 8','M5 5','M6 5',
               'SPEED 1000','M3 30','POSE M6=15 M1=20 M2=10 M3=40 M4=30 M5=20',
               'ALL 10','STATUS','RETURN','EXIT']
        code,text,prompts,b,root=self.execute(lines)
        self.assertEqual(code,0,text)
        self.assertEqual((b.scans,b.opens,b.initializations),(1,1,1))
        self.assertEqual(sum(p.startswith('SPEED:') for p in prompts),1)
        self.assertEqual(sum('YES' in p for p in prompts),1)
        moves=[c for c in b.calls if c[0]=='move']
        self.assertTrue(all(c[3]==500 for c in moves[:6]))
        self.assertTrue(all(c[3]==1000 for c in moves[6:]))
        self.assertFalse(any(c[0]=='broadcast_move' for c in b.calls))
        self.assertTrue(all(v==0 for v in b.positions.values()))
        self.assertEqual(b.calls[-3:],[('stop',0),('disable',0),('close',)])
        self.assertIn('模拟',text);self.assertIn('当前速度：1000',text)
        for internal in ('SDK_ANGLE_LIMITS','DISPATCH','run_id','FEEDBACK_COMPLETE','"hand_model"','SESSION_COMPLETE'):
            self.assertNotIn(internal,text)
        events=list((root/'.runtime/logs').glob('*/events.jsonl'))
        self.assertEqual(len(events),1)
        data=[json.loads(line) for line in events[0].read_text(encoding='utf-8').splitlines()]
        self.assertTrue(any(e['event']=='session_speed_changed' for e in data))
        self.assertEqual([e['velocity'] for e in data if e['event']=='session_speed_applied'],[c[3] for c in moves])

    def test_invalid_speed_angle_and_batch_never_dispatch_partial_motion(self):
        code,text,prompts,b,_=self.execute(['','abc','0','-1','nan','65536','500','YES',
            'M3 -1','M3 nan','M9 1','POSE M1=5 M6=999','ALL 999','SPEED 0','SPEED abc','SPEED','M3 7.5','EXIT'])
        self.assertEqual(code,0,text)
        self.assertEqual(b.angle_commands,[{3:7.5}])
        self.assertIn('输入',text);self.assertEqual(sum(p.startswith('SPEED:') for p in prompts),7)

    def test_stop_exit_eof_and_keyboard_interrupt_cleanup(self):
        for end in ('STOP','EXIT',None):
            with self.subTest(end=end):
                code,text,_,b,_=self.execute(['500','YES','M3 10']+([end] if end else []))
                self.assertEqual(code,0,text)
                self.assertEqual(b.calls[-3:],[('stop',0),('disable',0),('close',)])
                self.assertEqual(b.angle_commands,[{3:10.}])

    def test_keyboard_interrupt_while_waiting_command_still_cleans_up(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);shutil.copytree(ROOT/'config',root/'config')
            backend=DemoMockBackend();answers=iter(['500','YES','M3 10']);output=io.StringIO();clock=Clock()
            def answer(_):
                try:return next(answers)
                except StopIteration:raise KeyboardInterrupt()
            with patch('time.monotonic',clock.monotonic),patch('time.sleep',clock.sleep):
                result=demo.main(['--mock'],input_fn=answer,output=output,root=root,backend_factory=lambda:backend)
            self.assertNotEqual(result,0)
            self.assertEqual(backend.calls[-3:],[('stop',0),('disable',0),('close',)])

    def test_alarm_communication_and_timeout_stop_remaining_commands(self):
        for fault in ('alarm','communication','timeout'):
            with self.subTest(fault=fault):
                code,text,_,b,root=self.execute(['500','YES','M3 30','M4 20','EXIT'],fault=fault)
                self.assertNotEqual(code,0);self.assertEqual(b.angle_commands,[{3:30.}])
                self.assertEqual(b.calls[-3:],[('stop',0),('disable',0),('close',)])
                self.assertIn('未完成',text);self.assertNotIn('设备已经安全停止',text)
                self.assertTrue((root/'.runtime/logs/diagnostic.log').exists())

    def test_failed_stop_is_visible_not_reported_as_success(self):
        code,text,_,b,_=self.execute(['500','YES','M3 10','EXIT'],fault='stop_failure')
        self.assertNotEqual(code,0)
        self.assertIn('停止未确认',text)
        self.assertEqual(b.calls[-2:],[('disable',0),('close',)])

    def test_debug_only_shows_internal_output_when_requested(self):
        code,text,_,_,_=self.execute(['500','YES','M3 10','EXIT'],debug=True)
        self.assertEqual(code,0,text);self.assertIn('SDK_ANGLE_LIMITS',text)

    def test_cancel_before_yes_never_scans_or_opens(self):
        code,text,_,b,_=self.execute(['500','NO'])
        self.assertNotEqual(code,0)
        self.assertEqual((b.scans,b.opens,b.initializations),(0,0,0))
        self.assertNotIn('设备连接成功',text)

    def test_startup_error_never_prints_ready(self):
        code,text,_,b,_=self.execute(['500','YES','EXIT'],fault='no_adapter')
        self.assertNotEqual(code,0)
        self.assertNotIn('控制已就绪',text)
        self.assertFalse(any(c[0]=='move' for c in b.calls))

    def test_default_sdk_missing_has_friendly_message_without_hardware_access(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);shutil.copytree(ROOT/'config',root/'config')
            output=io.StringIO()
            self.assertNotEqual(demo.main([],output=output,root=root,input_fn=lambda _:self.fail('no prompt with missing SDK')),0)
            self.assertIn('SDK',output.getvalue());self.assertIn('vendor',output.getvalue())
            self.assertNotIn('Traceback',output.getvalue())


class DistributionTests(unittest.TestCase):
    def test_public_example_requires_private_config_for_real_devices(self):
        self.assertFalse((ROOT/'config/device.json').exists())
        self.assertEqual(json.loads((ROOT/'config/device.example.json').read_text(encoding='utf-8'))['adapter_serial'],'SET_YOUR_ADAPTER_SERIAL')
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);shutil.copytree(ROOT/'config',root/'config')
            with self.assertRaises(demo.LocalConfigurationError):demo.load_device_configuration(root)
            data=json.loads((root/'config/device.example.json').read_text(encoding='utf-8'))
            local=root/'config/device.local.json';local.write_text(json.dumps(data),encoding='utf-8')
            with self.assertRaises(demo.LocalConfigurationError):demo.load_device_configuration(root)
            data['adapter_serial']='LOCAL_TEST_ADAPTER'
            local.write_text(json.dumps(data),encoding='utf-8')
            self.assertEqual(demo.load_device_configuration(root).adapter_serial,'LOCAL_TEST_ADAPTER')
            self.assertEqual(demo.load_device_configuration(root,mock=True).adapter_serial,'MOCK-ADAPTER')

    def test_public_files_have_no_device_identifiers_or_absolute_machine_paths(self):
        import re
        patterns=(r'\bF080[0-9A-Fa-f]{12}\b',r'\b\d{20,24}\b',r'[A-Za-z]:\\(?:Robot|Users)\\')
        for folder in ('app','config','licenses','vendor'):
            for path in (ROOT/folder).rglob('*'):
                if path.is_file() and '__pycache__' not in path.parts and path.suffix in ('.py','.json','.txt'):
                    text=path.read_text(encoding='utf-8')
                    for pattern in patterns:self.assertIsNone(re.search(pattern,text),path.relative_to(ROOT).as_posix())

    def test_only_one_readme_and_no_historical_results_or_models(self):
        self.assertEqual(list(ROOT.glob('README.md')),[ROOT/'README.md'])
        self.assertFalse((ROOT/'experiments').exists());self.assertFalse((ROOT/'DH116_official_docs').exists())
        for suffix in ('*.stl','*.STL','*.mjcf','*.urdf','*.zip','*.7z','*.dll'):
            self.assertEqual(list((ROOT/'vendor').rglob(suffix)),[])

    def test_batch_paths_quoted_relative_and_missing_python_guarded(self):
        launch=(ROOT/'启动控制.bat').read_text(encoding='utf-8-sig')
        setup=(ROOT/'首次安装.bat').read_text(encoding='utf-8-sig')
        self.assertIn('cd /d "%~dp0"',launch);self.assertIn(r'.venv\Scripts\python.exe',launch)
        self.assertIn('首次安装.bat',launch);self.assertIn('pause',launch)
        self.assertIn('where py',setup);self.assertIn('where python',setup)
        for text in (launch,setup):self.assertNotIn('dh116_dev',text);self.assertNotIn('runas',text)

    def test_environment_check_is_static_and_errors_are_specific(self):
        self.assertIn('Python',check_environment(ROOT,version=(3,9),bits=64,system='Windows')[0])
        self.assertIn('64',check_environment(ROOT,version=(3,11),bits=32,system='Windows')[0])
        self.assertIn('Windows',check_environment(ROOT,version=(3,11),bits=64,system='Linux')[0])
        errors=check_environment(ROOT,version=(3,11),bits=64,system='Windows')
        self.assertTrue(any('SDK' in message for message in errors))
        self.assertTrue(any('ARM64' in message for message in check_environment(ROOT,version=(3,11),bits=64,system='Windows',machine='ARM64')))

    def test_non_x64_sdk_dll_rejected_without_loading_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);dll=root/'vendor/sdk/bin/LHandProLib.dll';dll.parent.mkdir(parents=True)
            dll.write_bytes(b'not a DLL')
            errors=check_environment(root,version=(3,11),bits=64,system='Windows',machine='AMD64',check_dependencies=False)
            self.assertTrue(any('不是有效的Windows x64' in message for message in errors))

    def test_log_size_rotation_bounded_and_lines_remain_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'raw.jsonl';stream=RollingText(path,max_bytes=160,backups=2)
            for i in range(80):stream.write(json.dumps({'i':i,'payload':'A'*40})+'\n')
            stream.close()
            files=list(path.parent.glob('raw.jsonl*'))
            self.assertLessEqual(len(files),3)
            for file in files:
                self.assertLessEqual(file.stat().st_size,160)
                for line in file.read_text(encoding='utf-8').splitlines():json.loads(line)

    def test_csv_rollover_keeps_headers_and_runtime_hidden_attribute(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            from app.runtime import hidden_logs
            logs=hidden_logs(root)
            if sys.platform=='win32':
                import ctypes
                self.assertTrue(ctypes.windll.kernel32.GetFileAttributesW(str(root/'.runtime'))&2)
            path=logs/'samples.csv';stream=RollingText(path,max_bytes=100,backups=2,header='motor,angle\r\n')
            stream.write('motor,angle\r\n');writer=csv.writer(stream)
            for i in range(30):writer.writerow([i,10.0])
            stream.close()
            for file in logs.glob('samples.csv*'):
                with file.open(encoding='utf-8',newline='') as rows:
                    reader=csv.DictReader(rows)
                    self.assertEqual(reader.fieldnames,['motor','angle'])

    def test_source_modules_are_loaded_from_this_distribution_only(self):
        import dh116_dev,controller
        for module in (dh116_dev,controller):
            self.assertTrue(Path(module.__file__).resolve().is_relative_to(ROOT/'app/_engine'))

    def test_completed_run_retention_is_bounded(self):
        from dh116_dev.models import DeviceConfig
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for _ in range(8):
                record=DemoRecorder(root,DeviceConfig(),root/'absent.dll')
                record.finish('MOCK_ONLY',[])
            completed=[path for path in (root/'.runtime/logs').iterdir() if path.is_dir()]
            self.assertEqual(len(completed),5)

    def test_readme_commands_match_actual_entry(self):
        help_text=subprocess.run([sys.executable,'-I',str(ROOT/'app/main.py'),'--help'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertIn('--mock',help_text);self.assertIn('--debug',help_text)
        for command in ('POSE','ALL','RETURN','STATUS','SPEED','HELP','STOP','EXIT'):
            self.assertIn(command,readme)
        self.assertEqual(readme.count('```')%2,0)

    def test_copy_to_unrelated_directory_and_run_without_original_pythonpath(self):
        with tempfile.TemporaryDirectory(prefix='DH116 独立复制 ') as tmp:
            moved=Path(tmp)/'控制 Demo'
            shutil.copytree(ROOT,moved,ignore=shutil.ignore_patterns('.venv','.runtime','__pycache__'))
            result=subprocess.run([sys.executable,'-I',str(moved/'app/main.py'),'--mock'],cwd=Path(tmp),
                input='500\nYES\nM3 10\nSPEED 1000\nM5 5\nRETURN\nEXIT\n',capture_output=True,text=True,encoding='utf-8',timeout=30)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertIn('模拟',result.stdout);self.assertIn('当前速度：1000',result.stdout)
            self.assertNotIn('DISPATCH',result.stdout)
            self.assertTrue((moved/'.runtime/logs').exists())


if __name__=='__main__':unittest.main()
