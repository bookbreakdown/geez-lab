#!/usr/bin/env python3
"""Display neighbouring transcription lines, line counts, and type-token ratios.

This supports manual continuity review; it does not establish that two readings
are correct or automatically decide whether their grammar joins. Only sequential
numbered lines inside TRANSCRIPTION are inspected, avoiding matches in notes.

Ge’ez Lab / https://ethiopiancanon.com. Code licensed under MIT.
"""
import re, glob, os, sys
from pathlib import Path

D = str(Path(__file__).resolve().parent / 'passes' / 'calibrated') + os.sep
ETH = re.compile(r'[ሀ-፿]')
SEP = re.compile(r'[፡።፨\s]+')
LATIN = re.compile(r'[A-Za-z]{3,}')
NUMBERED = re.compile(r'^\s*(\d+)[.):\]]\s*(.+)$')


def transcription(path):
    """Numbered lines of the TRANSCRIPTION block only, in order."""
    t = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'##\s*TRANSCRIPTION(.*?)(?=\n##|\Z)', t, re.S)
    if not m:
        return []
    out, expect = [], 1
    for raw in m.group(1).splitlines():
        g = NUMBERED.match(raw)
        if not g:
            continue
        n, body = int(g.group(1)), g.group(2).strip()
        # A notes sentence is Latin prose; a transcription line is Ethiopic and
        # may carry editorial markers like [blot] or [illegible]. Strip anything
        # bracketed before testing, or the marker kills the line and the whole
        # sequence stops there - which silently truncated f.160v from 23 lines
        # to 16 the first time this ran.
        if not ETH.search(body) or LATIN.search(re.sub(r'\[[^\]]*\]', '', body)):
            continue
        if n != expect:            # out of sequence means we left the block
            if n == 1 and out:
                break
            continue
        out.append(body)
        expect += 1
    return out


def folio_key(code):
    return (int(code[:-1]), 0 if code[-1] == 'R' else 1)


files = {os.path.basename(f)[6:10]: f for f in glob.glob(D + '*.md')}
codes = sorted(files, key=folio_key)

print(f"{'folio':<8} {'lines':>5} {'chars':>6} {'TTR':>6}   flag")
print("-" * 46)
tx = {}
for c in codes:
    L = transcription(files[c])
    tx[c] = L
    s = ' '.join(L)
    w = [x for x in SEP.split(s) if ETH.search(x)]
    ttr = len(set(w)) / len(w) if w else 0
    flag = '' if ttr >= 0.8 else 'LOW - check WHICH words repeat'
    print(f"{c:<8} {len(L):>5} {len(ETH.findall(s)):>6} {ttr:>6.2f}   {flag}")

print(f"\n{'seam':<16} last line of A  ->  first line of B")
print("-" * 76)
joined = gaps = 0
for a, b in zip(codes, codes[1:]):
    fa, fb = folio_key(a), folio_key(b)
    adjacent = (fb[0] == fa[0] and fb[1] == 1) or (fb[0] == fa[0] + 1 and fa[1] == 1 and fb[1] == 0)
    if not adjacent:
        print(f"  {a}->{b:<8} GAP - folios missing between these")
        gaps += 1
        continue
    if not tx.get(a) or not tx.get(b):
        continue
    joined += 1
    print(f"  {a}->{b}")
    print(f"      ...{tx[a][-1][-34:]}")
    print(f"         {tx[b][0][:34]}...")
print(f"\n{joined} adjacent seams available, {gaps} gaps in the sequence.")
print("Read each pair: a grammatical continuation is positive evidence for BOTH pages.")
