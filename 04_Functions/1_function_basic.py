def print_order(name, chai_type):
    print(f"{name} orderded {chai_type} chai!")


print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")



# Combining related steps into functions to avoid duplication
def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")


register_user()



# Function with trace
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")