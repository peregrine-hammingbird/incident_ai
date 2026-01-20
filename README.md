![Incident Reports Index Screenshot](output/examples/index.md)

# Incident AI – SOC Incident Triage Support Tool

Incident AI is a lightweight SOC support tool designed to help analysts
quickly understand security alerts and make informed escalation decisions.

This project focuses on **decision support**, not automation.
Final judgment always remains with human analysts.

---

## What Problem This Solves

In many SOC environments, alerts contain valuable signals,
but context is often scattered, inconsistent, or time-consuming to interpret.

Incident AI helps analysts:
- Normalize alert data
- Highlight relevant indicators
- Produce consistent, analyst-ready incident reports
- Reduce time spent rewriting similar reports

---

## Key Features

- Parses both **unstructured text alerts** and **structured JSON events**
- Extracts core indicators (host, source IP, event ID, timestamps)
- Generates standardized incident reports including:
  - Incident summary
  - Observed indicators
  - MITRE ATT&CK mapping
  - Escalation considerations
- Designed to **support L1 → L2 escalation decisions**
- Avoids black-box automation; emphasizes transparency and analyst judgment

---

## Quickstart

### Requirements
- Python 3.10+
- OpenAI API key (environment variable)

### Install
```bash
pip install openai
```

### Run (file input)
```bash
export OPENAI_API_KEY="YOUR_KEY"
python main.py samples/alert_4625.txt
```

### Run (stdin)
```bash
cat samples/alert_4625.txt | python main.py
```

### Optional: model knobs
```bash
export INCIDENT_AI_MODEL="gpt-4o-mini"
export INCIDENT_AI_TEMPERATURE="0.2"
```

After running:
- A new report is generated under `output/examples/*.md`
- `output/examples/index.md` and `output/examples/index.csv` are updated

---

## Demo (What to Expect)

### Input
- Raw alert text (Key: Value)
- Structured JSON (single object or list of events)

### Output
Incident AI generates a standardized Markdown report that includes:
- YAML front matter (SID, host, IP, event code, scoring)
- A **"Scoring (Reference Only)"** block (**suspicion / confidence** + explainable drivers)
- Analyst-oriented narrative sections (summary, indicators, ATT&CK mapping, gaps, escalation)

The repository also maintains:
- `output/examples/index.md` (human-readable table)
- `output/examples/index.csv` (spreadsheet view)

---

## Scoring (Reference Only)

Incident AI calculates two independent reference scores:
- **Suspicion (0–100):** how “attack-like” the observed pattern is (e.g., high-frequency failures, many usernames)
- **Confidence (0–100):** how complete the evidence is (e.g., source IP / host / event code present)

This tool does **not** make final severity decisions.
The scoring block provides **explainable drivers** for analyst review.

---

## Example Use Case

- Multiple failed SMB authentication attempts detected
- Windows Event ID 4625 observed within a short time window
- Multiple usernames targeted

Incident AI consolidates this data into a clear report,
allowing analysts to quickly assess severity and escalation needs.

---

## Why This Matters in SOC Operations

- Reduces alert fatigue by improving signal clarity
- Improves consistency of incident documentation
- Supports junior analysts without replacing human decision-making
- Reflects real-world SOC workflows and constraints

---

## Technologies

- Python
- Windows Security Event analysis (4624 / 4625)
- MITRE ATT&CK framework
- Log normalization and data structuring

---

## Design Philosophy

This tool is intentionally conservative.

It does not attempt to:
- Automatically classify incidents
- Replace analyst judgment
- Make final escalation decisions

Instead, it provides structured context so analysts can decide faster
and with greater confidence.

---

## Author

SOC-focused security analyst interested in alert triage,
incident response workflows, and practical security tooling.
