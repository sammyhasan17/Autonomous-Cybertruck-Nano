from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]   # go from /src to project root
EXE = ROOT / "bin" / "adder"

res = subprocess.run([str(EXE), "2", "3"], capture_output=True, text=True)

print("returncode:", res.returncode)
print("stdout:", res.stdout.strip())
print("stderr:", res.stderr.strip())
print("back in python")
