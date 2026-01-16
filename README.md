![Incident Reports Index Screenshot](docs/index_view.png)

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
