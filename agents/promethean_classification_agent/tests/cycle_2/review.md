# Cycle 2 review (v1.1)

The same four inputs were rerun with the revised instructions. Cycle 1 outputs were not edited. All eight archived outputs pass the frozen validator and the stricter contract check in `tests/verify_package.py`. Those checks confirm structure and archive integrity, not truth.

| Review question | Cycle 1 (v1.0) | Cycle 2 (v1.1) | Remaining limit |
|---|---|---|---|
| Course Layer 2 gate | Suppression test answered with uptake; passed as "emerging dissolution" | Answered in the present tense with dependence evidence (E6, E9, E12, E13); result "dissolution in progress, not yet testable"; capped at Breakthrough | Dependence evidence is mostly about generative AI broadly, not agents specifically |
| Classification | Potentially Promethean, Moderate | Breakthrough floor (Moderate) + Potential-Promethean candidacy UNRESOLVED (Low) | The floor/ceiling split is a student extension of the course instrument, labelled as such |
| Evidence use | Exposure and adoption speed counted as widespread impact | Admissibility table applied; exposure marked potential; Layer 3 scores marked prospective | Admissibility judgments are the author's, not an external standard |
| Tiers | Two tiers asserted | One tier observed; second tier "exposed, not reorganizing" | No direct measure of tier reorganization exists yet |
| Course exemplar | Generative AI's slide-20 label used as support | Not inherited; noted as an exemplar (Layer 1) | The instructor may weigh the exemplar differently; the record explains why |
| Counter-evidence | Listed, not weighed | Strongest case for a higher AND for a lower class, then an explicit weighing | Same-session reasoning |
| Significance to decision | Unstated weight; "proceed rather than wait", "core differentiator", "falling behind" | Explicit weight (Low in all four) + incremental-counterfactual PASS / CONDITIONAL / FAIL lists | Scale anchors are judgment rules, not calibrated |
| Hype probe | Label held, but recommendation accelerated by unverified claims | Seven claims listed and rejected or deferred; recommendation identical in substance to primary | Probe was designed by the same assistant that answered it |
| SPS baseline | Violet mentioned, ignored | Violet named as baseline; decisive comparison is now Violet/retrieval vs agent | Violet's design is unknown |

## Contrast results

- **Stayed the same (correctly):** the general technology paragraph is byte-identical in all four outputs, including under hype. So is the classification (Breakthrough; candidacy UNRESOLVED), and so is the Low significance weight.
- **Changed (correctly):**
  - SPS: complete the matched comparison against Violet and simple retrieval before any pilot.
  - Aggressive provider: a faster, larger, reversible experiment and in-house skills are allowed, but "core differentiator" positioning fails the counterfactual test.
  - Conservative hospital: no patient-facing agent within 18 months; preparation and a synthetic-data sandbox only.
  - Timing, scale and acceptable uncertainty differ across the three. The classification does not.
- **Hype invariance:** the hype probe's classification, weight and recommendation substance equal the primary's. The only additions are the list of rejected claims and a reply to the memo.

## Interpretation

The important improvement is a narrower claim, not a more dramatic one. v1.0 reached a label that matches the course's own timeline for generative AI. That made it attractive and hard to question. It got there by skipping the instrument's own gate. v1.1 applies the gate and keeps the Promethean question explicitly open, so a later reviewer can see what evidence would settle it.

## Limits of this evaluation

The same Claude session generated and reviewed both cycles. No ChatGPT run, blinded scoring, repeated sampling or second model was used. The cases include two synthetic organizations. This is a small, reproducible prompt-and-response diagnostic. It is not validation of a deployed agent. Recommended next step: paste `tests/prompts/cycle_2/primary.txt` and `hype_probe.txt` into ChatGPT, save the replies as new files, and compare.
