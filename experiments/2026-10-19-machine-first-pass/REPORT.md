# Five-side machine first pass: 169r–171r

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.

## Deliverable

[Read the provisional English](ENGLISH-FIRST-PASS.md): **five consecutive sides,
118 manuscript lines, 21 translation blocks**. All source lines are assigned to
blocks, including passages that could only be represented by a bracketed gap or
tentative interpretation. This is a new English drafting/review layer over five
previously transcribed sides, not 118 newly transcribed lines or five additions
to the historical 68-side corpus. Expert accuracy and correction time remain
unmeasured.

The result advances the machine first pass while expert review is being arranged.
It is not a finished translation, a reliable automatic correction system, or proof
that a larger unattended batch would meet a publication standard. Exact work
identification remains provisional within the catalogue-assigned missing-book
range. This batch was selected for consecutive discourse and available images,
not randomly or as fresh held-out reference material.

## Procedure actually followed

1. Froze the five existing Ge’ez transcriptions and numbered **24, 24, 23, 24,
   and 23 lines** respectively. The [protocol](PROTOCOL.md),
   [source readings](SOURCE-READINGS.md), hashes, and exact requests are retained.
2. Generated a new English draft from those Ge’ez lines only. The translator
   did not receive old English, gists, French, work identifications, or a modern
   edition. This input separation does not exclude prior model-training exposure.
3. The coordinating assistant viewed overlapping upper/middle/lower regions of
   every source image and two external boundary regions. This reviewer had read
   historical notes/gists and is not independent or blind. Eighteen image/source
   priorities and all six batch boundaries are recorded in [IMAGE-NOTES.md](IMAGE-NOTES.md).
4. A separate inference attempted to review the **initial** English against
   frozen Ge’ez, without images or coordinator notes. Its returned text failed
   JSON parsing. The failure and request are retained, but the original wrapper
   did not save the response/envelope before parsing; no findings or usage total
   can be recovered from that attempt. The wrapper now saves a sanitised envelope
   before parsing. A single explicit recovery call, with enforced output schema,
   reviewed the **coordinator-revised** English against Ge’ez and returned eight
   flags. This is not an exhaustive audit or an expert review.
5. The coordinator revised English, retained unresolved alternatives, and recorded
   before/after changes in [revision-log.json](revision-log.json). Initial output
   remains unchanged in [the translator run](runs/translate-five-sides.json).
   [Review dispositions](REVIEW-DISPOSITIONS.md) distinguish accepted cautions
   from findings not established by the text.

The recovery call reviewed the coordinating draft; dispositions record the
further changes after that review. Three calls were attempted, reaching the
protocol cap; no automatic retry or fourth call was made. Source reading
files remain unchanged. The two 153r Transkribus variants and earlier French
pilot are separate experiments; no Transkribus recognition was obtained for
these five sides.

The machine reviewer also made unsupported claims: it introduced a lord/master
noun not present in the cited source string, disputed a bracketed bride reading
with an unverified gloss, and attributed already translated clauses to incorrect
block indices. Those recommendations were not automatically accepted. This
reinforces the need for source-based disposition rather than an evaluator score.

## Findings affecting the draft

- A full consecutive packet can be produced from the current source readings
  without waiting for new HTR or expert input. Meaning is recoverable in substantial
  stretches, but no numerical accuracy or readability score is established.
- At 170r/170v, the “from within” expression crosses the physical page break.
  Reading it together avoids the old gist's misplaced “is holy” opening.
- The first draft added specificity at weak source points: a saw, a named group
  across a difficult boundary, an unmarked speaker change, and a bride/soul
  construction. The coordinating version removes or brackets those assumptions.
- Repeated offering terms, raised-hand imagery, and the four forty-values in
  Moses' days/nights pairs are retained. Negative and singular/plural ambiguities
  are not silently regularised into familiar scripture.
- Two joins remain linguistically unresolved: 169r/169v and the final word of
  170v continued on 171r. Neither implies a missing page. The batch starts and
  ends within larger discourse.

The translator's proposals and the reviewer's claims are evidence to inspect,
not ground truth. Do not count flags, brackets, model agreement, or source-line
assignment as translation accuracy. No head-to-head timing comparison was run.

## Reproduction and checks

The inference runner is [run_batch.py](run_batch.py); it requires the authenticated
Claude CLI and refuses automatic retries. Calls used safe mode, no tools/MCP,
an isolated temporary working directory, no session persistence, medium effort,
and a per-call reported budget cap. [The ledger](runs/ledger.json) records actual
cost/time. Retained results are sufficient to inspect the experiment without
rerunning paid or allowance-consuming calls.

Run structural verification and regenerate the readable packet:

```bash
python3 experiments/2026-10-19-machine-first-pass/validate_batch.py
python3 experiments/2026-10-19-machine-first-pass/render_packet.py
python3 scripts/validate_release.py
python3 -m unittest discover -s tests -q
```

These verify frozen hashes, request/result association, complete line assignment,
logged revisions, links, and package integrity. They do not verify Ge’ez or English
meaning. Model/call accounting is summarised in [ACCOUNTING.md](ACCOUNTING.md).

## Next machine work

Use this packet as the batch format: source-linked English, explicit uncertainties,
join notes, and a bounded review pass. Continue adjoining material in similarly
small batches, maintaining a terminology and unresolved-reading register.
Target image rereads at negation, names, numbers, joins, and any clause whose
meaning is blocked. Improve prompts only for a demonstrated recurring failure;
no larger genetic search is justified by this run. Expert correction time and
residual substantive errors remain the eventual quality test.

All research is attributed to EthiopianCanon.com. Manuscript images are from
University Library Tübingen, Ma IX 1; hashes and source links are in
[provenance.json](provenance.json). Images are excluded from Git. The 2008 edition
and derived digitisation were not used.
