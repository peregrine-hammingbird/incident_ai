---
splunk_sid: d013ed1e-1595-4567-8c92-cf7a4ae266c6
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
suspicion: 74
confidence: 35
generated_at_utc: 2026-01-15T08:50:53.395883+00:00
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

### 1. Incident Summary
The security alert indicates that multiple failed SMB (Server Message Block) login attempts were recorded on the target host DC01 from the source IP 10.10.14.23. Within a 5-minute time window, there were 25 failed login attempts associated with the usernames 'admin', 'test', and 'backup', raising potential security concerns regarding unauthorized access attempts.

### 2. Observed Indicators
- **Alert Name**: Multiple Failed SMB Logins
- **Source IP**: 10.10.14.23
- **Target Host**: DC01
- **Event Code**: 4625 (indicating failed logon)
- **Failed Count**: 25
- **Time Window**: 5 minutes
- **Usernames Attempted**: admin, test, backup
- **Splunk SID**: d013ed1e-1595-4567-8c92-cf7a4ae266c6

### 3. Possible Attack Scenarios
- **Brute Force Attack**: The high number of failed login attempts (25 in 5 minutes) could suggest an attempt to gain unauthorized access via brute force methods using common or known usernames like ‘admin’, ‘test’, and ‘backup’.
- **Credential Stuffing**: If the usernames correspond to accounts with known or reused passwords, this could indicate a credential stuffing attack, where attackers utilize leaked password lists.

### 4. MITRE ATT&CK Mapping
- **T1110**: Brute Force - The observed behavior of multiple failed login attempts fits within this technique, typically associated with unauthorized access attempts.
- **T1078**: Valid Accounts - If an attacker were successful, they might use valid account credentials to gain unauthorized access.

### 5. Uncertainty & Data Gaps
- The evidence provided does not confirm whether these login attempts were initiated by an external entity or an internal user may have mistakenly attempted to log in with incorrect credentials.
- There is no information about the context of the source IP (10.10.14.23) – whether it belongs to a trusted internal network or an external source.
- No information is provided on whether any successful login attempts occurred following these failed attempts.
- Additional logs and context regarding user account lockout policies and the activity associated with these usernames are missing.

### 6. Escalation Considerations (L2)
- Level 2 analysts should assess the context of the source IP address and verify whether it is consistent with known users or devices within the network.
- Analysts might consider correlations with other alerts or logs around the same time to determine if this activity is part of a broader pattern of suspicious behavior.
- Investigation into the user accounts (admin, test, backup) is warranted to determine their legitimacy, usage patterns, and potential for compromise.
- Review of any subsequent successful login attempts could provide further clarity on the situation.

### 7. Recommended Next Investigation Steps
- Investigate the source IP 10.10.14.23 to determine its origin and legitimacy within the network.
- Correlate this alert with other security alerts or logs (e.g., firewall logs, IDS/IPS alerts) that may indicate additional suspicious activity.
- Review account lockout policies and any additional logging related to the usernames involved in the failed logins.
- Analyze user behavior associated with the attempted usernames to establish if they have legitimate access or if their accounts may be misconfigured or compromised.