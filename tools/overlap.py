#!/usr/bin/env python3
"""Share of 8-word sequences in NEW that also appear in OLD (visible text only). Target: under 3%.
Usage: python3 tools/overlap.py content/blog/old.md content/blog/new.md"""
import re, sys
def words(p):
    t = open(p).read().split('---', 2)[-1]
    t = re.sub(r'<[^>]+>|\]\([^)]*\)|[#*_`|>\[\]]', ' ', t).lower()
    return re.findall(r"[a-z0-9€%.']+", t)
def sh(w, n=8): return {' '.join(w[i:i+n]) for i in range(len(w)-n+1)}
a, b = sh(words(sys.argv[1])), sh(words(sys.argv[2]))
print(f"overlap {100*len(a & b)/max(len(b),1):.1f}% of new 8-word sequences")
