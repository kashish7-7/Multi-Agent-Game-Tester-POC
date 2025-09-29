
from agents.executor_agent import cleanup_files, load_or_generate_test_cases, rank_test_cases, execute_tests, save_report
from agents.analyzer_agent import analyze_results

def run_pipeline():
    cleanup_files()
    all_tests = load_or_generate_test_cases(num_cases=20)
    top_tests = rank_test_cases(all_tests)
    results = execute_tests(top_tests)
    save_report(results)
    analyzed = analyze_results(results)
    save_report(analyzed, file_path="reports/analyzed_report.json")
    print("Pipeline complete! Check 'reports/analyzed_report.json' for results.")

if __name__ == "__main__":
    run_pipeline()
from agents.executor_agent_real import execute_tests_real, save_report_real
from agents.planner_agent import generate_test_cases
from agents.ranker_agent import rank_test_cases
from agents.analyzer_agent import analyze_results

def run_pipeline_real(game_url="https://play.ezygamers.com/", num_cases=20, repeat=2):
    """
    Run multi-agent pipeline:
    - Generates test cases
    - Ranks top 10
    - Executes repeatedly for reproducibility
    - Cross-agent validation
    """
    test_cases = generate_test_cases(num_cases=num_cases)
    top_tests = rank_test_cases(test_cases)
    all_results = []

    for i in range(repeat):
        print(f"Pipeline run {i+1}/{repeat}")
        results = execute_tests_real(top_tests, game_url)
        analyzed = analyze_results(results)
        all_results.extend(analyzed)

    test_verdict_map = {}
    for r in all_results:
        tid = r["test_id"]
        if tid not in test_verdict_map:
            test_verdict_map[tid] = [r["verdict"]]
        else:
            test_verdict_map[tid].append(r["verdict"])

    for r in all_results:
        tid = r["test_id"]
        verdicts = test_verdict_map[tid]
        r["reproducible"] = len(set(verdicts)) == 1

    save_report_real(all_results, file_path="reports/analyzed_report_real.json")
    print(f"Pipeline complete! Check 'reports/analyzed_report_real.json'")
from agents.report_generator import generate_html_report

generate_html_report()
