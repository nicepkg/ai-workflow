<div align="center">

<img src="website/public/icon.svg" width="120" height="120" />

# 🚀 AI Workflow

### **Supercharge Your AI Coding Assistant with Pre-built Skill Collections**

[![GitHub stars](https://img.shields.io/github/stars/nicepkg/ai-workflow?style=social)](https://github.com/nicepkg/ai-workflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/nicepkg/ai-workflow/pulls)

[简体中文](./README_cn.md) | English

<img src="https://img.shields.io/badge/Claude_Code-Supported-blueviolet?style=for-the-badge&logo=anthropic" />
<img src="https://img.shields.io/badge/Cursor-Supported-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Codex-Supported-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/OpenCode-Supported-orange?style=for-the-badge" />

---

**Stop teaching your AI assistant the same things over and over.**

One command. 170+ professional skills. Instant productivity boost.

[Get Started](#-quick-start) · [Browse Workflows](#-workflows) · [Create Your Own](#-create-your-own-workflow)

</div>

---

## ✨ Why AI Workflow?

> **Your AI is smart. But every session starts from zero.**
>
> Every time you open a new chat, you re-explain the same frameworks, best practices, and professional standards. That ends today.

### The Pain We Solve

| 😫 Without AI Workflow | 🎉 With AI Workflow |
|:-----------------------|:--------------------|
| **Content Creator**: "Use H2 for sections, add meta descriptions, include a CTA, optimize for featured snippets..." — explaining SEO basics every single time | AI already loaded with SEO best practices, content frameworks, and publishing checklists |
| **Marketer**: Teaching UTM structure, AIDA copywriting, funnel stages, conversion optimization... | AI equipped with marketing frameworks: GTM strategy, campaign templates, analytics interpretation |
| **Video Creator**: Explaining hook formulas, retention psychology, thumbnail rules, algorithm tips... | AI pre-trained on viral content patterns, script structures, and YouTube optimization |
| **Stock Trader**: "MACD crossover means..., RSI divergence indicates..., check the 200-day MA..." | AI loaded with technical analysis, fundamental screening, and multi-market expertise (US/CN/HK) |
| **Product Manager**: Re-explaining PRD templates, user story formats, prioritization matrices... | AI knows RICE, MoSCoW, Jobs-to-be-Done, and your entire product development lifecycle |
| **Presenter**: Figuring out slide structure, narrative flow, visual hierarchy... | AI builds McKinsey-style MECE narratives with Mermaid diagrams and professional themes |

### 170+ Skills, Zero Setup

```
📚  Industry best practices → Already packaged
🎯  Professional frameworks → Ready to use
⚡  One command → Instant expertise
```

**AI Workflow** = Pre-packaged domain expertise for your AI assistant. Skip the teaching. Start producing.

---

## 👤 Who Is This For?

<table>
<tr>
<td width="50%">

**📝 Content Creators**
Bloggers, newsletter writers, SEO specialists who want AI that already knows content frameworks, optimization techniques, and publishing best practices.

**📈 Marketers & Growth Hackers**
Digital marketers, PMMs, and growth teams who need AI pre-loaded with GTM strategies, funnel analysis, campaign templates, and analytics interpretation.

**🎬 Video Creators**
YouTubers, TikTokers, and video producers who want AI that understands hooks, retention psychology, thumbnail optimization, and platform algorithms.

</td>
<td width="50%">

**📊 Traders & Investors**
Stock traders covering US, China A-shares, Hong Kong, and Taiwan markets who need AI with technical analysis, fundamental screening, and multi-market expertise.

**🎯 Product Managers**
PMs, product owners, and heads of product who want AI fluent in PRDs, user stories, prioritization frameworks (RICE, MoSCoW), and the full product lifecycle.

**🎤 Presenters & Educators**
Keynote speakers, tech presenters, and educators who need AI that builds structured narratives, professional slides, and compelling visual stories.

</td>
</tr>
</table>

---

## 🎯 Workflows

| Workflow | For Who | Skills | Install |
|:---------|:--------|:------:|:--------|
| **[Content Creator](./workflows/content-creator-workflow/)** | Bloggers, Writers, SEO Specialists | 32 | `npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow` |
| **[Marketing Pro](./workflows/marketing-pro-workflow/)** | Digital Marketers, Growth Hackers, PMMs | 38 | `npx add-skill nicepkg/ai-workflow/workflows/marketing-pro-workflow` |
| **[Video Creator](./workflows/video-creator-workflow/)** | YouTubers, TikTokers, Video Producers | 29 | `npx add-skill nicepkg/ai-workflow/workflows/video-creator-workflow` |
| **[Stock Trader](./workflows/stock-trader-workflow/)** | Traders, Investors (US/CN/HK/TW Markets) | 29 | `npx add-skill nicepkg/ai-workflow/workflows/stock-trader-workflow` |
| **[Product Manager](./workflows/product-manager-workflow/)** | PMs, Product Owners, Head of Product | 23 | `npx add-skill nicepkg/ai-workflow/workflows/product-manager-workflow` |
| **[Talk to Slidev](./workflows/talk-to-slidev-workflow/)** | Keynote Speakers, Tech Presenters, Educators | 19 | `npx add-skill nicepkg/ai-workflow/workflows/talk-to-slidev-workflow` |

---

## ⚡ Quick Start

### Install a Complete Workflow (Recommended)

```bash
# Pick your workflow and run ONE command:
npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow

# That's it! Skills are now active in your AI assistant.
```

### Install Individual Skills

```bash
# Install just what you need
npx add-skill nicepkg/ai-workflow/workflows/stock-trader-workflow --skill a-share-analysis

# List available skills first
npx add-skill nicepkg/ai-workflow/workflows/marketing-pro-workflow --list
```

### Advanced Options

```bash
# Install globally (available in all projects)
npx add-skill nicepkg/ai-workflow/workflows/video-creator-workflow --global

# Install to specific AI tools only
npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow -a claude-code -a cursor

# Non-interactive mode (for CI/CD)
npx add-skill nicepkg/ai-workflow/workflows/marketing-pro-workflow -y
```

---

## 🤖 Supported AI Tools

Works with **14+ AI coding assistants** out of the box:

| AI Tool | Project Path | Global Path |
|:--------|:-------------|:------------|
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` |
| **Codex** | `.codex/skills/` | `~/.codex/skills/` |
| **OpenCode** | `.opencode/skill/` | `~/.config/opencode/skill/` |
| **Amp** | `.agents/skills/` | `~/.config/agents/skills/` |
| **Roo Code** | `.roo/skills/` | `~/.roo/skills/` |
| **Kilo Code** | `.kilocode/skills/` | `~/.kilocode/skills/` |
| **Goose** | `.goose/skills/` | `~/.config/goose/skills/` |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` |
| **Antigravity** | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| **Clawdbot** | `skills/` | `~/.clawdbot/skills/` |
| **Droid** | `.factory/skills/` | `~/.factory/skills/` |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |

---

## 🛠 Create Your Own Workflow

### Step 1: Clone This Repository

```bash
git clone https://github.com/nicepkg/ai-workflow.git
cd ai-workflow
```

### Step 2: Open with AI Coding Assistant

Open the project with any AI tool that supports skills:
- **Claude Code**: `claude` in terminal
- **Cursor**: Open folder in Cursor
- **Codex**: `codex` in terminal
- **OpenCode**: `opencode` in terminal

### Step 3: Ask AI to Create Your Workflow

```
"Create a researcher workflow for academic paper writing"
"Create a devops workflow for kubernetes management"
"Create a data-scientist workflow for ML projects"
```

The AI will automatically:
1. Create the workflow directory structure
2. Find and download relevant skills
3. Create custom skills as needed
4. Generate documentation

### Manual Creation

```
workflows/my-workflow/
└── .claude/skills/
    └── my-skill/
        └── SKILL.md       # Skill definition
```

**SKILL.md format:**
```markdown
---
name: my-skill
description: What this skill does and when AI should use it
---

# My Skill

Instructions for the AI to follow...
```

---

## 🌟 Star History

<a href="https://star-history.com/#nicepkg/ai-workflow&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=nicepkg/ai-workflow&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=nicepkg/ai-workflow&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=nicepkg/ai-workflow&type=Date" />
 </picture>
</a>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- ⭐ **Star this repo** - It helps others discover this project
- 🐛 **Report bugs** - Open an issue if something isn't working
- 💡 **Suggest skills** - What workflows would help you?
- 🔧 **Submit PRs** - Add new skills or improve existing ones

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Contributors

<a href="https://github.com/nicepkg/ai-workflow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=nicepkg/ai-workflow" />
</a>

---

## 📚 Skill Sources & Credits

Built on the shoulders of giants:

- [Anthropic Official Skills](https://github.com/anthropics/skills)
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)
- [skillhub.club](https://www.skillhub.club) - 1000+ skills collection

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

---

<div align="center">

**If this project helped you, please consider giving it a ⭐**

<a href="https://github.com/nicepkg/ai-workflow">
  <img src="https://img.shields.io/github/stars/nicepkg/ai-workflow?style=for-the-badge&logo=github&color=yellow" alt="GitHub stars" />
</a>

Made with ❤️ by the open source community

</div>
