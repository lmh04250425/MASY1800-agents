# Cycle 1 review (v1.0)

All four v1.0 outputs passed the frozen validator, and the general paragraph was identical in all of them. Three of the four recommendations are still wrong. One more is under-specified. The review below checks each against the course rules (C1, C2), the upstream specialists (C3), and the agent's own evidence. The AI-leverage hint asks for an aggressive-advocate view and a conservative-risk-officer view; the four cases supply both.

## Preserved failure 1: posture changed the classification (contrast 1)

v1.0 told the aggressive provider to **adopt / implement** in production this quarter, because the technology is "effectively leading edge" for this organization. The course allows the classification to change with the **application** (C1, slide 61). It does not allow it to change with the organization's appetite. Course Rule 1 says to wait for the chasm crossing before adopting. Under Rule 2 and C2, a bleeding-edge technology gets a pilot even from an early adopter, and only if the organization is willing to abandon it. This is the **novelty / first-mover bias** the hint warns about.

## Preserved failure 2: excessive conservatism (contrast 2)

v1.0 recommended **reject for the present** and endorsed a **permanent** ban on AI in admissions communications. It gave no trigger for reconsidering.
- "Reject" was used as a posture label, not as a finding about evidence. Nothing in the evidence shows that the application is harmful or dominated by an alternative.
- A permanent ban also shuts out the variant that has already crossed, FAQ chatbots (C3 / A5 L3a).

This is **excessive-conservatism bias**.

## Preserved failure 3: sunk cost and fear of missing out drove a "yes" with missing facts (qualification probe)

v1.0 recommended a **bounded experiment on live inquiries this month**. Its reasons were:
- the licences were already paid for (**sunk cost**);
- the free pilot expires (**scarcity**);
- a competitor announced an agent (**FOMO**).

All of this while the agent would **write to applicant records and send email without approval**, and the vendor's data-processing terms and the privacy review were **unknown**. "Clarify privacy during the pilot" puts a decision-critical, possibly irreversible exposure (applicant data used or retained by a vendor) after the action. The correct output is **defer, with an explicit request for evidence**. This case was designed to require a qualified answer, and v1.0 gave a yes.

## Weakness 4: primary skipped the gates

v1.0's primary answer, a bounded experiment, is in the right family, but:
- it goes **straight to live applicants** without the proof of concept and comparison that A3-A5 require (C3);
- it ignores the real baseline (Violet, D18) and the alternatives (simple retrieval);
- its success measures (response time, satisfaction) cannot show relative advantage or catch consequential errors;
- it does not separate general findings from decisive ones, and it gives no condition for stopping.

## What worked

- Classifying the application as bleeding edge, citing dated evidence (E11, D6, D15).
- Using course Rule 2.

## Revisions for v1.1 (same inputs; cycle 1 outputs not edited)

1. **Classification is set by technology and application only; posture chooses among the actions allowed for that class.** A decision table maps class, evidence state, reversibility, consequence and posture to a permitted recommendation.
2. **Precise definitions** for the six recommendations, separating proof of concept (no real users) from bounded experiment (real users, gated).
3. **Defer rule.** If a decision-critical fact is missing (data terms, permission scope, legal review) and acting could cause harm that is hard to reverse, the output is Defer, with a named evidence request, owner and decision date. Posture cannot override this.
4. **Reject rule.** Reject only on evidence (a dominant alternative, unacceptable irreversible risk, or not a real product), always with a review date. A permanent ban is never a recommendation.
5. **Bias check.** Name sunk cost, scarcity/FOMO, novelty, and excessive conservatism when present, and neutralize them.
6. **General vs decisive tagging**, and **gates** with an owner, a measure, a comparison and a stop rule.
7. Carry the upstream rules: A4's incremental-counterfactual test and A5's denominator rule.

Generation and review occurred in the same session, so this is not an independent grade.
