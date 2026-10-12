"""Build the manuscript with pdflatex and BibTeX, and refuse to finish on any unresolved warning.

Usage: python paper/build.py   (run from the repository root or from paper/)
"""
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE / "build"
OUT.mkdir(exist_ok=True)


def run(cmd):
    result = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, errors="replace", timeout=600)
    if result.returncode:
        print("\n".join(result.stdout.splitlines()[-45:]))
        raise SystemExit(f"Command failed: {' '.join(cmd)}")


latex = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", "main.tex"]
run(latex)
run(["bibtex", "build/main"])
for _ in range(5):
    run(latex)
    log = (OUT / "main.log").read_text(errors="replace")
    if "Rerun to get" not in log:
        break
warnings = [line for line in log.splitlines() if any(s in line for s in (
    "undefined", "Overfull", "multiply defined", "Rerun to get", "Citation"
))]
if warnings:
    print("\n".join(warnings))
    raise SystemExit("Unresolved manuscript build warnings; inspect paper/build/main.log.")
shutil.copy2(OUT / "main.pdf", HERE / "main.pdf")
print("Built paper/main.pdf; no undefined references or citations, duplicate labels, or overfull boxes.")
