import os
import shutil
import subprocess
from pathlib import Path

print("🔄 Uninstalling pyrtk-cli...")
subprocess.run(["pipx", "uninstall", "pyrtk-cli"], check=False)

print("🧹 Cleaning build artifacts...")
for folder in ["dist", "build"]:
    shutil.rmtree(folder, ignore_errors=True)

for item in Path(".").glob("*.egg-info"):
    shutil.rmtree(item, ignore_errors=True)

for item in Path(".").glob("*.whl"):
    item.unlink()

for item in Path(".").glob("*.tar.gz"):
    item.unlink()

print("🛠️  Building package...")
subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)

print("🚀 Installing with pipx...")
whl = next(Path("dist").glob("*.whl"))
subprocess.run(["pipx", "install", str(whl)], check=True)

print("✅ Done! Run 'pyrtk --help' to test it.")