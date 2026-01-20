---
source: https://code.claude.com/docs/en/discover-plugins
title: Discover and install prebuilt plugins through marketplaces
---

Plugins extend Claude Code with custom commands, agents, hooks, and MCP servers. Plugin marketplaces are catalogs that help you discover and install these extensions without building them yourself.
Looking to create and distribute your own marketplace? See [Create and distribute a plugin marketplace](/docs/en/plugin-marketplaces).

## [​](#how-marketplaces-work) How marketplaces work

A marketplace is a catalog of plugins that someone else has created and shared. Using a marketplace is a two-step process:

1

Add the marketplace

This registers the catalog with Claude Code so you can browse what’s available. No plugins are installed yet.

2

Install individual plugins

Browse the catalog and install the plugins you want.

Think of it like adding an app store: adding the store gives you access to browse its collection, but you still choose which apps to download individually.

## [​](#official-anthropic-marketplace) Official Anthropic marketplace

The official Anthropic marketplace (`claude-plugins-official`) is automatically available when you start Claude Code. Run `/plugin` and go to the **Discover** tab to browse what’s available.
To install a plugin from the official marketplace:

```bash
/plugin install plugin-name@claude-plugins-official
```

The official marketplace is maintained by Anthropic. To distribute your own plugins, [create your own marketplace](/docs/en/plugin-marketplaces) and share it with users.

The official marketplace includes several categories of plugins:

### [​](#code-intelligence) Code intelligence

Code intelligence plugins help Claude understand your codebase more deeply. With these plugins installed, Claude can jump to definitions, find references, and see type errors immediately after edits. These plugins use the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP), the same technology that powers VS Code’s code intelligence.
These plugins require the language server binary to be installed on your system. If you already have a language server installed, Claude may prompt you to install the corresponding plugin when you open a project.

| Language | Plugin | Binary required |
| --- | --- | --- |
| C/C++ | `clangd-lsp` | `clangd` |
| C# | `csharp-lsp` | `csharp-ls` |
| Go | `gopls-lsp` | `gopls` |
| Java | `jdtls-lsp` | `jdtls` |
| Lua | `lua-lsp` | `lua-language-server` |
| PHP | `php-lsp` | `intelephense` |
| Python | `pyright-lsp` | `pyright-langserver` |
| Rust | `rust-analyzer-lsp` | `rust-analyzer` |
| Swift | `swift-lsp` | `sourcekit-lsp` |
| TypeScript | `typescript-lsp` | `typescript-language-server` |

You can also [create your own LSP plugin](/docs/en/plugins-reference#lsp-servers) for other languages.

If you see `Executable not found in $PATH` in the `/plugin` Errors tab after installing a plugin, install the required binary from the table above.

### [​](#external-integrations) External integrations

These plugins bundle pre-configured [MCP servers](/docs/en/mcp) so you can connect Claude to external services without manual setup:

- **Source control**: `github`, `gitlab`
- **Project management**: `atlassian` (Jira/Confluence), `asana`, `linear`, `notion`
- **Design**: `figma`
- **Infrastructure**: `vercel`, `firebase`, `supabase`
- **Communication**: `slack`
- **Monitoring**: `sentry`

### [​](#development-workflows) Development workflows

Plugins that add commands and agents for common development tasks:

- **commit-commands**: Git commit workflows including commit, push, and PR creation
- **pr-review-toolkit**: Specialized agents for reviewing pull requests
- **agent-sdk-dev**: Tools for building with the Claude Agent SDK
- **plugin-dev**: Toolkit for creating your own plugins

### [​](#output-styles) Output styles

Customize how Claude responds:

- **explanatory-output-style**: Educational insights about implementation choices
- **learning-output-style**: Interactive learning mode for skill building

## [​](#try-it:-add-the-demo-marketplace) Try it: add the demo marketplace

Anthropic also maintains a [demo plugins marketplace](https://github.com/anthropics/claude-code/tree/main/plugins) (`claude-code-plugins`) with example plugins that show what’s possible with the plugin system. Unlike the official marketplace, you need to add this one manually.

1

Add the marketplace

From within Claude Code, run the `plugin marketplace add` command for the `anthropics/claude-code` marketplace:

```bash
/plugin marketplace add anthropics/claude-code
```

This downloads the marketplace catalog and makes its plugins available to you.

2

Browse available plugins

Run `/plugin` to open the plugin manager. This opens a tabbed interface with four tabs you can cycle through using **Tab** (or **Shift+Tab** to go backward):

- **Discover**: browse available plugins from all your marketplaces
- **Installed**: view and manage your installed plugins
- **Marketplaces**: add, remove, or update your added marketplaces
- **Errors**: view any plugin loading errors

Go to the **Discover** tab to see plugins from the marketplace you just added.

3

Install a plugin

Select a plugin to view its details, then choose an installation scope:

- **User scope**: install for yourself across all projects
- **Project scope**: install for all collaborators on this repository
- **Local scope**: install for yourself in this repository only

For example, select **commit-commands** (a plugin that adds git workflow commands) and install it to your user scope.You can also install directly from the command line:

```bash
/plugin install commit-commands@anthropics-claude-code
```

See [Configuration scopes](/docs/en/settings#configuration-scopes) to learn more about scopes.

4

Use your new plugin

After installing, the plugin’s commands are immediately available. Plugin commands are namespaced by the plugin name, so **commit-commands** provides commands like `/commit-commands:commit`.Try it out by making a change to a file and running:

```bash
/commit-commands:commit
```

This stages your changes, generates a commit message, and creates the commit.Each plugin works differently. Check the plugin’s description in the **Discover** tab or its homepage to learn what commands and capabilities it provides.

The rest of this guide covers all the ways you can add marketplaces, install plugins, and manage your configuration.

## [​](#add-marketplaces) Add marketplaces

Use the `/plugin marketplace add` command to add marketplaces from different sources.

**Shortcuts**: You can use `/plugin market` instead of `/plugin marketplace`, and `rm` instead of `remove`.

- **GitHub repositories**: `owner/repo` format (for example, `anthropics/claude-code`)
- **Git URLs**: any git repository URL (GitLab, Bitbucket, self-hosted)
- **Local paths**: directories or direct paths to `marketplace.json` files
- **Remote URLs**: direct URLs to hosted `marketplace.json` files

### [​](#add-from-github) Add from GitHub

Add a GitHub repository that contains a `.claude-plugin/marketplace.json` file using the `owner/repo` format—where `owner` is the GitHub username or organization and `repo` is the repository name.
For example, `anthropics/claude-code` refers to the `claude-code` repository owned by `anthropics`:

```bash
/plugin marketplace add anthropics/claude-code
```

### [​](#add-from-other-git-hosts) Add from other Git hosts

Add any git repository by providing the full URL. This works with any Git host, including GitLab, Bitbucket, and self-hosted servers:
Using HTTPS:

```bash
/plugin marketplace add https://gitlab.com/company/plugins.git
```

Using SSH:

```bash
/plugin marketplace add [email protected]:company/plugins.git
```

To add a specific branch or tag, append `#` followed by the ref:

```bash
/plugin marketplace add https://gitlab.com/company/plugins.git#v1.0.0
```

### [​](#add-from-local-paths) Add from local paths

Add a local directory that contains a `.claude-plugin/marketplace.json` file:

```bash
/plugin marketplace add ./my-marketplace
```

You can also add a direct path to a `marketplace.json` file:

```bash
/plugin marketplace add ./path/to/marketplace.json
```

### [​](#add-from-remote-urls) Add from remote URLs

Add a remote `marketplace.json` file via URL:

```bash
/plugin marketplace add https://example.com/marketplace.json
```

URL-based marketplaces have some limitations compared to Git-based marketplaces. If you encounter “path not found” errors when installing plugins, see [Troubleshooting](/docs/en/plugin-marketplaces#plugins-with-relative-paths-fail-in-url-based-marketplaces).

## [​](#install-plugins) Install plugins

Once you’ve added marketplaces, you can install plugins directly (installs to user scope by default):

```bash
/plugin install plugin-name@marketplace-name
```

To choose a different [installation scope](/docs/en/settings#configuration-scopes), use the interactive UI: run `/plugin`, go to the **Discover** tab, and press **Enter** on a plugin. You’ll see options for:

- **User scope** (default): install for yourself across all projects
- **Project scope**: install for all collaborators on this repository (adds to `.claude/settings.json`)
- **Local scope**: install for yourself in this repository only (not shared with collaborators)

You may also see plugins with **managed** scope—these are installed by administrators via [managed settings](/docs/en/settings#settings-files) and cannot be modified.
Run `/plugin` and go to the **Installed** tab to see your plugins grouped by scope.

Make sure you trust a plugin before installing it. Anthropic does not control what MCP servers, files, or other software are included in plugins and cannot verify that they work as intended. Check each plugin’s homepage for more information.

## [​](#manage-installed-plugins) Manage installed plugins

Run `/plugin` and go to the **Installed** tab to view, enable, disable, or uninstall your plugins.
You can also manage plugins with direct commands.
Disable a plugin without uninstalling:

```bash
/plugin disable plugin-name@marketplace-name
```

Re-enable a disabled plugin:

```bash
/plugin enable plugin-name@marketplace-name
```

Completely remove a plugin:

```bash
/plugin uninstall plugin-name@marketplace-name
```

The `--scope` option lets you target a specific scope with CLI commands:

```bash
claude plugin install formatter@your-org --scope project
claude plugin uninstall formatter@your-org --scope project
```

## [​](#manage-marketplaces) Manage marketplaces

You can manage marketplaces through the interactive `/plugin` interface or with CLI commands.

### [​](#use-the-interactive-interface) Use the interactive interface

Run `/plugin` and go to the **Marketplaces** tab to:

- View all your added marketplaces with their sources and status
- Add new marketplaces
- Update marketplace listings to fetch the latest plugins
- Remove marketplaces you no longer need

### [​](#use-cli-commands) Use CLI commands

You can also manage marketplaces with direct commands.
List all configured marketplaces:

```bash
/plugin marketplace list
```

Refresh plugin listings from a marketplace:

```bash
/plugin marketplace update marketplace-name
```

Remove a marketplace:

```bash
/plugin marketplace remove marketplace-name
```

Removing a marketplace will uninstall any plugins you installed from it.

### [​](#configure-auto-updates) Configure auto-updates

Claude Code can automatically update marketplaces and their installed plugins at startup. When auto-update is enabled for a marketplace, Claude Code refreshes the marketplace data and updates installed plugins to their latest versions. If any plugins were updated, you’ll see a notification suggesting you restart Claude Code.
Toggle auto-update for individual marketplaces through the UI:

1. Run `/plugin` to open the plugin manager
2. Select **Marketplaces**
3. Choose a marketplace from the list
4. Select **Enable auto-update** or **Disable auto-update**

Official Anthropic marketplaces have auto-update enabled by default. Third-party and local development marketplaces have auto-update disabled by default.
To disable all automatic updates entirely for both Claude Code and all plugins, set the `DISABLE_AUTOUPDATER` environment variable. See [Auto updates](/docs/en/setup#auto-updates) for details.
To keep plugin auto-updates enabled while disabling Claude Code auto-updates, set `FORCE_AUTOUPDATE_PLUGINS=true` along with `DISABLE_AUTOUPDATER`:

```bash
export DISABLE_AUTOUPDATER=true
export FORCE_AUTOUPDATE_PLUGINS=true
```

This is useful when you want to manage Claude Code updates manually but still receive automatic plugin updates.

## [​](#configure-team-marketplaces) Configure team marketplaces

Team admins can set up automatic marketplace installation for projects by adding marketplace configuration to `.claude/settings.json`. When team members trust the repository folder, Claude Code prompts them to install these marketplaces and plugins.
For full configuration options including `extraKnownMarketplaces` and `enabledPlugins`, see [Plugin settings](/docs/en/settings#plugin-settings).

## [​](#troubleshooting) Troubleshooting

### [​](#/plugin-command-not-recognized) /plugin command not recognized

If you see “unknown command” or the `/plugin` command doesn’t appear:

1. **Check your version**: Run `claude --version`. Plugins require version 1.0.33 or later.
2. **Update Claude Code**:
   - **Homebrew**: `brew upgrade claude-code`
   - **npm**: `npm update -g @anthropic-ai/claude-code`
   - **Native installer**: Re-run the install command from [Setup](/docs/en/setup)
3. **Restart Claude Code**: After updating, restart your terminal and run `claude` again.

### [​](#common-issues) Common issues

- **Marketplace not loading**: Verify the URL is accessible and that `.claude-plugin/marketplace.json` exists at the path
- **Plugin installation failures**: Check that plugin source URLs are accessible and repositories are public (or you have access)
- **Files not found after installation**: Plugins are copied to a cache, so paths referencing files outside the plugin directory won’t work
- **Plugin Skills not appearing**: Clear the cache with `rm -rf ~/.claude/plugins/cache`, restart Claude Code, and reinstall the plugin. See [Plugin Skills not appearing](/docs/en/skills#plugin-skills-not-appearing-after-installation) for details.

For detailed troubleshooting with solutions, see [Troubleshooting](/docs/en/plugin-marketplaces#troubleshooting) in the marketplace guide. For debugging tools, see [Debugging and development tools](/docs/en/plugins-reference#debugging-and-development-tools).

## [​](#next-steps) Next steps

- **Build your own plugins**: See [Plugins](/docs/en/plugins) to create custom commands, agents, and hooks
- **Create a marketplace**: See [Create a plugin marketplace](/docs/en/plugin-marketplaces) to distribute plugins to your team or community
- **Technical reference**: See [Plugins reference](/docs/en/plugins-reference) for complete specifications