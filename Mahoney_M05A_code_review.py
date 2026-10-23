"""
Script: Module 5 Part A Code Review - Repetition
Action: Corrects loop errors in three repetition problems.
Author: Erin Mahoney
Date: 06/29/2026
"""

# -----------------------------
# Problem 1
# This should print a 1-5 multiplication table.
# Error fixed: range(1, 5) only goes from 1 to 4.
# Changed it to range(1, 6) so it includes 5.
# Added end="\t" so the table prints in rows instead of one number per line.
# -----------------------------

print("Problem 1: 1-5 Multiplication Table")

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()  # Moves to the next line after each row


# -----------------------------
# Problem 2
# This should stop when the user enters "quit".
# Error fixed: The break statement was outside the if statement,
# so the loop stopped after only one input.
# Moved the break inside the if statement so it only exits when the user types quit.
# -----------------------------

print("\nProblem 2: Quit Program")

user_input = ""

while user_input != "quit":
    user_input = input("Enter something or 'quit' to exit: ")

    if user_input == "quit":
        print("Goodbye!")
        break
    else:
        print("You entered:", user_input)


# -----------------------------
# Problem 3
# This program lets the user guess a secret number between 1 and 10.
# The user should have 5 attempts.
# Errors fixed:
# 1. The loop used "or", which could make the loop continue too long.
#    Changed it to "and" so the loop stops when the user guesses correctly
#    or when attempts reaches 5.
# 2. input() returns a string, so guess needed to be converted to an integer.
# 3. Added break after a correct guess so the program stops immediately.
# 4. Added a final message only if the user runs out of attempts.
# -----------------------------

print("\nProblem 3: Secret Number Guessing Game")

import random

secret_number = random.randint(1, 10)
guess = 0
attempts = 0

while guess != secret_number and attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again.")

if guess != secret_number and attempts == 5:
    print("Sorry, you've used all your attempts.")
    print("The correct number was", secret_number)
