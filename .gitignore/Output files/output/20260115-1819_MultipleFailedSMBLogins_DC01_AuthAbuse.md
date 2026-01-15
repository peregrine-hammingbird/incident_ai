---
splunk_sid: 6b0de3ad-c9f6-45ee-b209-998142267596
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
suspicion: 74
confidence: 35
generated_at_utc: 2026-01-15T09:19:56.675633+00:00
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

## Incident Analysis Report

### 1. Incident Summary
This alert indicates multiple failed SMB (Server Message Block) login attempts on the target host 'DC01' from the source IP '10.10.14.23'. A total of 25 failed logins were recorded over a time window of 5 minutes. The usernames attempted during these logins include 'admin', 'test', and 'backup'.

### 2. Observed Indicators
- **Alert Name**: Multiple Failed SMB Logins
- **Source IP**: 10.10.14.23
- **Target Host**: DC01
- **Event Code**: 4625 (indicating failed logon attempts)
- **Failed Count**: 25 failed login attempts
- **Time Window**: 5 minutes
- **Usernames Attempted**: admin, test, backup
- **Splunk SID**: 6b0de3ad-c9f6-45ee-b209-998142267596

### 3. Possible Attack Scenarios
- **Brute Force Attack**: The high number of failed login attempts suggests a possible brute force attack where an unauthorized user may be attempting to gain access to the target host using common or default usernames.
- **Credential Stuffing**: If the usernames employed are known or common accounts, this could also reflect a credential stuffing attack, where previously leaked or guessed password combinations are being tested.
- **Technical Error**: There exists the possibility that these attempts may be the result of a misconfiguration or automated process misfiring rather than a direct attack.

### 4. MITRE ATT&CK Mapping
- **T1110 - Brute Force**: This technique involves repeated attempts to log in using different credentials to gain unauthorized access.
- **T1078 - Valid Accounts**: If valid credentials are used (though this is not confirmed) this may be applicable if an attacker is trying known usernames with compromised passwords.

### 5. Uncertainty & Data Gaps
- **User Context**: There is no indication whether the attempted logins originated from an internal or external IP without additional context on network segmentation or firewall rules.
- **Password Attempts**: Details on the passwords used for the login attempts are not available, preventing confirmation of attack vectors such as credential stuffing.
- **Account Lockout Policies**: The effectiveness of account lockout policies in place is unknown—no information on whether any accounts were locked following these failed attempts.

### 6. Escalation Considerations (L2)
- **Potential Threat Assessment**: Given the volume of failed login attempts, escalation to Level 2 is advisable for deeper analysis into the source IP's activity and historical patterns.
- **Further Investigation into User Accounts**: Level 2 analysts should examine whether the attempted usernames are legitimate and if those accounts have unusual access patterns or previously associated incidents.
- **Correlation with Other Alerts**: Review other alerts or logs that may correlate with the timing and context of this incident to establish a broader context.

### 7. Recommended Next Investigation Steps
- Collect additional logs for the source IP (10.10.14.23) to assess for other suspicious activity.
- Investigate the credentials used in these attempts by checking against known breaches or leaks for password information.
- Query the security settings and policies in place for account lockouts to understand potential vulnerabilities.
- Monitor the target host ‘DC01’ for any subsequent successful login attempts or abnormal activities that may suggest further attempts to exploit these failed logins.

By following these steps, analysts can build a clearer picture of this event and determine any necessary actions.