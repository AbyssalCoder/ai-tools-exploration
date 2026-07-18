## Star Pattern — Right Triangle

```python
n = 5
for i in range(1, n + 1):
    print('* ' * i)
```

Output:
```
* 
* * 
* * * 
* * * * 
* * * * * 
```


<!-- indent fix -->


<!-- snippet correction -->

## Palindrome — Two-pointer Approach

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Runs in O(n/2) comparisons with O(1) extra space.


<!-- indent fix -->

## 2026-07-18

Went through Pattern Printing concepts and examples.

Connecting this to what I learned last week about related concepts.
