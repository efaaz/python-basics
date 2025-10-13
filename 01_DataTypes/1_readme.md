# Python data types — mutable vs immutable

- Data type: the kind of value an object holds (numbers, text, collections, etc.).
- Common built-ins: `int`, `float`, `complex`, `bool`, `str`, `bytes`, `list`, `tuple`, `dict`, `set`, `frozenset`, `bytearray`.

## Immutable types
Definition: the object's state cannot be changed after creation. Operations that look like "modifying" produce new objects.
Examples: `int`, `float`, `complex`, `bool`, `str`, `tuple`, `bytes`, `frozenset`.

## Mutable types
Definition: the object's state can be changed in place without creating a new object.
Examples: `list`, `dict`, `set`, `bytearray`.

## Quick Python examples

```python
# immutable example (integers)
a = 1
b = a
print(id(a), id(b))   # same id
a += 1                # new integer object assigned to a
print(id(a), id(b))   # a's id changed, b's id unchanged

# mutable example (lists)
l = [1, 2]
m = l
print(id(l), id(m))   # same id
l.append(3)           # modifies list in place
print(id(l), id(m))   # ids still the same, both see the change

# tuple is immutable but can contain mutable elements
t = (1, [2, 3])
t[1].append(4)        # allowed: the list inside the tuple is mutable
print(t)              # (1, [2, 3, 4])
```

## Gotchas and recommendations
- Tuples are immutable, but elements inside may be mutable — be careful when using tuples to represent fixed data.
- Mutable default arguments in function definitions are a common pitfall:
  ```python
  def f(x, cache=[]):   # avoid: cache persists across calls
      cache.append(x)
      return cache
  ```
  Use `None` and initialize inside the function instead.
- Use `copy.copy()` for shallow copies and `copy.deepcopy()` when nested mutable objects must be duplicated.
- Immutable objects are hashable (usually) and safe to use as dict keys or set elements; mutable objects are not hashable by default.