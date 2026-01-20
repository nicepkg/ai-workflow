---
source: https://code.claude.com/docs/en/common-workflows
title: Common workflows
---

Each task in this document includes clear instructions, example commands, and best practices to help you get the most from Claude Code.

## [​](#understand-new-codebases) Understand new codebases

### [​](#get-a-quick-codebase-overview) Get a quick codebase overview

Suppose you’ve just joined a new project and need to understand its structure quickly.

1

Navigate to the project root directory

```bash
cd /path/to/project
```

2

Start Claude Code

```bash
claude
```

3

Ask for a high-level overview

```bash
> give me an overview of this codebase
```

4

Dive deeper into specific components

```bash
> explain the main architecture patterns used here
```

```bash
> what are the key data models?
```

```bash
> how is authentication handled?
```

Tips:

- Start with broad questions, then narrow down to specific areas
- Ask about coding conventions and patterns used in the project
- Request a glossary of project-specific terms

### [​](#find-relevant-code) Find relevant code

Suppose you need to locate code related to a specific feature or functionality.

1

Ask Claude to find relevant files

```bash
> find the files that handle user authentication
```

2

Get context on how components interact

```bash
> how do these authentication files work together?
```

3

Understand the execution flow

```bash
> trace the login process from front-end to database
```

Tips:

- Be specific about what you’re looking for
- Use domain language from the project

---

## [​](#fix-bugs-efficiently) Fix bugs efficiently

Suppose you’ve encountered an error message and need to find and fix its source.

1

Share the error with Claude

```bash
> I'm seeing an error when I run npm test
```

2

Ask for fix recommendations

```bash
> suggest a few ways to fix the @ts-ignore in user.ts
```

3

Apply the fix

```bash
> update user.ts to add the null check you suggested
```

Tips:

- Tell Claude the command to reproduce the issue and get a stack trace
- Mention any steps to reproduce the error
- Let Claude know if the error is intermittent or consistent

---

## [​](#refactor-code) Refactor code

Suppose you need to update old code to use modern patterns and practices.

1

Identify legacy code for refactoring

```bash
> find deprecated API usage in our codebase
```

2

Get refactoring recommendations

```bash
> suggest how to refactor utils.js to use modern JavaScript features
```

3

Apply the changes safely

```bash
> refactor utils.js to use ES2024 features while maintaining the same behavior
```

4

Verify the refactoring

```bash
> run tests for the refactored code
```

Tips:

- Ask Claude to explain the benefits of the modern approach
- Request that changes maintain backward compatibility when needed
- Do refactoring in small, testable increments

---

## [​](#use-specialized-subagents) Use specialized subagents

Suppose you want to use specialized AI subagents to handle specific tasks more effectively.

1

View available subagents

```bash
> /agents
```

This shows all available subagents and lets you create new ones.

2

Use subagents automatically

Claude Code automatically delegates appropriate tasks to specialized subagents:

```bash
> review my recent code changes for security issues
```

```bash
> run all tests and fix any failures
```

3

Explicitly request specific subagents

```bash
> use the code-reviewer subagent to check the auth module
```

```bash
> have the debugger subagent investigate why users can't log in
```

4

Create custom subagents for your workflow

```bash
> /agents
```

Then select “Create New subagent” and follow the prompts to define:

- A unique identifier that describes the subagent’s purpose (for example, `code-reviewer`, `api-designer`).
- When Claude should use this agent
- Which tools it can access
- A system prompt describing the agent’s role and behavior

Tips:

- Create project-specific subagents in `.claude/agents/` for team sharing
- Use descriptive `description` fields to enable automatic delegation
- Limit tool access to what each subagent actually needs
- Check the [subagents documentation](/docs/en/sub-agents) for detailed examples

---

## [​](#use-plan-mode-for-safe-code-analysis) Use Plan Mode for safe code analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely. In Plan Mode, Claude uses [`AskUserQuestion`](/docs/en/settings#tools-available-to-claude) to gather requirements and clarify your goals before proposing a plan.

### [​](#when-to-use-plan-mode) When to use Plan Mode

- **Multi-step implementation**: When your feature requires making edits to many files
- **Code exploration**: When you want to research the codebase thoroughly before changing anything
- **Interactive development**: When you want to iterate on the direction with Claude

### [​](#how-to-use-plan-mode) How to use Plan Mode

**Turn on Plan Mode during a session**
You can switch into Plan Mode during a session using **Shift+Tab** to cycle through permission modes.
If you are in Normal Mode, **Shift+Tab** first switches into Auto-Accept Mode, indicated by `⏵⏵ accept edits on` at the bottom of the terminal. A subsequent **Shift+Tab** will switch into Plan Mode, indicated by `⏸ plan mode on`.
**Start a new session in Plan Mode**
To start a new session in Plan Mode, use the `--permission-mode plan` flag:

```bash
claude --permission-mode plan
```

**Run “headless” queries in Plan Mode**
You can also run a query in Plan Mode directly with `-p` (that is, in [“headless mode”](/docs/en/headless)):

```bash
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### [​](#example:-planning-a-complex-refactor) Example: Planning a complex refactor

```bash
claude --permission-mode plan
```

```bash
> I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claude analyzes the current implementation and create a comprehensive plan. Refine with follow-ups:

```bash
> What about backward compatibility?
> How should we handle database migration?
```

### [​](#configure-plan-mode-as-default) Configure Plan Mode as default

```bash
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

See [settings documentation](/docs/en/settings#available-settings) for more configuration options.

## [​](#let-claude-interview-you) Let Claude interview you

For large features, start with a minimal spec and let Claude interview you to fill in the details:

```bash
> Interview me about this feature before you start: user notification system
```

```bash
> Help me think through the requirements for authentication by asking questions
```

```bash
> Ask me clarifying questions to build out this spec: payment processing
```

Claude uses the [`AskUserQuestion`](/docs/en/settings#tools-available-to-claude) tool to ask you multiple-choice questions for gathering requirements, clarifying ambiguity, and understanding your preferences before writing any code. This collaborative approach produces better specs than trying to anticipate every requirement upfront.

When you select “Type something” to provide a custom answer, press **Ctrl+G** to open your default text editor for longer responses.

This behavior is most active in Plan Mode. To encourage it in other modes, add guidance to your `CLAUDE.md` file:

```bash
Always ask clarifying questions when there are multiple valid approaches to a task.
```

If you’re building applications with the Agent SDK and want to surface clarifying questions to your users programmatically, see [Handle approvals and user input](https://platform.claude.com/docs/en/agent-sdk/user-input#handle-clarifying-questions).

---

## [​](#work-with-tests) Work with tests

Suppose you need to add tests for uncovered code.

1

Identify untested code

```bash
> find functions in NotificationsService.swift that are not covered by tests
```

2

Generate test scaffolding

```bash
> add tests for the notification service
```

3

Add meaningful test cases

```bash
> add test cases for edge conditions in the notification service
```

4

Run and verify tests

```bash
> run the new tests and fix any failures
```

Claude can generate tests that follow your project’s existing patterns and conventions. When asking for tests, be specific about what behavior you want to verify. Claude examines your existing test files to match the style, frameworks, and assertion patterns already in use.
For comprehensive coverage, ask Claude to identify edge cases you might have missed. Claude can analyze your code paths and suggest tests for error conditions, boundary values, and unexpected inputs that are easy to overlook.

---

## [​](#create-pull-requests) Create pull requests

Suppose you need to create a well-documented pull request for your changes.

1

Summarize your changes

```bash
> summarize the changes I've made to the authentication module
```

2

Generate a pull request with Claude

```bash
> create a pr
```

3

Review and refine

```bash
> enhance the PR description with more context about the security improvements
```

4

Add testing details

```bash
> add information about how these changes were tested
```

Tips:

- Ask Claude directly to make a PR for you
- Review Claude’s generated PR before submitting
- Ask Claude to highlight potential risks or considerations

## [​](#handle-documentation) Handle documentation

Suppose you need to add or update documentation for your code.

1

Identify undocumented code

```bash
> find functions without proper JSDoc comments in the auth module
```

2

Generate documentation

```bash
> add JSDoc comments to the undocumented functions in auth.js
```

3

Review and enhance

```bash
> improve the generated documentation with more context and examples
```

4

Verify documentation

```bash
> check if the documentation follows our project standards
```

Tips:

- Specify the documentation style you want (JSDoc, docstrings, etc.)
- Ask for examples in the documentation
- Request documentation for public APIs, interfaces, and complex logic

---

## [​](#work-with-images) Work with images

Suppose you need to work with images in your codebase, and you want Claude’s help analyzing image content.

1

Add an image to the conversation

You can use any of these methods:

1. Drag and drop an image into the Claude Code window
2. Copy an image and paste it into the CLI with ctrl+v (Do not use cmd+v)
3. Provide an image path to Claude. E.g., “Analyze this image: /path/to/your/image.png”

2

Ask Claude to analyze the image

```bash
> What does this image show?
```

```bash
> Describe the UI elements in this screenshot
```

```bash
> Are there any problematic elements in this diagram?
```

3

Use images for context

```bash
> Here's a screenshot of the error. What's causing it?
```

```bash
> This is our current database schema. How should we modify it for the new feature?
```

4

Get code suggestions from visual content

```bash
> Generate CSS to match this design mockup
```

```bash
> What HTML structure would recreate this component?
```

Tips:

- Use images when text descriptions would be unclear or cumbersome
- Include screenshots of errors, UI designs, or diagrams for better context
- You can work with multiple images in a conversation
- Image analysis works with diagrams, screenshots, mockups, and more
- When Claude references images (for example, `[Image #1]`), `Cmd+Click` (Mac) or `Ctrl+Click` (Windows/Linux) the link to open the image in your default viewer

---

## [​](#reference-files-and-directories) Reference files and directories

Use @ to quickly include files or directories without waiting for Claude to read them.

1

Reference a single file

```bash
> Explain the logic in @src/utils/auth.js
```

This includes the full content of the file in the conversation.

2

Reference a directory

```bash
> What's the structure of @src/components?
```

This provides a directory listing with file information.

3

Reference MCP resources

```bash
> Show me the data from @github:repos/owner/repo/issues
```

This fetches data from connected MCP servers using the format @server:resource. See [MCP resources](/docs/en/mcp#use-mcp-resources) for details.

Tips:

- File paths can be relative or absolute
- @ file references add `CLAUDE.md` in the file’s directory and parent directories to context
- Directory references show file listings, not contents
- You can reference multiple files in a single message (for example, “@file1.js and @file2.js”)

---

## [​](#use-extended-thinking-thinking-mode) Use extended thinking (thinking mode)

[Extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) is enabled by default, reserving a portion of the output token budget (up to 31,999 tokens) for Claude to reason through complex problems step-by-step. This reasoning is visible in verbose mode, which you can toggle on with `Ctrl+O`.
Extended thinking is particularly valuable for complex architectural decisions, challenging bugs, multi-step implementation planning, and evaluating tradeoffs between different approaches. It provides more space for exploring multiple solutions, analyzing edge cases, and self-correcting mistakes.

Phrases like “think”, “think hard”, “ultrathink”, and “think more” are interpreted as regular prompt instructions and don’t allocate thinking tokens.

### [​](#configure-thinking-mode) Configure thinking mode

Thinking is enabled by default, but you can adjust or disable it.

| Scope | How to configure | Details |
| --- | --- | --- |
| **Toggle shortcut** | Press `Option+T` (macOS) or `Alt+T` (Windows/Linux) | Toggle thinking on/off for the current session. May require [terminal configuration](/docs/en/terminal-config) to enable Option key shortcuts |
| **Global default** | Use `/config` to toggle thinking mode | Sets your default across all projects. Saved as `alwaysThinkingEnabled` in `~/.claude/settings.json` |
| **Limit token budget** | Set [`MAX_THINKING_TOKENS`](/docs/en/settings#environment-variables) environment variable | Limit the thinking budget to a specific number of tokens. Example: `export MAX_THINKING_TOKENS=10000` |

To view Claude’s thinking process, press `Ctrl+O` to toggle verbose mode and see the internal reasoning displayed as gray italic text.

### [​](#how-extended-thinking-token-budgets-work) How extended thinking token budgets work

Extended thinking uses a **token budget** that controls how much internal reasoning Claude can perform before responding.
A larger thinking token budget provides:

- More space to explore multiple solution approaches step-by-step
- Room to analyze edge cases and evaluate tradeoffs thoroughly
- Ability to revise reasoning and self-correct mistakes

Token budgets for thinking mode:

- When thinking is **enabled**, Claude can use up to **31,999 tokens** from your output budget for internal reasoning
- When thinking is **disabled** (via toggle or `/config`), Claude uses **0 tokens** for thinking

**Limit the thinking budget:**

- Use the [`MAX_THINKING_TOKENS` environment variable](/docs/en/settings#environment-variables) to cap the thinking budget
- When set, this value limits the maximum tokens Claude can use for thinking
- See the [extended thinking documentation](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for valid token ranges

You’re charged for all thinking tokens used, even though Claude 4 models show summarized thinking

---

## [​](#resume-previous-conversations) Resume previous conversations

When starting Claude Code, you can resume a previous session:

- `claude --continue` continues the most recent conversation in the current directory
- `claude --resume` opens a conversation picker or resumes by name

From inside an active session, use `/resume` to switch to a different conversation.
Sessions are stored per project directory. The `/resume` picker shows sessions from the same git repository, including worktrees.

### [​](#name-your-sessions) Name your sessions

Give sessions descriptive names to find them later. This is a best practice when working on multiple tasks or features.

1

Name the current session

Use `/rename` during a session to give it a memorable name:

```bash
> /rename auth-refactor
```

You can also rename any session from the picker: run `/resume`, navigate to a session, and press `R`.

2

Resume by name later

From the command line:

```bash
claude --resume auth-refactor
```

Or from inside an active session:

```bash
> /resume auth-refactor
```

### [​](#use-the-session-picker) Use the session picker

The `/resume` command (or `claude --resume` without arguments) opens an interactive session picker with these features:
**Keyboard shortcuts in the picker:**

| Shortcut | Action |
| --- | --- |
| `↑` / `↓` | Navigate between sessions |
| `→` / `←` | Expand or collapse grouped sessions |
| `Enter` | Select and resume the highlighted session |
| `P` | Preview the session content |
| `R` | Rename the highlighted session |
| `/` | Search to filter sessions |
| `A` | Toggle between current directory and all projects |
| `B` | Filter to sessions from your current git branch |
| `Esc` | Exit the picker or search mode |

**Session organization:**
The picker displays sessions with helpful metadata:

- Session name or initial prompt
- Time elapsed since last activity
- Message count
- Git branch (if applicable)

Forked sessions (created with `/rewind` or `--fork-session`) are grouped together under their root session, making it easier to find related conversations.

Tips:

- **Name sessions early**: Use `/rename` when starting work on a distinct task—it’s much easier to find “payment-integration” than “explain this function” later
- Use `--continue` for quick access to your most recent conversation in the current directory
- Use `--resume session-name` when you know which session you need
- Use `--resume` (without a name) when you need to browse and select
- For scripts, use `claude --continue --print "prompt"` to resume in non-interactive mode
- Press `P` in the picker to preview a session before resuming it
- The resumed conversation starts with the same model and configuration as the original

How it works:

1. **Conversation Storage**: All conversations are automatically saved locally with their full message history
2. **Message Deserialization**: When resuming, the entire message history is restored to maintain context
3. **Tool State**: Tool usage and results from the previous conversation are preserved
4. **Context Restoration**: The conversation resumes with all previous context intact

---

## [​](#run-parallel-claude-code-sessions-with-git-worktrees) Run parallel Claude Code sessions with Git worktrees

Suppose you need to work on multiple tasks simultaneously with complete code isolation between Claude Code instances.

1

Understand Git worktrees

Git worktrees allow you to check out multiple branches from the same
repository into separate directories. Each worktree has its own working
directory with isolated files, while sharing the same Git history. Learn
more in the [official Git worktree
documentation](https://git-scm.com/docs/git-worktree).

2

Create a new worktree

```bash
# Create a new worktree with a new branch
git worktree add ../project-feature-a -b feature-a

# Or create a worktree with an existing branch
git worktree add ../project-bugfix bugfix-123
```

This creates a new directory with a separate working copy of your repository.

3

Run Claude Code in each worktree

```bash
# Navigate to your worktree
cd ../project-feature-a

# Run Claude Code in this isolated environment
claude
```

4

Run Claude in another worktree

```bash
cd ../project-bugfix
claude
```

5

Manage your worktrees

```bash
# List all worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../project-feature-a
```

Tips:

- Each worktree has its own independent file state, making it perfect for parallel Claude Code sessions
- Changes made in one worktree won’t affect others, preventing Claude instances from interfering with each other
- All worktrees share the same Git history and remote connections
- For long-running tasks, you can have Claude working in one worktree while you continue development in another
- Use descriptive directory names to easily identify which task each worktree is for
- Remember to initialize your development environment in each new worktree according to your project’s setup. Depending on your stack, this might include:
  - JavaScript projects: Running dependency installation (`npm install`, `yarn`)
  - Python projects: Setting up virtual environments or installing with package managers
  - Other languages: Following your project’s standard setup process

---

## [​](#use-claude-as-a-unix-style-utility) Use Claude as a unix-style utility

### [​](#add-claude-to-your-verification-process) Add Claude to your verification process

Suppose you want to use Claude Code as a linter or code reviewer.
**Add Claude to your build script:**

```bash
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```

Tips:

- Use Claude for automated code review in your CI/CD pipeline
- Customize the prompt to check for specific issues relevant to your project
- Consider creating multiple scripts for different types of verification

### [​](#pipe-in,-pipe-out) Pipe in, pipe out

Suppose you want to pipe data into Claude, and get back data in a structured format.
**Pipe data through Claude:**

```bash
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

Tips:

- Use pipes to integrate Claude into existing shell scripts
- Combine with other Unix tools for powerful workflows
- Consider using —output-format for structured output

### [​](#control-output-format) Control output format

Suppose you need Claude’s output in a specific format, especially when integrating Claude Code into scripts or other tools.

1

Use text format (default)

```bash
cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt
```

This outputs just Claude’s plain text response (default behavior).

2

Use JSON format

```bash
cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
```

This outputs a JSON array of messages with metadata including cost and duration.

3

Use streaming JSON format

```bash
cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json
```

This outputs a series of JSON objects in real-time as Claude processes the request. Each message is a valid JSON object, but the entire output is not valid JSON if concatenated.

Tips:

- Use `--output-format text` for simple integrations where you just need Claude’s response
- Use `--output-format json` when you need the full conversation log
- Use `--output-format stream-json` for real-time output of each conversation turn

---

## [​](#create-custom-slash-commands) Create custom slash commands

Claude Code supports custom slash commands that you can create to quickly execute specific prompts or tasks.
For more details, see the [Slash commands](/docs/en/slash-commands) reference page.

### [​](#create-project-specific-commands) Create project-specific commands

Suppose you want to create reusable slash commands for your project that all team members can use.

1

Create a commands directory in your project

```bash
mkdir -p .claude/commands
```

2

Create a Markdown file for each command

```bash
echo "Analyze the performance of this code and suggest three specific optimizations:" > .claude/commands/optimize.md
```

3

Use your custom command in Claude Code

```bash
> /optimize
```

Tips:

- Command names are derived from the filename (for example, `optimize.md` becomes `/optimize`)
- You can organize commands in subdirectories (for example, `.claude/commands/frontend/component.md` creates `/component` with “(project:frontend)” shown in the description)
- Project commands are available to everyone who clones the repository
- The Markdown file content becomes the prompt sent to Claude when the command is invoked

### [​](#add-command-arguments-with-$arguments) Add command arguments with $ARGUMENTS

Suppose you want to create flexible slash commands that can accept additional input from users.

1

Create a command file with the $ARGUMENTS placeholder

```bash
echo 'Find and fix issue #$ARGUMENTS. Follow these steps: 1.
Understand the issue described in the ticket 2. Locate the relevant code in
our codebase 3. Implement a solution that addresses the root cause 4. Add
appropriate tests 5. Prepare a concise PR description' >
.claude/commands/fix-issue.md
```

2

Use the command with an issue number

In your Claude session, use the command with arguments.

```bash
> /fix-issue 123
```

This replaces $ARGUMENTS with “123” in the prompt.

Tips:

- The $ARGUMENTS placeholder is replaced with any text that follows the command
- You can position $ARGUMENTS anywhere in your command template
- Other useful applications: generating test cases for specific functions, creating documentation for components, reviewing code in particular files, or translating content to specified languages

### [​](#create-personal-slash-commands) Create personal slash commands

Suppose you want to create personal slash commands that work across all your projects.

1

Create a commands directory in your home folder

```bash
mkdir -p ~/.claude/commands
```

2

Create a Markdown file for each command

```bash
echo "Review this code for security vulnerabilities, focusing on:" >
~/.claude/commands/security-review.md
```

3

Use your personal custom command

```bash
> /security-review
```

Tips:

- Personal commands show “(user)” in their description when listed with `/help`
- Personal commands are only available to you and not shared with your team
- Personal commands work across all your projects
- You can use these for consistent workflows across different codebases

---

## [​](#ask-claude-about-its-capabilities) Ask Claude about its capabilities

Claude has built-in access to its documentation and can answer questions about its own features and limitations.

### [​](#example-questions) Example questions

```bash
> can Claude Code create pull requests?
```

```bash
> how does Claude Code handle permissions?
```

```bash
> what slash commands are available?
```

```bash
> how do I use MCP with Claude Code?
```

```bash
> how do I configure Claude Code for Amazon Bedrock?
```

```bash
> what are the limitations of Claude Code?
```

Claude provides documentation-based answers to these questions. For executable examples and hands-on demonstrations, refer to the specific workflow sections above.

Tips:

- Claude always has access to the latest Claude Code documentation, regardless of the version you’re using
- Ask specific questions to get detailed answers
- Claude can explain complex features like MCP integration, enterprise configurations, and advanced workflows

---

## [​](#next-steps) Next steps

[## Claude Code reference implementation

Clone our development container reference implementation.](https://github.com/anthropics/claude-code/tree/main/.devcontainer)