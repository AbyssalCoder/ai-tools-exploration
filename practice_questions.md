## Factorial

```python
# Iterative
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n - 1)

print(factorial_iter(5))  # 120
```


<!-- updated examples -->


<!-- updated examples -->

## Fibonacci Sequence

### Iterative approach

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fibonacci(i), end=' ')
# 0 1 1 2 3 5 8 13 21 34
```

**Key takeaway:** The iterative version runs in O(n) time and O(1) space.
