from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_all_schemas_are_json():
    for path in (ROOT / "schemas").glob("*.schema.json"):
        json.loads(path.read_text(encoding="utf-8"))

def test_all_examples_are_json():
    for path in (ROOT / "examples").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
