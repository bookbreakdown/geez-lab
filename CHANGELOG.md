# Changelog

Ge’ez Lab is a project of [EthiopianCanon.com](https://ethiopiancanon.com).
This file records changes to the public package. Historical research events
are documented separately in [HISTORY.md](docs/HISTORY.md).

## Unreleased

### Added

- Standalone repository prepared from the existing Ge’ez Lab research workspace.
- 68 consecutive calibrated draft sides, 47 earlier comparison files, eight
  historical reconciliations, six resolution-trial readings, and 12 calibration
  outputs, with provenance hashes.
- Public project overview, corpus guide, methodology, source credits, citation
  metadata, contribution guidance, and roadmap.
- MIT licensing for code and CC BY 4.0 for original research, with
  EthiopianCanon.com attribution and third-party exclusions.
- Release validation, focused tool checks, and continuous integration.

### Changed

- Analysis tools resolve paths from their checkout rather than a private machine.
- The image index distinguishes 249 unique manuscript sides from the 250 rows
  in the original book allocation; the shared 241r boundary is represented once.
- The downloader checks responses, writes images atomically, and reports failures.
- Historical notes carry notices explaining their provisional status and later
  corrections. Original reading files retain their imported text.

### Excluded from the public package

- Private correspondence, account and scheduling details, machine-specific run
  instructions, and the full internal chronological log.
- Manuscript photographs and image crops; images can be fetched from Tübingen.
- HMML microfilm material, modern reference translations, and specialist answer packs.

No version has been released or tagged yet.
