"""Regression tests for actual note targets, including decimal titles."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC=importlib.util.spec_from_file_location("link_check",Path(__file__).with_name("validate_links.py"))
m=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)

class LinkTargets(unittest.TestCase):
    def test_decimal_title_is_not_an_extension(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            p=root/"03 论文卡片"/"Robot 2.0.md";p.parent.mkdir();p.write_text("# correct")
            self.assertEqual(m.resolve(root,root/"index.md","03 论文卡片/Robot 2.0"),[p])

    def test_relative_markdown_target_decodes_spaces(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);source=root/"05 检索与引用"/"排序.md";source.parent.mkdir()
            p=root/"03 论文卡片"/"Human & Robot.md";p.parent.mkdir();p.write_text("# correct")
            self.assertEqual(m.resolve(root,source,"../03%20论文卡片/Human%20%26%20Robot.md"),[p])

    def test_duplicate_basename_requires_disambiguation(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for name in ("A","B"):
                p=root/name/"MEM.md";p.parent.mkdir();p.write_text("# "+name)
            self.assertEqual(len(m.resolve(root,root/"index.md","MEM")),2)
            self.assertEqual(m.resolve(root,root/"index.md","A/MEM"),[root/"A"/"MEM.md"])

    def test_pdf_extension_and_anchor_are_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);p=root/"paper.pdf";p.write_bytes(b"%PDF")
            self.assertEqual(m.resolve(root,root/"index.md","paper.pdf#page=2"),[p])
            self.assertEqual(m.resolve(root,root/"index.md","missing"),[])

if __name__=="__main__":
    unittest.main()
