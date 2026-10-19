# Promethean Technology Classification Agent

Assignment 4 (Lab 4 - SubAgent 3 Promethean). Specialist version 1.1. Student: Minghan Liu.

This specialist asks whether an emerging technology is incremental, a breakthrough, or potentially Promethean. It then asks, separately, how much that broad significance should influence an organization's present application decision. It applies the course Operational Classification (Layer 1 system test, barrier statement, suppression test, six criteria, tiers, mode). It adds a qualification rule and a significance firewall, both added after a preserved cycle 1 overclaim.

**Current answer for the team's technology (evidence date 2026-10-18):** agentic AI is a **Breakthrough** (moderate confidence). Its **Potential-Promethean candidacy is UNRESOLVED** (low confidence). For NYU SPS's applicant-support proposal, that broad significance should carry **Low** weight: it shapes monitoring and learning, not the pilot decision.

## Run

From the repository root, with Python 3 (standard library only; no API key):

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/promethean_classification_agent --case agents/promethean_classification_agent/cases/primary.json
```

Paste the generated packet from `work/` into ChatGPT and ask for JSON only. Save the reply as a NEW file so the archived tests stay intact, then run:

```bash
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/promethean_classification_agent/tests/verify_package.py
```

Repeat with `contrast_1.json`, `contrast_2.json` and `hype_probe.json`.

## Package map

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1 logic, admissibility table, qualification rule, significance firewall, embedded source register |
| `cases/` | primary (NYU SPS), contrast_1 (aggressive synthetic provider), contrast_2 (conservative synthetic hospital), hype_probe |
| `responses/` | final v1.1 outputs |
| `tests/cycle_1/` | v1.0 instructions, four outputs (including the preserved overclaim), review, hash manifest |
| `tests/cycle_2/` | v1.1 instructions, four outputs, review, hash manifest |
| `tests/prompts/` | exact prompt packets for both cycles |
| `tests/verify_package.py`, `tests/validation_log.txt` | 22 structural and invariance checks |
| `evidence/source_register.json` | C1-C3 course/upstream sources and E1-E17 external sources, each with what it does and does not support |
| `records/` | criteria, evidence for/against, course alignment, Agent Record (markdown), team handoff |
| `submission/` | Word Agent Record and submission checklist |

## Evaluation limits

All outputs were generated and reviewed in one Claude session, used in place of ChatGPT/Codex. They are not blinded, independent or repeated runs. Two of the four organizations are synthetic. No deployment, applicant data or measured outcome is involved. Course slide files are not republished here.
