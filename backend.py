
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.orchestrator_agent import run_pipeline_real
import uvicorn

app = FastAPI(title="Multi-Agent Game Tester API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/run_tests")
def run_tests(game_url: str = "https://play.ezygamers.com/"):
    """
    Trigger the multi-agent pipeline on a game URL.
    """
    run_pipeline_real(game_url)
    return {"status": "Pipeline executed. Check reports/analyzed_report_real.json"}

@app.get("/get_reports")
def get_reports():
    """
    Return all test results as JSON.
    """
    import json, os
    report_file = "reports/analyzed_report_real.json"
    if os.path.exists(report_file):
        with open(report_file) as f:
            data = json.load(f)
        return {"results": data}
    return {"results": [], "message": "No reports found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
