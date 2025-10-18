
## Python Comprehensions

Comprehensions provide a compact way to create collections (lists, sets, dictionaries) and generator expressions in Python. They let you build and transform iterables using a single readable expression instead of writing longer loops.

Why learn comprehensions?
- More concise code — fewer lines than equivalent for-loops.
- Often faster than an explicit loop because they are optimized in C.
- Declarative style — show what you want to create, not how to loop over it.

### Types of comprehensions

- List comprehensions — create lists.
- Set comprehensions — create sets (unique values).
- Dict comprehensions — create dictionaries (key: value pairs).
- Generator expressions — lazy iterators that produce values on demand.

### Basic syntax

- List: [expression for item in iterable]
- With condition: [expression for item in iterable if condition]

Example: square numbers 0–9

```python
squares = [x*x for x in range(10)]
print(squares)  # [0, 1, 4, 9, ..., 81]
```

### Conditional expressions

Only include items that meet a condition:

```python
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

### Nested loops

Comprehensions can include multiple for-clauses (like a nested loop):

```python
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0),(0,1),(0,2),(1,0),...]
```

### Set and dict comprehensions

Set comprehension (duplicates removed):

```python
unique_lengths = {len(s) for s in ['apple', 'pear', 'banana', 'kiwi']}
print(unique_lengths)  # e.g. {4, 5, 6}
```

Dict comprehension (build mapping):

```python
square_map = {x: x*x for x in range(6)}
print(square_map)  # {0:0, 1:1, 2:4, ...}
```

### Generator expressions (lazy)

Generator expressions use parentheses and produce values on demand. They are memory-efficient for large sequences.

```python
gen = (x*x for x in range(10))
for v in gen:
	print(v)
```

Use `sum(x*x for x in range(1000000))` when you only need an aggregate result; generators avoid building the whole list in memory.

### When to use comprehensions

- Use them for straightforward transformations and filters.
- Prefer comprehensions when they improve readability and reduce boilerplate.

When not to use them
- Avoid very large or deeply nested comprehensions that become hard to read.
- If the logic requires complex side effects or many statements, prefer a regular for-loop with clear variable names and comments.

### Common pitfalls

- Overly complex expressions hurt readability.
- Dict comprehensions require unique keys; duplicates will be overwritten silently.
- Set and dict comprehensions do not preserve order (in CPython 3.7+ dict preserves insertion order, but sets do not).

### Quick reference / contract

- Input: any iterable (range, list, dict keys, generator, file, etc.)
- Output: list, set, dict, or generator depending on comprehension type
- Error modes: TypeError if expression uses unsupported operations; Key collisions for dicts silently keep last value

### Examples (summary)

```python
# squares list
squares = [x**2 for x in range(10)]

# squares of even numbers
squares_even = [x**2 for x in range(10) if x % 2 == 0]

# unique word lengths from a list
lengths = {len(w) for w in ['apple', 'pear', 'apple']}

# map of number -> square
sq_map = {x: x**2 for x in range(5)}

# generator for large sequences
big_sum = sum(x**2 for x in range(1_000_000))
```

### Final notes

Comprehensions are a powerful, expressive feature of Python. Start by converting short, clear loops into comprehensions to get comfortable. Keep readability in mind — the goal is concise AND clear code.                                           
