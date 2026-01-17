---
splunk_sid: demo-sid-0001
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 203.0.113.10
event_code: 4625
suspicion: 80
confidence: 35
drivers_short: Multiple failed authentications (>=25); High frequency within short time window (<=5 min); Many distinct usernames targeted (>=5)
generated_at_utc: 2026-01-17T00:00:00+00:00
---

### Scoring (Reference Only)
- **Suspicion:** 80 / 100
- **Confidence:** 35 / 100

**Drivers (evidence-based):**
- Multiple failed authentications (>=25)
- High frequency within short time window (<=5 min)
- Many distinct usernames targeted (>=5)
- Privileged/common account names present
- Authentication-abuse pattern (e.g., 4625/login/auth)
- Source IP is specified
- Target host is specified
- Event code is specified

## 1. Incident Summary
A high volume of failed SMB authentication attempts was observed against host **DC01** from **203.0.113.10**. The pattern includes multiple distinct usernames within a short time window and corresponds to Windows logon failure event code **4625**.

## 2. Observed Indicators
- Target host: DC01
- Source IP: 203.0.113.10
- Event code: 4625 (failed logon)
- Failed attempts: 28 within 5 minutes
- Usernames: administrator, admin, svc_backup, test, guest

## 3. Possible Attack Scenarios
- Password spraying across multiple accounts.
- Brute force attempts targeting common or privileged usernames.
- Benign explanation is possible (misconfigured service, repeated user error), but the volume and diversity of usernames increase suspicion.

## 4. MITRE ATT&CK Mapping
- Credential Access: Brute Force (Password Spraying)

## 5. Uncertainty & Data Gaps
- No confirmation of successful authentication in the provided data.
- No process, network, or EDR correlation evidence is included.
- Missing: outcome context (success counts), destination service details, and whether the source IP is known/trusted.

## 6. Escalation Considerations (L2)
Escalate if any of the following are observed:
- Any successful logon from the same source IP or nearby timeframe.
- Repeated activity across multiple hosts or privileged accounts.
- Known-bad source reputation or geographic anomaly.

## 7. Recommended Next Investigation Steps
- Check for successful logons (e.g., 4624) for the targeted accounts around the same time.
- Review additional authentication telemetry (lockouts, MFA prompts, VPN logs) if available.
- Identify whether 203.0.113.10 is internal, partner, or external internet.
- Pivot on the source IP to see if it targeted other hosts.
