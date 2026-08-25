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

## 2026-07-16

Explored V0 — here are my notes.

Connecting this to what I learned last week about related concepts.


<!-- snippet correction -->

## UDP — User Datagram Protocol

- **Connectionless** — no handshake
- **Unreliable** — no delivery guarantee
- **Fast** — minimal overhead

### Use cases
- Video streaming
- Online gaming
- DNS queries
- VoIP

### TCP vs UDP
| Feature      | TCP          | UDP          |
|-------------|-------------|-------------|
| Connection   | Yes          | No           |
| Reliability  | Guaranteed   | Best effort  |
| Speed        | Slower       | Faster       |
| Ordering     | Yes          | No           |

## OSI Model — 7 Layers

| Layer | Name         | Protocol Examples    |
|-------|-------------|---------------------|
| 7     | Application  | HTTP, FTP, SMTP     |
| 6     | Presentation | SSL/TLS, JPEG       |
| 5     | Session      | NetBIOS, RPC        |
| 4     | Transport    | TCP, UDP            |
| 3     | Network      | IP, ICMP            |
| 2     | Data Link    | Ethernet, WiFi      |
| 1     | Physical     | Cables, Signals     |

**Mnemonic:** Please Do Not Throw Sausage Pizza Away (bottom-up)


<!-- updated examples -->

## DNS Resolution

DNS translates domain names to IP addresses.

### Resolution flow
1. Browser cache → OS cache → Router cache
2. Recursive resolver (ISP)
3. Root nameserver → TLD nameserver → Authoritative nameserver

### Common record types
| Type  | Purpose              | Example            |
|-------|----------------------|--------------------|
| A     | IPv4 address         | 93.184.216.34      |
| AAAA  | IPv6 address         | 2606:2800:220:1::  |
| CNAME | Alias                | www → example.com  |
| MX    | Mail server          | mail.example.com   |
| TXT   | Verification/SPF     | v=spf1 ...         |

```bash
nslookup example.com
dig example.com A
```

## UDP — User Datagram Protocol

- **Connectionless** — no handshake
- **Unreliable** — no delivery guarantee
- **Fast** — minimal overhead

### Use cases
- Video streaming
- Online gaming
- DNS queries
- VoIP

### TCP vs UDP
| Feature      | TCP          | UDP          |
|-------------|-------------|-------------|
| Connection   | Yes          | No           |
| Reliability  | Guaranteed   | Best effort  |
| Speed        | Slower       | Faster       |
| Ordering     | Yes          | No           |

## JWT Authentication

A JSON Web Token has three parts: `header.payload.signature`

### Flow
1. User logs in with credentials
2. Server validates and returns a signed JWT
3. Client stores JWT (usually in memory or httpOnly cookie)
4. Client sends JWT in `Authorization: Bearer <token>` header
5. Server verifies signature on each request

### Security tips
- Keep tokens short-lived (15-30 min)
- Use refresh tokens for re-auth
- Never store JWTs in localStorage (XSS risk)
- Always validate `exp` and `iss` claims
