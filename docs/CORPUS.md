# Corpus guide

A research resource from [EthiopianCanon.com](https://ethiopiancanon.com).

## File names and layers

`MAIX1-153R` means Tübingen Ma IX 1, leaf 153, recto. `V` means verso.
A “side” is one photographed page; a leaf has two sides.

| Directory | Files | Meaning |
| --- | ---: | --- |
| `passes/calibrated/` | 68 | Main run, 156r–189v; provisional Ge’ez, gist, numerals, confidence, notes |
| `passes/claude/` | 21 | Earlier machine readings with transcription and English layers |
| `passes/chatgpt/` | 25 | Earlier independent comparison readings |
| `passes/chatgpt-high/` | 1 | Additional experiment, overlapping an existing side |
| `reconciled/` | 8 | Historical two-pass comparisons with disagreements shown |
| `ab/out-*.txt` | 6 | Three sides at two resolutions |
| `groundtruth/out-*.txt` | 12 | Calibration and numeral investigations; not exact ground truth |

The archived `audits/batch1-chatgpt-review.md` in the original workspace described
an intended 40-side batch. Only 25 files survive in `passes/chatgpt/`; this public
package uses observed counts and makes no 40-file completion claim.

## Status of the text

Reading files are preserved byte for byte from the import. They contain
mistakes, conflicting hypotheses, confidence claims, and some conclusions
retracted later. Read [STATUS.md](STATUS.md), [HISTORY.md](HISTORY.md), and the
[handover](../HANDOVER.md) before citing a claim inside one of them.

The main drafts are not a continuous polished English translation. `GIST`
sections summarise a reader’s interpretation. Earlier `LITERAL` and `PROSE`
sections are experimental English renderings and carry their own uncertainties.

Historical model labels are retained as recorded. Exact provider model IDs,
versions, prompts, and sampling parameters were not consistently captured.
Comparisons are exploratory records, not a general model benchmark.

## Index and provenance

[folios.csv](../folios.csv) has 249 unique sides with source canvas numbers and
provisional catalogue allocations. `VI;VII` on 241r records the original shared
boundary rather than duplicating the image. The allocation is not verified text
identification.

[import-manifest.json](import-manifest.json) records source hashes and the parent
checkout’s commit at packaging time, including that uncommitted work was included.
[release-manifest.json](release-manifest.json) records hashes of the published
research artifacts. Public context notices were added to the handover and key;
the archived reading files were not normalised or rewritten.

The full private run log, expired operating briefs, and discarded reference
answer packs are not distributed. [HISTORY.md](HISTORY.md) preserves the main
experiment outcomes and retractions in a readable public form.
