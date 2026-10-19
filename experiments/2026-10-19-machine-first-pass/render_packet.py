#!/usr/bin/env python3
"""Render the reviewed draft without generating or changing translations.
Ge’ez Lab / https://ethiopiancanon.com. MIT.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent

def main():
    data = json.loads((HERE / 'reviewed-draft.json').read_text())
    images = {r['side']: r for r in json.loads((HERE / 'provenance.json').read_text())['images']}
    changes = json.loads((HERE / 'revision-log.json').read_text())['changes']
    headings = {'169R': 'Hearing, reception, and stewardship', '169V': 'The tabernacle and Moses on Sinai', '170R': 'Offerings and the pattern of the Church', '170V': 'Holy ground, Zion, and the golden lampstand', '171R': 'Steadfastness and the martyrs'}
    out = ['# Five consecutive sides: machine English first pass', '', 'Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.', '', '**169r–171r · five consecutive manuscript sides · 118 source lines.**', '', 'This is provisional AI translation for correction, not expert-verified English. Every recoverable clause was attempted; square brackets mark tentative readings, supplied wording, or unresolved source content. A source-line assignment is not proof that all meaning was recovered. Exact work identification remains unconfirmed; these sides lie in the catalogue-assigned missing-book range.', '', 'The initial translator received only numbered Ge’ez readings. The coordinating assistant then used the images, historical notes, and a separate machine review to prepare this version. Neither review establishes accuracy or human correction-time savings. See [report](REPORT.md), [image observations and joins](IMAGE-NOTES.md), and [machine review dispositions](REVIEW-DISPOSITIONS.md).', '', '## Reading the packet', '', 'Each numbered block names its manuscript line range. Page boundaries and repeated wording are retained; local uncertainty does not excuse skipping a whole passage. Footnotes are collected in [UNCERTAINTIES.md](UNCERTAINTIES.md). The [frozen Ge’ez](SOURCE-READINGS.md) and [raw translator response](runs/translate-five-sides.json) remain available. No text from the 2008 printed edition or its digitisation was used.', '']
    notes = ['# Uncertainty and revision register', '', 'Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.', '', 'Initial translator observations are retained below, followed by any coordinating revisions. They are hypotheses, not expert adjudications. Review this alongside the current English; an initial note may describe wording subsequently changed. Full before/after text is in [revision-log.json](revision-log.json).', '']
    for side in data['sides']:
        name=side['side'];image=images[name]
        out += [f'## {name.lower()} — {headings[name]}', '', f'[Source image, Tübingen canvas {image["canvas"]}]({image["image_url"]}) · [archived reading](../../passes/calibrated/MAIX1-{name}.md)', '']
        notes += [f'## {name}', '']
        for i, block in enumerate(side['blocks']):
            nums=block['lines'];location=str(nums[0]) if len(nums)==1 else f'{nums[0]}–{nums[-1]}'
            label=f'{name}-B{i+1:02d}'
            out += [f'**{label} · lines {location}.** {block["english"]}', '']
            if block.get('uncertainties'):
                notes += [f'### {label} · lines {location}', ''] + [f'- Initial translator: {n}' for n in block['uncertainties']] + ['']
            current=[c for c in changes if c['side']==name and c['block_index']==i]
            if current:
                if not block.get('uncertainties'):notes += [f'### {label} · lines {location}', '']
                notes += [f'- Coordinating revision: {c["reason"]}' for c in current]+['']
        if side.get('boundary_notes'):
            notes += ['### Current boundary notes', '']+[f'- {n}' for n in side['boundary_notes']]+['']
    out += ['## Next review', '', 'An expert can correct this packet block by block, preserving source readings and tracking omissions, additions, names, numbers, negation, and correction time. Machine drafting can continue while that review is arranged; this batch alone does not justify automatic publication of an English edition.', '']
    (HERE/'ENGLISH-FIRST-PASS.md').write_text('\n'.join(out).rstrip()+'\n')
    (HERE/'UNCERTAINTIES.md').write_text('\n'.join(notes).rstrip()+'\n')

if __name__ == '__main__':
    main()
