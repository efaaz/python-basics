
## Object-Oriented Programming (OOP) in Python — concise guide

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects — data structures that contain both data (attributes) and behavior (methods). Python supports OOP and makes it easy to model real-world concepts.

Why learn OOP?
- Encapsulate related data and behavior together.
- Reuse code through inheritance and composition.
- Make programs easier to reason about by modeling real-world entities.

### Core concepts

- Class: a blueprint for creating objects.
- Object (instance): a concrete occurrence of a class.
- Attribute: data stored on an object (instance attributes) or on a class (class attributes).
- Method: a function defined inside a class that operates on instances.
- Encapsulation: grouping data and methods; control access via conventions and properties.
- Inheritance: derive new classes from existing ones to reuse and extend behavior.
- Polymorphism: different classes provide the same method interface; code can use them interchangeably.
- Composition: build classes by including instances of other classes (has-a relationship).

### Basic class and instance

```python
class Dog:
	species = 'Canis familiaris'  # class attribute

	def __init__(self, name, age):
		self.name = name          # instance attribute
		self.age = age

	def speak(self):
		return f"{self.name} says woof"

fido = Dog('Fido', 3)
print(fido.speak())  # Fido says woof
```

### self and __init__

- `self` refers to the instance. Use it to access instance attributes and other methods.
- `__init__` is the initializer (constructor) called when creating a new instance.

### Inheritance

```python
class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError

class Cat(Animal):
	def speak(self):
		return f"{self.name} says meow"

kitty = Cat('Kitty')
print(kitty.speak())
```

### Method types: instance, class, static

```python
class MyClass:
	count = 0

	def __init__(self):
		MyClass.count += 1

	@classmethod
	def get_count(cls):
		return cls.count

	@staticmethod
	def helper(x, y):
		return x + y

print(MyClass.get_count())
print(MyClass.helper(1, 2))
```

### Properties (controlled access)

```python
class Person:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		if not value:
			raise ValueError('name cannot be empty')
		self._name = value

p = Person('Alice')
print(p.name)
p.name = 'Bob'
```

### Composition vs Inheritance

- Use composition (has-a) to assemble behavior from separate classes when inheritance leads to awkward hierarchies.

```python
class Engine:
	def start(self):
		print('engine starts')

class Car:
	def __init__(self):
		self.engine = Engine()

	def start(self):
		self.engine.start()
```

### Special methods (dunder methods)

- `__repr__`, `__str__`, `__eq__`, `__lt__`, `__len__` let your objects integrate with Python features.

Example `__repr__` and `__eq__`:

```python
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Point({self.x}, {self.y})'

	def __eq__(self, other):
		return isinstance(other, Point) and self.x == other.x and self.y == other.y

print(Point(1,2))
```

### When to use OOP

- Use OOP when your program models real-world entities or when encapsulation and reuse provide clarity.
- For small scripts, simple functions may be clearer.

### Common pitfalls

- Overusing inheritance: prefer composition when appropriate.
- Mutable class attributes: be careful — shared across instances.
- Tight coupling between classes makes testing harder.

### Quick reference / contract

- Input: data and behavior grouped by concept
- Output: instances that maintain state and provide methods
- Error modes: TypeError/AttributeError when wrong attributes/methods are used; watch for mutable shared state

### Final notes

Start small: create simple classes that model concrete concepts. Add tests for behavior (methods) and prefer composition over deep inheritance when possible.
