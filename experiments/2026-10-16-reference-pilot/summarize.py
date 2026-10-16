#!/usr/bin/env python3
"""Render the recorded pilot, without model calls.

Ge’ez Lab / https://ethiopiancanon.com. MIT.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def main():
    ledger = load('runs/ledger.json')
    spent = sum(x.get('reported_usd', 0) for x in ledger)
    seconds = sum(x.get('elapsed_seconds', 0) for x in ledger)
    models = sorted({model for row in ledger for model in load('runs/' + row['label'] + '.json').get('reported_models', {})})
    table = []
    for candidate in ['baseline', 'clause-audit', 'conservative-context']:
        result = load('scores/' + candidate + '-development.json')
        duration = load('runs/translate-' + candidate + '-development.json')['elapsed_seconds']
        table.append(f"| {candidate} | {result['mean_score']:.5f} | {result['contradictions']} | {result['additions']} | {duration:.1f}s |")
    report = f'''# French-reference translation pilot: results

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com). 2026-10-16.
Original analysis is CC BY 4.0; code is MIT. Historical French retains its own
source status and is excluded from our original-work licence grant.

## Result

**Short text experiments are feasible within a small budget. No improved
translation procedure was demonstrated, and the current evaluator/data should
not drive a larger evolutionary search.**

The simple baseline produced plausible, substantially corresponding English on
these selected narrative passages. That is an exploratory observation, not an
expert assessment of Ge’ez, a manuscript accuracy score, or evidence of transfer
to the missing books. The scored shared facts were deliberately narrow.

## What was run

- Six aligned excerpts: four development, two reserved from this prompt search.
- Source input: historical machine transcriptions of Ma IX 1, not new image reads
  or expert-corrected Ge’ez. French witness: Grébaut on d’Abbadie 78.
- French printed pages 141–142 were visually checked against PDF pages 145–146.
  No fresh strict English reference was used: scoring compared generated English
  with French plus hand-selected shared facts and preregistered exclusions.
- Three fixed generic translation procedures, each run on the same four
  development passages. No glossary, source-specific examples, or French was
  given to translators. Exact translator requests are retained under requests/.
- The baseline was frozen before its reserved test. Only the baseline was tested
  on the reserved passages; no claim of a paired held-out improvement is possible.
- No feedback mutation, fine-tuning, GEPA implementation, or image trial was run.
  The allowed mutation was declined because the remaining score differences were
  too small and entangled with evaluator/alignment errors to learn from safely.

## Evaluator qualification and audit

The initial judge scored 11/12: it caught all 8 deliberate substantive errors,
but rejected a faithful translation for omitting “En effet”. It failed the
original preregistered gate. That result is preserved, not overwritten.

After using that failure as calibration, a revised rubric passed 14/14 newly
constructed controls: five acceptable and nine defective, including narrowly
masked witness differences. These small constructed checks are not a validated
benchmark. The revised controls were not used to tune the translation procedures.

An audit then found a real scoring failure despite that control pass: the judge
penalised the baseline for the wives/concubines number distinction explicitly
excluded from scoring. It also penalised two alternatives for a trailing broken
source phrase in D03. Our passage selection leaves “from/among children…” before
the next sentence fragment; awkward English there is not established translation
inferiority. See [development-audit.json](development-audit.json).

**Consequently, the raw score differences below are not reliable evidence that
one procedure is better.** No automatic score was silently corrected or rerun.

## Raw development results

Scores are the mean of per-passage selected-fact coverage, with partial=.5.
They are **not percentages of translation accuracy**. Reference-only clauses,
known mismatched numbers, and other predeclared uncertain details were excluded.

| Procedure | Raw shared-fact score | Contradictions flagged | Additions flagged | Translation-call time |
| --- | ---: | ---: | ---: | ---: |
{chr(10).join(table)}

The baseline’s masked-number penalty means it should receive full credit on that
particular registered fact, but the original automatic 0.975 remains in the record.
Longer instructions did not demonstrate a gain on this narrow, near-ceiling set.
Each procedure was sampled once, so stochastic variation is unmeasured.

## Reserved result

The unchanged baseline received 1.0 on the 12 selected shared facts across H01 and
H02, with no contradictions or additions flagged. Disputed or absent material
remained review-only. This measures agreement on those facts, not accuracy on
all the Ge’ez, every clause, or the source images.

These excerpts come from a nearby narrative/chronology page and were used in
historical research. They were reserved from this new search, not previously
unseen by the project. This is a narrow sanity check, not broad generalisation.
See the [reading packet](READING-PACKET.md) to inspect the actual English and
uncertainties rather than relying on the score.

## Cost and execution

- {len(ledger)} model invocations; {spent:.6f} reported USD-equivalent total.
- {seconds:.1f} summed model-call seconds, excluding preparation and review.
- Reported model IDs: {', '.join('`'+m+'`' for m in models)}.
- Claude CLI 2.1.301, medium effort; aliases fable for translation and sonnet for
  judging. Both are from the same provider and may share errors.
- Fresh temporary working directory per call; explicit system prompt; safe mode,
  no built-in tools, no MCP servers, no slash commands or persistent sessions.
- Outputs cached; no failed or completed call retried. Original failed judge
  qualification counts toward the budget. No new API keys or paid-service setup.

The USD figure is the CLI’s token-cost report, not a confirmed subscription
charge. Small, batched text tests were inexpensive here; manuscript vision calls
and a larger search may have different costs.

## What this says about the proposed approach

A reference-guided search is technically implementable. This pilot tested whether
we had a useful evaluator and enough room for prompt improvement; it did not
perform a genetic search or establish that such a search cannot help.

The immediate limitations are the matched data and trustworthy evaluation,
rather than the number of trials we can afford. Chasing this judge’s tiny score
differences could encourage erasing real source differences or smoothing broken
input to match the French.

The next useful experiment is a broader, carefully bounded image-to-English
baseline, including less familiar prose and representative missing-book passages
for expert review. Strengthen the paired French/Ge’ez sample with better clause
boundaries and an expert-adjudicated subset before attempting many mutations.
The practical target remains an English draft that reduces expert correction
work, not duplication of a particular witness’s wording.

## Additional source review after the pilot

Two user-supplied analyses prompted a [source review](../../docs/EXTERNAL-REVIEW-2026-10-16.md).
A specialist Transkribus recogniser is available and deserves a small manuscript
trial. The proposed TheoDoor typed-source download was inspected and contains
only a placeholder, with no Ge’ez text. The underlying 2008 edition and derived
digitisation are excluded as commercial translation sources without explicit
permission. Neither finding changes this pilot’s
recorded results. They inform the next source-reading experiment.

## Reproduction

Inputs, freezes, exact requests, responses, usage, raw scores, and selection are
included. [PROTOCOL.md](PROTOCOL.md) records the original design;
[PROTOCOL-V2.md](PROTOCOL-V2.md) records the evaluator revision after failure.
The dataset and procedure hashes were frozen before translation trials.

Run `python summarize.py` from this experiment directory to render this report
and reading packet from saved outputs. `run_pilot.py` documents explicit model
stages; do not restart optimization using these reserved passages as if unseen.
The existing cached stages can be inspected without new calls. Reproducing an
independent run requires a new directory and an appropriate authenticated CLI.
'''
    (ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
    outputs = {}
    for split in ['development', 'heldout']:
        outputs.update({x['id']: x for x in load('runs/translate-baseline-' + split + '.json')['response']['records']})
    packet = ['# Baseline English reading packet', '',
              'Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com). 2026-10-16.', '',
              '**Machine-generated, provisional. No expert Ge’ez review.** This packet',
              'shows the fixed source transcription, French comparator, English output,',
              'and declared uncertainties. French was not shown to the translator.',
              'Review-only differences are excluded from the narrow score, not resolved.',
              'Original analysis and drafts: CC BY 4.0. Historical French: separate source.',
              'Read [the report](REPORT.md) for the evaluator failures and limits.', '']
    for data in load('dataset.json'):
        response = outputs[data['id']]
        packet += [f"## {data['id']} — {data['manuscript']}, {data['lines']} ({data['split']})", '',
                   '### Ge’ez input', '', '```text', '\n'.join(line.rstrip() for line in data['geez'].splitlines()), '```', '',
                   '### French comparator', '', data['reference_french'], '',
                   'Source: Grébaut, ROC 17 (1912), printed pages' + ','.join(map(str,data['reference_source']['printed_pages'])) + '.', '',
                   '### Baseline English', '', response['english'], '', '### Model-declared uncertainties', '']
        packet += ['- '+str(x) for x in response.get('uncertainties', [])] or ['None declared.']
        packet += ['', '### Predeclared review-only differences', '']
        packet += ['- '+x for x in data['review_only']]
        packet += ['']
    (ROOT / 'READING-PACKET.md').write_text('\n'.join(packet).rstrip()+'\n', encoding='utf-8')
    summary = {'date':'2026-10-16','project_home':'https://ethiopiancanon.com',
               'calls':len(ledger),'reported_usd_equivalent':round(spent,6),
               'summed_call_seconds':round(seconds,3),'reported_models':models,
               'candidate_improvement_demonstrated':False,'feedback_mutation_performed':False,
               'reserved_baseline_shared_fact_score':load('scores/baseline-heldout.json')['mean_score'],
               'evaluator_caveat':'A mask-handling error and fragment/alignment sensitivity invalidate interpreting tiny development score differences as gains.',
               'next_action':'Improve paired data and test an image-to-English baseline; do not scale evolutionary search on this evaluator.'}
    (ROOT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
