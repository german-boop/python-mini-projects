import subprocess

projects = [
    "projects/project01/main.py",
    "projects/project02/main.py",
    "projects/project03/main.py",
    "projects/project04/main.py",
    "projects/project05/main.py"
]

for p in projects:
    result = subprocess.run(["python", p], capture_output=True)
    assert result.returncode == 0, f"{p} failed"
