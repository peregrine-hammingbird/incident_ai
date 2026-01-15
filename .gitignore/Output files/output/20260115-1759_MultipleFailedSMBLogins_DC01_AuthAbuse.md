---
splunk_sid: 45c717ed-b2ed-4ca9-a063-59dd09ff518e
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
suspicion: 74
confidence: 35
generated_at_utc: 2026-01-15T08:59:19.710792+00:00
---

### Scoring (Reference Only)
- **Suspicion:** 74 / 100
- **Confidence:** 35 / 100

**Drivers (evidence-based):**
- Multiple failed authentications (>=25)
- High frequency within short time window (<=5 min)
- Multiple distinct usernames targeted (>=3)
- Privileged/common account names present
- Authentication-abuse pattern (e.g., 4625/login/auth)
- Source IP is specified
- Target host is specified
- Event code is specified

# Incident Analysis Report

## 1. Incident Summary
An alert indicating multiple failed SMB (Server Message Block) logins was triggered, originating from the IP address 10.10.14.23 targeting the host DC01. In a time window of 5 minutes, there have been 25 failed login attempts associated with multiple usernames.

## 2. Observed Indicators
- **Alert Name:** Multiple Failed SMB Logins
- **Source IP:** 10.10.14.23
- **Target Host:** DC01
- **Event Code:** 4625 (indicating failed logon attempts)
- **Failed Count:** 25
- **Time Window:** 5 minutes
- **Usernames Attempted:** admin, test, backup
- **Splunk SID:** 45c717ed-b2ed-4ca9-a063-59dd09ff518e

## 3. Possible Attack Scenarios
- **Brute Force Attack:** The high number of failed login attempts within a short period suggests a potential brute force attack aimed at gaining unauthorized access to SMB shares.
- **Misconfiguration or Legitimate Behavior:** It is possible that these failed logins are the result of a misconfigured application or legitimate user error.
- **Account Enumeration:** The use of multiple usernames may suggest attempts to enumerate valid accounts.

## 4. MITRE ATT&CK Mapping
- **T1110 - Brute Force:** The activity of trying multiple passwords against various accounts fits with tactics involved in brute force attacks.
- **T1078 - Valid Accounts:** The involvement of known usernames could suggest attempts to exploit valid accounts for access.

## 5. Uncertainty & Data Gaps
- There is currently insufficient evidence to determine the intent behind the failed login attempts (malicious vs. benign).
- The alert does not provide information on whether the attempted logins were made from a compromised host or by a legitimate user.
- Further investigation is required to verify the nature of the source IP address (e.g., whether it is internal, external, or a known asset).

## 6. Escalation Considerations (L2)
- Prioritize this alert for further investigation due to the high count of failed logins.
- Analyze logs related to the source IP for any additional patterns or activities occurring prior to this alert.
- Verify if there have been any recent changes to password policies or account configurations that may explain the failed attempts.

## 7. Recommended Next Investigation Steps
- Conduct a detailed analysis of logs from both the target host (DC01) and the source IP (10.10.14.23) to monitor for additional related activities.
- Cross-reference the usernames with user account status (e.g., are they active and potentially exposed?).
- Investigate whether there have been any alerts or incidents associated with the source IP previously.
- Review user access rights for the account attempts to ascertain if they should have the associated permissions.