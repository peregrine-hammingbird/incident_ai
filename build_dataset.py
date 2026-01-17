"""Build a JSONL dataset from facts + optional human labels.

- Reads:   data/facts/*.json
- Labels:  data/labels/<same_stem>.label.json (optional)
- Writes:  data/dataset.jsonl (JSON Lines)
          data/dataset_pretty.json (pretty-printed JSON for humans)
"""

import json
from pathlib import Path

FACTS_DIR = Path("data/facts")
LABELS_DIR = Path("data/labels")
OUT_PATH = Path("data/dataset.jsonl")
PRETTY_OUT_PATH = Path("data/dataset_pretty.json")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if not FACTS_DIR.exists():
        raise SystemExit(f"Facts directory not found: {FACTS_DIR}")
    if not LABELS_DIR.exists():
        raise SystemExit(f"Labels directory not found: {LABELS_DIR}")

    fact_files = sorted(FACTS_DIR.glob("*.json"))
    if not fact_files:
        raise SystemExit("No fact files found in data/facts")

    rows: list[dict] = []
    missing_labels: list[str] = []

    for fact_path in fact_files:
        base = fact_path.stem
        label_path = LABELS_DIR / f"{base}.label.json"

        fact = load_json(fact_path)

        if label_path.exists():
            label = load_json(label_path)
        else:
            label = None
            missing_labels.append(label_path.name)

        rows.append(
            {
                "id": base,
                "input": fact,
                "label": label,
            }
        )

    # Ensure output directory exists
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # JSONL
    with OUT_PATH.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Pretty JSON（人間用）
    with PRETTY_OUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"✅ Wrote dataset: {OUT_PATH} ({len(rows)} records)")
    if missing_labels:
        print("⚠ Missing label files (still included with label=None):")
        for name in missing_labels:
            print(f"  - {name}")

if __name__ == "__main__":
    main()
