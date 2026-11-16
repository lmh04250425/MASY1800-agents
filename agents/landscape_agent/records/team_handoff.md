# Team handoff (Assignment 8: Landscape specialist, the final specialist)

| Item | Content |
|---|---|
| Agent package | `agents/landscape_agent`: v1.1 instructions with the ten-dimension framework, flip test, evidence typing and freshness rules; a typed and dated register (31 sources); four cases; eight archived outputs; a 31-check verifier; records |
| Landscape position (SPS, 2026-11-15) | A fast-moving technology; the application at the existence-proof stage (named deployments, no measured outcomes, no adoption rate); a vendor ecosystem converging on the kind of platforms SPS already uses. Nothing justifies skipping the proof of concept or changing the bleeding-edge class |
| Most decision-relevant landscape signal | **Vendor convergence:** agent features are arriving inside higher-ed CRM and engagement platforms (D15, D40, D41). For SPS, "build an agent?" becomes "switch on and constrain the platform's agent features, and do they beat a better chatbot?" |
| Strongest competing or conventional alternative | **A generative/FAQ chatbot over approved content, with staff hand-off and a self-scheduling link.** It is past take-off (D11), already at NYU (D17, D49) and improving on the same platforms |
| Monitoring trigger | **Trigger 1 (quarterly):** the platform behind Violet and the CRM offers permission-scoped appointment actions with audit logs and admin approval. Then add a vendor-native arm to the proof of concept. **Trigger 2 (semiannual):** two or more named peer programs publish measured, non-vendor outcomes, or a survey with a denominator shows agent use near take-off. Then re-run the Adoption specialist |
| Stale claim fixed for the team | E11's 30% is replaced by D35's 42.9% (refreshed 2026-11-15), and capability claims are tagged FAST |
| Open question | Which platform runs Violet and SPS's CRM (D49 does not say) |

## Final interface and evidence requirements for the team mixture-of-experts integration

### 1. Common evidence object
Keep the frozen `evidence` fields. Standardize `evidence_type` as `<TYPE>; grade <A|B|C|n/a>; refresh <FAST|MEDIUM|SLOW>`:
- TYPE is one of VENDOR, INDUSTRY, INDEPENDENT, STANDARD-REG, ORGANIZATION, INFERENCE;
- `date_or_recency` always holds the source date;
- the shared register stores `verified_on`.

### 2. One shared, dated source register
All specialists draw on one register with stable IDs (C, D and E series), with `evidence_class` and `half_life` fields. The orchestrator re-verifies FAST items older than 6 months before any decision.

### 3. Shared stale-claim list
It starts with E11 (30%, now 42.9% per D35) and D22 (May 2025 per-action pricing). A specialist may not state a stale-listed claim as current.

### 4. Routing order
1. Fit screen (A7).
2. Classification and permitted step (A6).
3. Diffusion position (A5).
4. Significance firewall (A4).
5. Readiness for the step (A7).
6. Landscape relevance and triggers (A8).

Landscape triggers may **re-run** an upstream specialist. They never change the class or the step directly.

### 5. Conflict rules
| Question | Specialist that owns it |
|---|---|
| Maturity class | Adoption |
| Executability | Readiness |
| What could change the decision, and when to look again | Landscape |
| Vendor outcome claims | Nobody: they are hypotheses for the proof of concept, never inputs to class or readiness |

### 6. Final intake additions (beyond A7's ten organizational fields)
- The platform(s) the organization already runs for the application, with contract renewal dates.
- The jurisdiction(s) of the users served.
- The decision horizon, and the decisions in play (so the flip test can be applied).
- Who will watch each trigger.

### 7. Output summary for executives
Each integrated answer ends with three lines:
1. Where the application sits (with date).
2. What would change that.
3. When we look again.

There is no score.
