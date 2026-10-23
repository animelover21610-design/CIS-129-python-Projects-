'''
    script: Mahoney_M03_code_review.py
    action: reviews and corrects tuple code examples for Module 3 Part A
    author: Erin Mahoney
    date:   06/17/2026
'''


# Problem 1
# Calculate the total score from a tuple of scores

# Fixed error: changed variable name from score to scores because this stores multiple scores.
# Fixed error: changed "92" from a string to an integer so it can be added to the total.
scores = (90, 85, 88, 92)

# Calculate the total score
total_score = 0

# Fixed error: used the correct tuple name, scores, in the for loop.
for score in scores:
    total_score += score

# Fixed error: added a comma between the string and total_score in the print statement.
print("Problem 1")
print("The total score is:", total_score)



# Problem 2
# Swap values using a tuple

a = 5
b = 10

# Fixed error: the original code assigned a and b back to themselves.
# To swap the values, a should receive b's value and b should receive a's value.
a, b = (b, a)

print("\nProblem 2")
print("After swapping: a =", a, "b =", b)


# Problem 3
# Access and display elements in a tuple

fruits = ("apple", "banana", "cherry")

# Fixed error: the first item is index 0, not index 1.
print("\nProblem 3")
print("First fruit:", fruits[0])

# This line was already correct because -1 accesses the last item.
print("Last fruit:", fruits[-1])

# Fixed error: the second item is index 1, not index 2.
# Fixed error: added a comma between the string and tuple value.
print("Second fruit:", fruits[1])
