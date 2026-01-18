# Capture Triage - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2025-01-05 | Initial build as inbox-triage |
| v2.0 | 2025-01-05 | Renamed to capture-triage, added dry run preview |
| v2.1 | 2026-01-06 | Split preview into two steps, explicit Ready section routing |
| v2.2 | 2026-01-08 | Added docs/ folder (README, GUIDE, ROADMAP) |

## The Vision

Right now, capture triage processes what's in your Inbox folder. You trigger it manually as part of your daily review.

The vision: captures flow through automatically. Drop something in Drafts, and by the time you sit down for morning review, it's already classified and waiting for your approval.

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [ ] **Drafts Pro Integration** - Trigger triage automatically when Drafts syncs new captures. No manual "triage captures" step needed.

- [ ] **Smart Defaults** - Learn from your decisions. If you always reclassify "what if" captures as TASK instead of IDEA, start suggesting TASK.

- [ ] **Batch Research** - When multiple captures are classified as RESEARCH, offer to combine them into a single research-swarm run. More efficient than spawning multiple agents.

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **Voice Capture** - Record audio notes, transcribe with Whisper, process as captures. Lower friction than typing.

- **Image Capture** - Photos of whiteboards, business cards, etc. OCR → text → triage. Would need image processing pipeline.

- **Capture Templates** - Drafts actions that pre-tag captures. "Quick Task" action adds `Task:` hint automatically.

- **Time Sensitivity Detection** - If capture mentions "Monday" or "tomorrow," flag as time-sensitive in preview. Help prioritize.

- **Context Grouping** - If 5 captures all mention the same project, offer to process them together as a batch.

- **Undo / Restore** - Move from Processed/ back to Inbox/ if you made a mistake. Currently manual.

- **Statistics Dashboard** - Track capture patterns over time. "You capture 3x more tasks than ideas" kind of insights.

## What We've Learned

Building this skill taught us a few things:

**The preview step is non-negotiable.** Day one test processed 32 captures from a backlog. Without preview, that would have been overwhelming. The pause-and-approve pattern prevents surprises.

**Two-step preview works better than one.** Showing the table, then asking "what do you want to do?" in a separate message gives time to absorb. Cramming everything into one message feels rushed.

**Research-swarm must be opt-in.** Early versions auto-spawned agents for anything classified as RESEARCH. That got out of control fast. Now you explicitly approve each spawn.

**"Ready" not "Captures"** - the naming was confusing. The Inbox FOLDER feeds the Ready SECTION. The Captures section is for document links, not tasks. This distinction took a while to clarify.

**Everything to Ready is the right default.** Filing captures into different locations means they disappear. Putting everything in Ready forces a decision. You can always defer - but you can't ignore.

**Inline hints solve edge cases.** Auto-detection works 80% of the time. The ability to override with `IDEA:` or `Task:` handles the other 20%.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
