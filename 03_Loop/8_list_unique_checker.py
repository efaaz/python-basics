
"""
List Uniqueness Checker
Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
"""

numbers = [1, 2, 3, 4, 5, 3, 6, 7]
seen = set()
for num in numbers:
	if num in seen:
		print(f"Duplicate found: {num}")
		break
	seen.add(num)
else:
	print("All elements are unique.")