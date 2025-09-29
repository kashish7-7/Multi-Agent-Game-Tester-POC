from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from agents.orchestrator_agent import run_full_test_suite
import os

app = FastAPI(title="Multi-Agent Game Tester POC")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Multi-Agent Game Tester</h1>
    <p><a href="/run_tests">Run Full Test Suite</a></p>
    <p><a href="/view_report">View Final Report</a></p>
    """

@app.get("/run_tests")
def run_tests():
    report_path = run_full_test_suite()
    return {"message": "Tests executed successfully!", "report_path": report_path}

@app.get("/view_report")
def view_report():
    report_file = "reports/final_report.json"
    if os.path.exists(report_file):
        return FileResponse(report_file, media_type="application/json")
    return {"error": "Report not found. Run tests first."}
