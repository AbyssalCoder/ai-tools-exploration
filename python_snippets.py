## String Manipulation Basics

```python
s = 'hello world'

print(s.upper())         # HELLO WORLD
print(s.title())         # Hello World
print(s.split())         # ['hello', 'world']
print(s.replace('o', '0'))  # hell0 w0rld
print(s.count('l'))      # 3
print(s.find('world'))   # 6
```

String methods return new strings — strings are immutable in Python.

## List Comprehensions

```python
# Squares of even numbers
squares = [x**2 for x in range(20) if x % 2 == 0]
print(squares)

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Dict comprehension
char_pos = {ch: i for i, ch in enumerate('abcde')}
print(char_pos)
```

## Exception Handling

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None
    except TypeError as e:
        print(f'Type error: {e}')
        return None
    finally:
        print('Division attempted.')

print(safe_divide(10, 3))
print(safe_divide(10, 0))
```

`finally` always runs — useful for cleanup.
