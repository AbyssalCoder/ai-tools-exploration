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

## Roo Code — Fork of Cline

Enhanced fork with additional features.

### Differences from Cline
- Multiple modes (Code, Architect, Debug)
- Custom modes with specific instructions
- Better context management
- Community-driven development

### Setup
Install from VS Code marketplace → Search "Roo Code"

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
