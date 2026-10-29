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
md = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "smarty"], extension_configs={"toc": {"toc_depth": "2-3"}})

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

def parse(path: Path):
    text = path.read_text()
    m = FM_RE.match(text)
    meta, body = {}, text
    if m:
        for line in m.group(1).splitlines():
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

def write(url_path: str, html_text: str):
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

    # ---- situations (articles)
    sits = []
    for f in sorted((ROOT / "content" / "situations").glob("*.md")):
        meta, body = parse(f)
        if meta.get("draft"):
            continue
        slug = meta.get("slug") or f.stem
        meta.update(slug=slug, url=f"/situations/{slug}/", body=body, words=words(body))
        sits.append(meta)
    sits.sort(key=lambda m: m.get("date", ""), reverse=True)
    for m in sits:
        related = [s for s in sits if s["slug"] != m["slug"]][:3]
        write(m["url"], render("situation.html", page=m, related=related))
        pages.append((m["url"], m.get("updated", m.get("date")), "0.8"))
    write("/situations/", render("situations_index.html", page={"url": "/situations/", "title": "Situations: which chapter answers your question", "description": "Business situations, one page each, with the chapter of Steer, Don't Guess that answers them: crisis, priorities, cash, levers, plans that fail."}, situations=sits))
    pages.append(("/situations/", datetime.date.today().isoformat(), "0.7"))

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
    write("/", render("home.html", page=hm, situations=sits[:3]))
    pages.insert(0, ("/", hm.get("updated", datetime.date.today().isoformat()), "1.0"))

    # ---- 404
    (OUT / "404.html").write_text(render("404.html", page={"url": "/404.html", "title": "Undefined zone: no data here", "description": "Page not found."}))

    # ---- sitemap, rss, llms.txt
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lm, pr in pages:
        sm.append(f"  <url><loc>{abs_url(u)}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm))

    rss = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
           f"<title>{html.escape(SITE['name'])}: Situations</title>", f"<link>{SITE['url']}</link>",
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
