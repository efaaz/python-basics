"""
Problem: Multiplication Table
Print the multiplication table for a given number up to 15, but skip the fifth iteration and after 10th iteration break the loop
"""
mult = 5
for digit in range(0, 16):
    if(digit == 5):
        continue
    elif(digit == 11):
        break
    else:
        print(f"{mult} X {digit} = {mult*digit}")
