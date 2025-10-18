## File handling & Exception handling

File handling is how a program reads from and writes to files on disk. In Python, you typically use `open()` to get a file object and then call methods like `.read()` or `.write()`.

Key points:
- Use a context manager (`with open(...) as f:`) to ensure files are closed automatically.
- Choose the correct mode: `'r'` for read, `'w'` for write (overwrite), `'a'` for append, `'b'` for binary.
- Always handle possible I/O errors (e.g., FileNotFoundError, PermissionError) when working with files from external sources.

Example:

```python
with open('order.txt', 'w', encoding='utf-8') as f:
	f.write('ginger tea - 4 cups')
```

### What is exception handling?

Exception handling is how your program responds to unexpected events or errors (exceptions) that occur at runtime — for example, accessing a missing dictionary key, dividing by zero, or trying to open a file that doesn't exist.

Key concepts:
- `try` block: run code that might raise an exception.
- `except` block(s): catch and handle specific exception types.
- `finally` block: optional cleanup code that runs whether an exception occurred or not.
- `raise`: explicitly raise an exception to indicate an error.
- Custom exceptions: subclass `Exception` to create domain-specific errors.

Example:

```python
try:
	value = mydict['key']
except KeyError:
	print('Key not found')
```

### Cheatsheet — essential patterns

1) Basic try / except

```python
try:
	risky_operation()
except SomeError:
	handle_error()
```

2) Catch and inspect the exception

```python
try:
	do_work()
except Exception as e:
	print('error:', e)
```

3) Multiple except branches

```python
try:
	maybe_fails()
except KeyError:
	handle_missing_key()
except TypeError:
	handle_type_error()
```

4) Catch multiple types in one except

```python
try:
	maybe_fails()
except (TypeError, ValueError) as e:
	print('error:', e)
```

5) finally for cleanup

```python
try:
	f = open('file.txt')
	do_work(f)
finally:
	f.close()
```

6) Prefer `with` for file handling

```python
with open('file.txt', 'w', encoding='utf-8') as f:
	f.write('hello')
```

7) Define and raise custom exceptions

```python
class MyError(Exception):
	pass

if bad_condition:
	raise MyError('explain why')
```

8) Validate inputs early and raise clear exceptions

```python
def bill(flavor, cups):
	if flavor not in menu:
		raise ValueError('flavor not available')
	if not isinstance(cups, int):
		raise TypeError('cups must be int')
```

9) Avoid catching Exception too broadly in production — it can hide bugs

```python
try:
	do_work()
except Exception as e:
	# ok for debugging, but be specific in production
	print('error:', e)
```

10) Debug tip: run scripts without broad excepts to see full tracebacks when developing

### File summaries

The folder contains small example scripts demonstrating the patterns above (index errors, try/except, multiple except branches, raising errors, custom exceptions, finally, and file handling with `with`). See the individual files for short, focused examples.
