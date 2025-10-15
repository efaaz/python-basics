"""
Question: Iterate the list of customer names
Create a list of customer names with ready orders, print a message for each customer
indicating their order is ready.
Output: One line per customer, e.g. "Order ready for Efaz".
"""

orders = ["Efaz", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")