
# Recursion function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))


# Lambda function
chai_types = ["light", "kadak", "ginger", "kadak"]


strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)