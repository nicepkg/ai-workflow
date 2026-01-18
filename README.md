<div align="center">

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

One command. 104+ professional skills. Instant productivity boost.

[Get Started](#-quick-start) · [Browse Workflows](#-workflows) · [Create Your Own](#-create-your-own-workflow)

</div>

---

## ✨ Why AI Workflow?

| Before 😫 | After 🎉 |
|-----------|----------|
| "Write me a blog post..." then explain SEO, formatting, tone every time | AI already knows your content strategy, SEO rules, and brand voice |
| Manually teaching AI about stock analysis concepts | AI performs professional technical & fundamental analysis instantly |
| Repeating marketing frameworks and templates | AI generates on-brand copy with proper UTM tracking |
| Copy-pasting prompts from notes | Skills auto-activate based on your project |

**AI Workflow** = Pre-configured skill sets that make your AI assistant an expert in specific domains.

---

## 🎯 Workflows

| Workflow | For Who | Skills | Install |
|:---------|:--------|:------:|:--------|
| **[Content Creator](./content-creator-workflow/)** | Bloggers, Writers, SEO Specialists | 32 | `npx add-skill nicepkg/ai-workflow/content-creator-workflow` |
| **[Marketing Pro](./marketing-pro-workflow/)** | Digital Marketers, Growth Hackers, PMMs | 18 | `npx add-skill nicepkg/ai-workflow/marketing-pro-workflow` |
| **[Video Creator](./video-creator-workflow/)** | YouTubers, TikTokers, Video Producers | 29 | `npx add-skill nicepkg/ai-workflow/video-creator-workflow` |
| **[Stock Trader](./stock-trader-workflow/)** | Traders, Investors (US/CN/HK Markets) | 25 | `npx add-skill nicepkg/ai-workflow/stock-trader-workflow` |

<details>
<summary><b>📦 View All 104+ Skills</b></summary>

### Content Creator Workflow
`weak-signal-synthesizer` `content-trend-researcher` `competitive-ads-extractor` `twitter-reader` `article-extractor` `youtube-processor` `youtube-transcript` `content-research` `content-brief-generator` `content-brief` `skill-navigator` `blog-post-writer` `content-research-writer` `newsletter-coach` `fact-checker` `hook-stack-evaluator` `email-subject-line-optimizer` `ai-slop-detector` `content-repurposer` `social-repurposer` `social-media` `linkedin-announcement-generator` `podcast-content-suite` `pre-publish-post-assistant` `seo-wordpress-manager` `gsc-assistant` `astro-cta-injector` `nano-banana` `canvas-design` `docx` `pdf`

### Marketing Pro Workflow
`ad-copy-generator` `buyer-persona-generator` `utm-builder` `competitive-ads-extractor` `lead-research-assistant` `social-media-analyzer` `marketing-strategy-pmm` `email-campaign-creator` `landing-page-optimizer` `ab-test-designer` `funnel-analyzer` `roi-calculator` `brand-voice-guide` `market-research-assistant` `customer-journey-mapper` `pricing-strategy-advisor` `launch-checklist-generator` `growth-experiment-designer`

### Video Creator Workflow
`serpapi` `content-trend-researcher` `content-research` `capture-triage` `youtube-transcript` `youtube-to-markdown` `transcribe-and-analyze` `video-downloader` `tapestry` `video-script-writer` `video-script-collaborial` `video-hook-generator` `video-title-optimizer` `thumbnail-concept-generator` `canvas-design` `pexels-media` `media-processing` `video-to-gif` `youtube-seo-optimizer` `short-form-converter` `social-repurposer` `srt-translator` `instagram` `video-analytics-interpreter` `posthog-analytics` `webfluence` `sponsor-pitch-generator` `video-comparer` `n8n-skills`

### Stock Trader Workflow
`us-stock-analysis` `a-share-analysis` `hk-stock-analysis` `technical-analyst` `china-macro-analyst` `cross-border-flow-tracker` `a-share-screener` `portfolio-manager` `earnings-calendar` `market-news-analyst` `canslim-screener` `value-dividend-screener` `sector-analyst` `options-strategy-advisor` `backtest-expert` `scenario-analyzer` `institutional-flow-tracker` `market-environment-analysis` `breadth-chart-analyst` `pair-trade-screener` `dividend-growth-pullback-screener` `economic-calendar-fetcher` `weekly-trade-strategy` `us-market-bubble-detector` `stanley-druckenmiller-investment`

</details>

---

## ⚡ Quick Start

### Install a Complete Workflow (Recommended)

```bash
# Pick your workflow and run ONE command:
npx add-skill nicepkg/ai-workflow/content-creator-workflow

# That's it! Skills are now active in your AI assistant.
```

### Install Individual Skills

```bash
# Install just what you need
npx add-skill nicepkg/ai-workflow/stock-trader-workflow --skill a-share-analysis

# List available skills first
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow --list
```

### Advanced Options

```bash
# Install globally (available in all projects)
npx add-skill nicepkg/ai-workflow/video-creator-workflow --global

# Install to specific AI tools only
npx add-skill nicepkg/ai-workflow/content-creator-workflow -a claude-code -a cursor

# Non-interactive mode (for CI/CD)
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow -y
```

---

## 🤖 Supported AI Tools

Works with **8+ AI coding assistants** out of the box:

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
my-workflow/
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
