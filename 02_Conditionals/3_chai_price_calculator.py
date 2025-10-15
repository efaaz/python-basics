"""Problem: Coffee price calculator
Ask the user to choose a cup size: small, medium, or large (case-insensitive).
Print the corresponding price: small -> 10, medium -> 20, large -> 35.
If an unknown size is entered, print an appropriate error message.
"""

cupSize = input("Enter your desired cup size (small/medium/large): ").lower()
if cupSize == "small":
    print(f"Your orderd {cupSize} coffee and the price is $10")
elif cupSize == "medium":
    print(f"Your orderd {cupSize} coffee and the price is $20")
elif cupSize == "large":
    print(f"Your orderd {cupSize} coffee and the price is $35")
else:
    print("Unknown cup size given!")
