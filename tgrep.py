#!/usr/bin/env python3
"""Search ONLY the ## TRANSCRIPTION block of the calibrated passes.

Twice tonight an ad-hoc grep over these files matched an agent's prose ABOUT the
text instead of the text: once on ቆዬስ (the word appeared only in its own NOTES),
once on ንፍቀ/አናጕንስጢስ (the words appeared only inside a Falsifiers section, and a
naive grep would have reported f.181v falsifying its own three-grade claim).

Both near-misses would have produced a confident, wrong finding. This restricts
to numbered transcription lines, the way seams.py already does.

    tgrep.py <pattern> [<pattern> ...]

Ge’ez Lab / https://ethiopiancanon.com. Code licensed under MIT.
"""
import re, sys, glob, os
from pathlib import Path

D = str(Path(__file__).resolve().parent / 'passes' / 'calibrated') + os.sep
ETH = re.compile(r'[ሀ-፿]')
LATIN = re.compile(r'[A-Za-z]{3,}')
NUM = re.compile(r'^\s*(\d+)[.):\]]\s*(.+)$')

def lines(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'##\s*TRANSCRIPTION(.*?)(?=\n##|\Z)', t, re.S)
    if not m:
        return []
    out, expect = [], 1
    for raw in m.group(1).splitlines():
        g = NUM.match(raw)
        if not g:
            continue
        n, body = int(g.group(1)), g.group(2).strip()
        if not ETH.search(body) or LATIN.search(re.sub(r'\[[^\]]*\]', '', body)):
            continue
        if n != expect:
            if n == 1 and out:
                break
            continue
        out.append((n, body)); expect += 1
    return out

pats = sys.argv[1:]
if not pats:
    sys.exit(__doc__)
for pat in pats:
    hits = []
    for f in sorted(glob.glob(D + '*.md')):
        code = os.path.basename(f)[6:10]
        for n, body in lines(f):
            if pat in body:
                hits.append((code, n, body))
    print(f"\n{pat}  —  {len(hits)} hit(s) in transcription")
    # No cap. The 12-line cap silently hid f.189v (alphabetically last) from its
    # own agent's search, which then had to reason around an absence that was an
    # artifact of this script. A truncated list looks exactly like a short list.
    for code, n, body in hits:
        print(f"  {code} l.{n:<3} {body[:56]}")
