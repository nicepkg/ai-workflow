---
source: https://code.claude.com/docs/en/headless
title: Run Claude Code programmatically
---

The [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) gives you the same tools, agent loop, and context management that power Claude Code. It’s available as a CLI for scripts and CI/CD, or as [Python](https://platform.claude.com/docs/en/agent-sdk/python) and [TypeScript](https://platform.claude.com/docs/en/agent-sdk/typescript) packages for full programmatic control.

The CLI was previously called “headless mode.” The `-p` flag and all CLI options work the same way.

To run Claude Code programmatically from the CLI, pass `-p` with your prompt and any [CLI options](/docs/en/cli-reference):

```bash
claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"
```

This page covers using the Agent SDK via the CLI (`claude -p`). For the Python and TypeScript SDK packages with structured outputs, tool approval callbacks, and native message objects, see the [full Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/overview).

## [​](#basic-usage) Basic usage

Add the `-p` (or `--print`) flag to any `claude` command to run it non-interactively. All [CLI options](/docs/en/cli-reference) work with `-p`, including:

- `--continue` for [continuing conversations](#continue-conversations)
- `--allowedTools` for [auto-approving tools](#auto-approve-tools)
- `--output-format` for [structured output](#get-structured-output)

This example asks Claude a question about your codebase and prints the response:

```bash
claude -p "What does the auth module do?"
```

## [​](#examples) Examples

These examples highlight common CLI patterns.

### [​](#get-structured-output) Get structured output

Use `--output-format` to control how responses are returned:

- `text` (default): plain text output
- `json`: structured JSON with result, session ID, and metadata
- `stream-json`: newline-delimited JSON for real-time streaming

This example returns a project summary as JSON with session metadata, with the text result in the `result` field:

```bash
claude -p "Summarize this project" --output-format json
```

To get output conforming to a specific schema, use `--output-format json` with `--json-schema` and a [JSON Schema](https://json-schema.org/) definition. The response includes metadata about the request (session ID, usage, etc.) with the structured output in the `structured_output` field.
This example extracts function names and returns them as an array of strings:

```bash
claude -p "Extract the main function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}'
```

Use a tool like [jq](https://jqlang.github.io/jq/) to parse the response and extract specific fields:

```bash
# Extract the text result
claude -p "Summarize this project" --output-format json | jq -r '.result'

# Extract structured output
claude -p "Extract function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output'
```

### [​](#auto-approve-tools) Auto-approve tools

Use `--allowedTools` to let Claude use certain tools without prompting. This example runs a test suite and fixes failures, allowing Claude to execute Bash commands and read/edit files without asking for permission:

```bash
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"
```

### [​](#create-a-commit) Create a commit

This example reviews staged changes and creates a commit with an appropriate message:

```bash
claude -p "Look at my staged changes and create an appropriate commit" \
  --allowedTools "Bash(git diff:*),Bash(git log:*),Bash(git status:*),Bash(git commit:*)"
```

The `--allowedTools` flag uses [permission rule syntax](/docs/en/settings#permission-rule-syntax). The `:*` suffix enables prefix matching, so `Bash(git diff:*)` allows any command starting with `git diff`.

[Slash commands](/docs/en/slash-commands) like `/commit` are only available in interactive mode. In `-p` mode, describe the task you want to accomplish instead.

### [​](#customize-the-system-prompt) Customize the system prompt

Use `--append-system-prompt` to add instructions while keeping Claude Code’s default behavior. This example pipes a PR diff to Claude and instructs it to review for security vulnerabilities:

```bash
gh pr diff "$1" | claude -p \
  --append-system-prompt "You are a security engineer. Review for vulnerabilities." \
  --output-format json
```

See [system prompt flags](/docs/en/cli-reference#system-prompt-flags) for more options including `--system-prompt` to fully replace the default prompt.

### [​](#continue-conversations) Continue conversations

Use `--continue` to continue the most recent conversation, or `--resume` with a session ID to continue a specific conversation. This example runs a review, then sends follow-up prompts:

```bash
# First request
claude -p "Review this codebase for performance issues"

# Continue the most recent conversation
claude -p "Now focus on the database queries" --continue
claude -p "Generate a summary of all issues found" --continue
```

If you’re running multiple conversations, capture the session ID to resume a specific one:

```bash
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

## [​](#next-steps) Next steps

[## Agent SDK quickstart

Build your first agent with Python or TypeScript](https://platform.claude.com/docs/en/agent-sdk/quickstart)[## CLI reference

Explore all CLI flags and options](/docs/en/cli-reference)[## GitHub Actions

Use the Agent SDK in GitHub workflows](/docs/en/github-actions)[## GitLab CI/CD

Use the Agent SDK in GitLab pipelines](/docs/en/gitlab-ci-cd)