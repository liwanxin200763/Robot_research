"""Enforce the fixed eight research-direction files before index writes."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

spec=importlib.util.spec_from_file_location("direction_policy",Path(__file__).with_name("research_direction_policy.py"))
try:
    policy=importlib.util.module_from_spec(spec);spec.loader.exec_module(policy)
except FileNotFoundError:
    policy=None

class DirectionPolicyTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(policy,"fixed-direction policy is missing")

    def layout(self,root):
        folder=root/"02 研究方向";folder.mkdir()
        for name in policy.DIRECTION_FILES:(folder/name).write_text("# Existing\n")
        return folder

    def test_exact_eight_files_pass_and_paths_remain_fixed(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.layout(root)
            policy.validate_directory(root)
            self.assertEqual(policy.direction_path(root,"VLA.md"),root/"02 研究方向/VLA.md")

    def test_topic_and_subdirectory_are_rejected_without_deletion(self):
        for extra in ("新论文专题.md","专题子目录"):
            with self.subTest(extra=extra),tempfile.TemporaryDirectory() as d:
                root=Path(d);folder=self.layout(root);p=folder/extra
                p.write_text("# Keep") if extra.endswith(".md") else p.mkdir()
                with self.assertRaises(ValueError):policy.validate_directory(root)
                self.assertTrue(p.exists())

    def test_missing_category_and_arbitrary_output_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);folder=self.layout(root);(folder/"VLA.md").unlink()
            with self.assertRaises(ValueError):policy.validate_directory(root)
            for name in ("新项目.md","../VLA.md","数据与遥操作_专题.md"):
                with self.assertRaises(ValueError):policy.direction_path(root,name)

if __name__=="__main__":unittest.main()
