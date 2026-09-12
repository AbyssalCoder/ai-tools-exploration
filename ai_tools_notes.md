## V0 — Vercel's AI UI Generator

### What it does
- Generates React + Tailwind components from prompts
- Uses shadcn/ui component library
- Exports clean, usable code

### Best for
- UI prototyping
- Component design
- Landing pages
- Dashboard layouts

Output is clean and production-ready compared to most generators.

## OpenHands (formerly OpenDevin)

Open-source AI software developer agent.

### Setup
```bash
docker pull ghcr.io/all-hands-ai/openhands
docker run -p 3000:3000 ghcr.io/all-hands-ai/openhands
```

### Capabilities
- Browses the web
- Writes and runs code
- Uses terminal commands
- Creates full projects from description

It's like giving an AI its own computer to work on tasks.

## OpenCommit — AI Commit Messages

Generates meaningful commit messages from your staged changes.

### Setup
```bash
npm install -g opencommit
oco config set OCO_API_KEY=<key>
```

### Usage
```bash
git add .
oco  # generates commit message from diff
```

Follows conventional commit format. Saves time on writing descriptive messages.

## V0 — Vercel's AI UI Generator

### What it does
- Generates React + Tailwind components from prompts
- Uses shadcn/ui component library
- Exports clean, usable code

### Best for
- UI prototyping
- Component design
- Landing pages
- Dashboard layouts

Output is clean and production-ready compared to most generators.

## Windsurf — Codeium's IDE

### Features
- Cascade: agentic workflow that reads, plans, and edits
- Flows: tracks your intent across multiple steps
- Fast autocomplete
- Free tier available

### Compared to Cursor
- Cascade is more autonomous than Cursor's Composer
- Windsurf feels more guided, Cursor more manual
- Both are VS Code forks
