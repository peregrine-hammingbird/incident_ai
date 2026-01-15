---
splunk_sid: 2c4fc45f-cd0e-4080-8a89-8531201b48fa
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
generated_at_utc: 2026-01-15T08:03:05.240166+00:00
---

### Incident Analysis Report

#### 1. Incident Summary
An alert for 'Multiple Failed SMB Logins' has been triggered involving significant failed login attempts to the target server 'DC01' from the source IP '10.10.14.23'. The event was recorded with a total of 25 failed login attempts within a 5-minute time frame, utilizing multiple usernames.

#### 2. Observed Indicators
- **Source IP:** 10.10.14.23
- **Target Host:** DC01
- **Event Code:** 4625 (indicating failed login attempts)
- **Failed Count:** 25 failed logins
- **Time Window:** 5 minutes
- **Usernames Attempted:** admin, test, backup
- **Splunk SID:** 2c4fc45f-cd0e-4080-8a89-8531201b48fa

#### 3. Possible Attack Scenarios
- **Brute Force Attack:** The high number of failed login attempts (25) in a short time frame could suggest a brute force attack attempting to guess passwords for the user accounts listed.
- **Credential Stuffing Attack:** The attempt to access multiple accounts ('admin', 'test', 'backup') may indicate a credential stuffing scenario, where leaked credentials from other services are being tested.
- **Misconfiguration or Error:** It is also possible that these failed attempts are due to misconfigurations or legitimate users entering incorrect credentials.

#### 4. MITRE ATT&CK Mapping
- **T1110 - Brute Force:** The failed login attempts may be classified under this technique, as they appear to include a high number of attempts to guess user passwords.

#### 5. Uncertainty & Data Gaps
- The current data does not confirm whether these attempts are malicious or the result of legitimate users experiencing issues logging in.
- Additional context, such as historical login data for the specified accounts and source IP reputation, is not available.
- There is no information regarding the actual configuration of access restrictions or lockout policies in place for these accounts.

#### 6. Escalation Considerations (L2)
- Level 2 Analysts should be made aware of the high count of failed login attempts and the potential urgency for investigation into the source IP for any further malicious activities.
- Analysts should consider verifying the geographical origin of the IP address and any known reputation issues.
- Monitoring for successful logins post-failed attempts should be a priority to determine if any account compromise has occurred.

#### 7. Recommended Next Investigation Steps
- Investigate the source IP (10.10.14.23) to identify if it is associated with known malicious activities or patterns.
- Review account activity logs for the usernames involved to assess if there were any successful logins after the failed attempts.
- Determine if there are any active locking mechanisms in place for repeated failed login attempts and the effectiveness of those policies.
- Collect additional contextual data regarding typical login behavior for the accounts involved to discern any abnormal patterns or behavior.