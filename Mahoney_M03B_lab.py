'''
    script: Mahoney_M03B_lab.py
    action: calculates a shopping trip receipt using a list of item tuples
    author: Erin Mahoney
    date:   06/22/2026
'''

# display receipt title
print("Receipt:")

# create a shopping cart list
# each tuple stores the item name, price, and quantity
shopping_cart = [
    ("Apples", 1.50, 4),
    ("Bananas", 0.75, 6),
    ("Milk", 3.20, 2),
    ("Bread", 2.99, 1),
    ("Eggs", 4.49, 2),
    ("Cheese", 5.75, 1),
    ("Coffee", 8.99, 1)
]

# start overall subtotal at zero
subtotal = 0

# go through each item in the shopping cart
for item in shopping_cart:
    # get the name, price, and quantity from the tuple
    name = item[0]
    price = item[1]
    quantity = item[2]

    # calculate the subtotal for this item
    item_subtotal = price * quantity

    # add this item's subtotal to the overall subtotal
    subtotal += item_subtotal

    # display the item information
    print(f"{name}: ${price:.2f} x {quantity} = ${item_subtotal:.2f}")

# calculate tax and total cost
tax = subtotal * 0.05
total_cost = subtotal + tax

# display subtotal, tax, and total cost
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
