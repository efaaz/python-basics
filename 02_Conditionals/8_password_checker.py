"""
Problem: Password Strength Checker
Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
"""

password = "mn@1234"
print(f"pass lenght: {len(password)}")
if len(password) <= 6:
    print("Password is weak")
elif len(password) <= 10:
     print("Password is medium")
elif len(password) > 10:
     print("Password is strong")
     
