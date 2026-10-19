# Additional analyses: assessment and source checks

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com). October 16, 2026.

Two user-supplied analyses proposed specialist handwriting recognition, printed
Ge’ez sources, parallel-assisted translation, additional witnesses, dictionary
support, translation memory, and a small expert-reviewed sample. Their suggestions
were considered alongside the [translation pilot](../experiments/2026-10-16-reference-pilot/REPORT.md).
This note records our assessment; it does not redistribute the private analyses.

## Findings checked directly

### Specialist HTR model: a real and useful next experiment

The [official Transkribus model card](https://www.transkribus.org/models/ethiopic-classical-ethiopic-scripts-from-ethiopia-and-eritrea)
identifies model **48371**, a PyLaia recogniser for Classical Ethiopic manuscript
writing from the Beta maṣāḥǝft project. It reports **282 training pages, 21,173
lines, and 3.8% character error rate on its own validation data**. Those figures
are not an accuracy estimate for Ma IX 1. The page names several contributors,
including Bausi; it does not establish that Qalementos was the training text.

A specialist recogniser may offer useful complementary evidence and better
throughput. Different architecture alone does not prove uncorrelated failures;
agreement between HTR and a vision model still requires checking. Public hosted
availability also does not establish that model weights are openly licensed.

**Recommendation:** compare its output with the existing draft and a fresh image
reading on three to five representative sides. Keep a small independent corrected
subset for scoring. Include narrative, church-order prose, and difficult numerals.
A subsequent [public-demo pilot](../experiments/2026-10-16-transkribus-pilot/REPORT.md)
processed four uploads across three sides and confirmed model 48371. Only partial
previews were accessible; full export requested an account. No account was created
or purchase made, and no accuracy claim is made for our source. Leo was also
checked and ruled out for Ge’ez because its advertised recognition scope is Latin script.

### TheoDoor DOCX: currently a placeholder

We downloaded [B107-Clm.docx](https://tohdee.github.io/Dbbb-Ebc/B107-Clm.docx)
and inspected its Word document XML rather than assuming the link contained text.
Observed on October 16:

- 14,041 downloaded bytes.
- One text paragraph, 68 characters.
- Zero characters in the Ethiopic Unicode range U+1200–U+137F.
- The paragraph says: “We are currently working on digitizing the Ge’ez text for this book.”

The linked file therefore cannot currently bypass transcription or supply a
Qalementos comparison corpus. This does not show that TheoDoor will never publish
the digitisation. Even if it becomes available, the underlying 2008 edition and
its digitisation are excluded as sources for our commercial English translation
without explicit permission. See [the source policy](SOURCES.md).
The downloaded
DOCX is retained outside this repository. Its hash and inspection counts are
recorded in [the source check](source-checks/theodoor-2026-10-16.json).

The [project website](https://tohdee.github.io/) describes its general CC BY 4.0
policy with an exception for more restrictive source terms. That general notice
cannot establish the rights or quality of an as-yet unavailable Qalementos text.

## Recommendations to adopt or qualify

| Suggestion | Assessment and next step |
| --- | --- |
| Use the 2008 printed/typed Ge’ez edition | Excluded as a source for the commercial English translation without explicit permission. A host's general licence does not clear underlying modern editorial contributions. The current DOCX is also a placeholder. |
| Find a different printed/typed Ge’ez witness | Consider only after establishing provenance and rights for the intended commercial use. No eligible replacement source has been established by this review. |
| Compare earlier books with Grébaut | Useful for semantic correspondence and locating variants. Different-witness disagreement is neither manuscript CER nor a guaranteed upper bound on it. Errors can coincide with another witness and disappear from the comparison. |
| Use scriptural or literary parallels | Useful after preserving an independent source reading. Keep proposed parallels in a separate evidence layer. Resemblance does not by itself identify a work or justify replacing its wording with familiar scripture. |
| Add another manuscript witness | Potentially helpful for difficult passages; requires real alignment and readable access. It is not a prerequisite for every provisional English passage. |
| Resume with confidence-tiered gists | Gists help orientation, but the deliverable should be complete English of every recoverable clause, with gaps and alternatives visible. Confidence labels are not calibrated probabilities. |
| Dictionary and morphology support | Test targeted retrieval on genuinely unresolved words. The suggested parser endpoint did not load during this check; no availability or coverage claim is made. |
| Translation memory | Build from reviewed source/translation pairs. Do not promote unreviewed machine agreement into an accepted example that teaches the same mistake repeatedly. |
| Evolutionary prompt search | Keep bounded. Our pilot found a narrow scoring ceiling and evaluator errors; larger search should wait for more discriminating, trustworthy examples. |
| Delay the public research preview until accuracy is measured | A clearly labelled research preview can be shared independently of completing a translation. State measured and unmeasured outcomes accurately; do not imply expert approval. |

## Revised practical order

1. Test specialist HTR on a small representative sample and arrange a small
   independently corrected sample for meaningful comparison. A full critical
   edition or corpus-wide character score is not required to begin drafting.
2. Continue from the manuscript. A printed/typed alternative is eligible only
   after establishing rights for the intended use; the 2008 edition and derived
   digitisation remain excluded without explicit permission.
3. Produce **ten consecutive sides of complete English**, linked to the source,
   with proposed corrections and consequential uncertainties clearly recorded.
4. Assess whether an expert can correct that packet faster than starting from
   the image. Use the result to choose the next production step.
5. Expand dictionary support, reviewed translation memory, or prompt search
   where the sample reveals a specific recurring failure.

A lightweight contents map should grow with reading. A complete classification
of all 249 sides should not become a new prerequisite to producing the sample.
The historical Baruch identification remains a proposed identification awaiting
independent confirmation; it does not by itself prove the catalogue is wrong.
