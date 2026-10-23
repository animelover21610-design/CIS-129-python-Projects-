"""
Program: Module 6 Part A Code Review - Functions
Purpose: Correct function errors and explain fixes using comments.
Author: Erin Mahoney
Date: July 2026
"""

# Problem 1
# Return the sum of two provided numbers

def add_numbers(a, b):
    # Error fixed: The original function calculated the sum but did not return it.
    # I added a return statement so the result can be stored and printed.
    total = a + b
    return total

result = add_numbers(5, 3)
print("Problem 1 Result:", result)


# Problem 2
# Return the maximum number in a list of provided numbers

def find_max(numbers):
    # Error fixed: The original code started max_value at 0.
    # This caused incorrect results when all numbers in the list were negative.
    # I set max_value to the first number in the list instead.
    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

print("Problem 2 Result:", find_max([-10, -5, -1, -20]))


# Problem 3
# Return the value of the first even number in a provided list

def find_first_even(numbers):
    # Error fixed: The original code returned None inside the loop too early.
    # That made the function stop after checking only the first number.
    # I moved return None outside the loop so all numbers are checked first.
    for num in numbers:
        if num % 2 == 0:
            return num

    return None

print("Problem 3 Result:", find_first_even([1, 3, 5, 7, 10, 12]))
