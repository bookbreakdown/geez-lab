#!/usr/bin/env python3
"""
Reconcile two independent transcription passes of the same folio.

Pass 1 is produced here. Pass 2 is produced in a ChatGPT project and pasted
back. Neither sees the other, which is the whole point: agreement between two
systems that share an architecture measures nothing, and agreement between two
that have seen each other's output measures less than nothing.

  passes/claude/MAIX1-153R.md     pass 1, in the PROJECT-PROMPT.md format
  passes/chatgpt/MAIX1-153R.md    pass 2, same format

Produces, per folio:
  reconciled/MAIX1-153R.md        agreed text, with every disagreement marked

This is a historical comparison utility, retained to reproduce disagreements.
Disagreement is not character error rate, and agreement does not establish a
correct reading. A question-mark count does not establish image or reading
quality. See docs/METHODOLOGY.md for the limits of this experiment.

Ge’ez Lab / https://ethiopiancanon.com. Code licensed under MIT.
"""
import re, sys, difflib
from pathlib import Path

LAB = Path(__file__).resolve().parent
OUT = LAB / 'reconciled'
SECTIONS = ['TRANSCRIPTION', 'LITERAL', 'PROSE', 'UNCERTAIN', 'CONFIDENCE']


def parse(path: Path) -> dict:
    """Pull the PROJECT-PROMPT.md sections out of one pass."""
    txt = path.read_text(encoding='utf-8')
    out = {'code': txt.strip().split('\n')[0].strip()}
    for i, name in enumerate(SECTIONS):
        nxt = SECTIONS[i + 1] if i + 1 < len(SECTIONS) else None
        pat = rf'##\s*{name}\s*\n(.*?)(?=\n##\s*{nxt}\b|\Z)' if nxt else rf'##\s*{name}\s*\n(.*)'
        m = re.search(pat, txt, re.S | re.I)
        out[name.lower()] = m.group(1).strip() if m else ''
    return out


def eth(s: str) -> list:
    """Ethiopic words only, so punctuation and layout do not count as disagreement."""
    return [w for w in re.split(r'[\s፡።፣፤፥፦፧፨]+', s) if any(0x1200 <= ord(c) <= 0x137F for c in w)]


def reconcile(code: str) -> dict | None:
    p1, p2 = LAB / 'passes/claude' / f'{code}.md', LAB / 'passes/chatgpt' / f'{code}.md'
    if not (p1.exists() and p2.exists()):
        return None
    a, b = parse(p1), parse(p2)
    for src, d in (('claude', a), ('chatgpt', b)):
        if d['code'] != code:
            print(f"  !! {code}: {src} echoed '{d['code']}' — key mismatch, not reconciled")
            return None

    wa, wb = eth(a['transcription']), eth(b['transcription'])
    sm = difflib.SequenceMatcher(None, wa, wb)
    agreed = sum(bl.size for bl in sm.get_matching_blocks())
    total = max(len(wa), len(wb)) or 1
    rate = 1 - agreed / total

    lines, diffs = [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            lines.append(' '.join(wa[i1:i2]))
        else:
            x, y = ' '.join(wa[i1:i2]) or '—', ' '.join(wb[j1:j2]) or '—'
            diffs.append((x, y))
            lines.append(f'⟦{x} | {y}⟧')

    OUT.mkdir(parents=True, exist_ok=True)
    doc = [f'# {code}', '',
           f'**Agreement {agreed}/{total} words — disagreement rate {rate*100:.1f}%**', '',
           '## RECONCILED TRANSCRIPTION',
           'Marked ⟦pass1 | pass2⟧ where the two disagree. Every mark is a question',
           'for a Ge\'ez reader, not a decision we have made.', '',
           ' '.join(lines), '']
    if diffs:
        doc += ['## DISAGREEMENTS', '', '| pass 1 (Claude) | pass 2 (ChatGPT) |', '|---|---|']
        doc += [f'| {x} | {y} |' for x, y in diffs]
        doc.append('')
    doc += ['## PROSE — pass 1', '', a['prose'], '',
            '## PROSE — pass 2', '', b['prose'], '',
            '## UNCERTAINTIES DECLARED', '',
            '**pass 1:** ' + (a['uncertain'] or 'none'), '',
            '**pass 2:** ' + (b['uncertain'] or 'none'), '']
    (OUT / f'{code}.md').write_text('\n'.join(doc), encoding='utf-8')
    return {'code': code, 'agreed': agreed, 'total': total, 'rate': rate, 'diffs': len(diffs)}


if __name__ == '__main__':
    codes = sys.argv[1:] or sorted(p.stem for p in (LAB / 'passes/claude').glob('*.md'))
    rows = [r for c in codes if (r := reconcile(c))]
    if not rows:
        print('nothing to reconcile — need the same code in both passes/claude and passes/chatgpt')
        sys.exit(0)
    print(f"{'folio':<14}{'agreed':>10}{'disagree':>10}{'rate':>9}")
    print('-' * 43)
    for r in rows:
        print(f"{r['code']:<14}{r['agreed']:>6}/{r['total']:<4}{r['diffs']:>9}{r['rate']*100:>8.1f}%")
    tot = sum(r['total'] for r in rows); ag = sum(r['agreed'] for r in rows)
    print('-' * 43)
    print(f"{'ALL':<14}{ag:>6}/{tot:<4}{sum(r['diffs'] for r in rows):>9}{(1-ag/tot)*100:>8.1f}%")
    print(f"\nreconciled files in {OUT}")
