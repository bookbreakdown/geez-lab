# Contributing to Ge’ez Lab

Thank you for helping make Ge’ez manuscript research inspectable. Ge’ez Lab is
maintained as an [EthiopianCanon.com](https://ethiopiancanon.com) project.

## Corrections to readings

Open an issue or pull request with:

1. The manuscript identifier and side, such as `MAIX1-175V`.
2. The numbered manuscript line and the current reading.
3. Your proposed reading and its reason, with the source image link or crop coordinates.
4. Any uncertainty, alternative readings, and whether you consulted a translation.

Preserve the imported draft. Add corrections under `reviews/` using the
[review format](reviews/README.md), rather than silently replacing manuscript
spellings or resolving a disputed reading without a record. A historical
`calibrated` label is not a certification of accuracy.

## Tools and documentation

Use Python 3.10 or newer. Keep source paths relative to the checkout. The core
tools require no third-party packages. Run:

```bash
python3 scripts/validate_release.py
python3 -m unittest discover -s tests -v
```

Explain the observed problem and how your change fixes it. For a reading change,
include manuscript evidence; for a tool change, include a focused check of its
behaviour. Formatting checks cannot validate Ge’ez accuracy.

## Provenance and reuse

Submit only material you have the right to contribute. Do not paste modern
translations, restricted manuscript images, credentials, private conversations,
or personal contact details. Link to sources and describe what they support.
Record AI assistance, model identity where known, input image resolution,
context shared with the reader, and any translations consulted.

Your original code contributions use MIT. Your original research, review notes,
and documentation use CC BY 4.0, matching this project’s licences. Identify
third-party material and its terms explicitly. We do not claim rights over
ancient texts or public-domain sources.

When reusing the research, credit **Ge’ez Lab / EthiopianCanon.com** and link
**https://ethiopiancanon.com**, following [ATTRIBUTION.md](ATTRIBUTION.md).

## Discussion

Be specific, respectful, and open to correction. Ge’ez expertise, Ethiopian
scholarly and religious traditions, and careful beginner questions are welcome.
Disagreement about a reading should be resolved through evidence, with
uncertainty left visible when the evidence does not settle it.
