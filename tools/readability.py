#!/usr/bin/env python3
"""Readability check (Scott Adams + Orwell rules from the steer-blog-conveyor skill).
Usage: python3 tools/readability.py content/blog/<slug>.md
Targets: average sentence under 15 words, none over 25, zero filler, stock phrases, long words, softeners; passive under 10%.
"""
import re, sys
t = open(sys.argv[1]).read().split('---', 2)[-1]
t = re.sub(r'<[^>]+>|\[([^\]]*)\]\([^)]*\)|^#+ .*$|^\|.*$', lambda m: m.group(1) or ' ', t, flags=re.M)
s = [x for x in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', t)) if len(x.split()) > 2]
L = [len(x.split()) for x in s]
fill = r'\b(very|really|quite|just|actually|basically|simply|truly|highly|extremely|incredibly|in order to|the fact that)\b'
stock = r'(at the end of the day|game.changer|low.hanging fruit|move the needle|silver lining|perfect storm|tip of the iceberg|outside the box|no stone unturned|hit the ground running|double.edged sword|recipe for disaster|driver.s seat)'
long = r'\b(utilize|facilitate|commence|demonstrate|endeavou?r|sufficient|approximately|purchase|synergy|leverage|optimi[sz]e|stakeholders?|paradigm|holistic)\b'
soft = r'(it might be a good idea|you may want to consider|you might want to|it could be worth)'
passive = sum(bool(re.search(r'\b(is|are|was|were|be|been|being)\s+\w+ed\b', x)) for x in s)
print(f'sentences {len(s)}, avg {sum(L)/len(L):.1f} words, over 25: {sum(l>25 for l in L)}, passive {100*passive/len(s):.0f}%')
for name, rx in (('filler', fill), ('stock phrases', stock), ('long words', long), ('softeners', soft)):
    hits = re.findall(rx, t, flags=re.I)
    print(name, len(hits), sorted(set(h if isinstance(h, str) else h[0] for h in hits)))
for x in s:
    if len(x.split()) > 25: print('LONG:', x[:160])
