# mutable types are list, dict, set

# Lists are arrays they are ordered, changeable, and allow duplicate values
numbers = [1, 2, 3]
print(type(numbers))  # <class 'list'>
numbers.append(4)     # [1, 2, 3, 4]
numbers[0] = 10       # [10, 2, 3, 4]


# Dictionaries objects like, they are key-value pairs, they are unordered, changeable, and do not allow duplicate keys
person = {"name": "Efaz", "age": 42}
print(type(person))  # <class 'dict'>
print(person["name"])  # Efaz
person["age"] = 43   # {"name": "Efaz", "age": 43}
person["city"] = "New York"  # {"name": "Efaz", "age": 43, "city": "New York"}


# Sets are unordered collections of unique elements, they are changeable, and do not allow duplicate values
fruits = {"apple", "banana", "cherry"}
print(type(fruits))  # <class 'set'>
print(len(fruits))  # 3
fruits.add("orange")  # {"apple", "banana", "cherry", "orange"}
fruits.remove("banana")  # {"apple", "cherry", "orange"}
fruits.discard("grape")  # does nothing, no error
fruits.pop()  # removes and returns an arbitrary element
fruits.clear()  # removes all elements, now fruits is set()
empty_set = set()  # correct way to create an empty set


