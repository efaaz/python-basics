"""
Problem: Even Odd number checker
Problem: Determine if a number is even or odd. (if the number is divisble by 2 than it is even otherwise the given number is odd).
"""

num = int(input("Enter an integer number: "))
if num == 0:
    print("The number is 0")
else:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")