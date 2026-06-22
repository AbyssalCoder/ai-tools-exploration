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
