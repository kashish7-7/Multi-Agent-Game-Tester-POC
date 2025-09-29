# Multi-Agent Web Game Tester POC
This project implements a proof-of-concept (POC) multi-agent automated testing system for web-based number/math puzzle games. It leverages LangChain-style agent orchestration, LLM-powered test case generation, and browser automation to generate, select, execute, and validate game test cases dynamically.

The system targets web puzzle games like [SumLink](https://play.ezygamers.com/) but is designed to be adaptable to any similar web-based puzzle/math game URL.

## Key Features
- Generates 20 unique test cases using an LLM (Ollama).
- Ranks and selects the top 10 test cases for execution.
- Executes test case steps through Selenium WebDriver browser automation.
- Captures screenshots as testing artifacts.
- Validates test results by searching for expected outcomes on the page.
- Analyzes results to check reproducibility and issues.
- Planned support for Retrieval-Augmented Generation (RAG) or agentic learning for adaptive test case generation (work in progress).
- Modular multi-agent architecture for generation, ranking, execution, and analysis.
- (Future) FastAPI backend and minimal frontend UI to trigger tests and view reports.
