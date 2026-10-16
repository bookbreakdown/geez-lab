# Roadmap

A project of [EthiopianCanon.com](https://ethiopiancanon.com).

## First public research preview

- Review the prepared documentation, licensing, attribution, and packaged corpus.
- Run the repository checks and confirm source-image access.
- Publish the repository and a dated research-preview release when ready.
- Link the release from EthiopianCanon.com and cite the exact released commit.

## Next milestone: complete English for independent review

The priority is a small packet of **several complete manuscript sides**, with
all recoverable clauses translated, gaps visible, and consequential uncertainties
linked to image locations. Start with a three-side Grébaut-aligned packet; expand
to the missing books after review. Freeze the chosen sides before generating new
outputs and record any prior exposure. The previously reserved excerpts are now
consumed and cannot serve as fresh held-out evidence.

The [first Grébaut pilot](../experiments/2026-10-16-reference-pilot/REPORT.md)
is complete. It did not establish an improved procedure. Continue with the simple
baseline, improve page alignment and coverage checks, and assess complete English
before investing in a larger prompt search. Keep French comparison separate from
independent checking of Ma IX 1: Grébaut translated a different witness. Record
source variants separately from translation errors. Translators must not receive
the reference in a blind evaluation; any reference-assisted revision is a separate,
explicitly labelled condition.

For each side, provide source identifiers and line locations, a provisional
transcription, complete English, and a review table of omissions, additions,
wrong meaning, names, numerals, and unresolved source readings. Independent expert
review remains outstanding; additional AI review is not a substitute for it.

The primary outcome is **expert time to reach an acceptable provisional English
translation**, with remaining substantive errors and coverage reported alongside
time. Include reading, checking apparently correct text, and resolving flags.
A faster draft with more serious residual errors is not an improvement. Record
reviewer, task, stopping criteria, and exposure to previous outputs; repeated
review of the same passage introduces familiarity effects.

## Bounded supporting work: Transkribus

This workstream is separate from Grébaut optimisation and must not block the
English packet. Obtain full raw output for **153r and 168r** using model 48371;
the [public-demo previews](../experiments/2026-10-16-transkribus-pilot/REPORT.md)
are insufficient. Full export currently requires authenticated account access.

Compare three conditions on the same image regions: existing transcription,
Transkribus alone, and a combined candidate. Preserve all original readings.
Have a small representative sample independently transcribed from images before
adjudicating disagreements, including ordinary text, difficult letterforms,
numerals, and boundaries. Report character error rate with a declared
normalisation policy, substantive word errors, missing/duplicated lines, and
human correction time. Report sample size and uncertainty; do not extrapolate a
small sample into corpus-wide accuracy.

### Disagreement-driven correction experiment

Align the full transcripts to manuscript lines. Flag substitutions, insertions,
deletions, and alignment failures for targeted image inspection. Retain an
unaltered text layer when using normalisation for matching. Do not automatically
accept a reading because models agree or declare high confidence: both may share
the same mistake. Any automatic acceptance rule needs independently verified
evidence, an explicit scope, and an audit record. Until then, matching text is
provisional and disagreements are review candidates.

Review a sample of agreements as well as disagreements to detect shared errors.
Include alignment, targeted inference, and review overhead in the comparison.
Keep this method only if it reduces total correction work while preserving or
improving the reviewed quality of the English output. Leo is outside the
advertised script scope and receives no further Ge’ez evaluation effort.

## Other research priorities

- Obtain expert review of disputed numerals and recurring letterforms.
- Grow a contents map while reading; a complete manuscript classification is not
  a prerequisite to the English sample.
- Record corrections and cross-reader spelling choices without erasing originals.
- Resolve the 187r/187v join and the unanchored 30/50 shapes as relevant passages
  arise. Exact transcription reference data should grow from reviewed samples.
- Keep the 2008 edition and its derived digitisation excluded without explicit
  permission, as required by the [source policy](SOURCES.md).

## Community contribution

Useful contributions include expert reading notes, source identifications,
reproducible evaluations, accessible formats, and better tool behaviour. Credit
contributors in review records and the changelog. A future blog can explain
what the community can reuse and what still needs human scholarship; it should
not describe this preview as a completed translation or independently verified
benchmark.
