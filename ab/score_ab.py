#!/usr/bin/env python3
"""Compare saved low- and high-resolution readings from three manuscript sides.

Reports character and token similarity, type-token ratios, and a heuristic share
of substitutions within Ethiopic consonant blocks. These are exploratory output
comparisons, not character error rates. A low type-token ratio warrants review;
it does not prove fabrication. The consonant-block heuristic is not a complete
linguistic classification.

Ge’ez Lab / https://ethiopiancanon.com. Code licensed under MIT.
"""
import re, sys, unicodedata
from difflib import SequenceMatcher
from pathlib import Path

LAB = Path(__file__).resolve().parent
ETH = re.compile(r'[ሀ-፿]')
SEP = re.compile(r'[፡።፨\s]+')

def load(p):
    t = p.read_text(encoding='utf-8', errors='replace')
    body = [l for l in t.splitlines()
            if re.match(r'\s*\d+[.):\]]?\s', l) and ETH.search(l)]
    return ' '.join(re.sub(r'^\s*\d+[.):\]]?\s*', '', l) for l in body)

def ttr(s):
    w = [x for x in SEP.split(s) if ETH.search(x)]
    return (len(set(w)) / len(w) if w else 0), len(w)

def base(ch):
    """Ethiopic syllables run in blocks of 8 from a consonant base."""
    o = ord(ch)
    return (o - 0x1200) // 8 if 0x1200 <= o <= 0x1357 else None

def vowel_share(a, b):
    """Of substituted characters, how many share a consonant base?"""
    sm = SequenceMatcher(None, a, b, autojunk=False)
    same = diff = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'replace':
            continue
        for x, y in zip(a[i1:i2], b[j1:j2]):
            bx, by = base(x), base(y)
            if bx is None or by is None:
                continue
            diff += 1
            if bx == by:
                same += 1
    return (same / diff if diff else 0), diff

print(f"{'folio':<8} {'lo chars':>8} {'hi chars':>8} {'char':>7} {'word':>7} "
      f"{'TTR lo':>7} {'TTR hi':>7} {'vowel-only':>11}")
print("-" * 76)
rows = []
for f in ('153R', '154R', '155R'):
    lo, hi = LAB / f"out-lo-{f}.txt", LAB / f"out-hi-{f}.txt"
    if not (lo.exists() and hi.exists()):
        print(f"{f:<8} waiting  (lo={'y' if lo.exists() else 'n'} hi={'y' if hi.exists() else 'n'})")
        continue
    a, b = load(lo), load(hi)
    ac = ''.join(ETH.findall(a)); bc = ''.join(ETH.findall(b))
    char = SequenceMatcher(None, ac, bc, autojunk=False).ratio()
    wa = [x for x in SEP.split(a) if ETH.search(x)]
    wb = [x for x in SEP.split(b) if ETH.search(x)]
    word = SequenceMatcher(None, wa, wb, autojunk=False).ratio()
    ta, _ = ttr(a); tb, _ = ttr(b)
    vs, nd = vowel_share(ac, bc)
    rows.append((char, word, vs))
    print(f"{f:<8} {len(ac):>8} {len(bc):>8} {char:>6.1%} {word:>6.1%} "
          f"{ta:>6.2f} {tb:>6.2f} {vs:>10.1%} ({nd})")
if rows:
    n = len(rows)
    print("-" * 76)
    print(f"{'MEAN':<8} {'':>8} {'':>8} {sum(r[0] for r in rows)/n:>6.1%} "
          f"{sum(r[1] for r in rows)/n:>6.1%}")
