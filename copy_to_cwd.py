#!/usr/bin/env python3

"""
Copy .flake8 and pyproject.toml to the current working directory.
"""

import shutil
from pathlib import Path

script_dir = Path(__file__).parent

shutil.copy(script_dir / ".flake8", Path.cwd() / ".flake8")
if (Path.cwd() / "pyproject.toml").exists():
    should_continue = input("pyproject.toml already exists. Overwrite? [y/N] ")
    if should_continue.lower() != "y":
        print("pyproject.toml not overwritten.")
        exit(0)

shutil.copy(script_dir / "pyproject.toml", Path.cwd() / "pyproject.toml")
