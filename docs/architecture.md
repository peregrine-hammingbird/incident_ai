# Architecture (High level)

## Pipeline
1. **Input**: raw alert text (Key: Value) or JSON
2. **Parse & Normalize** (`parser.py`)
   - Extract standardized fields (Alert Name, Source IP, Target Host, Event Code, counts, etc.)
3. **Reference-only Scoring** (`compute_triage_scores`)
   - `suspicion`: attack-likeness
   - `confidence`: evidence completeness
   - `drivers`: explainable reasons
4. **Report Writing** (`prompt.py` + LLM)
   - Generate narrative sections (summary, indicators, ATT&CK mapping, gaps, escalation)
   - Non-goals: no final decisions, no remediation/containment recommendations
5. **Artifacts** (`main.py`)
   - Markdown report saved to `output/*.md`
   - `output/index.md` and `output/index.csv` regenerated for portfolio viewing
