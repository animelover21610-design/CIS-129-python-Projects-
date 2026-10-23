"""
Script: Module 4 Part A Code Review - IF Statements
Action: Corrects errors in two decision-making problems
Author: Erin Mahoney
Date: 06/24/2026
"""

# Problem 1

# Apply all eligible benefits to the customer's order.
# A customer can qualify for more than one benefit at the same time.

cart_total = 120
is_member = True
is_holiday = True

# Error fixed:
# The original code used elif, which only allows one benefit to print.
# Since the customer can qualify for more than one benefit,
# each condition needs its own if statement.

if is_member:
    print("Member benefit: free shipping.")

if is_holiday:
    print("Holiday benefit: free gift wrap.")

if cart_total > 100:
    print("Large order benefit: priority handling.")

print("Thank you for shopping with us!")

print()  # Blank line between problems

# Problem 2

# Calculate employee bonus.
# Employees must have worked 3 or more years.
# Ratings of 4 or above get $1000.
# Ratings of 3 or above get $500.
# Ratings less than 3 get no bonus.

years_worked = 5
performance_rating = 4  # Rating from 1 poor to 5 excellent
bonus = 0

# Errors fixed:
# 1. Changed years_worked > 3 to years_worked >= 3 because employees qualify if they worked 3 or more years.
# 2. Changed the second if to elif so a rating of 4 does not get overwritten from $1000 to $500.
# 3. Fixed the indentation under else.
# 4. Changed the final elif to else because anyone with less than
# 3 years does not qualify.

if years_worked >= 3:
    if performance_rating >= 4:
        bonus = 1000
    elif performance_rating >= 3:
        bonus = 500
else:
    print("No bonus for poor performance")
    print("Employees with less than 3 years do not qualify for bonuses")
    
print(f"Your bonus is ${bonus}")
