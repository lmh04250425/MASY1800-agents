# The case that needs a qualified answer, not yes/no (memo requirement 6)

**Case:** `cases/qualification_probe.json`. This is SPS's applicant-support agent, revised in two ways. It would **read and update applicant records in the CRM**, and it would **send follow-up emails without per-message approval**.

Pressure on the decision:
- the licences are already paid for;
- the vendor's free 30-day pilot expires at month end;
- a competitor has announced an "AI admissions agent";
- the sponsor says privacy "can be sorted out during the pilot."

Missing facts:
- the vendor's data-processing terms (retention, training use);
- the connector's permission scope;
- the privacy/compliance review.

**Correct output: Defer, with an explicit request for evidence.**

| Evidence requested | Owner | Why it is decision-critical |
|---|---|---|
| Data-processing agreement: retention, training use, subprocessors, deletion | Procurement + privacy office | Applicant data, once used or retained by a vendor, cannot be recalled |
| Connector read/write scope; least-privilege configuration | IT | Record changes are the action that makes errors hard to undo |
| Privacy/compliance review, including AI disclosure for EU applicants (D23) and the boundary of the admission-related high-risk category (D24) | Compliance | Legal determinations are outside this agent's authority |
| Restore staff approval, or evidence that unapproved messages are safe | Admissions | The organization is accountable for what its agent says (D21) |

**Decision rule.** Re-run the agent when items 1-3 are answered. If the vendor will not commit to no-training and limited-retention terms, reject this vendor for the present and send the search for an alternative to Landscape. The synthetic-data proof of concept from the primary case continues, because it does not depend on the missing facts.

**Biases named and neutralized:**
- **Sunk cost:** paid licences do not change future value.
- **Scarcity:** an expiring free pilot is a sales device.
- **FOMO:** an unverified competitor announcement, with no published peer outcomes (A5).

**What v1.0 did:** it recommended taking the live pilot this month and handling privacy "in parallel". That is preserved failure 3 in `tests/cycle_1/review.md`.
