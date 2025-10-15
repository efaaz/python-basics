"""
Probmen: Counting postive numbers form the list
Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
"""
count = 0
for num in [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]:
    if num > 0:
        count+=1
print(count)