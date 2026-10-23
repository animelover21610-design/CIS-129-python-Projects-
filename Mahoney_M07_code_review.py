"""
Program: Module 7 Code Review: Dictionaries
Purpose: Correct function errors and explain fixes using comments.
Author: Erin Mahoney
Date: July, 15 2026
"""


# Problem 1
def remove_low_scores(scores, threshold):
    """Remove students whose scores are below the given threshold."""
    # Make a list of the keys first. Changing a dictionary while directly
    # looping through it causes a RuntimeError.
    for student in list(scores.keys()):
        if scores[student] < threshold:
            del scores[student]


grades = {"Alice": 85, "Bob": 60, "Charlie": 72, "Diana": 90}
remove_low_scores(grades, 75)
print("Problem 1:", grades)


# Problem 2
def merge_dicts(dict1, dict2):
    """Return a new dictionary containing the entries from both dictionaries."""
    # update() changes a dictionary in place and returns None. Copy dict1,
    # update the copy, and then return the completed dictionary.
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = merge_dicts(d1, d2)
print("Problem 2:", merged)


# Problem 3
def build_student_records(names, grades):
    """Build and return a dictionary that matches each student to a grade."""
    records = {}
    # The original nested loops matched every name with every grade and kept
    # replacing the same "student" key. zip() pairs corresponding list items.
    for name, grade in zip(names, grades):
        records[name] = grade
    return records


students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
print("Problem 3:", build_student_records(students, scores))
