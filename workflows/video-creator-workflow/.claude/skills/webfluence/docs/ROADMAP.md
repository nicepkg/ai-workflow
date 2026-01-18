# Webfluence - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2025-12 | Initial framework with five layers + diagnostics |
| v1.1 | 2026-01 | Added docs/ folder (README, GUIDE, ROADMAP) |

## The Vision

Right now, Webfluence is a diagnostic framework. You describe a problem, it identifies the broken layer and prescribes a fix.

The vision: content web auditing. Given access to someone's actual content (YouTube channel, email sequences, social accounts), automatically score each dimension and identify gaps.

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [ ] **Audit Worksheet** - Structured questionnaire that walks through all five dimensions systematically. Produces a scored report.

- [ ] **Case Study Library** - Collection of diagnosed problems with solutions. "Here's someone who had the same pattern. Here's what they did."

- [ ] **Implementation Roadmap Generator** - After diagnosis, produce a prioritized list of what to build and in what order.

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **YouTube Channel Analyzer** - Given a channel URL, assess: is this functioning as a compounder? Are videos linking to each other? Is there a clear path to VSL?

- **Email Sequence Mapper** - Visualize an email sequence's belief-building progression. Where are the gaps?

- **Content Inventory Tool** - Catalog all existing content across platforms. Map what exists at each layer.

- **Time on Brand Calculator** - Given someone's content library, estimate how much "time on brand" a typical prospect experiences before the offer.

- **Competitor Analysis Mode** - Run webfluence analysis on a competitor's visible content web. See what's working for them.

- **Before/After Documentation** - When someone implements fixes, document the change. Build proof that the framework works.

## What We've Learned

Building this skill taught us a few things:

**The golden rule solves most problems.** 80% of "my funnel isn't working" issues come down to: they're skipping steps. Content → VSL → Offer Doc is the fix.

**47 minutes is the benchmark.** Time on brand matters more than number of touchpoints. One long YouTube video can do more than 20 short posts.

**Diagnosis before prescription.** Don't say "you need more content." Say "your outer ring is strong but nothing connects to your core - here's the specific fix."

**Building takes time.** Million Dollar Coach built their web over 18+ months. Setting expectations matters. This isn't a weekend project.

**Connectors are underrated.** Most people focus on content creation but ignore the threads between pieces. ManyChat, email sequences, tools - these are what move people through the web.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
