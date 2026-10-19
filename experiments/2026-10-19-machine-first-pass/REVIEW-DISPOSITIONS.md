# Machine review: disposition of flags

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.

The first review failed JSON parsing; its findings were not recoverable. The
[recovery review](runs/review-format-recovery.json) used the
[coordinator-revised candidate](reviewed-before-recovery.json), frozen Ge’ez,
and a schema-enforced response format. It had no images, dictionary, expert
reference, or coordinator image notes. The table below records the coordinator's
response to every returned flag. These dispositions are also AI judgements.

| Flag | Source location | Disposition |
| --- | --- | --- |
| f1 | 169r B02 | The candidate already brackets Father twice and labels the source uncertain; the reviewer overstates it as an unqualified assertion. Retain Father as a proposed reading, not exact transcription. The reviewer offers an equally unverified literal gloss. Source/person ambiguity remains an expert question; no Gospel clauses are inserted. |
| f2 | 169r B04, cited incorrectly as zero-based block 4 | Candidate already says “They kept [it] and made [unresolved expression], without abandoning …”. The subject and negation are present. The cited source belongs to zero-based block 3, not 4. No omission established; no change. |
| f3 | 169v B02 | Partly accept caution: change “fasted” to “[fasted?]”. Do not accept that fasting is impossible merely because the reviewer cannot parse the orthography. The wash/diminish phrase already has explicit uncertainty. |
| f4 | 169v B03 | Accept broader “food” in place of “bread”; change the bracket to “[ate / did not eat?; the negative reading is uncertain]”. The original candidate's negative was bracketed, not settled. The flag also cites an unrelated word from earlier on the side; that part is not evidence for the food clause. |
| f5 | 170r B03 | Do not accept the reviewer's unverified “order/ordinance” gloss as a correction of the bride-family form. Bride and its whole construction already remain bracketed hypotheses. Keep uncertainty and send to expert, without a forced alternative. |
| f6 | 170v B01 | Addressee is already bracketed and no “to me” assertion remains. Retain provisional sandals/feet instruction, supported by its repeated source sequence; document lexical uncertainty in the register. Quotation punctuation is editorial, not proof of exact direct-speech syntax. No new source reading established. |
| f7 | 170v B02 | Both nouns are represented, one as lamps and one as a marked gap, and the olive branches/connection are explicitly present. No demonstrated omission. Keep unknown noun and connection open; do not manufacture a second gloss to satisfy the reviewer. |
| f8 | 171r B01 | Reject addition of lord/master: the cited string has a possessive expression, not an independently established master noun. “Those people's command” is retained as the referential proposal. The singular subject is already “[He/it]”; no subject certainty is asserted. |

## Other returned notes checked

- The 169r B06 entrusting/name clause remains explicitly uncertain.
- The reviewer claims that 171r block 3 omits the contrast in lines 17–19.
  Those lines belong to zero-based block 2 (B03), whose English includes
  “Those, however, who made their right hands like a firm pillar …”. No such
  omission was established.
- Repeated heavenly standing is preserved, as the reviewer notes.
- The unresolved 170v/171r word remains bracketed on both sides; do not count
  the second fragment as a separately missing named group.

Two block changes were made after this review, both on 169v. There was no further
model call after them. The full sequence is in [revision-log.json](revision-log.json).
The review produced useful caution but also false or ungrounded flags. Its
findings are not an accuracy score or a substitute for independent source work.
