# Transkribus public-demo pilot

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 16, 2026.

## Result

The public demo successfully processed **four uploads covering three manuscript
sides** using Classical Ethiopic model **48371**. Both the submitted configuration
and job response identified that model. It returned Ge’ez text. This establishes
that we can run the specialist recogniser on our images; it does not establish
that it improves our transcription or English translation.

| Side | Image dimensions | Observed processing seconds | Demo line count |
| --- | --- | --- | --- |
| 153r | 3560 × 5000 | Not recorded | 25 |
| 41v | 3560 × 5000 | 35.12 | 25 |
| 168r | 1700 × 2387 | 15.04 | 25 |
| 153r | 1700 × 2387 | 12.57 | 25 |

These are individual browser observations, including service/browser latency,
not a throughput benchmark. Counts are the interface's reports, not independently
verified coverage of the full manuscript side.

## What we could inspect

The demo displayed partial text and a signup gate for the remaining lines.
The normal TXT export control also requested an account; no full transcript was
exported. The accompanying preview TXT files preserve only publicly displayed
text, unchanged. [observations.json](observations.json) records image hashes,
dimensions, model confirmation, timings, and preview text. No account was created
and no purchase was made.

The visible previews contain recognisable words alongside apparent substitutions,
word-boundary problems, and stray fragments. They require checking against the
images. No independently corrected transcription was available for scoring, and
no character error rate or comparison win is claimed.

The two resolution variants of 153r produced different previews. Their Ethiopic
character SequenceMatcher ratio was approximately 0.758, but neither is ground
truth, the preview extent/segmentation differs, and there was no repeat control.
This is neither accuracy nor evidence that one resolution is better.

## Next step

Obtain complete TXT and, if available, PAGE XML outputs through an authenticated
Transkribus account. Preserve raw outputs, compare aligned regions against the
existing draft and a fresh image reading, and obtain independent corrections on
a small sample. This will show whether specialist HTR reduces expert correction
work. The current demo alone does not justify replacing the translation workflow.

## Other lead: Leo

[Leo's homepage](https://www.tryleo.ai/) explicitly describes Latin-script input,
such as English, French, and German. Its
[historical translation documentation](https://www.tryleo.ai/resources/ai-in-the-humanities-and-cultural-heritage/historical-text-translation-ai)
also describes its ATR-1 transcription stage as Latin-script recognition.
It is therefore outside the advertised scope for our Ge’ez images. No Leo account
or image trial was undertaken. It could be reconsidered for French scans if a
specific OCR problem arises.

## Sources and attribution

- [Transkribus model card](https://www.transkribus.org/models/ethiopic-classical-ethiopic-scripts-from-ethiopia-and-eritrea): model 48371; its reported 3.8% validation CER is not a result on our manuscript.
- [Transkribus terms](https://legal.transkribus.org/terms): service terms apply separately from this repository's research licence.
- Manuscript images: Universitätsbibliothek Tübingen, Ma IX 1; see [source provenance](../../docs/SOURCES.md). Images are not redistributed here.
- The 2008 printed edition and derived digitisation were not used. The project's commercial-source restriction remains in force.

This report and its observations are provisional research from EthiopianCanon.com;
third-party material and service rights are not relicensed by this report.
