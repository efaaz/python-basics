"""
Problem: Sum of even numbers
Calculate the sum of even numbers up to a given number n using while loop.
"""
r = 11
value = 0
num = 1
while num < r:
    if num % 2 == 0:
        value += num
    num += 1

print(f"sum of even numers from 1 to {r} is {value}")