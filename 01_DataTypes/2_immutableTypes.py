# immutable types are int, float, bool, str, tuple, frozenset

age = 42
print(type(age))  # <class 'int'>
print(id(age))    # e.g. 140703303522512

age = age + 1
print(type(age))  # <class 'int'>
print(id(age))    # e.g. 140703303522544 (different from before
# This is valid, because it creates a new integer object and reassigns age to it

age = 42
print(type(age))  # <class 'int'>

pi = 3.14
print(type(pi))  # <class 'float'>

Name = "Efaz" 
print(type(Name))  # <class 'str'>

is_adult = True
is_adult = False
print(type(is_adult))  # <class 'bool'>

fruits = ("apple", "banana", "cherry")  # tuple is immutable list or array
print(type(fruits))  # <class 'tuple'>
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>
print(len(empty_tuple))  # 0

frozen_set = frozenset(["apple", "banana", "cherry"])   # frozenset is an immutable version of set
print(type(frozen_set))  # <class 'frozenset'>
print(len(frozen_set))  # 3

# Attempting to modify immutable types will raise errors
# frozen_set.add("orange")  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen_set.remove("banana")  # AttributeError: 'frozenset' object has no attribute 'remove'
# frozen_set.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
# frozen_set.pop()  # AttributeError: 'frozenset' object has no attribute 'pop'






