#!/usr/bin/env python3
"""Checks a blog post before publication (see 08_BLOGA_STRATEGIJA / 09_BLOGA_PROMPTS).
Usage: python3 tools/check_post.py content/blog/<slug>.md --keyword "main keyword"
       python3 tools/check_post.py --all          (dash check over all content and templates)
Exit code 1 if any error.
"""
import re, sys, argparse
from pathlib import Path

DASHES = {"—": "em dash", "–": "en dash", "‒": "figure dash", "―": "horizontal bar"}
BANNED = ["in today's fast-paced world", "game-changer", "game changer", "unlock", "delve", "revolutionize",
          "harness the power", "it's no secret", "at the end of the day", "navigate the complexities", "elevate"]

def dash_errors(path):
    errs = []
    for n, line in enumerate(Path(path).read_text().splitlines(), 1):
        for ch, name in DASHES.items():
            if ch in line:
                errs.append(f"{path}:{n}: {name}: {line.strip()[:90]}")
    return errs

def check_post(path, keyword):
    text = Path(path).read_text()
    errs, warns = dash_errors(path), []
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return errs + [f"{path}: no front matter"], warns
    fm, body = m.group(1), m.group(2)
    meta = dict((k.strip(), v.strip().strip('"')) for k, v in (l.split(":", 1) for l in fm.splitlines() if ":" in l))
    for f in ["title", "description", "date", "chapter", "slug", "answer"]:
        if not meta.get(f):
            errs.append(f"front matter: missing {f}")
    plain = re.sub(r"<[^>]+>|[#*_`>\[\]()]", " ", body)
    words = len(plain.split())
    if words < 1200: errs.append(f"too short: {words} words (min 1200)")
    if words > 2600: warns.append(f"long: {words} words")
    d = meta.get("description", "")
    if not 120 <= len(d) <= 170: warns.append(f"description length {len(d)} (aim 140 to 160)")
    if len(meta.get("title", "")) > 75: warns.append(f"title {len(meta['title'])} chars (aim <= 65)")
    a = len(meta.get("answer", "").split())
    if not 35 <= a <= 80: warns.append(f"answer {a} words (aim 40 to 70)")
    low = text.lower()
    for b in BANNED:
        if b in low: errs.append(f"banned phrase: '{b}'")
    if keyword:
        k = keyword.lower()
        first100 = " ".join(plain.split()[:100]).lower()
        h2s = " ".join(re.findall(r"^## (.*)$", body, re.M)).lower()
        checks = {"title": k in meta.get("title", "").lower(), "description": k in d.lower(),
                  "first 100 words (body or answer)": k in first100 or k in meta.get("answer", "").lower(),
                  "an H2": k in h2s}
        for where, ok in checks.items():
            if not ok: warns.append(f"keyword not in {where}")
        visible = re.sub(r"^keywords:.*$", "", low, flags=re.M)
        count = visible.count(k)
        per1000 = count * 1000 / max(words, 1)
        if per1000 > 10: errs.append(f"keyword stuffing risk: '{keyword}' {count}x ({per1000:.1f} per 1000 words)")
        elif per1000 > 7: warns.append(f"keyword density high: '{keyword}' {count}x ({per1000:.1f} per 1000 words)")
        print(f"keyword '{keyword}': {count}x visible ({per1000:.1f} per 1000 words)")
    links = re.findall(r"\]\((/[^)]*)\)|href=\"(/[^\"]*)\"", body)
    internal = {a or b for a, b in links}
    if not any(u.startswith("/blog/") for u in internal): errs.append("no internal link to another post")
    if not any("/buy/" in u for u in internal) and "amazon.com/dp/" not in body: errs.append("no link to /buy/ or Amazon")
    if "/blog/free-sample/" not in body: warns.append("no link to the free sample")
    if "## FAQ" not in body: errs.append("no FAQ section")
    if 'class="def"' not in body: warns.append("no definition block")
    if "takeaways" not in body: warns.append("no key takeaways")
    print(f"{path}: {words} words")
    return errs, warns

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?"); ap.add_argument("--keyword", default=""); ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if a.all:
        root = Path(__file__).resolve().parent.parent
        errs = [e for p in list((root / "content").rglob("*.*")) + list((root / "templates").rglob("*.html")) + list((root / "static").rglob("*.*")) if p.suffix in (".md", ".html", ".json", ".txt", ".css", ".svg") for e in dash_errors(p)]
        warns = []
    else:
        errs, warns = check_post(a.path, a.keyword)
    for w in warns: print("WARN ", w)
    for e in errs: print("ERROR", e)
    print("OK" if not errs else f"{len(errs)} error(s)")
    sys.exit(1 if errs else 0)
