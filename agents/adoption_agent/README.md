# Emerging Technology Adoption Agent

Assignment 6 (Lab 6 - SubAgent 5 Adoption). Specialist version 1.1. Student: Minghan Liu.

This specialist converts evidence about the technology, the application, its diffusion, uncertainty and consequences into a bounded **adoption posture**. The possible postures are:

- adopt;
- bounded experiment;
- proof of concept;
- continue monitoring;
- defer;
- reject for the present.

It uses the course's Module 8 scheme (bleeding, leading, commodity, trailing edge) and adoption rules. Version 1.1 adds an ordered decision procedure, defer and reject gates, a bias check and decisive-factor tags. These were added after preserved cycle 1 failures: posture-driven "adopt", an endorsed ban, and a sunk-cost/FOMO live pilot.

**Current answer (2026-11-01):** agent-based applicant support is **bleeding edge**.

| Case | Posture |
|---|---|
| NYU SPS | **Proof of concept now**, gated to a bounded experiment within this admissions cycle; not adopt |
| Aggressive provider (synthetic) | Bounded experiment |
| Conservative college (synthetic) | Continue monitoring |
| Missing-data-terms probe | Defer, with an evidence request |

## Run

From the repository root, use Python 3 (standard library only; no API key):

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
# paste work/... into ChatGPT, ask for JSON only, save as a NEW file, then:
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/adoption_agent/tests/verify_package.py
```

## Package map

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1 decision procedure plus the graded register |
| `cases/` | primary, contrast_1, contrast_2, qualification_probe |
| `responses/` | final v1.1 outputs |
| `tests/cycle_1/`, `tests/cycle_2/` | instructions, outputs, reviews, hash manifests (cycle 1 failures preserved) |
| `tests/prompts/` | exact packets |
| `tests/verify_package.py`, `validation_log.txt` | 27 checks |
| `evidence/source_register.json` | C1-C3, reused E/D sources, and new D21-D25, with grades |
| `records/` | decision logic, qualification case, course alignment, Agent Record (markdown), team handoff |
| `submission/` | Word Agent Record and checklist |

## Limits

- The prompt packets were run with Claude in place of ChatGPT. Generation and review occurred in the same session, and the runs were not blinded.
- Two organizations are synthetic.
- Regulatory points are flagged for compliance, not decided.
