# Newsletter Coach - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2025-12 | Initial 7-phase process with resource files |
| v1.1 | 2026-01 | Added docs/ folder (README, GUIDE, ROADMAP) |
| v1.2 | 2026-01-16 | Hook Stack scoring in Phase 4, Slop Detector polish in Phase 7, Hero Image generation option |

## The Vision

Right now, Newsletter Coach gets you from "something happened today" to "publish-ready draft" in a single conversation. That's the core loop, and it works.

But here's where it could go...

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [x] **Hook Stack Integration** - ✅ v1.2 - Auto-scores top 3 headlines in Phase 4, displays (X/15) scores, recommends highest scorer.

- [x] **AI Slop Detector Pass** - ✅ v1.2 - Automatically cleans draft before presenting in Phase 7. Invisible quality gate.

- [ ] **Word Count Targeting** - Add an option to specify word count targets. "I need 800 words for LinkedIn" vs "I need 2,000 for the newsletter." Adjust the expansion phase accordingly.

- [x] **Hero Image Generation** - ✅ v1.2 - Offers hero image after draft complete, invokes nano-banana-pro with article-specific prompts.

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **Calendar Integration** - What if it could read your calendar from yesterday and prompt you with "You had a call with Sarah at 2pm - anything interesting happen?" Removes the memory burden.

- **Swipe File Builder** - Every headline you generate gets saved. Every outline that worked. Build a personal swipe file over time. "Show me headlines that worked for coaching topics."

- **Multi-Format Output** - Same content, different formats. Newsletter version, LinkedIn version, Twitter thread version. One extraction, multiple outputs.

- **Publishing Pipeline** - Direct integration with Substack API. Click a button, it publishes. (Careful with this one - you probably want a human in the loop before anything goes live.)

- **Voice Memos as Input** - Instead of typing what happened, just talk. Transcribe the voice memo and extract from that. Lower friction for capture.

## What We've Learned

Building this skill taught us a few things:

**The interview matters more than the writing.** The 7-phase structure is really just a sophisticated extraction process. By the time you get to Phase 7, the content is already there - you're just formatting it. The magic is in Phases 1-3.

**One question at a time.** Early versions asked multiple questions per response. Users got overwhelmed. The "one question, wait for answer, next question" pattern keeps momentum going.

**Resource files as progressive disclosure.** Not everything needs to be in SKILL.md. The question banks, outline formats, and style examples load when needed. Keeps the main skill focused.

**Voice matching takes examples.** You can't just say "write like Ed." You need actual newsletter examples for the AI to pattern-match against. The newsletter-examples.md file is doing heavy lifting.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
