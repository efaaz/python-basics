"""Problem: Delivery fees waiver
Prompt the user for an order amount (integer). If the order amount is greater
than 300, waive the delivery fees (set to 0). Otherwise, charge a delivery fee
of 30. Print the delivery fees amount.
"""

order_amount = int(input("Enter your amount: "))
if order_amount >300:
    print("Your delivery fee is 0")
else:
    print("Your delivery fee is 30")


# using Ternary operator
delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is : {delivery_fees}")
order_amount = int(input("Enter the order amount: "))
