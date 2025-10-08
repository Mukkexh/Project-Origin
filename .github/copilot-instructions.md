## Copilot / AI Agent Instructions — Project Origin

Purpose: help an AI coding agent become productive quickly in this repository by describing the discovered architecture, required guardrails, and actionable patterns found in the workspace.

1) Big-picture architecture (from `Readme.md`)
- Data Layer: open genetic, archaeological, linguistic, and climate datasets (see `Readme.md` "Data Layer"). Treat datasets as large, sensitive artifacts — do not exfiltrate or assume public availability unless present in `assets/`.
- Processing Layer: Python + OpenAI ("Processing Layer (Python + Open AI)"). Expect helpers to convert ancestry summaries into migration routes and to generate GeoJSON / intermediate artifacts for visualization.
- Visualization Layer: Unity / Unreal ("Visualization Layer (Unity / Unreal Engine)") — 3D Earth + narrated VR scenes. Code for this layer is not present in the repo root; assume engine projects will live in new top-level folders when added.

2) What to look for in this workspace
- Files discovered: `Readme.md` (project vision + architecture), directories: `assets/`, `concepts/`, `scripts/` (currently empty). Use these as the primary anchors when augmenting the repo.
- If you need processing code, search for Python files or a `requirements.txt`/`pyproject.toml`. None were found—create new files under `scripts/` or a `python/` or `tools/` folder and document them in `Readme.md`.

3) Project-specific conventions and guardrails
- Licensing: CC-BY-NC 4.0 (from `Readme.md`) — avoid adding code or examples that enable commercial use unless explicitly requested.
- Privacy: Personal DNA and sensitive inputs must be described as local-only or encrypted. Never include instructions that upload sample personal DNA to third-party services.
- Ethical behavior: Prefer opt-in flows and note in comments where data must be encrypted or anonymized.

4) Actionable tasks an AI agent can perform immediately
- Add runnable Processing Layer scaffolding: create `scripts/process_ancestry.py` that accepts a local CSV/JSON and outputs GeoJSON into `assets/geojson/`. Keep code modular and include a small README in `scripts/` explaining inputs/outputs.
- If adding tests, prefer small unit tests using `pytest` in a `tests/` folder and only reference realistic, non-sensitive dummy datasets under `assets/sample/`.

5) Coding patterns & examples (discoverable from repo)
- Use `assets/` for all data artifacts (raw and processed). Example: output GeoJSON -> `assets/geojson/migration_<shortid>.json`.
- Document system decisions in `Readme.md` (already present) and keep short technical notes in `concepts/` next to diagrams or JSON samples.

6) Developer workflows (what's missing and assumptions)
- No build/test commands or dependency manifests were found. Assume Python tooling: create `requirements.txt` or `pyproject.toml` when adding Python code. Add `README` snippets in `scripts/` showing how to run local scripts (example: `python scripts/process_ancestry.py --input assets/sample.csv --out assets/geojson/`).
- For visualization work, add a top-level `unity/` or `unreal/` directory and include a short `README` explaining engine version and export conventions.

7) Communication & PR guidance for agents
- Keep changes minimal and self-contained. Add `README`/usage docs for any new tooling. For data-processing code, include an explicit statement that no real personal DNA was used and include synthetic sample inputs in `assets/sample/`.

8) Quick checks the agent should run before proposing code
- Verify `Readme.md` usage assumptions (architecture sections) and reference them in new files' headers.
- Avoid adding secrets, remote API keys, or instructions that upload sensitive inputs.

Assumptions made (minimal):
- The repository is an early-stage concept scaffold (no engine code, no Python packages yet). If you find additional hidden subfolders later, prefer merging changes into their existing layout.

If anything in this instruction is unclear or you'd like more specific scaffolding (example: a concrete `process_ancestry.py` starter, or a `requirements.txt`), say which target to add and I will create it and a small test harness.
