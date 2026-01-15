# parser.py
import re
import os
from datetime import datetime, timezone
import uuid

def ensure_splunk_sid(fields: dict) -> dict:
    """
    Splunk SID が無い場合は擬似SIDを生成して埋める。
    """
    if "Splunk SID" not in fields or not fields["Splunk SID"].strip():
        fields["Splunk SID"] = str(uuid.uuid4())
    return fields

def build_front_matter(fields: dict, scores: dict) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()

    sid = fields.get("Splunk SID", "UnknownSID")
    search_name = fields.get("Alert Name", "UnknownAlert")
    target_host = fields.get("Target Host", "UnknownHost")
    source_ip = fields.get("Source IP", "UnknownIP")
    event_code = fields.get("Event Code", "Unknown")

    suspicion = scores.get("suspicion", "Unknown")
    confidence = scores.get("confidence", "Unknown")

    fm = [
        "---\n",
        f"splunk_sid: {sid}\n",
        f"search_name: {search_name}\n",
        f"target_host: {target_host}\n",
        f"source_ip: {source_ip}\n",
        f"event_code: {event_code}\n",
        f"suspicion: {suspicion}\n",
        f"confidence: {confidence}\n",
        f"generated_at_utc: {generated_at}\n",
        "---\n\n",
    ]
    return "".join(fm)

def parse_alert_text(alert_text: str) -> dict:
    """
    Splunk / SIEM 風の Key: Value テキストを dict に変換
    """
    fields = {}

    for line in alert_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()

    # 最低限の正規化（欠損対策）
    normalized = {
        "Alert Name": fields.get("Alert Name", "UnknownAlert"),
        "Source IP": fields.get("Source IP", "UnknownIP"),
        "Target Host": fields.get("Target Host", "UnknownHost"),
        "Event Code": fields.get("Event Code", "Unknown"),
    }

    # 他フィールドも保持
    normalized.update(fields)

    return normalized


def sanitize(text: str) -> str:
    """
    ファイル名として安全な文字だけを残す
    """
    return re.sub(r"[^A-Za-z0-9_-]", "", text)


def build_filename(fields: dict) -> str:
    """
    Alert Fields から
    人間が見て分かるインシデントレポート名を生成
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")

    alert_name = sanitize(fields.get("Alert Name", "UnknownAlert"))
    target_host = sanitize(fields.get("Target Host", "UnknownHost"))

    alert_lower = alert_name.lower()
    if "smb" in alert_lower or "login" in alert_lower:
        category = "AuthAbuse"
    elif "powershell" in alert_lower:
        category = "LoLBins"
    elif "dns" in alert_lower:
        category = "C2Suspicion"
    else:
        category = "Generic"

    return f"{timestamp}_{alert_name}_{target_host}_{category}.md"

def parse_report_filename(filename: str) -> dict:
    """
    build_filename() で作った名前を前提に、一覧用の要素を復元する。
    例: 20260115-1412_MultipleFailedSMBLogins_DC01_AuthAbuse.md
    """
    base = os.path.basename(filename)
    name = base[:-3] if base.lower().endswith(".md") else base  # .md 除去

    # index.md は対象外にしたいので呼び出し側で除外する想定
    parts = name.split("_")
    # 期待: [timestamp, alert, host, category]
    if len(parts) < 4:
        return {
            "time": "Unknown",
            "alert": "Unknown",
            "host": "Unknown",
            "category": "Unknown",
            "file": base,
        }

    timestamp = parts[0]
    alert = parts[1]
    host = parts[2]
    category = parts[3]

    return {
        "time": timestamp,
        "alert": alert,
        "host": host,
        "category": category,
        "file": base,
    }

def read_front_matter(md_path: str) -> dict:
    """
    Markdown先頭の YAML front matter を読み取る。
    無い場合は空dictを返す。
    """
    meta = {}
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return meta

    if not lines or not lines[0].strip().startswith("---"):
        return meta

    for line in lines[1:]:
        if line.strip().startswith("---"):
            break
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta

def _to_int(value: str, default: int = 0) -> int:
    """
    '25', '25 attempts', '25 (approx)' みたいな文字列から整数を抜く
    """
    if value is None:
        return default
    m = re.search(r"\d+", str(value))
    return int(m.group(0)) if m else default

def compute_triage_scores(fields: dict) -> dict:
    """
    判断しないスコアリング（Reference Only）
    - suspicion: 行動が攻撃っぽい度合い
    - confidence: 根拠（証拠）がどれだけ揃っているか
    返り値:
      {
        "suspicion": int(0-100),
        "confidence": int(0-100),
        "drivers": [str, ...]
      }
    """
    drivers = []

    alert_name = (fields.get("Alert Name") or "").lower()
    event_code = str(fields.get("Event Code") or "").strip()

    failed = _to_int(fields.get("Failed Count", "0"))
    # "Time Window: 5 minutes" → 5
    window_min = _to_int(fields.get("Time Window", "0"), default=0)

    usernames = fields.get("Usernames", "") or fields.get("Usernames Attempted", "") or ""
    username_list = [u.strip() for u in str(usernames).split(",") if u.strip()]
    username_count = len(username_list)

    # --- Suspicion score（疑わしさ） ---
    suspicion = 0

    # 失敗回数
    if failed >= 50:
        suspicion += 35
        drivers.append("High volume of failed authentications (>=50)")
    elif failed >= 25:
        suspicion += 28
        drivers.append("Multiple failed authentications (>=25)")
    elif failed >= 10:
        suspicion += 18
        drivers.append("Repeated failed authentications (>=10)")
    elif failed >= 5:
        suspicion += 10
        drivers.append("Several failed authentications (>=5)")

    # 時間窓が短いほど怪しい
    if window_min > 0:
        if window_min <= 5:
            suspicion += 18
            drivers.append("High frequency within short time window (<=5 min)")
        elif window_min <= 15:
            suspicion += 10
            drivers.append("Repeated attempts within moderate time window (<=15 min)")

    # 複数ユーザー名（sprayっぽい）
    if username_count >= 5:
        suspicion += 18
        drivers.append("Many distinct usernames targeted (>=5)")
    elif username_count >= 3:
        suspicion += 12
        drivers.append("Multiple distinct usernames targeted (>=3)")

    # ありがちな特権系ユーザー名
    privileged_markers = {"admin", "administrator", "root", "svc", "service", "backup"}
    if any(u.lower() in privileged_markers for u in username_list):
        suspicion += 8
        drivers.append("Privileged/common account names present")

    # 4625（Windows失敗ログオン）などの “認証乱用”系
    if event_code == "4625" or "login" in alert_name or "auth" in alert_name:
        suspicion += 8
        drivers.append("Authentication-abuse pattern (e.g., 4625/login/auth)")

    # カテゴリ推定（build_filenameのcategoryと同じ思想で軽く補強）
    if "powershell" in alert_name:
        suspicion += 10
        drivers.append("PowerShell-related alert (potential LoLBin activity)")
    if "dns" in alert_name:
        suspicion += 8
        drivers.append("DNS-related alert (possible C2 activity)")

    suspicion = max(0, min(100, suspicion))

    # --- Confidence score（根拠の強さ） ---
    # ここは「証拠の有無」で決める。無いなら低いままが正しい。
    confidence = 10  # ベース（ログ1本だけの段階）

    # 具体フィールドが揃っているほど上げる
    if fields.get("Source IP") not in (None, "", "UnknownIP"):
        confidence += 10
        drivers.append("Source IP is specified")
    if fields.get("Target Host") not in (None, "", "UnknownHost"):
        confidence += 10
        drivers.append("Target host is specified")
    if event_code not in ("", "Unknown"):
        confidence += 5
        drivers.append("Event code is specified")

    # “成功”や相関があるなら大きく上げる（今は無いはずなので低いままが自然）
    success = _to_int(fields.get("Successful Count", "0"))
    if success > 0:
        confidence += 35
        drivers.append("Successful authentication observed")

    if str(fields.get("EDR Correlation", "")).lower() in ("true", "yes", "1"):
        confidence += 20
        drivers.append("EDR correlation present")

    if str(fields.get("Network Evidence", "")).lower() in ("true", "yes", "1"):
        confidence += 10
        drivers.append("Network evidence present")

    confidence = max(0, min(100, confidence))

    # driversが増えすぎると読みにくいので上限
    drivers = drivers[:10]

    return {
        "suspicion": suspicion,
        "confidence": confidence,
        "drivers": drivers,
    }


def build_scoring_block(scores: dict) -> str:
    """
    本文の前に差し込むスコアブロック（判断はしない）
    """
    suspicion = scores.get("suspicion", "Unknown")
    confidence = scores.get("confidence", "Unknown")
    drivers = scores.get("drivers", [])

    lines = []
    lines.append("### Scoring (Reference Only)\n")
    lines.append(f"- **Suspicion:** {suspicion} / 100\n")
    lines.append(f"- **Confidence:** {confidence} / 100\n")
    if drivers:
        lines.append("\n**Drivers (evidence-based):**\n")
        for d in drivers:
            lines.append(f"- {d}\n")
    lines.append("\n")
    return "".join(lines)

def summarize_drivers(drivers: list[str], limit: int = 3) -> str:
    """
    index 用に drivers を短縮表現にする
    """
    if not drivers:
        return ""
    short = drivers[:limit]
    # セミコロン区切りで1セルに収める
    return "; ".join(short)

def classify_tier(suspicion: int) -> str:
    if suspicion >= 80:
        return "High"
    if suspicion >= 50:
        return "Medium"
    return "Low"

def format_tier(tier: str) -> str:
    """
    index.md 用の視覚的 tier 表現
    """
    if tier == "High":
        return "🔴 High"
    if tier == "Medium":
        return "🟠 Medium"
    if tier == "Low":
        return "🟢 Low"
    return tier