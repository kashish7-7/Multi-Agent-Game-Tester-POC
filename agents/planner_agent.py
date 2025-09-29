import json
import ollama

TEST_FILE = "test_cases.json"

def generate_test_cases(game_type="SumLink: Number Match Puzzle Game", num_cases=20, save_to_file=True):
    prompt = f"""
    Generate {num_cases} unique test cases for a {game_type}.
    Each test case should include:
    1) test_id
    2) description (1 sentence)
    3) steps (list of actions to perform)
    4) expected_result (short description)
    Return only a valid JSON array of objects, no extra text.
    """

    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": prompt}]
    )

 
    try:
        raw_content = response.content  
    except AttributeError:
        raw_content = str(response)

    try:
        test_cases = json.loads(raw_content)
    except json.JSONDecodeError as e:
        print("JSON parse error:", e)
        print("Raw response:\n", raw_content)
        test_cases = []

  
    for idx, case in enumerate(test_cases, start=1):
        case.setdefault("test_id", f"TL{idx:03d}")

 
    if save_to_file and test_cases:
        with open(TEST_FILE, "w") as f:
            json.dump(test_cases, f, indent=2)
        print(f" {len(test_cases)} test cases saved to {TEST_FILE}")

    return test_cases


if __name__ == "__main__":
    generate_test_cases()
