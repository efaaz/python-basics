"""
Problem: Grade Calculator
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
"""

marks = 60
if(90 <= marks <= 100):
    print("Your grade is A")
elif(80 <= marks <90):
    print("Your grade is B")
elif(70 <= marks <80):
    print("Your grade is C")
elif(60 <= marks <70):
    print("Your grade is D")
else:
     print("Your grade is F")