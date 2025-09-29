import json
import os

REPORT_JSON = "reports/analyzed_report_real.json"
REPORT_HTML = "reports/final_report.html"

def generate_html_report(json_file=REPORT_JSON, html_file=REPORT_HTML):
    if not os.path.exists(json_file):
        print(" Report JSON not found.")
        return

    with open(json_file) as f:
        results = json.load(f)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Game Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { text-align: center; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #f4f4f4; }
            .pass { background-color: #c8e6c9; }
            .fail { background-color: #ffcdd2; }
            .error { background-color: #ffe0b2; }
            img { max-width: 200px; border: 1px solid #ddd; padding: 2px; }
        </style>
    </head>
    <body>
        <h1>Game Test Report</h1>
        <table>
            <tr>
                <th>Test ID</th>
                <th>Description</th>
                <th>Verdict</th>
                <th>Reproducible</th>
                <th>Notes</th>
                <th>Evidence</th>
            </tr>
    """

    for r in results:
        verdict_class = r["verdict"].lower()
        notes = r.get("notes", "")
        evidence_imgs = ""
        for img_path in r.get("evidence", []):
            if os.path.exists(img_path):
                evidence_imgs += f'<img src="../{img_path}" alt="{r["test_id"]}">'
        html_content += f"""
        <tr class="{verdict_class}">
            <td>{r['test_id']}</td>
            <td>{r['description']}</td>
            <td>{r['verdict']}</td>
            <td>{r.get('reproducible', True)}</td>
            <td>{notes}</td>
            <td>{evidence_imgs}</td>
        </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
