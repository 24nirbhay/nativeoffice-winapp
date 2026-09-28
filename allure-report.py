import subprocess
from pathlib import Path


def allure_report():
    root = Path(__file__).resolve().parent
    results_dir = root / "allure-results"
    report_dir = root / "allure-report"

    if not results_dir.exists():
        print("No Allure results found; skipping report generation.")
        return

    print("Generating Allure report...")
    subprocess.run(
        [
            "allure",
            "generate",
            str(results_dir),
            "--clean",
            "-o",
            str(report_dir),
            "--single-file",
        ],
        check=False,
    )
    print("Allure report generated successfully.")


if __name__ == "__main__":
    allure_report()