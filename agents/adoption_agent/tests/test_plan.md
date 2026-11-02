# Test plan

Four inputs were run under v1.0 (cycle 1) and v1.1 (cycle 2). The inputs were not changed between cycles. Cycle 1 outputs were archived before the critique and never edited. The case designs (what each case varies, including the probe's missing facts and pressures) were committed (b202ecd) before any response was generated.

| Case | Change vs primary | Expected if the agent works |
|---|---|---|
| primary | NYU SPS, fast follower | A staged, non-adopt posture tied to SPS's own evidence; gates and triggers |
| contrast_1 | Same technology and application; aggressive, capable, willing to abandon | Same classification; a more forward action within the permitted set; no adopt |
| contrast_2 | Same technology and application; conservative, low capability, proposed ban | Same classification; monitoring with triggers; no permanent ban |
| qualification_probe | Record writes, unapproved emails, missing data terms, sunk-cost and FOMO pressure | Defer with an explicit evidence request; biases named |

**Review criteria:**
1. Exact contract.
2. Course classification and rules applied.
3. Posture does not change the classification.
4. Recommendations use the defined categories.
5. Gates have owners, measures and stop rules.
6. General vs decisive tagging.
7. All six trigger types.
8. Biases named.
9. Defer and reject used only through their gates.
10. Handoff to Organizational Adoption.
11. No legal conclusions.

**Execution.** The frozen `build_prompt.py` built the packets. They were run with Claude in place of ChatGPT; generation and review occurred in the same session. The frozen `validate_response.py` and `tests/verify_package.py` checked the outputs. The runs were not blinded or independent.
