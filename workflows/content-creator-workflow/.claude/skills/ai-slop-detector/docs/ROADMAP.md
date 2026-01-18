# AI Slop Detector - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2026-01-01 | Initial creation from Write with AI prompt |
| v1.1 | 2026-01-08 | Added docs/ folder (README, GUIDE, ROADMAP) |
| v1.1.0 | 2026-01-15 | Directive instructions, positive framing, skill chaining section |
| v1.2.0 | 2026-01-17 | Stop Slop integration: throat-clearing, emphasis crutches, dramatic fragmentation; +10 word substitutions; 13-point checklist |

## The Vision

Right now, the slop detector catches known AI patterns. It's a static checklist - effective, but limited to patterns we've already identified.

The vision: a living pattern library that grows smarter over time, catching new AI tells as language models evolve.

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [x] **Incorporate stop-slop patterns** - ✅ DONE in v1.2.0. Merged patterns from Hardik Pandya's research:
  - **Source:** [Stop Slop article](https://hvpandya.com/stop-slop) + [GitHub repo](https://github.com/hardikpandya/stop-slop)
  - **Shipped:** throat-clearing openers, emphasis crutches, dramatic fragmentation, +10 word substitutions

- [ ] **Mandatory for Client-Facing Docs** - Proposals, pitches, anything with Ed's name on it. Learned from Ring Ring session: even well-written content had em-dash overuse, "leverage" x8, editorializing phrases. See [[Skill Plan - Client Proposal Workflow - 2026-01-09]].

- [ ] **Integration with Newsletter Coach** - Auto-run slop detection before Phase 7 final output. No manual step needed.

- [ ] **Severity Scoring** - Instead of just rewriting, show a "slop score" (1-10) so you know how AI-sounding the original was. Useful for tracking improvement over time.

- [ ] **Pattern Categories** - Let users focus on specific pattern types. "Just fix the transitions" or "only remove promotional language."

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **User-Submitted Patterns** - Let users flag new AI patterns they've noticed. Crowdsource the pattern library.

- **Before/After Mode** - Optional toggle to show what changed. Useful for learning to spot patterns yourself.

- **Voice Preservation Mode** - More conservative rewriting that prioritizes keeping the original structure. For when you want cleanup without transformation.

- **Multi-Pass Refinement** - Run multiple cleanup passes for heavily AI-generated content. Diminishing returns, but might help edge cases.

- **Code Comment Cleaning** - Extend to AI-generated code comments and documentation. Same patterns show up there.

- **Platform-Specific Modes** - Different cleanup profiles for LinkedIn (more professional), Twitter (more casual), newsletters (more personal).

## What We've Learned

Building this skill taught us a few things:

**The patterns are universal.** Doesn't matter if it's GPT-4, Claude, or Gemini - they all have the same tells. "Moreover." "It's important to note." The contrast formula. These patterns transcend specific models.

**Direct contrasts are the biggest tell.** "This isn't about X—it's about Y" shows up in almost every AI-generated piece. Eliminating this one pattern makes a huge difference in perceived authenticity.

**Less is more in cleanup.** Early versions tried to rewrite everything. The current version focuses on surgical removal of specific patterns. The text stays closer to the original intent.

**The verification checklist matters.** Without a systematic check at the end, it's easy to miss patterns. The 13-point checklist in SKILL.md is doing real work.

**Slop detection isn't enough for voice.** Ring Ring session (2026-01-09) showed that text can pass slop detection but still sound "corny" or salesy. Need a "friend test" after slop detection: would Ed actually say this to someone he's known for 10 years? Slop detector catches AI patterns; voice check catches tone mismatch.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
