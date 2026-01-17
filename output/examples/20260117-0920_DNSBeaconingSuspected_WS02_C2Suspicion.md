---
splunk_sid: demo-sid-0003
search_name: DNS Beaconing Suspected
target_host: WS02
source_ip: 10.0.0.5
event_code: Unknown
suspicion: 8
confidence: 30
drivers_short: DNS-related alert (possible C2 activity); Source IP is specified; Target host is specified
generated_at_utc: 2026-01-17T00:00:00+00:00
---

### Scoring (Reference Only)
- **Suspicion:** 8 / 100
- **Confidence:** 30 / 100

**Drivers (evidence-based):**
- DNS-related alert (possible C2 activity)
- Source IP is specified
- Target host is specified

## 1. Incident Summary
A DNS-related alert labeled as potential beaconing was observed for host WS02. The data provided is not sufficient to confirm command-and-control behavior. This report captures the key identifiers and outlines the minimum enrichment needed to validate whether the pattern is benign or suspicious.

## 2. Observed Indicators
- Target host: WS02
- Source IP: 10.0.0.5
- Event code: not provided

## 3. Possible Attack Scenarios
- Benign periodic DNS lookups by legitimate software.
- Misconfigured application retrying name resolution.
- Malware communicating via DNS-based beaconing or resolution of C2 infrastructure.

## 4. MITRE ATT&CK Mapping
- Command and Control: Application Layer Protocol - DNS (T1071.004) (candidate mapping based on DNS C2 suspicion).

## 5. Uncertainty & Data Gaps
- No queried domain names, query types, or response codes are provided.
- No timing characteristics (interval regularity) are provided.
- No process attribution or EDR correlation is provided.

## 6. Escalation Considerations (L2)
- Escalate if domains are newly registered, high-entropy, or known malicious.
- Escalate if DNS activity correlates with suspicious processes, new persistence, or outbound network anomalies.

## 7. Recommended Next Investigation Steps
- Extract the domains queried, query frequency, and interval regularity.
- Attribute DNS queries to a process or user context on WS02.
- Check for other network indicators (HTTP(S) beacons, unusual destinations) from WS02.
- Compare against a baseline for WS02 to determine whether this pattern is new.
