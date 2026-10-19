# Reference-guided translation pilot: preregistered small experiment

Ge’ez Lab / https://ethiopiancanon.com. Prepared 2026-10-16.

## Question
Can a small search over translation instructions improve English semantic
coverage against an aligned French witness on reserved passages? This is a
text-to-English smoke test, not an accuracy benchmark for manuscript reading.

## Frozen design
- Six short passages selected from historical machine transcriptions of Ma IX 1.
- Four development passages from41v/42r; two reserved passages from42v.
- Reserved passages are withheld from candidate generation, evaluation feedback,
  and mutation until a candidate is frozen. The data assembler saw them. These
  pages were used in earlier research and are not historically pristine tests.
- French: Grébaut, ROC17(1912), printed141–142, PDF145–146. Visually checked
  against the scans. Reference clauses outside the selected source or involving
  known differences are declared review-only before running.
- Translation requests contain only IDs, Ge’ez, and generic procedure instructions;
  never French, expected facts, evaluator results, or old English translations.
- Three initial procedures; at most one feedback-guided revision of a procedure.
- Same generator model alias fable, medium effort; evaluator alias sonnet,
  medium effort. These share a provider; fresh contexts do not guarantee
  independent errors. Record exact reported model IDs from each invocation.
- Judge qualification: 12 randomly ordered controls, eight deliberately wrong
  and four faithful/paraphrased. Judge sees neither labels nor mutation names.
  All8 wrong must be rejected and all4 faithful accepted to use this judge for
  exploratory selection. No rubric tuning after looking at qualification results.
- Ranking: score each preregistered fact as supported=1, partial=.5,
  missing/contradicted=0. Average within a passage, then equally over passages.
  Count unsupported additions separately. Do not score declared review-only
  details. Select highest mean, breaking ties by fewer contradictions/additions,
  then prefer baseline or the simpler original procedure.
- To avoid leaking expected answers into future translations, any revised
  procedure must contain general instructions only: no passage names, numbers,
  source phrases, target answers, or disguised examples from this dataset.
- Evaluate baseline and selected procedure on reserved passages after freezing.
  No further selection, tuning, or model substitution after the reserved test.
- Pilot ceiling: 14 model invocations, 240 seconds each; at most 3 USD-equivalent
  CLI budget per invocation and24 cumulative reported USD-equivalent. These
  reported token costs are not a claim of actual subscription billing. Cache
  outputs and do not rerun a completed call. No automatic retries.
- Do not add image trials to this pilot: success here first motivates a separately
  documented end-to-end image test. No scholarly accuracy or significance claim.

## Scope and interpretation
All passages are nearby narrative/chronology; success cannot establish transfer
to Books IV–VII’s other genres. Fixed source transcription can contain errors.
French is a translation of d’Abbadie78, not exact ground truth for Ma IX1.
The hand-selected facts are a narrow coverage measure, not exhaustive meaning.
An LLM judge and its synthetic control pass do not replace expert review.
A prompt gain must be observed on reserved passages, with no increase in serious
errors, before recommending a larger trial. Even then this is provisional.

## Reuse
Original experiment code: MIT. Original documentation and readings: CC BY4.0,
credit Ge’ez Lab / EthiopianCanon.com. Historical French is third-party source
material, excluded from our licence grant. Source images remain outside Git.
