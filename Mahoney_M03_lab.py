'''
    script: Mahoney_M03_lab.py
    action: calculates a shopping trip receipt using tuples for item data
    author: Erin Mahoney
    date:   06/17/2026
'''

# display welcome message
print("Welcome to the Shopping Trip Calculator!")

# create tuples for each item
# each tuple stores the item name, price, and quantity
item1 = ("Apples", 1.50, 4)
item2 = ("Bananas", 0.75, 6)
item3 = ("Milk", 3.20, 2)

# calculate the subtotal for each item
item1_subtotal = item1[1] * item1[2]
item2_subtotal = item2[1] * item2[2]
item3_subtotal = item3[1] * item3[2]

# calculate the overall subtotal
subtotal = item1_subtotal + item2_subtotal + item3_subtotal

# calculate the tax and total cost
tax = subtotal * 0.05
total_cost = subtotal + tax

# display the receipt
print("\nReceipt:")
print(f"{item1[0]}: ${item1[1]:.2f} x {item1[2]} = ${item1_subtotal:.2f}")
print(f"{item2[0]}: ${item2[1]:.2f} x {item2[2]} = ${item2_subtotal:.2f}")
print(f"{item3[0]}: ${item3[1]:.2f} x {item3[2]} = ${item3_subtotal:.2f}")

# display subtotal, tax, and total cost
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
