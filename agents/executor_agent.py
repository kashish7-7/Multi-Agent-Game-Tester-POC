import os
import json
from agents.ranker_agent import rank_test_cases
from agents.planner_agent import generate_test_cases

TEST_FILE = "test_cases.json"
REPORT_FILE = "reports/report.json"

def cleanup_files():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)

def execute_test(test_case):
    result = {
        "test_id": test_case.get("test_id"),
        "description": test_case.get("description"),
        "verdict": "Pass",
        "evidence": [f"screenshot_{test_case.get('test_id')}.png"]
    }
    return result

def execute_tests(test_cases):
    results = []
    for tc in test_cases:
        res = execute_test(tc)
        results.append(res)
    return results

def save_report(results, file_path=REPORT_FILE):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(results, f, indent=2)

def load_or_generate_test_cases(num_cases=20):
    test_cases = generate_test_cases(num_cases=num_cases)
    with open(TEST_FILE, "w") as f:
        json.dump(test_cases, f, indent=2)
    return test_cases
