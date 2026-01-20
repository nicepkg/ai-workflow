---
source: https://code.claude.com/docs/en/vs-code
title: Use Claude Code in VS Code
---

![VS Code editor with the Claude Code extension panel open on the right side, showing a conversation with Claude](https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=300652d5678c63905e6b0ea9e50835f8)
The VS Code extension provides a native graphical interface for Claude Code, integrated directly into your IDE. This is the recommended way to use Claude Code in VS Code.
With the extension, you can review and edit Claude’s plans before accepting them, auto-accept edits as they’re made, @-mention files with specific line ranges from your selection, access conversation history, and open multiple conversations in separate tabs or windows.

## [​](#prerequisites) Prerequisites

- VS Code 1.98.0 or higher
- An Anthropic account (you’ll sign in when you first open the extension). If you’re using a third-party provider like Amazon Bedrock or Google Vertex AI, see [Use third-party providers](#use-third-party-providers) instead.

You don’t need to install the Claude Code CLI first. However, some features like MCP server configuration require the CLI. See [VS Code extension vs. Claude Code CLI](#vs-code-extension-vs-claude-code-cli) for details.

## [​](#install-the-extension) Install the extension

Click the link for your IDE to install directly:

- [Install for VS Code](vscode:extension/anthropic.claude-code)
- [Install for Cursor](cursor:extension/anthropic.claude-code)

Or in VS Code, press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux) to open the Extensions view, search for “Claude Code”, and click **Install**.

You may need to restart VS Code or run “Developer: Reload Window” from the Command Palette after installation.

## [​](#get-started) Get started

Once installed, you can start using Claude Code through the VS Code interface:

1

Open the Claude Code panel

Throughout VS Code, the Spark icon indicates Claude Code: ![Spark icon](https://mintcdn.com/claude-code/mfM-EyoZGnQv8JTc/images/vs-code-spark-icon.svg?fit=max&auto=format&n=mfM-EyoZGnQv8JTc&q=85&s=a734d84e785140016672f08e0abb236c)The quickest way to open Claude is to click the Spark icon in the **Editor Toolbar** (top-right corner of the editor). The icon only appears when you have a file open.![VS Code editor showing the Spark icon in the Editor Toolbar](https://mintcdn.com/claude-code/mfM-EyoZGnQv8JTc/images/vs-code-editor-icon.png?fit=max&auto=format&n=mfM-EyoZGnQv8JTc&q=85&s=eb4540325d94664c51776dbbfec4cf02)Other ways to open Claude Code:

- **Command Palette**: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux), type “Claude Code”, and select an option like “Open in New Tab”
- **Status Bar**: Click **✱ Claude Code** in the bottom-right corner of the window. This works even when no file is open.

You can drag the Claude panel to reposition it anywhere in VS Code. See [Customize your workflow](#customize-your-workflow) for details.

2

Send a prompt

Ask Claude to help with your code or files, whether that’s explaining how something works, debugging an issue, or making changes.

Select text in the editor and press `Alt+K` to insert an @-mention with the file path and line numbers directly into your prompt.

Here’s an example of asking about a particular line in a file:![VS Code editor with lines 2-3 selected in a Python file, and the Claude Code panel showing a question about those lines with an @-mention reference](https://mintcdn.com/claude-code/FVYz38sRY-VuoGHA/images/vs-code-send-prompt.png?fit=max&auto=format&n=FVYz38sRY-VuoGHA&q=85&s=ede3ed8d8d5f940e01c5de636d009cfd)

3

Review changes

When Claude wants to edit a file, it shows you a diff and asks for permission. You can accept, reject, or tell Claude what to do instead.![VS Code showing a diff of Claude's proposed changes with a permission prompt asking whether to make the edit](https://mintcdn.com/claude-code/FVYz38sRY-VuoGHA/images/vs-code-edits.png?fit=max&auto=format&n=FVYz38sRY-VuoGHA&q=85&s=e005f9b41c541c5c7c59c082f7c4841c)

For more ideas on what you can do with Claude Code, see [Common workflows](/docs/en/common-workflows).

## [​](#customize-your-workflow) Customize your workflow

Once you’re up and running, you can reposition the Claude panel or switch to terminal mode.

### [​](#change-the-layout) Change the layout

You can drag the Claude panel to reposition it anywhere in VS Code. Grab the panel’s tab or title bar and drag it to:

- **Secondary sidebar** (default): The right side of the window
- **Primary sidebar**: The left sidebar with icons for Explorer, Search, etc.
- **Editor area**: Opens Claude as a tab alongside your files

The Spark icon only appears in the Activity Bar (left sidebar icons) when the Claude panel is docked to the left. Since Claude defaults to the right side, use the Editor Toolbar icon to open Claude.

### [​](#switch-to-terminal-mode) Switch to terminal mode

By default, the extension opens a graphical chat panel. If you prefer the CLI-style interface, open the [Use Terminal setting](vscode://settings/claudeCode.useTerminal) and check the box.
You can also open VS Code settings (`Cmd+,` on Mac or `Ctrl+,` on Windows/Linux), go to Extensions → Claude Code, and check **Use Terminal**.

## [​](#vs-code-commands-and-shortcuts) VS Code commands and shortcuts

Open the Command Palette (`Cmd+Shift+P` on Mac or `Ctrl+Shift+P` on Windows/Linux) and type “Claude Code” to see all available VS Code commands for the Claude Code extension:

These are VS Code commands for controlling the extension. For Claude Code slash commands (like `/help` or `/compact`), not all CLI commands are available in the extension yet. See [VS Code extension vs. Claude Code CLI](#vs-code-extension-vs-claude-code-cli) for details.

| Command | Shortcut | Description |
| --- | --- | --- |
| Focus Input | `Cmd+Esc` (Mac) / `Ctrl+Esc` (Windows/Linux) | Toggle focus between editor and Claude |
| Open in Side Bar | — | Open Claude in the left sidebar |
| Open in Terminal | — | Open Claude in terminal mode |
| Open in New Tab | `Cmd+Shift+Esc` (Mac) / `Ctrl+Shift+Esc` (Windows/Linux) | Open a new conversation as an editor tab |
| Open in New Window | — | Open a new conversation in a separate window |
| New Conversation | `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux) | Start a new conversation (when Claude is focused) |
| Insert @-Mention Reference | `Alt+K` | Insert a reference to the current file (includes line numbers if text is selected) |
| Show Logs | — | View extension debug logs |
| Logout | — | Sign out of your Anthropic account |

Use **Open in New Tab** or **Open in New Window** to run multiple conversations simultaneously. Each tab or window maintains its own conversation history and context.

## [​](#configure-settings) Configure settings

The extension has two types of settings:

- **Extension settings**: Open with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux), then go to Extensions → Claude Code.

  | Setting | Description |
  | --- | --- |
  | Selected Model | Default model for new conversations. Change per-session with `/model`. |
  | Use Terminal | Launch Claude in terminal mode instead of graphical panel |
  | Initial Permission Mode | Controls approval prompts for file edits and commands. Defaults to `default` (ask before each action). |
  | Preferred Location | Default location: sidebar (right) or panel (new tab) |
  | Autosave | Auto-save files before Claude reads or writes them |
  | Use Ctrl+Enter to Send | Use Ctrl/Cmd+Enter instead of Enter to send prompts |
  | Enable New Conversation Shortcut | Enable Cmd/Ctrl+N to start a new conversation |
  | Respect Git Ignore | Exclude .gitignore patterns from file searches |
  | Environment Variables | Set environment variables for the Claude process. **Not recommended**—use [Claude Code settings](/docs/en/settings) instead so configuration is shared between extension and CLI. |
  | Disable Login Prompt | Skip authentication prompts (for third-party provider setups) |
  | Allow Dangerously Skip Permissions | Bypass all permission prompts. **Use with extreme caution**—recommended only for isolated sandboxes with no internet access. |
  | Claude Process Wrapper | Executable path used to launch the Claude process |
- **Claude Code settings** (`~/.claude/settings.json`): These settings are shared between the VS Code extension and the CLI. Use this file for allowed commands and directories, environment variables, hooks, and MCP servers. See the [settings documentation](/docs/en/settings) for details.

## [​](#use-third-party-providers) Use third-party providers

By default, Claude Code connects directly to Anthropic’s API. If your organization uses Amazon Bedrock, Google Vertex AI, or Microsoft Foundry to access Claude, configure the extension to use your provider instead:

1

Disable login prompt

Open the [Disable Login Prompt setting](vscode://settings/claudeCode.disableLoginPrompt) and check the box.You can also open VS Code settings (`Cmd+,` on Mac or `Ctrl+,` on Windows/Linux), search for “Claude Code login”, and check **Disable Login Prompt**.

2

Configure your provider

Follow the setup guide for your provider:

- [Claude Code on Amazon Bedrock](/docs/en/amazon-bedrock)
- [Claude Code on Google Vertex AI](/docs/en/google-vertex-ai)
- [Claude Code on Microsoft Foundry](/docs/en/microsoft-foundry)

These guides cover configuring your provider in `~/.claude/settings.json`, which ensures your settings are shared between the VS Code extension and the CLI.

## [​](#vs-code-extension-vs-claude-code-cli) VS Code extension vs. Claude Code CLI

The extension doesn’t yet have full feature parity with the CLI. If you need CLI-only features, you can run `claude` directly in VS Code’s integrated terminal.

| Feature | CLI | VS Code Extension |
| --- | --- | --- |
| Slash commands | [Full set](/docs/en/slash-commands) | Subset (type `/` to see available) |
| MCP server config | Yes | No (configure via CLI, use in extension) |
| Checkpoints | Yes | Coming soon |
| `!` bash shortcut | Yes | No |
| Tab completion | Yes | No |

### [​](#run-cli-in-vs-code) Run CLI in VS Code

To use the CLI while staying in VS Code, open the integrated terminal (`` Ctrl+` `` on Windows/Linux or `` Cmd+` `` on Mac) and run `claude`. The CLI automatically integrates with your IDE for features like diff viewing and diagnostic sharing.
If using an external terminal, run `/ide` inside Claude Code to connect it to VS Code.

### [​](#switch-between-extension-and-cli) Switch between extension and CLI

The extension and CLI share the same conversation history. To continue an extension conversation in the CLI, run `claude --resume` in the terminal. This opens an interactive picker where you can search for and select your conversation.

## [​](#security-considerations) Security considerations

With auto-edit permissions enabled, Claude Code can modify VS Code configuration files (like `settings.json` or `tasks.json`) that VS Code may execute automatically. This could potentially bypass Claude Code’s normal permission prompts.
To reduce risk when working with untrusted code:

- Enable [VS Code Restricted Mode](https://code.visualstudio.com/docs/editor/workspace-trust#_restricted-mode) for untrusted workspaces
- Use manual approval mode instead of auto-accept for edits
- Review changes carefully before accepting them

## [​](#fix-common-issues) Fix common issues

### [​](#extension-won’t-install) Extension won’t install

- Ensure you have a compatible version of VS Code (1.98.0 or later)
- Check that VS Code has permission to install extensions
- Try installing directly from the Marketplace website

### [​](#spark-icon-not-visible) Spark icon not visible

The Spark icon appears in the **Editor Toolbar** (top-right of editor) when you have a file open. If you don’t see it:

1. **Open a file**: The icon requires a file to be open—having just a folder open isn’t enough
2. **Check VS Code version**: Requires 1.98.0 or higher (Help → About)
3. **Restart VS Code**: Run “Developer: Reload Window” from the Command Palette
4. **Disable conflicting extensions**: Temporarily disable other AI extensions (Cline, Continue, etc.)
5. **Check workspace trust**: The extension doesn’t work in Restricted Mode

Alternatively, click ”✱ Claude Code” in the **Status Bar** (bottom-right corner)—this works even without a file open. You can also use the **Command Palette** (`Cmd+Shift+P` / `Ctrl+Shift+P`) and type “Claude Code”.

### [​](#claude-code-never-responds) Claude Code never responds

If Claude Code isn’t responding to your prompts:

1. **Check your internet connection**: Ensure you have a stable internet connection
2. **Start a new conversation**: Try starting a fresh conversation to see if the issue persists
3. **Try the CLI**: Run `claude` from the terminal to see if you get more detailed error messages
4. **File a bug report**: If the problem continues, [file an issue on GitHub](https://github.com/anthropics/claude-code/issues) with details about the error

### [​](#standalone-cli-not-connecting-to-ide) Standalone CLI not connecting to IDE

- Ensure you’re running Claude Code from VS Code’s integrated terminal (not an external terminal)
- Ensure the CLI for your IDE variant is installed:
  - VS Code: `code` command should be available
  - Cursor: `cursor` command should be available
  - Windsurf: `windsurf` command should be available
  - VSCodium: `codium` command should be available
- If the command isn’t available, install it from the Command Palette → “Shell Command: Install ‘code’ command in PATH”

## [​](#uninstall-the-extension) Uninstall the extension

To uninstall the Claude Code extension:

1. Open the Extensions view (`Cmd+Shift+X` on Mac or `Ctrl+Shift+X` on Windows/Linux)
2. Search for “Claude Code”
3. Click **Uninstall**

To also remove extension data and reset all settings:

```bash
rm -rf ~/.vscode/globalStorage/anthropic.claude-code
```

For additional help, see the [troubleshooting guide](/docs/en/troubleshooting).

## [​](#next-steps) Next steps

Now that you have Claude Code set up in VS Code:

- [Explore common workflows](/docs/en/common-workflows) to get the most out of Claude Code
- [Set up MCP servers](/docs/en/mcp) to extend Claude’s capabilities with external tools. Configure servers using the CLI, then use them in the extension.
- [Configure Claude Code settings](/docs/en/settings) to customize allowed commands, hooks, and more. These settings are shared between the extension and CLI.