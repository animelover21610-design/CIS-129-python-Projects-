"""
Script: Module 4 Part B Lab - Shopping Cart Application
Action: Creates an interactive shopping cart using tuples, lists, and if statements
Author: Erin Mahoney
Date: 06/25/2026
"""

# List of tuples for the available shopping items.
# Each tuple contains the item name and item price.
available_items = [
    ("Apples", 1.50),
    ("Bananas", 0.75),
    ("Milk", 3.20),
    ("Bread", 2.50)
]

# Empty list that will store the items added to the cart.
# Each cart entry will be a tuple with item name, item price, and quantity.
shopping_cart = []

subtotal = 0
tax_rate = 0.05

print("Welcome to the Shopping Cart Program!")

# Ask the user how many items they want to add.
number_of_items = int(input("How many items would you like to add to your cart? (max 5) "))

# If the user enters more than 5, only allow 5 items.
if number_of_items > 5:
    print("The maximum number of items is 5. Your cart will be set to 5 items.")
    number_of_items = 5

# If the user enters less than 1, set the cart to 1 item.
if number_of_items < 1:
    print("You must add at least 1 item. Your cart will be set to 1 item.")
    number_of_items = 1

# Display the menu of available items.
print()
print("Available items:")
print(f"1. {available_items[0][0]} - ${available_items[0][1]:.2f} each")
print(f"2. {available_items[1][0]} - ${available_items[1][1]:.2f} each")
print(f"3. {available_items[2][0]} - ${available_items[2][1]:.2f} each")
print(f"4. {available_items[3][0]} - ${available_items[3][1]:.2f} each")
print()

# Item 1
if number_of_items >= 1:
    item_number = int(input("Enter the number of the item you want to add: "))
    quantity = int(input("Enter the quantity: "))

    if item_number == 1:
        shopping_cart.append((available_items[0][0], available_items[0][1], quantity))
    elif item_number == 2:
        shopping_cart.append((available_items[1][0], available_items[1][1], quantity))
    elif item_number == 3:
        shopping_cart.append((available_items[2][0], available_items[2][1], quantity))
    elif item_number == 4:
        shopping_cart.append((available_items[3][0], available_items[3][1], quantity))
    else:
        print("Invalid item number. This item was not added.")

# Item 2
if number_of_items >= 2:
    item_number = int(input("Enter the number of the next item you want to add: "))
    quantity = int(input("Enter the quantity: "))

    if item_number == 1:
        shopping_cart.append((available_items[0][0], available_items[0][1], quantity))
    elif item_number == 2:
        shopping_cart.append((available_items[1][0], available_items[1][1], quantity))
    elif item_number == 3:
        shopping_cart.append((available_items[2][0], available_items[2][1], quantity))
    elif item_number == 4:
        shopping_cart.append((available_items[3][0], available_items[3][1], quantity))
    else:
        print("Invalid item number. This item was not added.")

# Item 3
if number_of_items >= 3:
    item_number = int(input("Enter the number of the next item you want to add: "))
    quantity = int(input("Enter the quantity: "))

    if item_number == 1:
        shopping_cart.append((available_items[0][0], available_items[0][1], quantity))
    elif item_number == 2:
        shopping_cart.append((available_items[1][0], available_items[1][1], quantity))
    elif item_number == 3:
        shopping_cart.append((available_items[2][0], available_items[2][1], quantity))
    elif item_number == 4:
        shopping_cart.append((available_items[3][0], available_items[3][1], quantity))
    else:
        print("Invalid item number. This item was not added.")

# Item 4
if number_of_items >= 4:
    item_number = int(input("Enter the number of the next item you want to add: "))
    quantity = int(input("Enter the quantity: "))

    if item_number == 1:
        shopping_cart.append((available_items[0][0], available_items[0][1], quantity))
    elif item_number == 2:
        shopping_cart.append((available_items[1][0], available_items[1][1], quantity))
    elif item_number == 3:
        shopping_cart.append((available_items[2][0], available_items[2][1], quantity))
    elif item_number == 4:
        shopping_cart.append((available_items[3][0], available_items[3][1], quantity))
    else:
        print("Invalid item number. This item was not added.")

# Item 5
if number_of_items >= 5:
    item_number = int(input("Enter the number of the next item you want to add: "))
    quantity = int(input("Enter the quantity: "))

    if item_number == 1:
        shopping_cart.append((available_items[0][0], available_items[0][1], quantity))
    elif item_number == 2:
        shopping_cart.append((available_items[1][0], available_items[1][1], quantity))
    elif item_number == 3:
        shopping_cart.append((available_items[2][0], available_items[2][1], quantity))
    elif item_number == 4:
        shopping_cart.append((available_items[3][0], available_items[3][1], quantity))
    else:
        print("Invalid item number. This item was not added.")

# Print the receipt and calculate totals.
print()
print("Receipt:")

if len(shopping_cart) >= 1:
    line_total = shopping_cart[0][1] * shopping_cart[0][2]
    subtotal = subtotal + line_total
    print(f"{shopping_cart[0][0]}: ${shopping_cart[0][1]:.2f} x {shopping_cart[0][2]} = ${line_total:.2f}")

if len(shopping_cart) >= 2:
    line_total = shopping_cart[1][1] * shopping_cart[1][2]
    subtotal = subtotal + line_total
    print(f"{shopping_cart[1][0]}: ${shopping_cart[1][1]:.2f} x {shopping_cart[1][2]} = ${line_total:.2f}")

if len(shopping_cart) >= 3:
    line_total = shopping_cart[2][1] * shopping_cart[2][2]
    subtotal = subtotal + line_total
    print(f"{shopping_cart[2][0]}: ${shopping_cart[2][1]:.2f} x {shopping_cart[2][2]} = ${line_total:.2f}")

if len(shopping_cart) >= 4:
    line_total = shopping_cart[3][1] * shopping_cart[3][2]
    subtotal = subtotal + line_total
    print(f"{shopping_cart[3][0]}: ${shopping_cart[3][1]:.2f} x {shopping_cart[3][2]} = ${line_total:.2f}")

if len(shopping_cart) >= 5:
    line_total = shopping_cart[4][1] * shopping_cart[4][2]
    subtotal = subtotal + line_total
    print(f"{shopping_cart[4][0]}: ${shopping_cart[4][1]:.2f} x {shopping_cart[4][2]} = ${line_total:.2f}")

tax = subtotal * tax_rate
total = subtotal + tax

print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

