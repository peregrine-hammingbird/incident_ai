# Demo Walkthrough (2 minutes)

Use this in interviews when you want to **show finished reports** instead of running the tool live.

## 1) What problem it solves (15s)
"Alerts arrive in inconsistent formats and analysts waste time rewriting the same triage narrative. incident_ai normalizes key fields and produces a consistent report format to speed up L1→L2 handoff."

## 2) Show the input (15s)
Open `samples/alert_4625.txt` and highlight these fields:
- Alert Name
- Source IP
- Target Host
- Event Code
- Failed Count
- Time Window
- Usernames

Point: the input can be simple key/value text or JSON.

## 3) Show the output artifact (45s)
Open one report in `output/examples/` and show the structure:
1) YAML front matter (SID, host, IP, event code, scoring)
2) "Scoring (Reference Only)" block
3) Narrative sections (Summary, Indicators, ATT&CK Mapping, Data Gaps, Escalation)

Key message: scoring is reference-only and explainable (drivers), and the tool does not make final decisions.

## 4) Show portfolio navigation (20s)
Open `output/examples/index.md`:
- Reports are listed in a table with time, alert, host, category, tier, and scores.
- This makes the project easy to review like a mini case library.

## 5) Close (15s)
"My focus is operational quality: consistent triage, clear uncertainty, and clean escalation notes. incident_ai demonstrates how I would improve SOC workflows even as a junior analyst."
