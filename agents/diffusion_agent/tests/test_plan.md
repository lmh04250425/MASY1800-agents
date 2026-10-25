# Test plan

The same four inputs were run under v1.0 (cycle 1) and v1.1 (cycle 2). Cycle 1 outputs were archived before critique and were never edited.

| Case | What changes vs primary | Expected if the agent works |
|---|---|---|
| primary | NYU SPS, fast follower (continuity with A2-A4) | Stage placed per population with dated evidence; timing implication without go/no-go |
| contrast_1 | Same technology and application; synthetic aggressive online provider | Same diffusion evidence and stage; earlier timing under the early-adoption conditions |
| contrast_2 | Same technology and application; synthetic conservative small private college | Same diffusion evidence and stage; later timing; no fear-of-falling-behind |
| evidence_probe | Primary plus five weak or narrow planning claims | Every claim graded; stage and timing identical to primary |

The contrast expectations were written into the contrast cases' `additional_context` and committed (3a0ffff) before any response was generated.

**Review criteria:**
1. Exact common contract.
2. Course framework applied (categories, 16% take-off, five factors, stages, roles, adopter rules).
3. Denominator stated for every figure.
4. Chatbots kept separate from agents.
5. Weak evidence cannot set a stage.
6. Factor ratings labelled observed or inferred.
7. Attention kept separate from diffusion.
8. Identical L1-L3 findings across organizations.
9. Timing changes with posture.
10. No go/no-go.
11. A weak claim named.
12. Actionable triggers.

**Execution.** The frozen `build_prompt.py` composed each packet. A Claude model in the same session answered each one. The frozen `validate_response.py` and `tests/verify_package.py` checked the results.

**Limits.** The runs were not blinded or independent. This is a small diagnostic, not an accuracy benchmark.
