"""
script: Mahoney_M09_code_review.py
action: Corrects three file-handling examples using pathlib.
author: Erin Mahoney
date: 07/27/2026
"""

from pathlib import Path

# Problem 1
# Error 1: "from" was misspelled as "rom".
# Error 2: write_text() replaces existing file contents, so two separate
# calls would leave only the second line. Both lines are written at once.
example_path = Path("example.txt")
example_path.write_text("Line 1\nLine 2\n")

print("Problem 1:")
print(example_path.read_text())

# Problem 2
# Error: read_text() raises FileNotFoundError when data.txt does not exist.
# The try/except block creates the file the first time, then continues.
data_path = Path("data.txt")

try:
    contents = data_path.read_text()
except FileNotFoundError:
    data_path.write_text("No data has been saved yet.\n")
    contents = data_path.read_text()

print("Problem 2:")
print(contents)

# Problem 3
# Error: the original path was hard-coded for one Windows user.
# Path.home() finds the current user's home folder on any operating system,
# and the / operator safely joins the folder and file names.
home_data_path = Path.home() / "Documents" / "data.txt"

# Create the Documents folder and a sample file if they do not already exist
# so the program can run successfully on the first attempt.
home_data_path.parent.mkdir(parents=True, exist_ok=True)

if not home_data_path.exists():
    home_data_path.write_text("Data from the current user's home directory.\n")

print("Problem 3:")
print(home_data_path.read_text())
