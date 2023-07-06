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
    else:
        shutil.copy(script_dir / "pyproject.toml", Path.cwd() / "pyproject.toml")
else:
    shutil.copy(script_dir / "pyproject.toml", Path.cwd() / "pyproject.toml")
if (Path.cwd() / ".clang-format").exists():
    should_continue = input(".clang-format already exists. Overwrite? [y/N] ")
    if should_continue.lower() != "y":
        print(".clang-format not overwritten.")
    else:
        shutil.copy(script_dir / ".clang-format", Path.cwd() / ".clang-format")
else:
    shutil.copy(script_dir / ".clang-format", Path.cwd() / ".clang-format")
