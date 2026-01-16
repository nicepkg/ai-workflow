# Contributing to AI Workflow

First off, thanks for taking the time to contribute! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

- Check if the bug has already been reported in [Issues](https://github.com/nicepkg/ai-workflow/issues)
- If not, create a new issue using the bug report template
- Include as much detail as possible

### 💡 Suggesting New Skills or Workflows

- Open an issue with the "feature request" template
- Describe the use case and target users
- List the skills you think should be included

### 🔧 Submitting Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-skill`)
3. Make your changes
4. Test your skills with Claude Code or other supported tools
5. Commit your changes (`git commit -m 'Add amazing-skill'`)
6. Push to the branch (`git push origin feature/amazing-skill`)
7. Open a Pull Request

## Creating New Skills

### Skill Structure

```
skill-name/
├── SKILL.md          # Required: Skill definition
├── references/       # Optional: Reference documents
│   └── guide.md
└── assets/           # Optional: Templates, examples
    └── template.md
```

### SKILL.md Format

```markdown
---
name: skill-name
description: Brief description of what this skill does and when to use it
---

# Skill Name

## Overview

Detailed description of the skill.

## When to Use

- Trigger condition 1
- Trigger condition 2

## Workflow

Step-by-step instructions for the AI.

## Output Format

Expected output format.
```

### Best Practices

1. **Clear trigger conditions** - Make it easy for AI to know when to use the skill
2. **Specific instructions** - Be detailed about what the AI should do
3. **Examples** - Include example inputs and outputs
4. **References** - Add supporting documents for complex skills

## Creating New Workflows

### Workflow Structure

```
workflow-name/
├── .claude/skills/    # Claude Code skills
├── README.md          # English documentation
├── README_cn.md       # Chinese documentation
└── AGENTS.md          # Agent routing guide
```

### Checklist

- [ ] At least 10 skills included
- [ ] README.md with clear target users
- [ ] README_cn.md for Chinese users
- [ ] AGENTS.md for AI routing
- [ ] Symlinks for multi-AI tool support

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## Questions?

Feel free to open an issue with your question!
