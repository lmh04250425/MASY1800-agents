# Emerging Technology Diffusion Agent

Assignment 5 (Lab 5 - SubAgent 4 Diffusion). Specialist version 1.1. Student: Minghan Liu.

This specialist uses Rogers' diffusion framework (as taught in Module 6) to assess how far a technology and a specific application have spread, what is accelerating or inhibiting them, and what that implies for an organization's **timing**. It does not make the adoption decision. Version 1.1 adds a denominator rule, a four-level diffusion ladder, A/B/C evidence grades, observed/inferred factor labels and posture-specific timing. These were added after a preserved cycle 1 failure in which mixed populations produced a false "past the chasm" verdict.

**Current answer (evidence date 2026-10-25):**

| Level | Placement |
|---|---|
| Generative AI among people | Past take-off |
| Any AI among U.S. firms | At the take-off line (19.8%) |
| Agentic AI in organizations | Early adopters, before the chasm |
| FAQ chatbots in admissions | Past take-off |
| Tool-using recruitment agents | Innovators / early adopters |

The factor that matters most is **low observability**. For NYU SPS (a fast follower), the implication is: **prepare and trial now; no applicant-facing launch on diffusion grounds this cycle.**

## Run

Use Python 3, standard library only; no API key is needed.

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
# paste work/... into ChatGPT, ask for JSON only, save as a NEW file, then:
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/diffusion_agent/tests/verify_package.py
```

## Package map

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1 logic plus the graded source register |
| `cases/` | primary (SPS), contrast_1 (aggressive synthetic provider), contrast_2 (conservative synthetic college), evidence_probe |
| `responses/` | final v1.1 outputs |
| `tests/cycle_1/`, `tests/cycle_2/` | instructions, outputs, reviews and hash manifests for each round; the cycle 1 failures are preserved |
| `tests/prompts/` | exact prompt packets |
| `tests/verify_package.py`, `validation_log.txt` | 24 structural and invariance checks |
| `evidence/source_register.json` | C1-C3 and D1-D20, with dates, grades, supports and limits |
| `records/` | diffusion-factor assessment, weak claim, course alignment, Agent Record (markdown), team handoff |
| `submission/` | Word Agent Record and checklist |

## Limits

- All outputs were generated and reviewed in one Claude session, used in place of ChatGPT/Codex. They are not blinded or independent.
- Two organizations are synthetic.
- No representative measure of agent adoption exists.
