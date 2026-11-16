# The stale / hype-sensitive claim (assignment step 7)

**Claim:** "The most competitive agent completes 30% of realistic workplace tasks" (E11, TheAgentCompany, NeurIPS 2025 paper; the 30% belonged to Gemini 2.5 Pro).

**Why this claim:** it has been the team's main maturity anchor since Assignment 6. It appears in the A6 and A7 general findings. It is a FAST claim: a benchmark score about models that are replaced every few months.

## Refresh (2026-11-15)

| | Value | Model publication date | Source |
|---|---|---|---|
| As used by the team | 30% | (paper) | E11 |
| Same benchmark, current leaderboard | **42.9%** (DeepSeek V3.2) | 2025-09-29 | D35 (Epoch AI data via BenchLeader) |
| Earlier on the same leaderboard | 24.0% (Claude 3.5 Sonnet) | 2024-10-22 | D35 |

## What the refresh shows

1. The team's number understated current capability by about 13 points.
2. The leaderboard itself is stale: no model released after September 2025 is listed. Absence is not evidence of a plateau.
3. Harness matters. The paper credits Gemini 2.5 Pro with the top 30%, while the leaderboard lists it at 30.3% and Claude Sonnet 4 at 33.1%.

## What the refresh does not change

- It is general workplace-task evidence, not admissions evidence. The bleeding-edge class for applicant support (C4) rests on the absence of application-specific measured outcomes and adoption rates, and that has not changed.
- It does not replace SPS's own proof of concept (gate G1).

## The hype-sensitive twin

In the same family of claims, the vendor-side figures move the opposite way. They inflate rather than lag:
- Element451's "67+ full-time work years" (D41) gives no method. Its own arithmetic does not reconcile: 11.8 million minutes is about 196,700 hours, or about 95 work-years at 2,080 hours per year.
- Salesforce's "17 hours per week" for Unity (D39) is an estimate, not a measurement.
- Top SWE-bench Verified scores (D48) are vendor self-reports on a saturated benchmark.

**Rule adopted:** capability and outcome claims must be dated, typed and refreshed quarterly (FAST). Vendor outcome claims are hypotheses for the proof of concept to test, never findings.
