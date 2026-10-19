# Image comparison: 153r and 168r, with 41v control material

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com).
Reviewer: Codex assistant, October 16, 2026. **AI proposals; no expert adjudication.**
Reviewed commit: `b4dbd3fd2d2b78c5c5a4a11c28b079efdded868e`.

## Evidence and procedure

Images: University Library Tübingen, Ma IX 1,
[library record](https://opendigi.ub.uni-tuebingen.de/opendigi/MaIX1).
The [provenance record](../experiments/2026-10-16-image-review/provenance.json)
records exact local image hashes and reference exposure. We inspected overlapping
upper, middle, and lower image regions of 153r (3560 × 5000), 168r (1700 × 2387),
and 41v (3560 × 5000), plus the following side 168v for the closing join.
These are local source-image observations; manuscript spelling is not regularised
by the proposals below. No outside dictionary or modern edition was consulted.
Historical draft translations and earlier French comparisons were already visible,
so this is neither independent nor blind. The confidence descriptions below are
qualitative judgements, not calibrated probabilities.

The [71-line comparison](../experiments/2026-10-16-image-review/line-comparison.csv)
aligns the two target sides and 41v. For 153r and 168r, remove the single leading
recognition fragment from line assignment. For 41v, exclude supplied lines 2 and
11 (floating fragments); the remaining 23 output lines follow the 23 main-text
lines. Excluded fragments remain in raw files. None is silently merged into text.
Alignment was checked by following the image sequence, not character similarity
alone. Each row remains provisional; exact letter adjudication is incomplete.

## Targeted observations

| ID | Side / manuscript lines | Existing versus supplied evidence | Proposed action and confidence |
| --- | --- | --- | --- |
| R01 | 153r 4–5 | Claude has ፩ … ወ፩ስሙ; supplied section 1 has ፩ … ወፅዕሙ, section 4 has ወወአሰሙ. Image shows barred one-signs on both lines. | Retain “one God … his name one”; strong visual support for the numeral structure. HTR loses the second numeral. |
| R02 | 153r 6–7 | Claude splits ይድኅ / ን; section 1 has ይዶቀ / የጥበ; section 4 has ይ፡ ድኀ / ንጥበ. Image has a continuation into initial ን on line 7. | Retain “will be saved” provisionally; favour word continuation over treating each recognition line as a complete word. Moderate exact-glyph confidence. |
| R03 | 153r 7–8, 13–16 | Claude records repeated መዓዘሁ but leaves it untranslated or suggests time; ChatGPT supplies days-forms. Both HTR variants also contain forms with መዓዝ. Image repeats the same core sequence. | Propose fragrance/savour as the semantic family, rather than days. Exact vowels/inflections remain open. Moderate confidence; no claim that HTR independently proves the lexical meaning. |
| R04 | 153r 10–11 | Claude north/south sequence; supplied section 1 has በዲቡዝ, section 4 በዳቡብ. Image's short word follows the north clause and resembles the draft's south-word. | Retain north/south; do not accept the extra supplied prefix or final character without review. Moderate. |
| R05 | 153r 13–14 | Claude ንሕነሰኬ … ለክርስ / ስቲስ; ChatGPT introduces Paul and days. HTR corrupts the same phrase. | Preserve “we … Christ …” and propose “Christ's fragrance” with brackets. Do not insert Paul's name: image does not establish it here. Moderate for rejection of an explicit supplied name; lower for exact syntax. |
| R06 | 153r 15 | Claude saints went to the desert and renounced the world; section 4 includes መነኑ፡ ዓለመ. The visible image supports that sequence. | Retain desert/renunciation. Matching wording is still checked, not auto-accepted. Moderate. |
| R07 | 153r 16–21 | Claude hearts/resolution; ChatGPT garments/washing; HTR variants include ል…ሙ but corrupt neighbouring letters. Image line 21 has a short heart-like noun, not an obvious full garment-word. | Prefer hearts provisionally. Keep line 17's exact preceding word and verb morphology unresolved. Moderate-to-low. |
| R08 | 153r 22 | Claude and supplied outputs retain a head-word and cutting verb, though HTR splits it. Image supports the long head-word. | Retain “their heads were cut off”; moderate. Agreement does not remove need for checking. |
| R09 | 153r 23 | Claude እእዳዊቲሆሙ (“hands”); high-resolution historical trial አእይንቲሆሙ; supplied section 4 also has a sequence ending ንቲሆሙ. Image favours an eye-word. | Propose eyes, not hands. Translate the action tentatively as “put out”; exact verb remains open. Moderate, needs expert confirmation. |
| R10 | 168r 1–2 | Both earlier readers and HTR preserve repeated ብሂልየ / በፈቃድየ wording. Image visibly repeats the phrase. | Preserve repetition; do not silently edit it out as a scribal mistake. Strong structural support. |
| R11 | 168r 3–5 | Drafts have death, died, rose; HTR has ሞቅኩ in place of ሞትኩ. Image supports the draft's death-word and resurrection sequence. | Retain “died and rose”; moderate exact-letter confidence. Increasing/abounding verb at line 5 remains tentative. |
| R12 | 168r 7 | Image has horizontal cancellation strokes over the first clause. Calibrated draft marks [[ወእለ፡ተወክፉ]]; HTR emits an unmarked corrupted sequence. | Preserve a deletion note; exclude cancelled words from running English. Strong visual support. |
| R13 | 168r 9–12 | Receive teaching / enter life; refusal follows. Image has a negative marker in the refusal clause, while HTR distorts it. | Retain positive/negative contrast. Moderate; model agreement alone is insufficient for negation. |
| R14 | 168r 13–16 | Older readings disagree over judgment verb, rebuke/praise, and final judgment expression. Image favours a rebuke-type sequence over the ChatGPT praise-form, but difficult glyphs remain. | English “rebukes” provisional; keep exact judgment construction bracketed. Do not promote full reconstructed Ge’ez to corrected ground truth. Low-to-moderate. |
| R15 | 168r 17–20 | Shared Son/Father/word sequence; ChatGPT introduces “we worked,” Claude “not empty,” HTR is corrupt. Image includes a negation-like sequence and adjective-like word, not clear support for “we worked.” | Propose “our word is not empty” with explicit uncertainty; moderate-to-low. |
| R16 | 168r 22 | Calibrated and Claude drafts have መድኃኒነ; ChatGPT proposes a comparative phrase. Image supports the Saviour noun. | “Our Saviour” preferred provisionally. Moderate. |
| R17 | 168r 24 → 168v 1 | Claude/supplied final word interpreted as saved; calibrated reads እምኵነኔ. Following image opens a conditional/negation sequence. | Do not finish “they would have been saved” on 168r. Preserve a broken conditional with an unresolved final expression; following side does not settle exact 168r glyphs by itself. Strong for incomplete boundary, low for final-word adjudication. |
| R18 | 41v 5–7 | Image shows barred ፯፻ and later ፩. HTR has letter-like strings and ፪, respectively; existing machine reading has 700 and one. | Preserve 700 and one provisionally. Do not import the French witness's extra numerical distinction. Strong structural support, expert numeral review pending. |
| R19 | 41v 2, 10 | Small letters occur above the main text; HTR emits floating fragments or misses their relation to the words. Existing transcription records supralinear insertion. | Retain insertion notes; do not count fragments as additional main-text lines. Moderate-to-strong visual support. |
| R20 | 41v 23 | Both existing reading and HTR give a barred 30-sign for Moses' age. Image supports a numeral here. | Retain 30 provisionally rather than substituting a familiar scriptural age; exact numeral check remains with expert. Moderate. |

## Interpretation

This pass establishes inspectable corrections and review priorities, not an error
rate. HTR sometimes supplies useful alternative evidence, including the fragrance
sequence and eye-word candidate, but the historical high-resolution trial already
contained the latter alternative. No exclusive discovery advantage is claimed.
The specialist output also loses numerals and cancellation information. An
unchecked replacement would discard useful information in the existing drafts.

Combining outputs is therefore retained only as a **candidate review method**.
This pass did not measure expert time, use random sampling, or compare blinded
conditions; it cannot establish that the combination saves work. Disagreement
inspection was useful for finding issues, but full text/image inspection was still
needed to interpret cancellations and test agreement.
