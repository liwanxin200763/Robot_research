import io
import json
import tempfile
import unittest
import urllib.error
from datetime import date
from pathlib import Path

import citations as c


class CitationSafetyTests(unittest.TestCase):
    def make_card(self, count="7", status="已核验"):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / "paper.md"
        body = ("# Paper\n\n## 基本信息\n\n- 英文标题：Example Robot Policy\n"
                "- 作者：Alice Smith; Bob Lee\n- 年份：2025\n- DOI：10.1234/example\n"
                "- arXiv：—\n- 摘要依据：—\n" + f"- 引用量：{count}\n" +
                "- 引用量来源：OpenAlex\n- 引用量来源链接：https://openalex.org/W123\n"
                "- 引用量查询日期：2026-09-27\n" + f"- 引用量状态：{status}\n" +
                "- 引用量查询状态：verified\n- OpenAlex Work ID：W123\n"
                "- 排序引用量：7\n- 排序引用量来源：OpenAlex\n")
        path.write_text(body, encoding="utf-8")
        return c.Card(path, "paper.md", body, "Example Robot Policy", "Alice Smith; Bob Lee", 2025, "CoRL",
                      "10.1234/example", "", "W123", int(count) if count.isdigit() else None,
                      "OpenAlex", "https://openalex.org/W123", "2026-09-27", status, "verified")

    def work(self, count):
        return {"id": "https://openalex.org/W123", "title": "Example Robot Policy",
                "publication_year": 2025, "doi": "https://doi.org/10.1234/example",
                "authorships": [{"author": {"display_name": "Alice Smith"}}], "cited_by_count": count}

    def test_failure_preserves_verified_count(self):
        card = self.make_card()
        entry = {"citation_count": 7, "citation_source": "OpenAlex", "citation_checked": "2026-09-27"}
        result = c.apply_result(card, entry, None, "rate_limited", "OpenAlex", "HTTP 429", "2026-10-01")
        self.assertEqual(result["citation_count"], 7)
        self.assertEqual(result["last_query_status"], "rate_limited")
        self.assertIn("- 引用量：7", card.path.read_text(encoding="utf-8"))

    def test_null_is_not_zero(self):
        card = self.make_card(count="—", status="待核验")
        result = c.apply_result(card, {}, self.work(None), "ok", "OpenAlex", "", "2026-10-01")
        self.assertEqual(result["last_query_status"], "parse_error")
        self.assertIn("- 引用量：—", card.path.read_text(encoding="utf-8"))

    def test_explicit_zero_and_decrease(self):
        empty = self.make_card(count="—", status="待核验")
        result = c.apply_result(empty, {}, self.work(0), "ok", "OpenAlex", "", "2026-10-01")
        self.assertEqual(result["citation_count"], 0)
        self.assertEqual(result["last_query_status"], "verified_zero")
        self.assertIn("- 引用量：0", empty.path.read_text(encoding="utf-8"))
        card = self.make_card()
        lower = c.apply_result(card, {"citation_count": 7}, self.work(4), "ok", "OpenAlex", "", "2026-10-01")
        self.assertEqual(lower["last_query_status"], "suspicious_decrease")
        self.assertEqual(lower["candidate_count"], 4)
        self.assertIn("- 引用量：7", card.path.read_text(encoding="utf-8"))

    def test_identity_requires_title_author_year(self):
        card = self.make_card()
        self.assertTrue(c.oa_match(self.work(7), card)[0])
        wrong = self.work(7) | {"authorships": [{"author": {"display_name": "Someone Else"}}]}
        self.assertFalse(c.oa_match(wrong, card)[0])

    def test_arxiv_version_can_match_changed_title(self):
        card = self.make_card()
        card.arxiv = "2501.12345"
        work = self.work(7) | {"title": "Example Robot Policy: A Study", "doi": "https://doi.org/10.48550/arxiv.2501.12345",
                               "ids": {"arxiv": "https://arxiv.org/abs/2501.12345"}}
        self.assertTrue(c.oa_match(work, card)[0])

    def test_retry_after_and_exhausted_429(self):
        sleeps = []
        calls = []
        def opener(request, timeout):
            calls.append(request.full_url)
            if len(calls) == 1:
                raise urllib.error.HTTPError(request.full_url, 429, "limited", {"Retry-After": "3"}, io.BytesIO(b""))
            return io.BytesIO(json.dumps({"id": "W123"}).encode())
        config = c.load_json(c.CONFIG, {}) | {"openalex_min_interval_seconds": 0, "max_retries": 1}
        client = c.Client(config, sleep=sleeps.append, clock=lambda: 0, opener=opener)
        data, status, _ = client.get("https://api.openalex.org/works/W123", "openalex")
        self.assertEqual(status, "ok")
        self.assertEqual(data["id"], "W123")
        self.assertEqual(sleeps, [3.0])
        self.assertEqual(len(calls), 2)

    def test_exhausted_429_has_no_count(self):
        def opener(request, timeout):
            raise urllib.error.HTTPError(request.full_url, 429, "limited", {"Retry-After": "1"}, io.BytesIO(b""))
        config = c.load_json(c.CONFIG, {}) | {"openalex_min_interval_seconds": 0, "max_retries": 1}
        waits = []
        data, status, detail = c.Client(config, sleep=waits.append, clock=lambda: 0, opener=opener).get("https://api.openalex.org/works/W123", "openalex")
        self.assertIsNone(data)
        self.assertEqual(status, "rate_limited")
        self.assertEqual(detail, "HTTP 429")
        self.assertEqual(waits, [1.0])

    def test_saved_work_id_skips_title_search(self):
        card = self.make_card()
        class FakeClient:
            def __init__(self, work):
                self.work, self.urls = work, []
            def get(self, url, source):
                self.urls.append(url)
                return self.work, "ok", ""
        client = FakeClient(self.work(8))
        result, status, _ = c.lookup_oa(card, {"openalex_id": "W123"}, client)
        self.assertEqual(status, "ok")
        self.assertEqual(result["cited_by_count"], 8)
        self.assertEqual(client.urls, ["https://api.openalex.org/works/W123"])

    def test_doi_lookup_precedes_title_search(self):
        card = self.make_card()
        card.oa_id = ""
        class FakeClient:
            def __init__(self, work):
                self.work, self.urls = work, []
            def get(self, url, source):
                self.urls.append(url)
                return self.work, "ok", ""
        client = FakeClient(self.work(8))
        _, status, _ = c.lookup_oa(card, {}, client)
        self.assertEqual(status, "ok")
        self.assertEqual(client.urls, ["https://api.openalex.org/works/https://doi.org/10.1234/example"])

    def test_refresh_interval_and_failure_cooldown(self):
        card = self.make_card()
        config = c.load_json(c.CONFIG, {})
        entry = {"citation_checked": "2026-09-27", "last_query_status": "verified"}
        self.assertFalse(c.due(card, entry, config, date(2026, 10, 1), False))
        self.assertTrue(c.due(card, entry, config, date(2026, 10, 12), False))
        entry.update(last_query_status="rate_limited", last_attempt_at="2026-10-12")
        self.assertFalse(c.due(card, entry, config, date(2026, 10, 12), False))


if __name__ == "__main__":
    unittest.main()
