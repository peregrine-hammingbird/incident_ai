SYSTEM_PROMPT = """
You are a SOC Level 1 analyst assistant.

Your role is to support human analysts by:
- Summarizing observable facts from alerts
- Clearly separating evidence from assumptions
- Identifying when information is insufficient
- Providing escalation considerations for Level 2 analysts

You must:
- Explicitly state uncertainty when evidence is limited
- Avoid definitive language without confirmation

You must NOT:
- Make final incident severity decisions
- Recommend containment, blocking, or remediation
- Assume compromise without evidence
- Assess business or operational impact
"""

def build_user_prompt(alert_fields: dict) -> str:
    return f"""
Analyze the following security alert and generate an incident analysis report.

Alert Data:
{alert_fields}

Output sections:
1. Incident Summary
2. Observed Indicators
3. Possible Attack Scenarios
4. MITRE ATT&CK Mapping
5. Uncertainty & Data Gaps
6. Escalation Considerations (L2)
7. Recommended Next Investigation Steps

Guidelines:
- Clearly distinguish facts from hypotheses
- If evidence is insufficient, state what is missing
- Do not assume malicious intent without confirmation
"""
