---
name: ai-traffic-vs-organic-search-report
description: Compares traffic, engagement, and conversion performance between AI search platforms (ChatGPT, Perplexity, Claude, Gemini) and traditional organic search. Use when analyzing AI referral traffic or measuring GEO vs SEO performance.
---

# AI Traffic vs Organic Search Report

## Overview

Evaluates and compares referral traffic, user engagement, and conversion metrics from generative AI search engines against traditional organic search channels. Helps marketers and SEO specialists quantify GEO (Generative Engine Optimization) impact alongside standard SEO without relying on proprietary connectors.

## When to Use

- User wants to compare traffic or conversions from AI search tools (ChatGPT, Perplexity, Claude, Gemini, Copilot) versus Google/Bing organic search
- User provides analytics data (GA4 exports, CSV tables, server logs, or live MCP data) and asks how AI referrals are performing
- User needs a structured GEO vs. SEO performance report with actionable optimization steps

## Workflow

1. **Data Segmentation:** Separate sessions, engagement metrics, and conversions into two segments:
   - **AI Search Referrals:** Traffic from `chatgpt.com`, `chat.openai.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`, and similar LLM interfaces.
   - **Traditional Organic Search:** Traffic from `google / organic`, `bing / organic`, `duckduckgo / organic`, etc.
2. **Volume & Trend Comparison:** Calculate total sessions, percentage share of total search traffic, and period-over-period growth rates for both channels.
3. **Quality & Conversion Analysis:** Compare engagement rate, bounce rate, average session duration, conversion count, conversion rate (CVR), and revenue per session between AI referrals and traditional organic search.
4. **Landing Page & Intent Gap Analysis:** Identify top landing pages receiving AI citations/referrals and compare them against top organic SEO pages to find content gaps or high-converting GEO winners.
5. **Actionable Recommendations:** Formulate concrete next steps for structured data (Schema.org), entity authority, and content formatting to scale AI search visibility.

## Output Format

### Example Input
```text
Compare our last 30 days of GA4 traffic:
- Organic Search: 42,000 sessions, 61% engagement rate, 840 conversions ($42,000 revenue)
- AI Referrals (chatgpt.com, perplexity.ai, claude.ai): 3,150 sessions, 74% engagement rate, 110 conversions ($6,600 revenue)
Top AI landing pages: /blog/best-crm-tools, /pricing, /integrations