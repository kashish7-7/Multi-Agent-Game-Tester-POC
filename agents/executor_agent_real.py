from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, os

def execute_tests_real(test_cases, game_url):
    results = []
    os.makedirs("screenshots", exist_ok=True)

    for test_case in test_cases:
        result = {
            "test_id": test_case.get("test_id"),
            "description": test_case.get("description"),
            "verdict": "Fail",
            "evidence": []
        }

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(game_url)
        time.sleep(2)

        try:
            for step in test_case.get("steps", []):
                action = step.get("action")
                target = step.get("target")
                value = step.get("value", "")

                if action == "click":
                    driver.find_element(By.CSS_SELECTOR, target).click()
                elif action == "input":
                    driver.find_element(By.CSS_SELECTOR, target).send_keys(value)
                time.sleep(0.5)

            screenshot_path = f"screenshots/{test_case.get('test_id')}.png"
            driver.save_screenshot(screenshot_path)
            result["evidence"].append(screenshot_path)

            expected = test_case.get("expected_result", "")
            if expected.lower() in driver.page_source.lower():
                result["verdict"] = "Pass"
            else:
                result["verdict"] = "Fail"

        except Exception as e:
            result["verdict"] = "Error"
            result["notes"] = str(e)
        finally:
            driver.quit()

        results.append(result)

    return results

def save_report_real(results, file_path="reports/report_real.json"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    import json
    with open(file_path, "w") as f:
        json.dump(results, f, indent=2)
