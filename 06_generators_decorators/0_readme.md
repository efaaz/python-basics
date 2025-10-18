
## Generators & Decorators

This short guide explains two powerful and commonly used Python features: generators and decorators. Both help write cleaner, more expressive, and more efficient code when used appropriately.

-----

## Generators

Generators are a way to produce a sequence of values lazily (on demand) instead of building the entire sequence in memory. Generators help with memory efficiency and can model infinite streams.

Why use generators?
- Save memory for large sequences because values are produced one at a time.
- Compose data pipelines cleanly using iterators.
- Model infinite sequences (e.g., event streams) without storing everything.

Basic syntax — generator function:

```python
def count_up_to(n):
	i = 0
	while i < n:
		yield i
		i += 1

for x in count_up_to(5):
	print(x)
```

Generator expression (short form):

```python
gen = (x*x for x in range(10))
print(next(gen))  # 0
```

Key points
- A generator function uses `yield` instead of `return` to produce values.
- Each `yield` pauses the function’s state; calling `next()` resumes it.
- Generators raise `StopIteration` when exhausted.

Common patterns
- Streaming processing: read large files line-by-line, transform, and write results without large memory spikes.
- Pipelines: chain generators with comprehensions, map/filter, or itertools.

Example — read and process a large file lazily:

```python
def read_lines(path):
	with open(path, 'r', encoding='utf-8') as f:
		for line in f:
			yield line.strip()

def words(lines):
	for line in lines:
		for w in line.split():
			yield w.lower()

for w in words(read_lines('bigfile.txt')):
	process(w)
```

Pitfalls and tips
- Generators are single-use: once exhausted you must recreate them.
- Use generator expressions when you only need to iterate once or compute aggregates (sum, any, all).
- For debugging, convert to a list (careful with very large generators).

-----

## Decorators

Decorators are a way to modify or enhance functions (or classes) without changing their code. A decorator is a callable that takes a function and returns a new function (or a wrapper) with added behavior.

Why decorators?
- Keep cross-cutting concerns (logging, timing, caching, permissions) separate from business logic.
- Reuse behavior by applying the decorator to many functions.

Basic syntax — simple decorator:

```python
def my_decorator(func):
	def wrapper(*args, **kwargs):
		print('Before')
		result = func(*args, **kwargs)
		print('After')
		return result
	return wrapper

@my_decorator
def greet(name):
	print(f'Hello {name}')

greet('Alice')
```

Decorators with arguments

```python
def repeat(n):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for _ in range(n):
				func(*args, **kwargs)
		return wrapper
	return decorator

@repeat(3)
def say_hi():
	print('hi')

say_hi()
```

Preserve metadata with functools.wraps

When writing decorators, use `functools.wraps` so the wrapper keeps the original function's name, docstring, and signature:

```python
from functools import wraps

def my_decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print('Before')
		return func(*args, **kwargs)
	return wrapper
```

Common applications
- Logging and tracing
- Authorization / authentication checks
- Caching / memoization (e.g., lru_cache)
- Retrying failed operations

Example — simple logging decorator:

```python
from functools import wraps
import time

def timeit(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		print(f"{func.__name__} took {end-start:.6f}s")
		return result
	return wrapper

@timeit
def work(n):
	total = 0
	for i in range(n):
		total += i*i
	return total

work(100000)
```

Pitfalls and tips
- Debugging wrapped functions can be harder without `wraps`.
- Order matters when stacking multiple decorators (top-most is applied first at definition time).
- Keep decorators simple; if a decorator becomes complex, consider making it a class with __call__.

-----

## When to use generators vs decorators

- Use generators when you need lazy evaluation or to handle large/streaming data.
- Use decorators when you want to add/modify behavior of functions cleanly and repeatedly (logging, auth, caching).

## Quick reference / contract

- Generators: input = any control logic; output = iterator producing values; errors = StopIteration when done.
- Decorators: input = function/class; output = new function/class (often a wrapper); errors = decorator can change signature/behavior — use carefully.

## Final notes

Both generators and decorators are widely used in real-world Python: web frameworks, data processing, and libraries rely heavily on them. Practice by converting small tasks into generator pipelines and extracting cross-cutting concerns into decorators.
