# Module 2 Part B Lab: Applying Variables and Data Types
# This program calculates the total cost of a shopping trip.

# Tax rate stored as a float
tax_rate = 0.05

# Get information for item 1
item1_name = input("Enter the name of item 1: ")
item1_price = float(input(f"Enter the price of {item1_name}: "))
item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))

# Get information for item 2
item2_name = input("Enter the name of item 2: ")
item2_price = float(input(f"Enter the price of {item2_name}: "))
item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))

# Get information for item 3
item3_name = input("Enter the name of item 3: ")
item3_price = float(input(f"Enter the price of {item3_name}: "))
item3_quantity = int(input(f"Enter the quantity of {item3_name}: "))

# Calculate the line total for each item
item1_total = item1_price * item1_quantity
item2_total = item2_price * item2_quantity
item3_total = item3_price * item3_quantity

# Calculate subtotal, tax, and total cost
subtotal = item1_total + item2_total + item3_total
tax = subtotal * tax_rate
total_cost = subtotal + tax

# Display the receipt
print()
print("Receipt:")
print(f"{item1_name}: ${item1_price:.2f} x {item1_quantity} = ${item1_total:.2f}")
print(f"{item2_name}: ${item2_price:.2f} x {item2_quantity} = ${item2_total:.2f}")
print(f"{item3_name}: ${item3_price:.2f} x {item3_quantity} = ${item3_total:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
