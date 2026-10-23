# Problem 1

length = 10  # Fixed: changed from string "10" to number 10 so it can be used in math
width = 5.0  # Width of the rectangle

area = length * width  # Fixed: now both values are numbers, so multiplication works

# Fixed: used an f-string so the number can be printed with text
print(f"The area of the rectangle is {area}")


# Problem 2

# Calculate the average of three exam scores
exam1 = 85
exam2 = 90
exam3 = 88  # Fixed: changed exam_3 to exam3 and changed "88" from a string to a number

# Fixed: added parentheses so all three scores are added before dividing by 3
average = (exam1 + exam2 + exam3) / 3

# Fixed: used an f-string to print text and a number together
print(f"The average exam score is: {average}")


# Problem 3

# Calculate the total cost of a road trip
distance = 300  # Distance of the trip in miles
mpg = 25  # Fuel efficiency in miles per gallon
fuel_price = 3.5  # Fixed: changed from string "3.5" to float 3.5 for math

# Total fuel cost
total_cost = distance / mpg * fuel_price  # Fixed: all values are now numbers

# Fixed: used an f-string to print the dollar amount with text
print(f"The total cost of the trip is: ${total_cost}")
