"""Prevent index refresh from overwriting the hand-written research guide."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT=Path(__file__).with_name("update_data_teleop_index.py")
try:
    spec=importlib.util.spec_from_file_location("data_teleop_index",SCRIPT)
    index=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(index)
except FileNotFoundError:
    index=None

class DataTeleopIndexTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(index,"the single-page index updater is not implemented")

    def note(self,root,pid,title):
        path=root/"03 论文卡片"/"08_数据与遥操作"/(title+".md")
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text("---\npaper_id: "+pid+"\ntitle: "+json.dumps(title,ensure_ascii=False)+"\nvenue: \"arXiv preprint\"\nyear: 2026\n---\n# "+title+"\n\n- 研究主题：手物交互\n",encoding="utf-8")
        return path

    def test_only_managed_region_changes_and_render_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.note(root,"P218","Robot 2.0 - 人类 & Robot")
            source="研究分析原文，不可覆盖\n\n"+index.BEGIN+"\n旧索引\n"+index.END+"\n\n实验与研究设想仍保留\n"
            result=index.render_page(source,index.collect(root))
            self.assertTrue(result.startswith(source.split(index.BEGIN)[0]))
            self.assertTrue(result.endswith(source.split(index.END)[1]))
            self.assertEqual(index.render_page(result,index.collect(root)),result)
            self.assertEqual(result.count("| P218 |"),1)
            self.assertIn("Robot%202.0%20-%20",result)

    def test_missing_or_duplicated_markers_are_rejected(self):
        for body in ["完整人工笔记",index.BEGIN+"\n没有结尾",index.BEGIN+"\n"+index.BEGIN+"\n"+index.END,index.END+"\n"+index.BEGIN]:
            with self.subTest(body=body):
                with self.assertRaises(ValueError):
                    index.render_page(body,[])

    def test_new_card_updates_only_existing_main_page_and_preserves_annotations(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);p=self.note(root,"P218","Old")
            page=root/index.PAGE;page.parent.mkdir(parents=True)
            page.write_text("人工研究路线\n\n"+index.BEGIN+"\n| 编号 | 论文主卡 | 研究主题与阅读说明 |\n|---|---|---|\n| P218 | [旧显示名](old.md) | 保留此处人工阅读说明 |\n"+index.END+"\n\n人工实验设想\n",encoding="utf-8")
            old_note=p.read_bytes()
            self.note(root,"P238","New 中文")
            index.update(root,write=True)
            body=page.read_text(encoding="utf-8")
            self.assertIn("保留此处人工阅读说明",body)
            self.assertEqual(body.count("| P218 |"),1)
            self.assertEqual(body.count("| P238 |"),1)
            self.assertEqual(p.read_bytes(),old_note)
            self.assertEqual([x.name for x in page.parent.glob("数据与遥操作*.md")],["数据与遥操作.md"])
            before=page.read_bytes()
            index.update(root,write=True)
            self.assertEqual(page.read_bytes(),before)

    def test_duplicate_stable_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.note(root,"P218","A");self.note(root,"P218","B")
            with self.assertRaisesRegex(ValueError,"P218"):
                index.collect(root)

    def test_missing_indexed_card_is_not_silently_dropped(self):
        body=index.BEGIN+"\n| P218 | [原卡](old.md) | 原信息 |\n"+index.END
        with self.assertRaisesRegex(ValueError,"P218"):
            index.render_page(body,[])

    def test_cli_refuses_to_replace_unmarked_manual_page(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);page=root/index.PAGE;page.parent.mkdir(parents=True)
            page.write_text("仍未划分的人工研究分析",encoding="utf-8")
            before=page.read_bytes()
            run=subprocess.run([sys.executable,"-B",str(SCRIPT),"--root",str(root),"--write"],capture_output=True)
            self.assertNotEqual(run.returncode,0)
            self.assertEqual(page.read_bytes(),before)

    def test_refresh_rejects_extra_topic_before_writing(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.note(root,"P218","Existing")
            page=root/index.PAGE;page.parent.mkdir(parents=True)
            page.write_text(index.BEGIN+"\n"+index.END,encoding="utf-8")
            extra=page.parent/"新专题.md";extra.write_text("keep",encoding="utf-8")
            before=page.read_bytes()
            with self.assertRaises(ValueError):index.update(root,write=True)
            self.assertEqual(page.read_bytes(),before)
            self.assertTrue(extra.exists())

if __name__=="__main__":
    unittest.main()
