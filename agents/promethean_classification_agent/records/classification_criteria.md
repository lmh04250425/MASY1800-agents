# Significance classification criteria (v1.1)

These are the criteria the agent applies. They are written so a skeptical reviewer can challenge any step. The source is marked for each rule. **C1** means the course instrument: ET Promethean Technologies FA26, slides 8-10, 15-17, 19-20. **Student extension** means a rule added after the cycle 1 failure. Extensions are not the instructor's rules.

## The gates, in order

| Step | Question | Decision rule | Source |
|---|---|---|---|
| Layer 1 | Is it a usable, deployed system rather than a component? | No → "Not yet evaluable", stop. Evaluate the named system; do not inherit a parent technology's or a course exemplar's label. | C1; inheritance rule is a student extension |
| Layer 2a | Barrier statement | "Before this technology, [activity] required [constraint]; this was not experienced as a limitation but as the definition of [domain]." Must not overstate. | C1 |
| Layer 2b | Suppression test, **present tense** | Answer only from dependence evidence (share of activity run through the technology, systems that now require it, cost of reverting). Results: *dissolution confirmed* → Layer 3; *reduction* → Breakthrough at most, stop; *dissolution in progress, not yet testable* → qualification rule. | C1 gate; present-tense and three-result wording are student extensions |
| Layer 3 | Six criteria | Order-of-magnitude (about 10X), widespread impact, paradigm shift, catalytic effect, democratizing effect, irreversibility. Each scored Supported / Partial / Not supported / Unknown. Scores are *prospective* and cannot raise the class unless Layer 2b was "confirmed". | C1, C2; "prospective" label is a student extension |
| Tiers | How many tiers of human existence reorganized? | Count a tier only with evidence that it is *reorganizing*, not merely exposed. One tier = Breakthrough. Two or more after confirmed dissolution = Promethean candidate. | C1; "reorganizing, not exposed" is a student extension |
| Mode | Confirmed or Potential? | Confirmed only for settled historical cases. "Irreversibility can only be verified after the fact." | C1 slide 17 |

## Labels

- **Incremental:** improves performance inside an existing constraint. No barrier is named that it removes.
- **Breakthrough:** a genuine step change, or a reduction of a real barrier, within one tier. Supported by independent capability evidence.
- **Potentially Promethean:** dissolution confirmed in the present tense, across two or more tiers, with irreversibility not yet verified.
- **Confirmed Promethean:** historical cases only (for example the printing press or electricity).
- **Not yet evaluable / Not yet distinguishable:** no usable system, no independent evidence, or a technology defined only by marketing language.

## Qualification rule (memo requirement 6)

When the suppression test cannot yet be answered, the agent reports **two** things and never merges them:

- **Floor:** the highest class present evidence supports, with its own confidence.
- **Ceiling:** "Potential-Promethean candidacy: UNRESOLVED", with its own (normally low) confidence, the best case for it, and named upgrade and downgrade triggers.

This is how the agent shows confidence without forcing certainty. It also keeps an open question from being read as a "no". The agent abstains entirely only when even the floor cannot be supported.

## Evidence admissibility (anti-hype control, memo requirement 4)

| Evidence | Can support | Cannot support |
|---|---|---|
| Independent capability evaluations | 10X capability; Breakthrough floor | Dependence, tiers, field impact |
| Exposure estimates | Potential breadth (labelled potential) | Widespread *impact* |
| Adoption speed, user counts | Diffusion context (Diffusion specialist) | Dissolution, Promethean status |
| Measured productivity or labor outcomes | Realized impact, positive or null | A long-run ceiling (lags are normal, E2) |
| Ecosystem and standards signals | Early catalytic effect (marked self-reported) | Realized value |
| Vendor, analyst and competitor claims; forecasts | Questions for another specialist | Classification or urgency |
| Executive rhetoric, investment totals, media framing | Nothing | Everything |
| Course exemplars | How to use the instrument | Evidence about this system |

## From broad significance to the present decision (memo requirement 3)

**Significance weight:**

- **None:** the broad class is irrelevant to the application.
- **Low:** it may shape monitoring cadence, learning investment and lock-in avoidance, but not go/no-go or scale.
- **Moderate:** only if the application sits directly on the dissolved barrier *and* the step is reversible and learning-oriented.
- **High:** only for Confirmed Promethean technologies, where non-adoption would cut the organization off from infrastructure others depend on.

**Incremental-counterfactual test:** an adoption step is justified only if it would still be justified were the technology merely incremental. Steps that fail are being driven by broad significance, so the specialist does not recommend them.

Posture, capability and consequence may change timing, scale and acceptable uncertainty. They may never change the classification.
