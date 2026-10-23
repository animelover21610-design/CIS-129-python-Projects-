# Module 2 Part A Code Review: Strings

# Problem 1
# Print a user's name in all caps
first_name = "John"
last_name = "Doe"
# Fixed: added parentheses to capitalize()
# Methods need parentheses to run.
full_name = first_name + " " + last_name.capitalize()
# Fixed: added parentheses to upper()
# Fixed: used an f-string to make the print statement cleaner.
print(f"Hello, {full_name.upper()}!")

# Problem 2
# Code to extract quick and fox, convert quick to all uppercase,
# capitalize fox, then print. Output = QUICK Fox
quote = "The quick brown fox jumps over the lazy dog"
# Fixed: string slicing.
# "quick" starts at index 4 and ends before index 9.
word1 = quote[4:9]
# Fixed: "fox" starts at index 16 and ends before index 19.
word2 = quote[16:19]
# Fixed: added parentheses to upper() and capitalize()
# Fixed: added a space between the two words.
formatted_quote = f"{word1.upper()} {word2.capitalize()}"
print(formatted_quote)
