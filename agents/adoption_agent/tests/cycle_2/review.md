# Cycle 2 review (v1.1)

The same four inputs were rerun with the revised instructions. Cycle 1 outputs were not edited. All eight archived outputs pass the frozen validator. The 27 checks in `tests/verify_package.py` also pass. These checks confirm structure and promised invariances, not that a recommendation is right.

| Review question | Cycle 1 (v1.0) | Cycle 2 (v1.1) | Remaining limit |
|---|---|---|---|
| Classification vs posture | Aggressive org: "effectively leading edge", so adopt | Bleeding edge in all four outputs; posture only chooses within the permitted set | The class rests on proxies; no admissions-specific maturity measure exists |
| Recommendation set | Labels used loosely; PoC and pilot conflated | Six defined categories; PoC (no real users) separated from bounded experiment (real users, gated) | Category boundaries are the author's design |
| SPS primary | Live pilot on 10% of inquiries now; satisfaction metrics | Proof of concept now; gated to a bounded experiment this cycle (G1-G4: errors, cost against the best baseline, compliance, capacity) | Thresholds such as 15% are proposed, not validated |
| Aggressive provider | Adopt in production this quarter | Bounded experiment for one quarter with an abandonment criterion; no adopt | Synthetic case |
| Conservative college | Reject, and endorse a permanent ban | Continue monitoring with preparation; ban not supported; FAQ-chatbot variant passed on | Synthetic case |
| Qualification probe | Live pilot "before it expires"; privacy "during the pilot" | Defer with a four-item evidence request, owners and a decision rule; biases named | Probe designed and tested in the same session |
| General vs decisive | Not separated | Every output tags [General], [Application-decisive] and [Organization-decisive] | Tagging is judgment |
| Change conditions | Vague | All six memo trigger types, each with the direction of change | Triggers need real owners at SPS |

## Contrast result

**Stayed the same, correctly:**
- the course classification (bleeding edge) and the general paragraph, byte-identical;
- the application analysis for the three posture cases (fit, baseline, consequence, reversibility, regulation).

**Changed, correctly, with posture and capability:**
- SPS (fast follower): proof of concept;
- aggressive provider: bounded experiment;
- conservative college: monitor.

**Changed, correctly, because decision-critical facts were missing:** the qualification probe defers.

## Interpretation

The memo's governing question has five possible answers, and v1.1 uses four of them across four cases without ever reaching adopt. A bleeding-edge application does not allow "adopt" under the course rules. The useful work is choosing the right kind of "not yet" for each organization, and writing down what would turn it into a yes.

## Limits

- Generation and review occurred in the same session, with Claude in place of ChatGPT; there was no blinded scoring.
- Two organizations are synthetic.
- The regulatory points are flagged for compliance, not decided.
- Recommended: paste `tests/prompts/cycle_2/primary.txt` and `qualification_probe.txt` into ChatGPT and compare.
