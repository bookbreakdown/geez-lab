# Ge’ez Lab

**Open research on reading Ge’ez manuscripts with AI, from [EthiopianCanon.com](https://ethiopiancanon.com).**

Ge’ez Lab shares provisional manuscript transcriptions, a working scribal key,
comparison data, and small Python tools from our investigation of Qalementos.
Our aim is to make the work inspectable and useful to Ge’ez readers, researchers,
and developers working on manuscript transcription.

**Status: unreleased research preview.** The readings are machine generated and
have not received a complete review by a qualified Ge’ez scholar. This is a
partial research corpus; it is not a critical edition or a completed translation
of Qalementos Books IV–VII.

## What is here

| Material | Extent | Start here |
| --- | --- | --- |
| Main transcription drafts | 68 consecutive manuscript sides, 156r–189v | [Calibrated passes](passes/calibrated) |
| Earlier comparison passes | 47 files across three directories; overlapping readings | [Corpus guide](docs/CORPUS.md) |
| Historical reconciliations | 8 files showing disagreements | [Reconciled drafts](reconciled) |
| Resolution comparison | 3 sides, each read at two resolutions | [A/B records](ab) |
| Calibration readings | 12 exploratory outputs, not verified ground truth | [Calibration guide](groundtruth/README.md) |
| Working scribal key | Letterforms, numerals, corrections, unresolved shapes | [Scribal key](SCRIBAL-KEY.md) |
| Methods and project history | What worked, failed, and was retracted | [Methodology](docs/METHODOLOGY.md), [history](docs/HISTORY.md) |

The principal source is **University Library Tübingen, Ma IX 1**, a nineteenth
century manuscript catalogued as *Qālēmenṭos*. See the [library record](https://opendigi.ub.uni-tuebingen.de/opendigi/MaIX1)
and DOI [10.20345/digitue.24335](https://doi.org/10.20345/digitue.24335).
Images are fetched from the library; they are not bundled in this repository.
[Sources and provenance](docs/SOURCES.md) explain the source terms and limits.

## What we learned

- Fluent English and a transcription with no question marks can still conceal
  incorrect readings. A three-side trial needed 35 interventions across 72 lines.
- Agreement between models is not accuracy. Two passes can share mistakes;
  spelling differences can also inflate disagreement without changing meaning.
- The September run reported useful checks from quotations and continuity
  between sides. These support selected readings, not a corpus-wide accuracy claim.
- The run identified the *Rest of the Words of Baruch* within the range initially
  treated as Book IV. The book labels in our old index need expert checking.
- Some apparent reading errors were differences between manuscript witnesses.
  An English translation of d’Abbadie 78 is not exact ground truth for Ma IX 1.

The [current status](docs/STATUS.md) distinguishes reported checks, unresolved
readings, and hypotheses. Character error rate on this manuscript is unmeasured.

## Try the tools

Python **3.10 or newer** is sufficient. The included tools use only the Python
standard library. No model account, API key, or paid service is required to inspect
the corpus or run the local tools.

```bash
python3 scripts/validate_release.py
python3 tgrep.py 'ኤርምያስ'
python3 seams.py
python3 ab/score_ab.py
python3 ab/cross.py 153R
```

`tgrep.py` searches numbered transcription lines, avoiding matches in commentary.
`seams.py` displays neighbouring lines for a reader to assess; it does not decide
whether they join correctly. A low type-token ratio is a review signal, not a
hallucination detector with a validated threshold.

To fetch one manuscript image and build a local index:

```bash
python3 make_chunks.py --download 1 --only MAIX1-153R
```

To fetch up to all 249 distinct sides in the original investigation range:

```bash
python3 make_chunks.py --download 249
```

These commands contact Tübingen’s image service and require network access.
The book boundaries remain provisional. The downloader records the shared 241r
boundary once. See [reproduction](docs/REPRODUCING.md) for formats and limitations.

## Contribute

The most useful contributions are corrections grounded in the manuscript image,
expert review of uncertain readings, and improved evaluation against exact
transcriptions. Include the manuscript code, line, proposed reading, and evidence.
Keep the original reading visible. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence and attribution

- **Python tools and original automation:** [MIT](LICENSE).
- **Original research notes, draft transcriptions, and generated research metadata:**
  [CC BY 4.0](LICENSE-RESEARCH.md), to the extent rights exist.
- **Third-party sources and quotations:** retain their own terms; our licences
  do not relicense them. See [ATTRIBUTION.md](ATTRIBUTION.md).

Suggested credit:

> Ge’ez Lab, an EthiopianCanon.com project — https://ethiopiancanon.com.
> Research material licensed under CC BY 4.0. Changes: describe your changes.

Keep source credits and uncertainty notices with reused extracts. For a scholarly
reference, use [CITATION.cff](CITATION.cff) and cite the commit or released version
you used. Project home: **[ethiopiancanon.com](https://ethiopiancanon.com)**.
