# Steer, Don't Guess — book website

Source of https://mjirgensons.github.io (the website for *Steer, Don't Guess* by Martin Jirgenson, The Jirgenson Model).

- `content/` — Markdown pages and situations (one file = one page), `site.json`, `book.json` (prices, ASINs, links: the single source for buttons and JSON-LD).
- `templates/` — Jinja2 templates. `static/` — CSS, images, robots.txt.
- `build.py` — builds everything into `docs/`, which GitHub Pages serves (Settings → Pages → Deploy from branch `main`, folder `/docs`).

Build: `python3 build.py` (needs Python 3 with `markdown` and `jinja2`). Commit `docs/` together with the source.

Adding a situation page: copy a file in `content/situations/`, keep the front matter fields, run the build, commit. The FAQ block (`## FAQ` with `### question` items) becomes FAQPage JSON-LD automatically.

© Martin Jirgenson. Site code may be reused; texts and the book are not.
