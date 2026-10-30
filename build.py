#!/usr/bin/env python3
"""Static site generator for the Steer, Don't Guess book site.
Markdown + front matter in content/, Jinja2 templates in templates/, output in docs/ (GitHub Pages).
Run: python3 build.py
"""
import json, re, shutil, datetime, html
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SITE = json.loads((ROOT / "content" / "site.json").read_text())
BOOK = json.loads((ROOT / "content" / "book.json").read_text())

env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
def nice_date(v):
    try:
        d = datetime.date.fromisoformat(str(v)); return f"{d.day} {d.strftime('%b')} {d.year}"
    except Exception:
        return v
env.filters["nice_date"] = nice_date
md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3"}})

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

def parse_fm(block):
    meta = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()]
            elif v.lower() in ("true", "false"):
                v = v.lower() == "true"
            else:
                v = v.strip('"')
            meta[k.strip()] = v
    return meta

def parse(path: Path):
    text = path.read_text()
    m = FM_RE.match(text)
    meta, body = {}, text
    if m:
        meta = parse_fm(m.group(1))
        body = m.group(2)
    # FAQ block: "## FAQ" followed by "### question" + answer paragraphs, until next "## " or end
    faq = []
    fm = re.search(r"\n## FAQ\n(.*?)(?=\n## |\Z)", body, re.S)
    if fm:
        for q in re.split(r"\n### ", "\n" + fm.group(1).strip())[1:]:
            lines = q.strip().split("\n", 1)
            question = lines[0].strip()
            answer = re.sub(r"\s+", " ", lines[1].strip()) if len(lines) > 1 else ""
            faq.append({"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}})
        body = body.replace(fm.group(0), "\n")
    meta["faq_jsonld"] = faq
    md.reset()
    html_body = md.convert(body)
    meta["toc"] = md.toc
    return meta, html_body

def words(html_text):
    return len(re.sub(r"<[^>]+>", " ", html_text).split())

def wrap_tables(html_text):
    # every table scrolls inside its own box on phones (design v2)
    html_text = re.sub(r"<table\b", '<div class="tbl"><table', html_text)
    return html_text.replace("</table>", "</table></div>")

def external_new_tab(html_text):
    # links that leave the site open in a new tab so the reader keeps the page (Martin, 2026-10-30)
    def fix(m):
        tag = m.group(0)
        href = re.search(r'href="([^"]+)"', tag)
        if not href or not href.group(1).startswith("http") or "mjirgensons.github.io" in href.group(1):
            return tag
        tag = re.sub(r'\s(target|rel)="[^"]*"', "", tag)
        return tag[:-1] + ' target="_blank" rel="noopener">'
    return re.sub(r"<a\b[^>]*>", fix, html_text)

def straight_apostrophes(html_text):
    # one apostrophe style across the site: straight ' (Martin, 2026-10-30)
    return html_text.replace("\u2019", "'").replace("\u2018", "'")

def write(url_path: str, html_text: str):
    html_text = straight_apostrophes(external_new_tab(wrap_tables(html_text)))
    p = OUT / url_path.strip("/") / "index.html" if url_path not in ("", "/") else OUT / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html_text)

def abs_url(path):
    return SITE["url"].rstrip("/") + "/" + path.strip("/") + ("/" if path.strip("/") else "")

def render(template, **ctx):
    t = env.get_template(template)
    return t.render(site=SITE, book=BOOK, now=datetime.date.today().isoformat(), abs_url=abs_url, **ctx)

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "static", OUT, dirs_exist_ok=True)

    pages = []  # for sitemap: (url, lastmod, priority)

    # ---- blog posts (content/blog/*.md and *.html)
    posts = []
    for f in sorted((ROOT / "content" / "blog").iterdir()):
        if f.suffix == ".md":
            meta, body = parse(f)
        elif f.suffix == ".html":
            text = f.read_text(); m = FM_RE.match(text)
            meta, _ = parse_fm(m.group(1)), None
            body = m.group(2); meta["faq_jsonld"] = []
        else:
            continue
        if meta.get("draft"):
            continue
        slug = meta.get("slug") or f.stem
        h2s = re.findall(r'<h2\s+id="([^"]+)"[^>]*>(.*?)</h2>', body, re.S)
        meta.update(slug=slug, url=f"/blog/{slug}/", body=body, words=words(body),
                    sections=[(i, re.sub(r"<[^>]+>", "", t)) for i, t in h2s])
        posts.append(meta)
    posts.sort(key=lambda m: (bool(m.get("pinned")), m.get("date", "")), reverse=True)
    for m in posts:
        related = [s for s in posts if s["slug"] != m["slug"]][:3]
        write(m["url"], render("post.html", page=m, related=related))
        pages.append((m["url"], m.get("updated", m.get("date")), "0.9" if m.get("pinned") else "0.8"))
    write("/blog/", render("blog_index.html", page={"url": "/blog/", "title": "Blog: the Jirgenson Model in practice", "description": "Free chapters of Steer, Don't Guess and articles on business situations: crisis, priorities, cash, levers, plans that fail, AI for business decisions. Each post names the chapter that covers it."}, posts=posts))
    pages.append(("/blog/", datetime.date.today().isoformat(), "0.8"))
    # old /situations/ URLs -> /blog/ (never submitted to search engines; kept as redirects)
    for slug in ["business-crisis-what-to-do-first", "set-priorities-refusal-order", "busy-but-not-profitable", ""]:
        target = abs_url(f"/blog/{slug}/" if slug else "/blog/")
        p = OUT / "situations" / slug / "index.html" if slug else OUT / "situations" / "index.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f'<!doctype html><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="{target}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={target}"><a href="{target}">{target}</a>')
    sits = posts

    # ---- simple pages from content/pages/*.md
    for f in sorted((ROOT / "content" / "pages").glob("*.md")):
        meta, body = parse(f)
        url = meta.get("url", f"/{f.stem}/")
        meta.update(url=url, body=body)
        write(url, render(meta.get("template", "page.html"), page=meta))
        pages.append((url, meta.get("updated", datetime.date.today().isoformat()), meta.get("priority", "0.7")))

    # ---- home
    hm, hbody = parse(ROOT / "content" / "home.md")
    hm.update(url="/", body=hbody)
    write("/", render("home.html", page=hm, situations=sits[:4]))
    pages.insert(0, ("/", hm.get("updated", datetime.date.today().isoformat()), "1.0"))

    # ---- 404
    (OUT / "404.html").write_text(straight_apostrophes(external_new_tab(render("404.html", page={"url": "/404.html", "title": "Undefined zone: no data here", "description": "Page not found."}))))

    # ---- sitemap, rss, llms.txt
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lm, pr in pages:
        sm.append(f"  <url><loc>{abs_url(u)}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm))

    rss = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
           f"<title>{html.escape(SITE['name'])}: Blog</title>", f"<link>{SITE['url']}</link>",
           f"<description>{html.escape(SITE['description'])}</description>"]
    for m in sits:
        rss.append(f"<item><title>{html.escape(m['title'])}</title><link>{abs_url(m['url'])}</link><guid>{abs_url(m['url'])}</guid>"
                   f"<pubDate>{datetime.datetime.fromisoformat(m['date']).strftime('%a, %d %b %Y 00:00:00 GMT')}</pubDate>"
                   f"<description>{html.escape(m.get('description',''))}</description></item>")
    rss.append("</channel></rss>")
    (OUT / "rss.xml").write_text("\n".join(rss))

    llms = [f"# {SITE['name']}", "", f"> {SITE['description']}", "", "## Pages", ""]
    for u, lm, pr in pages:
        llms.append(f"- {abs_url(u)}")
    (OUT / "llms.txt").write_text("\n".join(llms) + "\n")

    print(f"built {len(pages)} pages -> {OUT}")

if __name__ == "__main__":
    main()
