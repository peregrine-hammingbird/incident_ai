---
splunk_sid: demo-sid-0002
search_name: Suspicious PowerShell EncodedCommand
target_host: WS01
source_ip: UnknownIP
event_code: 4104
suspicion: 10
confidence: 25
drivers_short: PowerShell-related alert (potential LoLBin activity); Target host is specified; Event code is specified
generated_at_utc: 2026-01-17T00:00:00+00:00
---

### Scoring (Reference Only)
- **Suspicion:** 10 / 100
- **Confidence:** 25 / 100

**Drivers (evidence-based):**
- PowerShell-related alert (potential LoLBin activity)
- Target host is specified
- Event code is specified

## 1. Incident Summary
A PowerShell script block logging event (Event Code 4104) triggered an alert labeled as suspicious encoded command usage on host WS01. The provided data lacks the script content and any source context, so this should be treated as a triage lead rather than a confirmed malicious execution.

## 2. Observed Indicators
- Target host: WS01
- Event code: 4104 (PowerShell script block logging)
- Source IP: not provided

## 3. Possible Attack Scenarios
- Legitimate administrative automation using encoded command.
- User-initiated scripting for troubleshooting.
- Malicious execution via PowerShell (living-off-the-land) using encoding to obfuscate intent.

## 4. MITRE ATT&CK Mapping
- Execution: PowerShell (T1059.001) (candidate mapping based on PowerShell activity).

## 5. Uncertainty & Data Gaps
- Script block content is not included.
- Parent process, command line, user context, and network connections are not included.
- No EDR correlation is provided.

## 6. Escalation Considerations (L2)
- If WS01 is a high-value endpoint (admin workstation, server), prioritize enrichment.
- Escalate if script content indicates download/execution, credential access, or persistence.

## 7. Recommended Next Investigation Steps
- Retrieve the full PowerShell script block content and any related event fields.
- Identify the executing user, parent process, and command line that produced the script block.
- Correlate with EDR telemetry for suspicious child processes and outbound connections.
- Check for repeated occurrences of encoded command usage on the same host.
