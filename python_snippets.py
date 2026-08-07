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

## Armstrong Number

An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits.

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

# Examples: 153 = 1^3 + 5^3 + 3^3
print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
```

## Reverse a Number

```python
def reverse_number(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n

print(reverse_number(12345))  # 54321
```

This uses modulus and integer division — no string conversion needed.

## Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))  # 2
print(linear_search(nums, 5))  # -1
```

Time complexity: O(n). Works on unsorted arrays.

## Nested Loop — Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
    print('---')
```

Useful for practising nested iteration and formatting.


<!-- updated examples -->

## File Handling in Python

```python
# Writing
with open('output.txt', 'w') as f:
    f.write('Hello, file!\n')
    f.write('Second line\n')

# Reading
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

Always use `with` statements — they handle closing automatically.

## Selection Sort

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([29, 10, 14, 37, 13]))
```

Always O(n²) — not adaptive, but minimal swaps (n-1 at most).

## Armstrong Number

An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits.

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

# Examples: 153 = 1^3 + 5^3 + 3^3
print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
```

## Inheritance Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'

for a in [Dog('Rex'), Cat('Whiskers')]:
    print(a.speak())
```
