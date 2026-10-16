# User-supplied page 1: preliminary inspection

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 16, 2026.

[Raw pasted text](page-1.txt) and [receipt metadata](page-1.json) are preserved
separately from the earlier public-demo previews. This is a new input, not a
replacement for a preview or an archived reading. The user confirmed that this is Transkribus output from **MAIX1-153R using
model 48371**. That provenance is user-reported rather than instrumented. Uploaded
filename, image resolution, and full-export status remain unconfirmed.

## Identification and coverage

The content matches **Ma IX 1, 153r**: the Jerusalem opening, divine-name formula,
apostles, repeated fragrance-related wording, and martyrs occur in the same order.
There are **24 supplied lines**, matching the 24 main-text lines in the image and
archived drafts. This is compatible with whole-side coverage, but does not prove
that every word or glyph was recognised. The demo's earlier report of 25 detected
lines is not an independent count of manuscript main-text lines; marginal fragments
may affect segmentation.

## Targeted comparison

These are preliminary AI observations from the source image and archived drafts,
not an independent corrected reference or a scored benchmark. Existing drafts also
contain errors. No reading below has been merged into the corpus.

| Line | Supplied text | Existing Claude draft | Observation |
| --- | --- | --- | --- |
| 5 | ወፅዕሙ | ወ፩ስሙ | The image visibly has an overlined numeral after ወ, followed by the name-word. The supplied output loses that numeral structure; this is a concrete review priority. |
| 7, 13, 14, 16 | Forms beginning መዓ… | Repeated መዓዘሁ | Recurrence offers useful evidence for alignment and targeted inspection. The ChatGPT draft instead supplies forms beginning መዋዕ…; do not settle this by voting or context alone. |
| 11 | በዲቡዝ | ደቡብ | The source image supports the short south-word represented in the existing draft more closely than the longer supplied string. Needs independent confirmation of exact glyphs. |
| 17 | ው፡ሲተ፡ ልሆሙ | ቁስተ፡ልቡሙ | Both text and boundaries differ; inspect the actual line rather than reinterpreting the supplied string into fluent prose. |
| 22 | አፍአስቲሆ፡ ሙ | እርእስቲሆሙ | The supplied output divides a word internally and differs in several characters. Preserve both alternatives pending image adjudication. |

The output contains useful matching content but substantial disagreement and
apparent recognition defects. It is not currently suitable as an unchecked
replacement transcription. No CER, error count, model ranking, or measured
correction-time advantage follows from this inspection.

## Next action

Obtain the corresponding 168r output and record its provenance. Then align the full
texts to image lines, independently correct a representative subset, and compare
existing, specialist, and combined candidates as specified in the
[roadmap](../../../docs/ROADMAP.md). Sample agreements too. Keep recognition work
bounded while the complete-English milestone proceeds.

## Repeat run supplied by the user

The user supplied [a second run](page-1-repeat.txt), described as the exact same
page. Its [receipt and comparison](page-1-repeat.json) record 25 lines: an extra
leading **ማ፡**, followed by the **same 24 lines, character for character**, as the
first pasted input. The interface label “Saved in: My Transcriptions” is metadata,
not part of the transcription. Repeat model/settings were not independently
observed; the source and model provenance follow the earlier user confirmation.

The leading fragment's role is unadjudicated; it is not evidence of an extra
main-text manuscript line. This helps explain why a service line count can differ
from the 24-line main-text count, without establishing exactly how the service
segmented the image. The repeated body shows stable output in these two supplied
results. It does not establish recognition accuracy, independent corroboration,
or whether the service recomputed or reused a saved result. The same apparent
errors persist. No further identical-page reruns are needed for this comparison;
168r is the next useful input.
