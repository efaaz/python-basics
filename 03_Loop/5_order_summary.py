"""
Question: Given two lists (names and corresponding bills), print a summary pairing each
customer with the amount they paid. Use zip to iterate in parallel.

Output example: "Efaz paid 50 dollars"
"""

names = ["Efaz", "Jhon", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")