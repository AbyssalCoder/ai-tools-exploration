## Jules — Google's Async Coding Agent

Jules works asynchronously on GitHub issues and PRs.

### Key features
- Assigns itself to GitHub issues
- Creates branches and PRs automatically
- Runs in the background (no IDE needed)
- Good for bug fixes and small tasks

### Workflow
1. Label an issue for Jules
2. Jules analyzes the codebase
3. Creates a PR with the fix
4. You review and merge

## Fibonacci — Recursive with Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Without memoization, the recursive version is O(2^n). With `lru_cache` it becomes O(n).

## VLAN Basics

A Virtual LAN segments a physical network into logical groups.

### Why VLANs?
- Reduce broadcast domains
- Improve security (isolate departments)
- Simplify network management

### Types
- **Data VLAN** — regular user traffic
- **Voice VLAN** — VoIP traffic priority
- **Management VLAN** — switch management
- **Native VLAN** — untagged trunk traffic

VLAN tagging uses IEEE 802.1Q standard.


<!-- snippet correction -->

## OpenCode — Terminal AI Coding Tool

Open-source terminal-based coding assistant.

### Setup
```bash
go install github.com/opencode-ai/opencode@latest
opencode
```

### Features
- Runs in terminal (TUI interface)
- Supports multiple LLM providers
- File editing with diff preview
- Session history

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


<!-- snippet correction -->

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


<!-- fixed typo -->

## Goose — Block's AI Developer Agent

### Features
- Extensible via toolkits
- Runs terminal commands
- Manages files and projects
- Can browse the web

### Setup
```bash
pip install goose-ai
goose session start
```

Modular design — add toolkits for GitHub, Jira, etc.

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


<!-- updated examples -->
