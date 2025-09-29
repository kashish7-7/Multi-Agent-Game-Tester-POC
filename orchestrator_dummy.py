from agents.executor_agent import execute_tests, save_report
from agents.planner_agent import generate_test_cases
from agents.ranker_agent import rank_test_cases
from agents.analyzer_agent import analyze_results
from agents.report_generator import generate_html_report

def run_pipeline_dummy(num_cases=10):
    """
    Fast dummy pipeline that does NOT open browser.
    Useful for verifying system and generating reports instantly.
    """
    # Generate test cases
    test_cases = generate_test_cases(num_cases=num_cases)
    
    # Rank top tests
    top_tests = rank_test_cases(test_cases)
    
    # Execute tests using dummy executor (all pass)
    results = execute_tests(top_tests)
    
    # Save JSON report
    save_report(results, file_path="reports/analyzed_report_real.json")
    
    # Analyze results (reproducibility etc.)
    analyzed = analyze_results(results)
    save_report(analyzed, file_path="reports/analyzed_report_real.json")
    
    # Generate human-readable HTML report
    generate_html_report()
    
    print("✅ Dummy pipeline complete! Reports generated instantly.")


if __name__ == "__main__":
    run_pipeline_dummy(num_cases=10)
