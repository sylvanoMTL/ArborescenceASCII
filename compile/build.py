import subprocess
import sys

def build():
    cmd = [
        "nuitka",
        "--standalone",
        "--include-data-dir=utils=utils",
        "ArborescenceASCII.py"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    build()