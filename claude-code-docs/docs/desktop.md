---
source: https://code.claude.com/docs/en/desktop
title: Claude Code on desktop
---

![Claude Code on desktop interface](https://mintcdn.com/claude-code/zEGbGSbinVtT3BLw/images/desktop-interface.png?fit=max&auto=format&n=zEGbGSbinVtT3BLw&q=85&s=c4e9dc9737b437d36ab253b75a1cc595)

## [​](#claude-code-on-desktop-preview) Claude Code on desktop (Preview)

The Claude desktop app provides a native interface for running multiple Claude Code sessions on your local machine and seamless integration with Claude Code on the web.

## [​](#installation) Installation

Download the Claude desktop app for your platform:

[## macOS

Universal build for Intel and Apple Silicon](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs)[## Windows

For x64 processors](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs)

For Windows ARM64, [download here](https://claude.ai/api/desktop/win32/arm64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs).

Local sessions are not available on Windows ARM64.

## [​](#features) Features

Claude Code on desktop provides:

- **Parallel local sessions with `git` worktrees**: Run multiple Claude Code sessions simultaneously in the same repository, each with its own isolated `git` worktree
- **Include files listed in your `.gitignore` in your worktrees**: Automatically copy files in your `.gitignore`, like `.env`, to new worktrees using `.worktreeinclude`
- **Launch Claude Code on the web**: Kick off secure cloud sessions directly from the desktop app

## [​](#using-git-worktrees) Using Git worktrees

Claude Code on desktop enables running multiple Claude Code sessions in the same repository using Git worktrees. Each session gets its own isolated worktree, allowing Claude to work on different tasks without conflicts. The default location for worktrees is `~/.claude-worktrees` but this can be configured in your settings on the Claude desktop app.

If you start a local session in a folder that does not have Git initialized, the desktop app will not create a new worktree.

### [​](#copying-files-ignored-with-gitignore) Copying files ignored with `.gitignore`

When Claude Code creates a worktree, files ignored via `.gitignore` aren’t automatically available. Including a `.worktreeinclude` file solves this by specifying which ignored files should be copied to new worktrees.
Create a `.worktreeinclude` file in your repository root:

```bash
.env
.env.local
.env.*
**/.claude/settings.local.json
```

The file uses `.gitignore`-style patterns. When a worktree is created, files matching these patterns that are also in your `.gitignore` will be copied from your main repository to the worktree.

Only files that are both matched by `.worktreeinclude` AND listed in `.gitignore` are copied. This prevents accidentally duplicating tracked files.

### [​](#launch-claude-code-on-the-web) Launch Claude Code on the web

From the desktop app, you can kick off Claude Code sessions that run on Anthropic’s secure cloud infrastructure.
To start a web session from desktop, select a remote environment when creating a new session.
For more details, see [Claude Code on the web](/docs/en/claude-code-on-the-web).

## [​](#bundled-claude-code-version) Bundled Claude Code version

Claude Code on desktop includes a bundled, stable version of Claude Code to ensure a consistent experience for all desktop users. The bundled version is required and downloaded on first launch even if a version of Claude Code exists on the computer. Desktop automatically manages version updates and cleans up old versions.

The bundled Claude Code version in Desktop may differ from the latest CLI version. Desktop prioritizes stability while the CLI may have newer features.

## [​](#environment-configuration) Environment configuration

For local environments, Claude Code on desktop automatically extracts your `$PATH` environment variable from your shell configuration. This allows local sessions to access development tools like `yarn`, `npm`, `node`, and other commands available in your terminal without additional setup.

### [​](#custom-environment-variables) Custom environment variables

Select “Local” environment, then to the right, select the settings button. This will open a dialog where you can update local environment variables. This is useful for setting project-specific variables or API keys that your development workflows require. Environment variable values are masked in the UI for security reasons.

Environment variables must be specified as key-value pairs, in [`.env` format](https://www.dotenv.org/). For example:

```bash
API_KEY=your_api_key
DEBUG=true

# Multiline values - wrap in quotes
CERT="-----BEGIN CERT-----
MIIE...
-----END CERT-----"
```

## [​](#enterprise-configuration) Enterprise configuration

Organizations can disable local Claude Code use in the desktop application with the `isClaudeCodeForDesktopEnabled` [enterprise policy option](https://support.claude.com/en/articles/12622667-enterprise-configuration#h_003283c7cb). Additionally, Claude Code on the web can be disabled in your [admin settings](https://claude.ai/admin-settings/claude-code).

## [​](#related-resources) Related resources

- [Claude Code on the web](/docs/en/claude-code-on-the-web)
- [Claude Desktop support articles](https://support.claude.com/en/collections/16163169-claude-desktop)
- [Enterprise Configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)
- [Common workflows](/docs/en/common-workflows)
- [Settings reference](/docs/en/settings)