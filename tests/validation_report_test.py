import json
from pathlib import Path

root = Path(__file__).parents[1]

validation_report_path = root / "reports" / "validation_report.json"

def test_report_structure():
    with open(validation_report_path, "r") as file:
        data = json.load(file)
        assert type(data) == list
        for item in data:
            assert type(item) == dict
            assert {"dataset", "check", "status", "message"}.issubset(item.keys())
            assert item["status"] in {"PASSED", "FAILED", "SKIPPED", "NOT_CONFIGURED"}
            assert item['dataset']
            assert item['check']
            assert item['message']
        # print(len(data))
        # print(data[0])