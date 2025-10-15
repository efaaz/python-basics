"""Problem: Snack suggestion
Prompt the user to enter their preferred snack.
Accept only 'cookies' or 'samosa' (case-insensitive). If the user chooses one of
these, print a confirmation message showing the chosen snack. Otherwise,
print a message that only cookies or samosa are served with tea.
"""

snack = input("please enter the preferred snack: ").lower()
if snack == "cookies" or snack == "samosa":
    print(f"Thank you for your order! your {snack} is prepareing...")
else:
    print("Only cookies and somasa's are avilable")