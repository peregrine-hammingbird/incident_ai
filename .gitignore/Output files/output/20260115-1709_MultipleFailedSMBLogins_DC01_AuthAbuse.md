---
splunk_sid: 86e26890-acfc-439a-a423-14a2f41a87a8
search_name: Multiple Failed SMB Logins
target_host: DC01
source_ip: 10.10.14.23
event_code: 4625
generated_at_utc: 2026-01-15T08:09:23.658980+00:00
---

### Incident Analysis Report

#### 1. Incident Summary
An alert for 'Multiple Failed SMB Logins' has been triggered, indicating a series of failed authentication attempts directed at the target host 'DC01' from the source IP '10.10.14.23'. There have been 25 failed login attempts recorded within a 5-minute time window, with multiple usernames attempted.

#### 2. Observed Indicators
- **Alert Name**: Multiple Failed SMB Logins
- **Source IP**: 10.10.14.23
- **Target Host**: DC01
- **Event Code**: 4625 (indicates failed login attempts)
- **Failed Count**: 25
- **Time Window**: 5 minutes
- **Usernames Attempted**: admin, test, backup
- **Splunk SID**: 86e26890-acfc-439a-a423-14a2f41a87a8

#### 3. Possible Attack Scenarios
- A brute-force attack may be occurring against the SMB service on 'DC01', as evidenced by the multiple failed login attempts using various usernames.
- The attempt could also be a deliberate test of unknown accounts or a misconfiguration leading to unauthorized access attempts.
- It is also possible that legitimate users could be experiencing issues with their credentials, although this is speculative without additional context on user activity.

#### 4. MITRE ATT&CK Mapping
- **Credential Dumping (T1003)**: The attempt may fall under the credential access techniques if it is confirmed to be an unauthorized attempt to gain access.
- **Brute Force (T1110)**: This alert appears to align with brute-force attack techniques given the high number of failed logins in a short timeframe.

#### 5. Uncertainty & Data Gaps
- There is insufficient evidence to conclusively determine the intent behind the failed logins. Possible motives include unauthorized access attempts or user credential misconfigurations.
- Additional data such as user activity logs, network access controls, or an analysis of historical login patterns is needed to ascertain the legitimacy of the login attempts and identify potential compromised users.

#### 6. Escalation Considerations (L2)
- This alert warrants further investigation by Level 2 analysts due to the high number of failed login attempts, which could indicate a potential security risk.
- Analysts should consider analyzing whether any of the usernames are associated with administrative privileges and whether the IP has a history of suspicious activity.

#### 7. Recommended Next Investigation Steps
- Validate if the source IP '10.10.14.23' is recognized within the network. If not, further analysis may be warranted.
- Check the logs for any successful logins following the failed attempts—this could indicate that the attacker may have been successful in gaining access.
- Review the usernames attempted: Are they all valid usernames in the environment? Which accounts have high privileges?
- Gather additional context around the users involved (e.g., were they recently changed or disabled?) and investigate any associated network activities around the same time.
- Consider consulting with system and application owners regarding any expected changes or maintenance activities that might relate to the login attempts.