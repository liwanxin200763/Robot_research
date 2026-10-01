import unittest
from pathlib import Path

import citations as c


class ManualCitationTests(unittest.TestCase):
    def sample(self, count="456", source="OpenAlex"):
        return ("# 论文\n\n## 基本信息\n- 英文标题：Robot Policy\n"
                f"- 引用量：{count}\n- 引用量来源：{source}\n"
                "- 引用量来源链接：https://openalex.org/W123\n"
                "- 引用量查询日期：2026-09-27\n- 引用量状态：已核验\n"
                "- 引用量查询状态：verified\n- OpenAlex Work ID：W123\n"
                "- 排序引用量：14\n- 排序引用量来源：OpenAlex\n"
                "\n## 正文\n正文保持原样。\n")

    def test_clean_removes_maintenance_evidence_and_preserves_number(self):
        original = self.sample()
        cleaned, removed, changed = c.clean_text(original)
        self.assertEqual(c.value(cleaned, "引用量"), "456")
        self.assertEqual(c.value(cleaned, "引用量来源"), "Google Scholar")
        self.assertEqual(removed, 7)
        self.assertTrue(changed)
        self.assertNotIn("引用量来源链接", cleaned)
        self.assertNotIn("引用量状态", cleaned)
        self.assertIn("## 正文\n正文保持原样。", cleaned)
        self.assertNotIn("OpenAlex Work ID", cleaned)
        self.assertEqual(c.clean_text(cleaned), (cleaned, 0, False))

    def test_unsupported_source_normalizes_to_manual_source(self):
        cleaned, _, changed = c.clean_text(self.sample(source="Unknown"))
        self.assertEqual(c.value(cleaned, "引用量来源"), "Google Scholar")
        self.assertTrue(changed)

    def test_dash_and_zero_remain_distinct(self):
        for original in ("—", "0", "待核验", ""):
            with self.subTest(original=original):
                cleaned, _, _ = c.clean_text(self.sample(original))
                self.assertEqual(c.value(cleaned, "引用量"), original)

    def test_crlf_survives_cleaning(self):
        original = self.sample().replace("\n", "\r\n")
        cleaned, _, _ = c.clean_text(original)
        self.assertEqual(cleaned.count("\r\n"), cleaned.count("\n"))
        self.assertEqual(c.value(cleaned, "引用量"), "456")

    def test_ranking_reads_card_number_and_places_missing_last(self):
        def card(title, value):
            return c.Card(Path("01_VLA") / f"{title}.md", f"02_论文/01_VLA/{title}.md",
                          title, "2025", value, c.citation_number(value))
        result = c.ranking_text([card("A", "—"), card("B", "3"), card("C", "12"), card("D", "0")], "2026-09-28")
        rows = [line for line in result.splitlines() if "[[" in line]
        self.assertEqual([next(name for name in "ABCD" if f"/{name}|" in row) for row in rows], ["C", "B", "D", "A"])
        self.assertEqual(result.count("[["), 4)
        self.assertIn("## 待补充引用量\n\n- [[02_论文/01_VLA/A|A]]", result)
        self.assertNotIn("OpenAlex", result)

    def test_csv_uses_current_card_values(self):
        cards = [c.Card(Path("01_VLA/A.md"), "02_论文/01_VLA/A.md", "A", "2025", "99", 99),
                 c.Card(Path("01_VLA/B.md"), "02_论文/01_VLA/B.md", "B", "2025", "—", None)]
        output = c.ranking_csv_text(cards)
        self.assertIn(",2025,01_VLA,99,Google Scholar", output)
        self.assertIn(",2025,01_VLA,—,Google Scholar", output)
        self.assertNotIn("ranking_count", output)

    def test_zero_is_marked_for_manual_review(self):
        api = c.Card(Path("01_VLA/ACE.md"), "02_论文/01_VLA/ACE.md", "ACE", "2026", "0", 0)
        manual = c.Card(Path("01_VLA/Other.md"), "02_论文/01_VLA/Other.md", "Other", "2026", "0", 0)
        page = c.manual_text([api, manual])
        self.assertIn("/ACE|", page)
        self.assertIn("/Other|", page)

    def test_duplicate_count_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "expected one 引用量"):
            c.clean_text(self.sample() + "- 引用量：999\n")


if __name__ == "__main__":
    unittest.main()
