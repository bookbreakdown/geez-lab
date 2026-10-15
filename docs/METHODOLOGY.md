# Methods and limitations

Open research from [EthiopianCanon.com](https://ethiopiancanon.com).

## Separate the tasks

Reading an image into Ge’ez characters, interpreting Ge’ez, and writing clear
English are separate tasks. A fluent result at the last step cannot establish
that the first step was correct. The research therefore preserves transcription,
interpretation, and uncertainty as distinct layers.

## Independent readings

The September main run used fresh contexts for individual sides. The historical
run notes report that readers did not see each other’s pages, though they shared
a working scribal key. That shared key is useful context and a possible source
of shared error. These records are not fully reproducible model runs: exact
model versions and settings were not consistently captured.

## Comparison metrics

The tools report different quantities:

- `reconcile.py` compares Ethiopic word tokens with `SequenceMatcher`, using the
  matching count divided by the longer token sequence. It writes disagreements.
- `ab/cross.py` compares Ethiopic character sequences with `SequenceMatcher`.
- `ab/score_ab.py` reports character and token similarity, type-token ratio,
  and a heuristic classification of substituted characters by consonant block.

None of these is character error rate against a correct transcription. They
also filter punctuation and other characters, so results cannot be described
as exact whole-text agreement. Different metrics should not be compared as if
interchangeable. A heuristic Unicode-block grouping is not a linguistic analysis.

The small resolution trial did not show a reliable benefit in agreement with
another model. It did not establish that resolution is irrelevant to manuscript
reading in general or measure the true accuracy of either configuration.

## Neighbouring sides and quotations

Readers registered expected continuations before neighbouring sides were read.
This helped identify some errors and recover words. `seams.py` displays adjacent
lines and missing sides; a human must judge continuity. It does not run the
historical checks automatically or certify a join.

Quotations can support the interpretation of selected passages. They also create
an anchoring risk: a reader may supply familiar wording instead of reading the
ink. Record whether expected wording was revealed before a reading.

## Witnesses and corrections

The calibration initially treated an English rendering descended from d’Abbadie
78 as if it were exact ground truth for Ma IX 1. That confused manuscript variants
with model errors. A proposed systematic low-tens bias was withdrawn. Instructions
based on it had already influenced later readers, illustrating how a mistaken
prior can propagate through a shared key.

Use a matching manuscript transcription for character accuracy. Use a translation
of another witness only for limited semantic comparisons, with its identity named.

## What would strengthen this work

Expert transcription of a small, representative sample; independent adjudication;
explicit model and input records; and accuracy scores against that transcription.
A result on clean modern Ethiopic type does not establish manuscript accuracy.
Avoid publication claims based on the model’s confidence or a question-mark count.
