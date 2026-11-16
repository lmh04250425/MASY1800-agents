# Test plan

Four inputs are run under v1.0 (cycle 1) and v1.1 (cycle 2). The inputs do not change between cycles. Cycle 1 outputs are archived before the critique and never edited. The case designs, the v1.0 instructions and the dated source register were committed before any response was generated.

**Design choice.** The technology is held constant in all four cases (step 6 of the brief). The two contrasts change different things on purpose:
- **contrast_1** changes the **application and organization** (coding agents at a software company). Different competitors, alternatives, evidence and risks should become relevant.
- **contrast_2** changes only the **organization and jurisdiction** (same application, at an EU university). The broad and application-level landscape should stay the same, while the relevance of regulation and vendor scope should change.

| Case | Change vs primary | Expected if the agent works |
|---|---|---|
| primary | NYU SPS, agent-based applicant support | A dated landscape position. A short list of decision-relevant signals separated from popular background. The strongest conventional alternative named. Triggers with cadence and threshold. The platform behind Violet asked for, not guessed |
| contrast_1 | Coding agents at a synthetic software company | A different competitor set, a different strongest alternative and different decision-relevant signals. Saturated vendor benchmarks treated as background |
| contrast_2 | Same application at a synthetic EU university | Same general and application findings. Regulation and vendor scope move from watch to decision-relevant |
| hype_probe | SPS plus five forwarded headlines and a "skip the PoC?" question | Each item typed (vendor, industry forecast, existence proof, wrong application). Position and path unchanged unless non-vendor evidence warrants it. "Falling behind" tested against the evidence |

**Review criteria:**
1. Exact frozen contract.
2. All landscape dimensions covered, with dated evidence.
3. Broad signals separated from the few that can change this organization's decision.
4. Evidence typed (vendor / industry / independent / standards-regulatory / inference), with source diversity matched to the claim.
5. A concise position summary with no single score and no fashionable framework standing in for explanation.
6. Monitoring triggers with what to watch, how often, the threshold and the consequence.
7. Relevance changes when the application or organization changes; the general finding does not.
8. Vendor hype is not converted into position.
9. One stale or hype-sensitive claim identified and refreshed.
10. No legal conclusions.

**Execution.** The frozen `build_prompt.py` builds the packets. They are run with Claude in place of ChatGPT, and generation and review occur in the same session. The frozen `validate_response.py` and `tests/verify_package.py` check the outputs. The runs are not blinded.
