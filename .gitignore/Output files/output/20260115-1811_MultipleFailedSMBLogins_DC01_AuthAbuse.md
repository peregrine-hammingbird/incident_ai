---
splunk_sid: a302ebac-d9b5-4b58-b374-6ae837442e8c
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
suspicion: 74
confidence: 35
generated_at_utc: 2026-01-15T09:11:38.193782+00:00
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

### Incident Analysis Report

#### 1. Incident Summary
The alert indicates that there were multiple failed SMB (Server Message Block) login attempts detected on the target host, DC01, originating from the source IP address 10.10.14.23. In a time window of 5 minutes, there were 25 failed authentication attempts associated with the usernames: admin, test, and backup.

#### 2. Observed Indicators
- **Alert Name:** Multiple Failed SMB Logins
- **Source IP:** 10.10.14.23
- **Target Host:** DC01
- **Event Code:** 4625
- **Failed Login Count:** 25
- **Time Window:** 5 minutes
- **Usernames Attempted:** admin, test, backup
- **Splunk SID:** a302ebac-d9b5-4b58-b374-6ae837442e8c

#### 3. Possible Attack Scenarios
The observed failed logins may suggest several scenarios, including:
- **Brute Force Attack:** An attempt to guess passwords for the provided usernames due to the high number of failed attempts in a short period.
- **Misconfiguration or Typing Errors:** Legitimate users may have incorrectly entered their credentials multiple times.
- **Scripted Attack/Automated Tool:** The rapid nature of failed logins could indicate the use of a script or automation to test username-password combinations.

#### 4. MITRE ATT&CK Mapping
- **Brute Force:** T1110
- **Account Lockout:** T1110.001
(Note: Further investigation would be needed to determine if any accounts are getting locked, which would indicate a successful or ongoing brute force effort.)

#### 5. Uncertainty & Data Gaps
- There is uncertainty surrounding whether these failed authentication attempts are malicious in nature or due to legitimate user behavior, as no additional context is provided.
- Details regarding whether any accounts were locked or additional context about user activity during this time are missing.
- There is no information on the status of the accounts used in the failed logins (e.g., if they are active or have had recent changes).

#### 6. Escalation Considerations (L2)
- Consider escalating due to the high number of failed login attempts which may indicate an active exploration of weak account credentials.
- Analysts at Level 2 may want to review logs surrounding the source IP for additional context and investigate any related network activity.

#### 7. Recommended Next Investigation Steps
- Collect and review additional logs from DC01 related to the attempted logins, including any responses to these failed attempts.
- Investigate the activity of the source IP (10.10.14.23) across the network to determine if there are any other suspicious activities.
- Check the account statuses of the usernames involved in the failed logins to ascertain their legitimacy and recent changes.
- Identify if there were any successful logins that occurred from the source IP during or after the time window of the alert. 

This report presents a summary of the alert and potential considerations for further investigation but does not draw definitive conclusions about the nature of the activity described in the alert.