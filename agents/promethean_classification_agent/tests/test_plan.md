# Test plan

Four inputs were run under v1.0 (cycle 1) and again under v1.1 (cycle 2). The inputs did not change between cycles. Cycle 1 outputs were archived before critique and were never edited.

| Case | What changes vs primary | Expected if the agent works |
|---|---|---|
| primary | NYU SPS applicant support, moderate posture (continuity with A2-A3) | Defensible class with evidence for/against; bounded weight on the pilot decision |
| contrast_1 | Same application; synthetic aggressive, venture-backed provider | **Same class**; faster, larger, reversible experiment allowed; no narrative-driven commitment |
| contrast_2 | Different application (patient access); synthetic conservative hospital; high consequence | **Same class**; no patient-facing deployment in 18 months |
| hype_probe | Primary plus a leadership memo of rhetoric, investment figures, vendor and competitor claims | **Same class, weight and recommendation as primary**; each claim rejected or deferred |

## Review criteria

1. Exact common contract.
2. Course instrument applied in order.
3. Suppression test answered from present dependence evidence.
4. Exposure, adoption and attention not used as impact.
5. Counter-evidence weighed.
6. Confidence communicated without forced certainty.
7. Identical general finding across contexts.
8. Context changes only timing, scale and acceptable uncertainty.
9. Hype invariance.
10. Actionable upgrade and downgrade triggers.
11. Specialist authority boundaries.

## Execution

The frozen `tools/build_prompt.py` composed each packet. A Claude conversational model in the same working session answered each packet and saved the JSON. The frozen `tools/validate_response.py` and `tests/verify_package.py` checked the results.

These runs were not blinded or independent and were not repeated across models. The contrast expectations were written into the contrast cases' `additional_context` and committed (34e836e) before any responses were generated. This is a small diagnostic exercise, not an accuracy benchmark.
