> **Historical handover, September 17, 2026.** Published as provisional research
> by [EthiopianCanon.com](https://ethiopiancanon.com), under CC BY 4.0.
> “68 folios” below means 68 photographed sides (34 leaves). Verification
> tallies are the original run’s reports, not an independent scholarly audit.
> The emphatic trust claims below describe that run’s assessment; they do not
> certify the transcription. Read [current status](docs/STATUS.md) first.

# Ma IX 1, ff.156r-189v — what this is and how to read it

68 folios of Tübingen Ma IX 1, drafted 2026-09-17. Each read cold by one model
in a fresh context; no reader saw another's page.

**Read this before the drafts.** The single thing that matters:

> **Every INTERPRETATION tested during this run failed or was qualified.
> Every OBSERVATION tested held.**

Six candidate source-markers were proposed and destroyed. Five claims by the
supervising session were withdrawn, including its most-cited finding. Meanwhile
eighteen scriptural citations were checked against published English and all
eighteen stood.

So the files are in two halves, and they deserve different amounts of your time.

---

## TRUST — observations, checkable, held up under testing

**The transcriptions.** In `passes/calibrated/`, one file per folio, under
`## TRANSCRIPTION`, numbered per manuscript line. Nonstandard spellings are the
scribe's and were deliberately NOT normalised. Unresolvable words are letter-by-
letter with a flag. **That discipline is why three words were recoverable** —
smoothing ዕቢራት to the standard መበለታት would have erased the evidence that this
compiler uses a different word for "widows".

**Eighteen scriptural citations**, located by chapter and verse, verified against
our published English: Matthew (11 places), Luke, John (3), Acts, Romans,
1 Corinthians, Hebrews, 1 Peter, 2 John, Jude, Genesis, Exodus (2), Leviticus,
Deuteronomy, 1 and 2 Samuel, Psalms (2), Isaiah, Zechariah, Sirach, 4 Ezra.
Loci are in each folio's `## NOTES`.

**Seam continuity.** 62 seams between consecutive sides were checked; readers
registered what the neighbouring page must contain BEFORE it was read. 61 join.
**One does not** — ff.187r/187v, a doubled ነ — and it is flagged, not smoothed.

**ff.165v-166v are the Rest of the Words of Baruch**, ch.8-9. Identified from the
ink by three readers independently and scored against a published English of that
book. This is the firmest single result here.

**Numerals carry bounding bars above AND below.** Six letter/numeral collisions
were caught by that rule. One reading that fitted the context perfectly — "one of
a hundred" in the lost-sheep parable — was rejected because the bars were absent.

---

## DO NOT TRUST WITHOUT CHECKING — interpretation

**Every `## WORK` section.** These are hypotheses about what text a page belongs
to. Their track record in this run is poor. Six markers were tested and rejected:
rank-list length, the bishop-word, the words ዑቁ and ስሕቱ, speaker-person, and
"formula habit = penitential canons". One reader's `## WORK` prose contradicted
its own corpus query six paragraphs later.

**Anything about strata or boundaries.** The supervising session twice claimed a
source boundary and twice withdrew it. What survives is narrow: **Matthew 18:10
appears twice, on f.158r as "he said TO US" and on f.186r as "as he said in the
Gospel"** — one verse, two incompatible framings, which indicates a boundary
somewhere before f.158r and rests on nothing stylistic.

**The Arabic-Vorlage suggestion.** Three candidate loans with roots (ክለዕ, ይትከነስ,
ፉል) against four readers reporting none. Suggestive, unsettled, and none of the
readers is an Arabist.

---

## KNOWN DEFECTS

**Cross-agent orthographic drift, UNFIXED.** Readers transcribed the same
recurring formula differently and each stayed internally consistent across its
own folio — ርኵስ against ርኩስ, ቤተ against ቢተ. **A normalisation pass is required
before publication, and it must FLAG variants as transcriber's calls rather than
silently harmonise them.** Harmonising would destroy the evidence that recovered
three words.

**One retracted instruction contaminated four readings.** A "low-tens bias" was
recorded, written into the key, and carried in every brief — then retracted when
on-page controls showed two of its six founding cases were manuscript variants,
not misreadings. Exposure in these folios is **four tens figures**; three are
anchored to Deuteronomy 9:9 and one (f.182v l.24, ፲ወ፫) was already flagged
uncertain by its own reader.

**Two numeral signs are UNANCHORED**: ፴ = 30 and ፶ = 50 have no observed shape in
the key. Treat every tens reading as narrowed to two values, not settled.

---

## THREE QUESTIONS ONLY A READER CAN SETTLE

1. **f.42r l.15, Othniel.** The ink appears to give **20**; our published English
   gives 50; Judges 3:11 gives 40. Grounds for 20 are in
   `groundtruth/out-42R-othniel.txt` — two strokes not three, three ፵ controls in
   the same pen on the same leaf. **If correct, our printed edition carries a
   figure this manuscript does not support.**
2. **f.41v, the man Moses kills** reads **ናሆም**; our English has "Nesom".
3. **The ፴/፶ shapes.** One sighting in an externally pinned slot closes both
   gaps, since the other is then the stemless three-prong by elimination.

---

## FILES

    passes/calibrated/MAIX1-*.md   the 68 drafts
    SCRIBAL-KEY.md                 letterforms, numerals, process rules, limits
    groundtruth/                   the scored controlled-pair work
    seams.py                       seam checker
    tgrep.py                       searches ONLY transcription blocks
    docs/HISTORY.md                curated history and corrections

`tgrep.py` exists because ordinary grep over these files matches readers' prose
about the text as readily as the text, which twice nearly produced a false
finding.
