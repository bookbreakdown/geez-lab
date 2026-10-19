# Inference accounting

Ge’ez Lab / [EthiopianCanon.com](https://ethiopiancanon.com), October 19, 2026.

| Call | Status | Reported USD-equivalent | Recorded seconds |
| --- | --- | --- | --- |
| Five-side translation | Usable | 0.763900 | 309.957 |
| Initial machine review | Failed JSON parsing | Unknown | Unknown |
| Schema-enforced review recovery | Usable | 0.063432 | 18.591 |

**Three calls attempted; two usable results.** The known successful-call sum is
**$0.827332 reported USD-equivalent** and **328.548 call seconds**. These
exclude the failed review and are not a whole-batch total, wall-clock project
duration, a subscription bill, or human correction time. No account purchase
was made. The failure's usage cannot be reconstructed from the retained record.

Actual reported models: `claude-fable-5-1` for the translator and
`claude-sonnet-5-5` for the successful review. CLI version: `2.1.303`.
The [ledger](runs/ledger.json) and [machine-readable accounting](accounting.json)
preserve the distinction. The three-call protocol cap was reached; no further
inference or automatic retry was made.
