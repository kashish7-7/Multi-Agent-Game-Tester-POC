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
    print("🎯 Pipeline complete! Check 'reports/analyzed_report.json' for results.")

if __name__ == "__main__":
    run_pipeline()
