#!/usr/bin/env python3
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = ROOT / "examples"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def require_fields(obj, schema):
    missing = [field for field in schema.get("required", []) if field not in obj]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

def main():
    failures = 0
    for path in SCHEMA_DIR.glob("*.schema.json"):
        try:
            load_json(path)
            print(f"OK schema JSON: {path.name}")
        except Exception as exc:
            failures += 1
            print(f"FAIL schema JSON: {path.name}: {exc}")
    for path in EXAMPLE_DIR.glob("*.json"):
        try:
            load_json(path)
            print(f"OK example JSON: {path.name}")
        except Exception as exc:
            failures += 1
            print(f"FAIL example JSON: {path.name}: {exc}")
    return failures

if __name__ == "__main__":
    sys.exit(main())
