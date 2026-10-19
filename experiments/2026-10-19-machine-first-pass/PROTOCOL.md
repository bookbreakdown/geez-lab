# Five-side machine first pass

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.

## Frozen scope

Five consecutive manuscript sides: **169r, 169v, 170r, 170v, 171r**, from
Tübingen Ma IX 1, within the catalogue-assigned missing-book range. Exact work
identification is not established. These are historical machine transcriptions,
not expert ground truth. This is production-method exploration, not a blind
accuracy benchmark, a French-reference optimisation, or a critical edition.

1. Generate complete English from numbered Ge’ez alone using the simple baseline.
   No old English, gists, French, modern edition, or book-identification claims
   are supplied to this translator call. Adjacent sides provide context.
2. The coordinating assistant inspects all five images and boundary context;
   record corrections and uncertainty separately. This assistant has seen old
   gists, so its revisions are not independent or blind.
3. A separate model inference reviews the draft for source omissions, unsupported
   additions, terminology, numbers, negation, and joins. No tools or research
   access are granted. A separate inference is not an independent expert or
   statistically independent evidence.
4. Resolve or explicitly retain each substantive review flag. Publish provisional
   English, source-line mapping, open issues, boundary notes, and provenance.

Maximum three experimental calls, each capped at $3 reported USD-equivalent;
no automatic retries. Planned calls: one translator and one reviewer. No purchase
is authorised or required by this protocol. Report actual CLI usage/cost and
failures; subscription accounting is not established by model-reported USD.
No further Transkribus uploads or large prompt search are part of this batch.

Success for this pass means a readable five-side draft with every source line
assigned to translation blocks, explicit unrecovered content, reviewed joins,
and inspectable changes. Structural coverage does not establish linguistic
completeness. Human correction time, accuracy, and production readiness remain
unmeasured until expert review. No original corpus reading is overwritten.

## Execution note: explicit format recovery

The original review returned text that failed JSON parsing. No successful review
findings are attributed to that attempt; its failure/request remain visible.
The coordinating English revisions proceeded from source/image observations.
Within the predeclared three-call cap, one explicit recovery review was then
requested with a JSON schema and at most eight material flags, using the revised
English and the same Ge’ez. This was a formatting recovery, not a favourable-score
search. No automatic retries or fourth call are allowed. The failed attempt's
response and usage envelope were not saved by the initial wrapper, so total
model-reported cost for all attempts cannot be established. The wrapper now
persists sanitised envelopes before parsing.
