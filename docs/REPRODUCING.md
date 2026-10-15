# Reproducing the local analyses

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com).

## Environment

Python 3.10 or newer; standard library only. Commands below are run from the
repository root. Tool paths resolve from their own files, so an absolute script
path also works from another working directory. Text files are UTF-8.

```bash
python3 scripts/validate_release.py
python3 -m unittest discover -s tests -v
python3 tgrep.py 'ኤርምያስ'
python3 seams.py
python3 ab/score_ab.py
python3 ab/cross.py 153R
```

These inspect bundled text without network access or model calls. `tgrep.py`
uses literal strings. It searches only sequentially numbered Ge’ez lines inside
`TRANSCRIPTION`, not the `NOTES` discussion. Its parser can omit malformed lines;
consult the source file when a missing occurrence matters.

`seams.py` displays 67 available joins across the main 68-side corpus. It does
not independently reproduce the 62 historical checks or judge grammar.
A low type-token ratio prompts review and is not proof of fabrication.

`reconcile.py MAIX1-153R` regenerates a comparison from earlier Claude and ChatGPT
passes and writes under `reconciled/`. This can change an imported artifact;
use a disposable checkout if preserving the imported state matters. The files
in `passes/calibrated/` use a different output format from those earlier passes.

## Downloading source images

```bash
python3 make_chunks.py --download 1 --only MAIX1-153R
python3 make_chunks.py --download 249
```

Downloads are limited per invocation, resume from existing JPEGs at the requested
width, and write a local `chunks-index.csv`. A request failure exits nonzero;
partial images are not installed. The JPEG signature check is a transport check,
not full image decoding or scholarly quality control. The library’s service may
be unavailable or change. Keep [source credits](SOURCES.md) with downloaded material.

`python3 make_chunks.py` refreshes the local index without downloading.
The published `folios.csv` is a source map with no machine-specific download state.
`chunks/` and `chunks-index.csv` are ignored by Git. Images are not model outputs.

## What cannot be reproduced exactly

The archived model calls lack complete model version and sampling records.
The public package excludes proprietary modern reference text and the original
account-bound workflow. It reproduces analysis of saved outputs; it cannot
promise to regenerate identical AI readings or score exact manuscript accuracy.

For a new experiment, record the exact model, date, settings, prompt, image URL,
input dimensions, crop coordinates, references revealed to the reader, and output.
Keep blind readings independent and distinguish exact transcription ground truth
from a translation of another manuscript.
