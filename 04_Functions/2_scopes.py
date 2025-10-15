def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi" # Global
chai_counter()
print("Global :", chai_order)


# nonlocal example

chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()


# global example

chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()


front_desk()
print("Final global chai: ", chai_type)