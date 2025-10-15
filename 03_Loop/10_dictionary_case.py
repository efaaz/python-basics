"""
Question: Given a list of users where each user has an id, total bill amount, and a coupon code,
use a discounts mapping to determine the discount (percentage or fixed) for each coupon and
print how much discount each user will get for their next visit.

Input shape:
 - users: list of dicts, each with keys 'id', 'total', 'coupon'
 - discounts: dict mapping coupon code -> (percent_discount, fixed_amount)

Output: Printed lines describing the discount each user receives based on their coupon.
"""

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    # use single quotes inside the f-string to avoid quote collision
    print(f"{user['id']} paid {user['total']} and got discount for next visit of dollar {discount}")