"""Build the sundeco.ca mirror from docs/.

Layout:
  /                     author page (Martin Jirgenson, list of books)
  /steer-dont-guess/    the full book site (docs/ with every root-relative link prefixed)

Canonical, og:url and JSON-LD stay absolute on https://mjirgensons.github.io while that is the main site.
A future book is one more entry in BOOKS and one more folder.

Usage: python3 tools/build_mirror.py <out_dir>
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = json.loads((ROOT / "content" / "site.json").read_text())
BOOK_SLUG = "steer-dont-guess"
SKIP = {"CNAME", "googlee2e8a318213db3cc.html", "BingSiteAuth.xml"}

BOOKS = [
    {
        "slug": BOOK_SLUG,
        "title": "Steer, Don't Guess",
        "subtitle": "Setting Priorities, Reading the Numbers and Correcting Course in Business and Life",
        "year": "2026",
        "blurb": "A direct management method for business owners, CEOs and top managers: set priorities, "
                 "read the numbers and correct course before the damage arrives. Built on the Jirgenson Model.",
        "cover": f"/{BOOK_SLUG}/img/cover.jpg",
        "cover_webp": f"/{BOOK_SLUG}/img/cover.webp",
        "kindle": "https://www.amazon.com/dp/B0HPBR6BNX",
        "sample": f"/{BOOK_SLUG}/blog/free-sample/",
    },
]

ATTR = re.compile(r'(\s(?:href|src|action|poster)=")/(?!/)')
SRCSET = re.compile(r'(\ssrcset=")([^"]*)(")')
CSSURL = re.compile(r'url\((["\']?)/(?!/)')


def prefix_html(text: str) -> str:
    text = ATTR.sub(rf"\1/{BOOK_SLUG}/", text)

    def fix_srcset(m):
        parts = [p.strip() for p in m.group(2).split(",")]
        parts = [f"/{BOOK_SLUG}{p}" if p.startswith("/") and not p.startswith("//") else p for p in parts]
        return m.group(1) + ", ".join(parts) + m.group(3)

    return SRCSET.sub(fix_srcset, text)


def copy_book(out: Path):
    dest = out / BOOK_SLUG
    for src in DOCS.rglob("*"):
        rel = src.relative_to(DOCS)
        if src.is_dir() or rel.parts[0] in SKIP:
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".html":
            target.write_text(prefix_html(src.read_text()))
        elif src.suffix == ".css":
            target.write_text(CSSURL.sub(rf"url(\1/{BOOK_SLUG}/", src.read_text()))
        else:
            shutil.copy2(src, target)


def book_card(b):
    return f"""
<article class="hub-book">
  <a class="hub-cover" href="/{b['slug']}/"><picture><source srcset="{b['cover_webp']}" type="image/webp"><img src="{b['cover']}" width="200" height="306" alt="{html.escape(b['title'])} book cover"></picture></a>
  <div>
    <h3><a href="/{b['slug']}/">{html.escape(b['title'])}</a></h3>
    <p class="hub-sub">{html.escape(b['subtitle'])} ({b['year']})</p>
    <p>{html.escape(b['blurb'])}</p>
    <div class="btn-row"><a class="btn btn-buy btn-sm" href="/{b['slug']}/">About the book</a><a class="btn btn-line btn-sm" href="{b['sample']}">Read Chapter 1 free</a><a class="btn btn-line btn-sm" href="{b['kindle']}" rel="noopener">Kindle</a></div>
  </div>
</article>"""


def hub_page() -> str:
    name = SITE["author"]
    desc = f"{name}: {SITE['author_title']}. Books and open methods for steering a business with numbers instead of guesses."
    person = {
        "@context": "https://schema.org", "@type": "Person", "name": name, "url": "https://sundeco.ca/",
        "jobTitle": SITE["author_title"], "image": f"https://sundeco.ca/{BOOK_SLUG}/img/martin-jirgenson.jpg",
        "sameAs": [SITE[k] for k in ("linkedin", "amazon_author", "goodreads_author", "wikidata_author", "orcid", "github_user") if SITE.get(k)],
    }
    links = [("LinkedIn", SITE["linkedin"]), ("Amazon author page", SITE["amazon_author"]),
             ("Goodreads", SITE["goodreads_author"]), ("GitHub", SITE["github_user"])]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#F7F8F6">
<title>{html.escape(name)}: author</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://sundeco.ca/">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="profile">
<meta property="og:title" content="{html.escape(name)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://sundeco.ca/">
<meta property="og:image" content="https://sundeco.ca/{BOOK_SLUG}/img/martin-jirgenson.jpg">
<link rel="icon" href="/{BOOK_SLUG}/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/{BOOK_SLUG}/css/site.css?v=3">
<style>
.hub-head{{display:flex;gap:24px;align-items:center;flex-wrap:wrap;padding:48px 0 24px}}
.hub-head img{{width:132px;height:132px;border-radius:50%;object-fit:cover}}
.hub-head h1{{margin:0 0 6px}}
.hub-lead{{color:var(--muted);margin:0}}
.hub-book{{display:grid;grid-template-columns:140px 1fr;gap:24px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-card);padding:24px;margin:16px 0}}
.hub-book h3{{margin:0 0 4px}} .hub-book h3 a{{color:var(--ink);text-decoration:none}}
.hub-sub{{color:var(--muted);margin:0 0 12px;font-size:15px}}
.hub-links{{display:flex;gap:16px;flex-wrap:wrap;padding:8px 0 48px}}
@media (max-width:560px){{.hub-book{{grid-template-columns:1fr}}.hub-cover img{{width:140px}}}}
</style>
<script type="application/ld+json">{json.dumps(person)}</script>
</head>
<body>
<main id="main" class="wrap" style="max-width:860px">
  <header class="hub-head">
    <picture><source srcset="/{BOOK_SLUG}/img/martin-jirgenson.webp" type="image/webp"><img src="/{BOOK_SLUG}/img/martin-jirgenson.jpg" width="132" height="132" alt="{html.escape(name)}"></picture>
    <div><h1>{html.escape(name)}</h1><p class="hub-lead">{html.escape(SITE['author_title'])} · {html.escape(SITE['author_location'])}</p></div>
  </header>
  <p>I build business systems that scale, operate reliably and drive revenue. With over 25 years of experience in business development and operations, I rely on hard data and practical execution rather than guesswork.</p>
  <h2>Books</h2>
  {''.join(book_card(b) for b in BOOKS)}
  <h2>Find me</h2>
  <div class="hub-links">{''.join(f'<a href="{u}" rel="noopener">{t}</a>' for t, u in links)}<a href="/{BOOK_SLUG}/contact/">Contact</a></div>
</main>
</body>
</html>
"""


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    copy_book(out)
    (out / "index.html").write_text(hub_page())
    (out / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    shutil.copy2(DOCS / "404.html", out / "404.html")
    (out / "404.html").write_text(prefix_html((DOCS / "404.html").read_text()))
    print(f"mirror built -> {out}")


if __name__ == "__main__":
    main()
