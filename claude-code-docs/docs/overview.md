---
source: https://code.claude.com/docs/en/overview
title: Claude Code overview
---

## [​](#get-started-in-30-seconds) Get started in 30 seconds

Prerequisites:

- A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**
To install Claude Code, use one of the following methods:

- Native Install (Recommended)
- Homebrew
- WinGet

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```bash
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

```bash
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

```bash
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

**Start using Claude Code:**

```bash
cd your-project
claude
```

You’ll be prompted to log in on first use. That’s it! [Continue with Quickstart (5 minutes) →](/docs/en/quickstart)

See [advanced setup](/docs/en/setup) for installation options, manual updates, or uninstallation instructions. Visit [troubleshooting](/docs/en/troubleshooting) if you hit issues.

## [​](#what-claude-code-does-for-you) What Claude Code does for you

- **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
- **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
- **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/docs/en/mcp) can pull from external data sources like Google Drive, Figma, and Slack.
- **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## [​](#why-developers-love-claude-code) Why developers love Claude Code

- **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
- **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/docs/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
- **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
- **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](/docs/en/security), [privacy](/docs/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

## [​](#next-steps) Next steps

[## Quickstart

See Claude Code in action with practical examples](/docs/en/quickstart)[## Common workflows

Step-by-step guides for common workflows](/docs/en/common-workflows)[## Troubleshooting

Solutions for common issues with Claude Code](/docs/en/troubleshooting)[## IDE setup

Add Claude Code to your IDE](/docs/en/vs-code)

## [​](#additional-resources) Additional resources

[## About Claude Code

Learn more about Claude Code on claude.com](https://claude.com/product/claude-code)[## Build with the Agent SDK

Create custom AI agents with the Claude Agent SDK](https://docs.claude.com/en/docs/agent-sdk/overview)[## Host on AWS or GCP

Configure Claude Code with Amazon Bedrock or Google Vertex AI](/docs/en/third-party-integrations)[## Settings

Customize Claude Code for your workflow](/docs/en/settings)[## Commands

Learn about CLI commands and controls](/docs/en/cli-reference)[## Reference implementation

Clone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)[## Security

Discover Claude Code’s safeguards and best practices for safe usage](/docs/en/security)[## Privacy and data usage

Understand how Claude Code handles your data](/docs/en/data-usage)