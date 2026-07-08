## Essential Linux Commands

```bash
# File operations
ls -la                  # List all with details
cp -r src/ dest/        # Copy directory
mv old.txt new.txt      # Rename/move
rm -rf dir/             # Remove directory
find . -name '*.py'     # Find files

# Text processing
cat file.txt            # Display file
grep -r 'pattern' .     # Search recursively
wc -l file.txt          # Count lines
head -20 file.txt       # First 20 lines
tail -f log.txt         # Follow log file

# System
ps aux                  # List processes
top                     # Process monitor
df -h                   # Disk usage
chmod 755 script.sh     # Set permissions
```


<!-- snippet correction -->

## GitHub Actions — CI/CD

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python -m pytest
```

Workflows live in `.github/workflows/` and trigger on events.

## 2026-07-01

Revisited Docker Networking and took better notes.

Going to revisit this topic next week for deeper understanding.

## Git Basics

```bash
git init                        # Initialize repo
git add .                       # Stage all changes
git commit -m 'Initial commit'  # Commit
git status                      # Check status
git log --oneline               # Compact log
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```

### Three areas
Working Directory → Staging Area → Repository


