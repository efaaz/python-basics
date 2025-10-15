"""
Question: Print a numbered tea menu by enumerating a list of tea names. Start numbering from 1.
Output example:
1 : Espresso 
2 : Capuchino
3 : Latte
"""
menu = ["Espresso", "Capuchino", "Latte", "Frappe"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item}")