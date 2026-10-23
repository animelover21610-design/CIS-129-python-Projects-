'''
    script: Mahoney_M03B_code_review.py
    action: reviews and corrects list code examples for Module 3 Part B
    author: Erin Mahoney
    date:   06/22/2026
'''

# Problem 1
# Change the lowest score in the list to 80.5

scores = [85, 90, 78, 92]

# Fixed error: the lowest score, 78, is at index 2, not index 3.
scores[2] = 80.5

# Fixed error: added a comma between the string and the list in the print statement.
print("Problem 1")
print("Updated scores are:", scores)

# Problem 2
# Manage a list of fruits

fruits = ["apple", "banana", "cherry"]

# Add a new fruit to the end of the list.
fruits.append("orange")

# Fixed error: remove is a method and needs parentheses.
# Removed "banana" from the list.
fruits.remove("banana")

# Fixed error: a list cannot be added directly to a string with +.
# Used a comma to print the string and list together.
print("\nProblem 2")
print("Final fruit list is:", fruits)

# Problem 3
# Iterate through and print a list of names

names = ["Alice", "Bob", "Charlie"]

# Fixed error: the print statement must be indented inside the for loop.
print("\nProblem 3")
for name in names:
    print("Name:", name)
