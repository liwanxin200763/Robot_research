"""Maintain citation metadata for the existing Chinese Obsidian paper cards.

Only an identity-verified API integer can replace a citation count. Failed
requests and ambiguous identities update the query status, never the count.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import email.utils
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CARDS = ROOT / "02_论文"
AUDIT = HERE / "CITATION_FULL_AUDIT.csv"
CACHE = HERE / "citation_cache.json"
CONFIG = HERE / "config.json"
RANKING = ROOT / "01_检索与审计" / "按引用量排序.md"
MANUAL = ROOT / "01_检索与审计" / "引用量待人工核验.md"
LOG = HERE / "query_log.csv"
SELECT = "id,doi,title,publication_year,publication_date,authorships,cited_by_count,ids,primary_location,type"
S2_FIELDS = "paperId,title,year,authors,citationCount,externalIds,url,publicationDate,venue"
OA_ID = re.compile(r"\bW\d+\b")
DOI = re.compile(r"10\.\d{4,9}/[^\s\]<>，；;]+", re.I)
ARXIV = re.compile(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b")
STATUS = {"verified", "verified_zero", "pending", "pending_identity", "rate_limited", "network_error", "api_error", "parse_error", "not_found", "suspicious_decrease"}


def load_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def atomic_json(path: Path, value: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def atomic_text(path: Path, value: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(value, encoding="utf-8")
    tmp.replace(path)


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").lower()
    return re.sub(r"[^a-z0-9]", "", value)


def surname(value: str) -> str:
    first = re.split(r"[;；、]", value or "")[0].strip()
    if not first or first == "—":
        return ""
    if "," in first:
        return norm(first.split(",", 1)[0])
    words = first.split()
    return norm(words[-1]) if words else ""


def clean_doi(value: str) -> str:
    match = DOI.search(value or "")
    return match.group(0).rstrip(".,)") if match else ""


def clean_arxiv(value: str) -> str:
    match = ARXIV.search(value or "")
    return re.sub(r"v\d+$", "", match.group(0)) if match else ""


def field(body: str, name: str) -> str:
    match = re.search(r"^- " + re.escape(name) + r"：([^\r\n]*)", body, re.M)
    return match.group(1).strip() if match else ""


def put_field(body: str, name: str, value: str, after: str) -> str:
    pattern = re.compile(r"^- " + re.escape(name) + r"：[^\r\n]*", re.M)
    matches = list(pattern.finditer(body))
    if len(matches) == 1:
        return pattern.sub(lambda _: f"- {name}：{value}", body, count=1)
    if matches:
        raise ValueError(f"duplicate field {name}")
    anchor = re.search(r"^- " + re.escape(after) + r"：[^\r\n]*", body, re.M)
    if not anchor:
        raise ValueError(f"missing anchor {after}")
    return body[:anchor.end()] + f"\n- {name}：{value}" + body[anchor.end():]


@dataclass
class Card:
    path: Path
    relative: str
    body: str
    title: str
    authors: str
    year: int | None
    venue: str
    doi: str
    arxiv: str
    oa_id: str
    count: int | None
    source: str
    source_url: str
    checked: str
    display_status: str
    query_status: str


def read_card(path: Path) -> Card:
    body = path.read_text(encoding="utf-8-sig")
    if body.count("## 基本信息") != 1:
        raise ValueError(f"basic information section missing/duplicated: {path}")
    year_text = field(body, "年份")
    year_match = re.search(r"\b(?:19|20)\d{2}\b", year_text)
    value = field(body, "引用量")
    count = int(value.replace(",", "")) if re.fullmatch(r"[\d,]+", value) else None
    raw_id = field(body, "OpenAlex Work ID") or field(body, "引用量来源链接")
    id_match = OA_ID.search(raw_id)
    return Card(path, path.relative_to(ROOT).as_posix(), body, field(body, "英文标题"),
                field(body, "作者"), int(year_match.group()) if year_match else None, field(body, "发表 venue"),
                clean_doi(field(body, "DOI")), clean_arxiv(field(body, "arXiv")),
                id_match.group() if id_match else "", count, field(body, "引用量来源"),
                field(body, "引用量来源链接"), field(body, "引用量查询日期"),
                field(body, "引用量状态"), field(body, "引用量查询状态"))


def cards() -> list[Card]:
    return [read_card(path) for path in sorted(CARDS.glob("*/*.md"))]


def oa_match(work: dict[str, Any], card: Card, known_authors: str = "") -> tuple[bool, float, str]:
    title = work.get("title") or work.get("display_name") or ""
    ratio = difflib.SequenceMatcher(None, norm(title), norm(card.title)).ratio()
    year = work.get("publication_year")
    year_diff = abs(year - card.year) if type(year) is int and card.year else 99
    got_doi = clean_doi(work.get("doi") or "")
    same_doi = bool(card.doi and got_doi and norm(card.doi) == norm(got_doi))
    arxiv_sources = " ".join([str(work.get("doi") or ""), str(work.get("ids") or ""),
                               str((work.get("primary_location") or {}).get("landing_page_url") or "")])
    arxiv_ok = bool(card.arxiv and card.arxiv in arxiv_sources)
    venue = ((work.get("primary_location") or {}).get("source") or {}).get("display_name", "")
    venue_ok = bool(card.venue and card.venue != "—" and norm(card.venue) in norm(venue))
    authors = [item.get("author", {}).get("display_name", "") for item in work.get("authorships", [])]
    first = surname(card.authors) or surname(known_authors)
    author_ok = bool(first and any(surname(name) == first for name in authors))
    # Publisher DOI and arXiv DOI can differ for one work. A conflicting pair of
    # distinct publisher DOIs is not accepted on title similarity alone.
    doi_conflict = bool(card.doi and got_doi and not same_doi and
                        not card.doi.lower().startswith("10.48550/arxiv.") and
                        not got_doi.lower().startswith("10.48550/arxiv."))
    verified = author_ok and not doi_conflict and (
        (same_doi or arxiv_ok) and ratio >= 0.78 and year_diff <= 2 or
        ratio >= 0.91 and year_diff <= 1)
    reason = f"title={ratio:.3f}; year_diff={year_diff}; author={author_ok}; doi={same_doi}; arxiv={arxiv_ok}; venue={venue_ok}; doi_conflict={doi_conflict}"
    return verified, ratio + (0.2 if same_doi else 0) + (0.1 if arxiv_ok else 0) + (0.03 if venue_ok else 0) - 0.02 * year_diff, reason


def s2_match(paper: dict[str, Any], card: Card, known_authors: str = "") -> tuple[bool, str]:
    ratio = difflib.SequenceMatcher(None, norm(paper.get("title", "")), norm(card.title)).ratio()
    year = paper.get("year")
    year_ok = type(year) is int and card.year is not None and abs(year-card.year) <= 1
    names = [a.get("name", "") for a in paper.get("authors", [])]
    first = surname(card.authors) or surname(known_authors)
    author_ok = bool(first and any(surname(name) == first for name in names))
    ids = paper.get("externalIds") or {}
    doi_ok = bool(card.doi and norm(ids.get("DOI", "")) == norm(card.doi))
    arxiv_ok = bool(card.arxiv and clean_arxiv(str(ids.get("ArXiv", ""))) == card.arxiv)
    verified = author_ok and year_ok and (doi_ok and ratio >= 0.78 or arxiv_ok and ratio >= 0.78 or ratio >= 0.94)
    return verified, f"title={ratio:.3f}; year={year_ok}; author={author_ok}; doi={doi_ok}; arxiv={arxiv_ok}"


def retry_seconds(value: str | None) -> float | None:
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            return max(0.0, (email.utils.parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds())
        except (TypeError, ValueError):
            return None


class Client:
    def __init__(self, config: dict[str, Any], sleep=time.sleep, clock=time.monotonic, opener=urllib.request.urlopen):
        self.config, self.sleep, self.clock, self.opener = config, sleep, clock, opener
        self.last: dict[str, float] = {}

    def get(self, url: str, source: str) -> tuple[dict[str, Any] | None, str, str]:
        interval = float(self.config[f"{source}_min_interval_seconds"])
        max_retries = int(self.config["max_retries"])
        for attempt in range(max_retries + 1):
            elapsed = self.clock() - self.last.get(source, -1e9)
            if elapsed < interval:
                self.sleep(interval - elapsed)
            self.last[source] = self.clock()
            headers = {"User-Agent": self.config["user_agent"]}
            if source == "semantic_scholar" and os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
                headers["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]
            request = urllib.request.Request(url, headers=headers)
            try:
                with self.opener(request, timeout=float(self.config["request_timeout_seconds"])) as response:
                    raw = response.read()
                try:
                    data = json.loads(raw)
                except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                    return None, "parse_error", str(exc)
                if not isinstance(data, dict):
                    return None, "parse_error", "API JSON is not an object"
                return data, "ok", ""
            except urllib.error.HTTPError as exc:
                status = "rate_limited" if exc.code == 429 else "not_found" if exc.code == 404 else "api_error"
                detail = f"HTTP {exc.code}"
                if exc.code == 429 or 500 <= exc.code <= 599:
                    if attempt < max_retries:
                        retry = retry_seconds(exc.headers.get("Retry-After"))
                        delay = retry if retry is not None else float(self.config["backoff_base_seconds"]) * 2 ** attempt + random.uniform(0, 0.5)
                        exc.close()
                        self.sleep(retry if retry is not None else min(delay, float(self.config["backoff_max_seconds"])))
                        continue
                exc.close()
                return None, status, detail
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt < max_retries:
                    delay = float(self.config["backoff_base_seconds"]) * 2 ** attempt + random.uniform(0, 0.5)
                    self.sleep(min(delay, float(self.config["backoff_max_seconds"])))
                    continue
                return None, "network_error", str(exc)
        raise AssertionError("unreachable")


def oa_url(identifier: str) -> str:
    return "https://api.openalex.org/works/" + identifier


def oa_search(title: str) -> str:
    return "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per_page": 8, "select": SELECT})


def s2_urls(card: Card) -> list[str]:
    urls = []
    if card.doi:
        ident = "DOI:" + card.doi
        urls.append("https://api.semanticscholar.org/graph/v1/paper/" + urllib.parse.quote(ident, safe=":./") + "?fields=" + S2_FIELDS)
    if card.arxiv:
        ident = "ARXIV:" + card.arxiv
        urls.append("https://api.semanticscholar.org/graph/v1/paper/" + urllib.parse.quote(ident, safe=":./") + "?fields=" + S2_FIELDS)
    urls.append("https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode({"query": card.title, "limit": 8, "fields": S2_FIELDS}))
    return urls


def lookup_oa(card: Card, entry: dict[str, Any], client: Client) -> tuple[dict[str, Any] | None, str, str]:
    candidates: list[dict[str, Any]] = []
    known = entry.get("identity_authors", "")
    ids = []
    if card.oa_id or entry.get("openalex_id"):
        ids.append(card.oa_id or entry["openalex_id"])
    else:
        if card.doi:
            ids.append("https://doi.org/" + urllib.parse.quote(card.doi, safe="/"))
        if card.arxiv and not card.doi:
            ids.append("https://doi.org/10.48550/arXiv." + card.arxiv)
    for ident in ids:
        data, status, detail = client.get(oa_url(ident), "openalex")
        if status == "ok":
            candidates.append(data)
        elif status != "not_found":
            return None, status, detail
    if candidates:
        matched = [(oa_match(work, card, known), work) for work in candidates]
        verified = [pair for pair in matched if pair[0][0]]
        if verified:
            return verified[0][1], "ok", verified[0][0][2]
        if card.oa_id or entry.get("openalex_id"):
            return None, "pending_identity", "saved OpenAlex ID failed identity recheck: " + matched[0][0][2]
    # Title search is only the last resort. Do not repeat it on every refresh.
    data, status, detail = client.get(oa_search(card.title), "openalex")
    if status != "ok":
        return None, status, detail
    options = data.get("results")
    if not isinstance(options, list):
        return None, "parse_error", "search results missing"
    scored = [(oa_match(work, card, known), work) for work in options if isinstance(work, dict)]
    valid = sorted([pair for pair in scored if pair[0][0]], key=lambda pair: pair[0][1], reverse=True)
    if not valid:
        return None, "pending_identity" if options else "not_found", "no candidate passed title/author/year/identifier checks"
    if len(valid) > 1 and valid[0][0][1] - valid[1][0][1] < 0.04:
        return None, "pending_identity", "multiple plausible OpenAlex Works"
    return valid[0][1], "ok", valid[0][0][2]


def lookup_s2(card: Card, entry: dict[str, Any], client: Client) -> tuple[dict[str, Any] | None, str, str]:
    saw_candidates = False
    for url in s2_urls(card):
        data, status, detail = client.get(url, "semantic_scholar")
        if status == "not_found":
            continue
        if status != "ok":
            return None, status, detail
        options = data.get("data") if "data" in data else [data]
        if not isinstance(options, list):
            return None, "parse_error", "Semantic Scholar result list invalid"
        saw_candidates = saw_candidates or bool(options)
        valid = []
        for item in options:
            if isinstance(item, dict):
                good, why = s2_match(item, card, entry.get("identity_authors", ""))
                if good:
                    valid.append((item, why))
        if len(valid) == 1:
            return valid[0][0], "ok", valid[0][1]
        if len(valid) > 1:
            return None, "pending_identity", "multiple plausible Semantic Scholar papers"
    return None, "pending_identity" if saw_candidates else "not_found", "no unique Semantic Scholar identity match"


def apply_result(card: Card, entry: dict[str, Any], result: dict[str, Any] | None, status: str,
                 source: str, reason: str, today: str, dry_run: bool = False) -> dict[str, Any]:
    """Apply one lookup. Failure never changes a previously verified count."""
    new = dict(entry)
    new["last_attempt_at"] = today
    new["last_query_status"] = status
    new["last_error"] = reason if status != "ok" else ""
    if status != "ok" or result is None:
        if status not in STATUS:
            raise ValueError(status)
        body = put_field(card.body, "引用量查询状态", status, "引用量状态")
        if not dry_run and body != card.body:
            atomic_text(card.path, body)
        return new
    count_key = "cited_by_count" if source == "OpenAlex" else "citationCount"
    count = result.get(count_key)
    if type(count) is not int or count < 0:
        return apply_result(card, entry, None, "parse_error", source, f"{count_key} absent or not a nonnegative integer", today, dry_run)
    if card.count is not None and count < card.count:
        new.update(last_query_status="suspicious_decrease", last_error=f"new {count} < existing {card.count}", candidate_count=count)
        body = put_field(card.body, "引用量查询状态", "suspicious_decrease", "引用量状态")
        if not dry_run and body != card.body:
            atomic_text(card.path, body)
        return new
    status = "verified_zero" if count == 0 else "verified"
    if source == "OpenAlex":
        ident = OA_ID.search(str(result.get("id", "")))
        if not ident:
            return apply_result(card, entry, None, "parse_error", source, "OpenAlex ID missing", today, dry_run)
        work_id = ident.group()
        url = "https://openalex.org/" + work_id
        new["openalex_id"] = work_id
    else:
        paper_id = result.get("paperId")
        if not paper_id:
            return apply_result(card, entry, None, "parse_error", source, "Semantic Scholar paperId missing", today, dry_run)
        url = "https://www.semanticscholar.org/paper/" + paper_id
        work_id = card.oa_id or new.get("openalex_id", "")
    new.update(citation_count=count, citation_source=source, citation_checked=today,
               last_query_status=status, last_error="", identity_authors=card.authors or new.get("identity_authors", ""))
    body = card.body
    for name, value, after in [
        ("引用量", str(count), "摘要依据"),
        ("引用量来源", source, "引用量"),
        ("引用量来源链接", url, "引用量来源"),
        ("引用量查询日期", today, "引用量来源链接"),
        ("引用量状态", "已核验", "引用量查询日期"),
        ("引用量查询状态", status, "引用量状态"),
        ("OpenAlex Work ID", work_id or "—", "引用量查询状态"),
        ("排序引用量", str(count) if source == "OpenAlex" else "—", "OpenAlex Work ID"),
        ("排序引用量来源", "OpenAlex" if source == "OpenAlex" else "未被统一来源可靠收录", "排序引用量")]:
        body = put_field(body, name, value, after)
    if not dry_run and body != card.body:
        atomic_text(card.path, body)
    return new


def age_days(value: str, today: date) -> int | None:
    try:
        return (today - date.fromisoformat(value[:10])).days
    except (ValueError, TypeError):
        return None


def due(card: Card, entry: dict[str, Any], config: dict[str, Any], today: date, force: bool) -> bool:
    if force:
        return True
    last_status = entry.get("last_query_status", "")
    if last_status in {"rate_limited", "network_error", "api_error", "parse_error", "suspicious_decrease"}:
        attempt_age = age_days(entry.get("last_attempt_at", ""), today)
        wait_days = int(config["pending_retry_days"] if last_status == "suspicious_decrease" else config["failed_retry_days"])
        if attempt_age is not None and attempt_age < wait_days:
            return False
    if card.count is not None and card.display_status == "已核验":
        age = age_days(entry.get("citation_checked", card.checked), today)
        return age is None or age >= int(config["citation_refresh_days"])
    age = age_days(entry.get("last_attempt_at", ""), today)
    return age is None or age >= int(config["pending_retry_days"])


def bootstrap(dry_run: bool = False) -> None:
    with AUDIT.open(encoding="utf-8-sig", newline="") as f:
        audit = {row["canonical_file"]: row for row in csv.DictReader(f)}
    all_cards = cards()
    if len(all_cards) != len(audit) or len(all_cards) != 134:
        raise ValueError("card/audit count mismatch")
    cache = load_json(CACHE, {"schema_version": 1, "papers": {}, "works": {}, "aliases": {}})
    cache.setdefault("works", {})
    cache.setdefault("aliases", {})
    for card in all_cards:
        row = audit[card.relative]
        existing = cache["papers"].get(card.relative)
        if existing and existing.get("citation_count") != card.count:
            raise ValueError(f"cache/card count differs: {card.relative}")
        if not existing and row["new"] != (str(card.count) if card.count is not None else "—"):
            raise ValueError(f"audit/card count differs: {card.relative}")
        verified = row["status"] == "已核验" and card.count is not None
        work_id_match = OA_ID.search(row["source_url"] if row["citation_source"] == "OpenAlex" else "")
        work_id = (existing or {}).get("openalex_id") or (work_id_match.group() if work_id_match else "")
        if verified and row["citation_source"] == "OpenAlex" and not work_id:
            raise ValueError(f"verified OpenAlex record lacks ID: {card.relative}")
        query_status = (existing or {}).get("last_query_status") or ("verified_zero" if verified and card.count == 0 else "verified" if verified else "pending_identity")
        body = put_field(card.body, "引用量查询状态", query_status, "引用量状态")
        body = put_field(body, "OpenAlex Work ID", work_id or "—", "引用量查询状态")
        if not dry_run and body != card.body:
            atomic_text(card.path, body)
        cache["papers"][card.relative] = existing or {
            "openalex_id": work_id,
            "identity_authors": row["authors"],
            "citation_count": card.count,
            "citation_source": row["citation_source"] if verified else None,
            "citation_checked": row["checked_date"] if verified else None,
            "last_attempt_at": row["checked_date"],
            "last_query_status": query_status,
            "last_error": row["identity_evidence"] if not verified else ""
        }
        if work_id:
            current = cache["papers"][card.relative]
            cache["works"][work_id] = {"citation_count": current["citation_count"], "checked_at": current["citation_checked"], "source": "OpenAlex", "title": card.title, "year": card.year, "authors": row["authors"]}
            if card.doi:
                cache["aliases"]["doi:" + norm(card.doi)] = work_id
            if card.arxiv:
                cache["aliases"]["arxiv:" + card.arxiv] = work_id
    if not dry_run:
        atomic_json(CACHE, cache)
    print(f"[BOOTSTRAP] {len(all_cards)} cards; OpenAlex IDs {sum(bool(x['openalex_id']) for x in cache['papers'].values())}; dry_run={dry_run}")


def log_event(relative: str, source: str, status: str, count: int | None, detail: str) -> None:
    new = not LOG.exists()
    with LOG.open("a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
        writer = csv.writer(f)
        if new:
            writer.writerow(["checked_at", "canonical_file", "source", "status", "candidate_count", "detail"])
        writer.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), relative, source, status, "" if count is None else count, detail])


def update(limit: int | None, force: bool, dry_run: bool, offline: bool, paper: str | None = None) -> None:
    config = load_json(CONFIG, {})
    cache = load_json(CACHE, {"schema_version": 1, "papers": {}, "works": {}, "aliases": {}})
    if cache.get("schema_version") != 1:
        raise ValueError("citation cache schema mismatch")
    client = Client(config)
    today = date.today()
    all_cards = cards()
    selected = [card for card in all_cards if due(card, cache["papers"].get(card.relative, {}), config, today, force)]
    if paper:
        selected = [card for card in selected if paper.casefold() in card.path.stem.casefold() or paper.casefold() in card.title.casefold()]
    if limit is not None:
        selected = selected[:limit]
    summary = Counter()
    for card in selected:
        entry = dict(cache["papers"].get(card.relative, {}))
        if not card.oa_id and not entry.get("openalex_id"):
            alias = (cache.get("aliases", {}).get("doi:" + norm(card.doi)) if card.doi else None) or (cache.get("aliases", {}).get("arxiv:" + card.arxiv) if card.arxiv else None)
            if alias:
                entry["openalex_id"] = alias
        if offline:
            print(f"[DUE] {card.path.stem}")
            summary["due"] += 1
            continue
        work, status, reason = lookup_oa(card, entry, client)
        source = "OpenAlex"
        if status in ("not_found", "pending_identity") and config["enable_semantic_scholar_fallback"]:
            backup, backup_status, backup_reason = lookup_s2(card, entry, client)
            if backup_status == "ok":
                work, status, reason, source = backup, backup_status, backup_reason, "Semantic Scholar"
            else:
                reason += f"; Semantic Scholar {backup_status}: {backup_reason}"
                if backup_status in {"rate_limited", "network_error", "api_error", "parse_error"}:
                    status = backup_status
        count_key = "cited_by_count" if source == "OpenAlex" else "citationCount"
        candidate = work.get(count_key) if work else None
        new_entry = apply_result(card, entry, work, status, source, reason, today.isoformat(), dry_run)
        final = new_entry["last_query_status"]
        summary[final] += 1
        marker = "ZERO" if final == "verified_zero" else "OK" if final == "verified" else "429" if final == "rate_limited" else "PENDING" if final in ("pending_identity", "not_found") else "ERROR"
        print(f"[{marker}] {card.path.stem} | {source} | {final} | {candidate if type(candidate) is int else '—'}")
        if not dry_run:
            cache["papers"][card.relative] = new_entry
            if final in {"verified", "verified_zero"} and source == "OpenAlex" and new_entry.get("openalex_id"):
                work_id = new_entry["openalex_id"]
                cache.setdefault("works", {})[work_id] = {"citation_count": new_entry["citation_count"], "checked_at": today.isoformat(), "source": "OpenAlex", "title": card.title, "year": card.year, "authors": card.authors}
                if card.doi:
                    cache.setdefault("aliases", {})["doi:" + norm(card.doi)] = work_id
                if card.arxiv:
                    cache.setdefault("aliases", {})["arxiv:" + card.arxiv] = work_id
            atomic_json(CACHE, cache)
            log_event(card.relative, source, final, candidate if type(candidate) is int else None, reason or new_entry.get("last_error", ""))
    current = cards() if not (dry_run or offline) else all_cards
    print("[SUMMARY]", {"total": len(current), "selected": len(selected), "cache_fresh_or_not_selected": len(all_cards)-len(selected),
                        "verified": sum(c.count is not None for c in current), "uncertain": sum(c.count is None for c in current),
                        "verified_zero": sum(c.count == 0 for c in current), "query_results": dict(summary)})
    if not dry_run and not offline:
        render()
        validate()


def render(dry_run: bool = False) -> None:
    all_cards = cards()
    cache = load_json(CACHE, {"papers": {}}).get("papers", {})
    ranked = sorted(all_cards, key=lambda c: (c.source != "OpenAlex" or c.count is None, -(c.count or 0), c.path.stem))
    today = date.today().isoformat()
    def link(card: Card) -> str:
        return f"[[{card.relative[:-3]}|{card.path.stem}]]"
    lines = ["# 按引用量排序", "", f"按 OpenAlex 已核验引用量降序排列；页面生成日期：{today}。不同来源的数值不混入这一排序。", "", "## 全部论文", ""]
    for index, card in enumerate(ranked, 1):
        count = str(card.count) if card.source == "OpenAlex" and card.count is not None else "—"
        label = "OpenAlex" if count != "—" else (card.source + "（不参与统一排名）" if card.count is not None else "待核验")
        lines.append(f"{index}. {link(card)} — 引用量：{count}；年份：{card.year or '—'}；来源：{label}")
    for category in dict.fromkeys(card.path.parent.name for card in ranked):
        group = [card for card in ranked if card.path.parent.name == category]
        lines.extend(["", f"## {category}", ""])
        lines.extend(f"{index}. {link(card)} — {card.count if card.source == 'OpenAlex' and card.count is not None else '—'}" for index, card in enumerate(group, 1))
    manual = ["# 引用量待人工核验", "", "只列当前无可靠引用量或出现可疑下降的论文。查询失败时，已核验的旧值保留在论文卡中。Semantic Scholar 限流不会被当作 0；Google Scholar 仅供人工正常访问时复核。", ""]
    for card in all_cards:
        if card.count is not None and card.query_status != "suspicious_decrease":
            continue
        entry = cache.get(card.relative, {})
        reason = entry.get("last_error") or "尚无可唯一确认的数据库记录"
        query_url = "https://openalex.org/works?search=" + urllib.parse.quote(card.title)
        manual.extend([f"## {card.path.stem}", "", f"- 论文：{link(card)}", f"- 英文标题：{card.title}",
                       f"- 作者：{card.authors if card.authors and card.authors != '—' else entry.get('identity_authors') or '—'}", f"- 年份：{card.year or '—'}", f"- DOI / arXiv：{card.doi or '—'} / {card.arxiv or '—'}",
                       f"- 当前引用量：{card.count if card.count is not None else '—'}", f"- 查询状态：{card.query_status or 'pending'}",
                       f"- 已检查来源：[OpenAlex 完整标题检索]({query_url})；库内 DOI：{card.doi or '—'}；arXiv：{card.arxiv or '—'}",
                       f"- 不确定原因：{reason}", "- 建议人工检查方式：核对 DOI、标题、首位作者、年份和发表版本，再确认数据库 Work ID。", ""])
    if not dry_run:
        atomic_text(RANKING, "\n".join(lines)+"\n")
        atomic_text(MANUAL, "\n".join(manual).rstrip()+"\n")
        with (HERE / "CITATION_RANKING.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["canonical_file", "chinese_title", "english_title", "year", "category", "ranking_count", "citation_source", "checked_date"])
            for card in ranked:
                writer.writerow([card.relative, card.path.stem, card.title, card.year or "", card.path.parent.name,
                                 card.count if card.source == "OpenAlex" and card.count is not None else "—", card.source, card.checked])
    print(f"[RENDER] ranked={len(ranked)} manual={sum(c.count is None or c.query_status == 'suspicious_decrease' for c in all_cards)} dry_run={dry_run}")


def validate() -> None:
    all_cards = cards()
    cache = load_json(CACHE, {"papers": {}})
    errors = []
    if not all_cards or len({card.relative for card in all_cards}) != len(all_cards):
        errors.append("empty or duplicate canonical card paths")
    for card in all_cards:
        entry = cache.get("papers", {}).get(card.relative)
        if sum(len(re.findall(r"^- " + re.escape(name) + r"：", card.body, re.M)) != 1 for name in ("引用量", "引用量状态", "引用量查询状态", "OpenAlex Work ID")):
            errors.append(f"missing or duplicate citation field: {card.relative}")
        if card.query_status and card.query_status not in STATUS:
            errors.append(f"invalid query status: {card.relative}")
        if card.count == 0:
            if not (card.display_status == "已核验" and entry and entry.get("citation_count") == 0 and entry.get("citation_source") in ("OpenAlex", "Semantic Scholar") and entry.get("citation_checked") and (card.oa_id if entry.get("citation_source") == "OpenAlex" else card.source_url)):
                errors.append(f"unverified zero: {card.relative}")
        if card.count is not None and card.display_status != "已核验":
            errors.append(f"numeric count without verified display status: {card.relative}")
        if card.source == "OpenAlex" and card.count is not None and not card.oa_id:
            errors.append(f"OpenAlex count without stable Work ID: {card.relative}")
        if entry and entry.get("citation_count") != card.count:
            errors.append(f"cache/card count mismatch: {card.relative}")
    if errors:
        raise ValueError("\n".join(errors))
    counts = Counter("verified_zero" if c.count == 0 else "verified" if c.count is not None else "pending" for c in all_cards)
    print("[VALID]", len(all_cards), dict(counts), "unverified_zero=0")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("bootstrap", "update", "render", "validate"):
        command = sub.add_parser(name)
        if name != "validate":
            command.add_argument("--dry-run", action="store_true")
        if name == "update":
            command.add_argument("--force", action="store_true", help="ignore refresh interval")
            command.add_argument("--offline", action="store_true", help="show due papers without network or writes")
            command.add_argument("--limit", type=int)
            command.add_argument("--paper", help="filter paper by title or filename substring")
    args = parser.parse_args()
    if args.command == "bootstrap":
        bootstrap(args.dry_run)
    elif args.command == "update":
        update(args.limit, args.force, args.dry_run, args.offline, args.paper)
    elif args.command == "render":
        render(args.dry_run)
    else:
        validate()


if __name__ == "__main__":
    main()
