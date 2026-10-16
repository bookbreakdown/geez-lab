# Four-output file: intake and comparison status

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 16, 2026.

The supplied file contains four labelled sections. Its original bytes, including
Windows line endings and copied interface labels, are retained in
[manuscript-test-original.txt](manuscript-test-original.txt). The
[receipt](manuscript-test-receipt.json) records hashes and extraction rules.

| Section | User's side label | Extracted lines, including fragments | Finding |
| --- | --- | --- | --- |
| 1 | 153R | 25 | Matches the previous repeat paste after line-ending normalisation. |
| 2 | 41V | 25 | Additional full-length supplied text, beyond the earlier preview. |
| 3 | 168R | 25 | Supplies the second target side needed for comparison. |
| 4 | 153R | 25 | Different text from section 1; retain as a separate variant. |

The user previously confirmed 153r and model 48371 for the first pasted output.
The user subsequently confirmed using all four images in the prepared upload
folder. Inspection confirms this input set:

| Image | Dimensions | Output mapping |
| --- | --- | --- |
| MAIX1-41V-3560px.jpg | 3560 × 5000 | Section 2, uniquely identified by side |
| MAIX1-168R-1700px.jpg | 1700 × 2387 | Section 3, uniquely identified by side |
| MAIX1-153R-3560px.jpg | 3560 × 5000 | One of sections 1 and 4 |
| MAIX1-153R-1700px.jpg | 1700 × 2387 | The other of sections 1 and 4 |

The two different 153r results therefore involve different source sizes in the
confirmed input set; which output belongs to which size is not yet resolved.
Their difference is not evidence of instability on an identical image. Per-run
recognition settings were not independently observed. Hashes and dimensions are
recorded in the receipt. No further uploads are needed for intake.

## Comparison prepared

The [full-output packet](FULL-OUTPUT-PACKET.md) places each extracted output and
both historical AI transcriptions in numbered blocks. Those numbers describe
output lines, not adjudicated manuscript-line alignment. Extra fragments in 41v
occur within the output as well as at the start, so blindly shifting all lines by
one would produce false disagreements.

For 168r, the opening repeated phrase, death/resurrection passage, teaching to the
ends of the world, and closing incomplete clause correspond to the existing draft.
This makes it usable for a real comparison. It also contains many letter and
boundary differences: for example, supplied **ሞቅኩ** against draft **ሞትኩ**,
and supplied **ወኢያም / ስቡ** against draft **ወኢያም / ስጡ**.
These are review targets, not adjudications. The draft itself has unresolved words
and an explicitly marked scribal cancellation that plain recognition text does
not reliably distinguish from running text.

## What remains

We no longer need another pasted 168r output to begin comparison. Complete
coverage and correct reading order still need image checks. Independently
corrected source regions and measured human correction time remain unavailable,
so no character accuracy, superiority, or productivity result is claimed.

Next: confirm per-section settings, align to manuscript lines with manual checks,
then inspect a bounded set of disagreements and agreements against the images.
Use the resulting evidence to prepare proposed corrections without replacing
archived drafts. The complete-English review milestone remains the priority.
