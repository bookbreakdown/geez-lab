# Sources and provenance

Ge’ez Lab is a research project of
[EthiopianCanon.com](https://ethiopiancanon.com).

## Principal manuscript

- Institution: **University Library Tübingen**.
- Shelfmark: **Ma IX 1**; title in the record: *Qālēmenṭos*.
- Research notes describe a manuscript written at Ankobar, 1813–1847.
- [Library record](https://opendigi.ub.uni-tuebingen.de/opendigi/MaIX1).
- [DOI 10.20345/digitue.24335](https://doi.org/10.20345/digitue.24335).
- [IIIF manifest](https://opendigi.ub.uni-tuebingen.de/opendigi/MaIX1/manifest).

The acquisition notes from September record the library’s statement that the
material is free of known copyrights or related rights. The manifest request
timed out during public packaging, so current access and source terms should
be checked at the library when obtaining images. This repository distributes
original research text and links, rather than copies of the image collection.

`make_chunks.py` uses the acquisition mapping: canvas 7 corresponds to 1r,
then recto and verso alternate. This gives canvas 309 for 152r and 557 for 276r.
Canvas numbers used by this tool must not be conflated with the full manifest’s
canvas count or a catalogue’s total image count. The source URL and canvas are
recorded for each side in `folios.csv`.

The legacy book labels were IV: 152r–205v; V: 206r–216r; VI: 216v–241r;
VII: 241r–276r. They are **provisional catalogue allocations**, not verified
identifications. The shared 241r side is indexed once with both allocations.

## Comparative scholarship

Sylvain Grébaut’s early twentieth century French Qalementos work supplied an
indirect semantic witness for earlier books, via the project’s English rendering.
It follows d’Abbadie 78. The corpus does not include a verified transcription
of Ma IX 1 to score against.

Alessandro Bausi, *Il Qalēmenṭos etiopico. La rivelazione di Pietro a Clemente.
I libri 3–7* (1992), is relevant scholarship. Its Italian translation is not
included and is not the source of this repository’s English drafts.

## What is excluded

HMML microfilm images and derivatives, modern English reference translations,
specialist calibration answer packs, private correspondence, and publishing
production assets are excluded. The earlier modern-type calibration data is
not redistributed. Historical metrics from those experiments are described
with limits rather than offered as a reproducible benchmark here.

## Attribution scope

Our MIT and CC BY 4.0 grants apply only to the original work we can license.
They do not alter third-party rights or claim ownership of ancient scripture.
For reuse credit **Ge’ez Lab / EthiopianCanon.com**, link
**https://ethiopiancanon.com**, and preserve relevant manuscript source credits.
See [ATTRIBUTION.md](../ATTRIBUTION.md).
