#!/usr/bin/env python3
"""Cross-compare saved readings of a side in the resolution experiment.

Historical run labels are retained. Similarity to another model is an exploratory
comparison, not accuracy against a verified transcription. Small changes may be
run-to-run variation; shared mistakes may increase apparent agreement.

Ge’ez Lab / https://ethiopiancanon.com. Code licensed under MIT.
"""
import re, sys
from difflib import SequenceMatcher
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
ETH = re.compile(r'[ሀ-፿]')

def chars(p):
    if not p.exists():
        return None
    t = p.read_text(encoding='utf-8', errors='replace')
    # historical passes: everything under ## TRANSCRIPTION until the next heading
    m = re.search(r'##\s*TRANSCRIPTION(.*?)(?=\n##|\Z)', t, re.S)
    if m:
        t = m.group(1)
    else:
        t = '\n'.join(l for l in t.splitlines()
                      if re.match(r'\s*\d+[.):\]]?\s', l) and ETH.search(l))
    return ''.join(ETH.findall(t))

def sim(a, b):
    return SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else None

folio = sys.argv[1] if len(sys.argv) > 1 else '153R'
srcs = {
    'fable-43px  (new)':  LAB / f'ab/out-lo-{folio}.txt',
    'fable-87px  (new)':  LAB / f'ab/out-hi-{folio}.txt',
    'fable-43px  (Sep14)': LAB / f'passes/claude/MAIX1-{folio}.md',
    'astra-43px  (Sep14)': LAB / f'passes/chatgpt/MAIX1-{folio}.md',
}
got = {k: chars(v) for k, v in srcs.items()}
print(f"=== {folio} ===")
for k, v in got.items():
    print(f"  {k:<22} {'MISSING' if v is None else str(len(v)) + ' chars'}")
keys = [k for k, v in got.items() if v]
if len(keys) < 2:
    sys.exit()
print(f"\n  {'':<22}" + ''.join(f"{k.split()[0][:9]:>11}" for k in keys))
for a in keys:
    row = f"  {a:<22}"
    for b in keys:
        s = sim(got[a], got[b])
        row += f"{'-':>11}" if a == b else f"{s:>10.1%} "
    print(row)

astra = 'astra-43px  (Sep14)'
lo, hi = 'fable-43px  (new)', 'fable-87px  (new)'
if got.get(astra) and got.get(lo) and got.get(hi):
    a, b = sim(got[lo], got[astra]), sim(got[hi], got[astra])
    print(f"\n  THE TEST - agreement with the independent model (Astra):")
    print(f"    Fable at 43px : {a:.1%}")
    print(f"    Fable at 87px : {b:.1%}")
    d = b - a
    verdict = ("resolution RECOVERS signal" if d > 0.03 else
               "resolution LOSES signal" if d < -0.03 else
               "no material change")
    print(f"    delta         : {d:+.1%}   -> {verdict}")
