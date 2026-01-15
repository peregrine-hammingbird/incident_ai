# incident_ai  
SOC向けインシデントトリアージ支援AI（プロトタイプ）

---

## 概要
`incident_ai` は、**SIEM（Splunk想定）のアラート内容を入力するだけで**  
SOC業務における **L1トリアージを支援**するためのインシデント分析レポートと  
ケース一覧（インデックス）を自動生成するツールです。

本ツールは **AIに最終判断をさせない** ことを設計原則としています。

---

## 想定ユースケース（SOC業務フロー）

```text
[Splunk Alert]
      ↓
[L1 Analyst]
  アラート内容を incident_ai に投入
      ↓
[incident_ai]
  ・事実整理
  ・ルールベーススコア算出
  ・インシデントレポート生成
  ・ケース一覧（index）更新
      ↓
[L1 / L2 Analyst]
  スコアと根拠を基に人間が判断

## 主な機能
1. インシデントレポート自動生成
Splunk風の Key: Value 形式アラートを解析
事実ベースの Incident Analysis Report を生成
Markdown形式で保存（UTF-8）

2. Front Matter による追跡性の確保
各レポートの先頭に、以下のメタデータを付与します。

yamlコードをコピーする
splunk_sid: <UUID or Splunk SID>
search_name: <Alert Name>
target_host: <Host>
source_ip: <IP>
event_code: <Event Code>
suspicion: <0-100>
confidence: <0-100>
generated_at_utc: <UTC timestamp>

これにより、
L2がSplunk検索結果に即復帰可能
監査・後追い調査に対応可能
となっています。

3. ルールベース・スコアリング（判断はしない）
以下の2種類のスコアを算出します。

Suspicion Score（疑わしさ）
行動パターンがどれだけ攻撃的か
Confidence Score（根拠の強さ）
証拠がどれだけ揃っているか

## 特徴：
完全ルールベース（再現性・説明責任を重視）
AIはスコアを決定しない
スコアの根拠（drivers）を本文に明示

4. ケース一覧（index）自動生成
output/ 配下に以下を自動生成します。

index.md（人間向け）
time / alert / host / category
tier（🟥🟠🟢）
suspicion / confidence
レポートへのリンク
index.csv（機械・運用向け）
Excel / Splunk lookup / 後処理向け
sid / tier / scores / drivers を含む完全情報

なぜ「AIに判断させない」のか
SOC業務では以下が重要です。

誤検知時の責任問題
監査・再現性
人間による最終判断

そのため本ツールでは、
スコア算出：ルールベース
文章化・要約：LLM
判断：人間（L1/L2）
という明確な責務分離を行っています。

## 対応環境
Windows（PowerShell）
Linux / Kali
stdin / ファイル引数 両対応
UTF-8 明示対応

## 使用例
Windows / PowerShell
powershell
Get-Content sample_alerts\smb_bruteforce.txt -Encoding UTF8 | python main.py
Linux
bash
python main.py < sample_alerts/smb_bruteforce.txt

## 想定される拡張
Splunk Webhook JSON 直接入力
MITRE ATT&CK ID の付与
誤検知フィードバックによるスコア重み調整

## 開発の狙い
本ツールは
**「AIを作ること」ではなく「SOC業務を分解・設計すること」**
を目的として開発しました。

L1トリアージの負荷軽減
L2への引き継ぎ品質向上
判断の属人化防止

を重視しています。