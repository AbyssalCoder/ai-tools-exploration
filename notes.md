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
