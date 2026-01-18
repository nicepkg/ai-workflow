# Hook Stack Evaluator - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2026-01-01 | Initial creation from Hook-Stack-Evaluator app |
| v1.1 | 2026-01-05 | Added Mode Detection (Automatic vs Interactive) |
| v1.2 | 2026-01-08 | Added docs/ folder (README, GUIDE, ROADMAP) |

## The Vision

Right now, Hook Stack evaluates one hook at a time. You bring a hook, get a score, refine if needed.

The vision: a hook testing system that tracks what works over time. Score before publishing, then feed back performance data. "Hooks that scored 14/15 got 2x engagement vs hooks that scored 10/15."

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [ ] **Newsletter Coach Integration** - Auto-score headlines during Phase 4 of newsletter writing. Pick the highest-scoring option automatically.

- [ ] **Batch Scoring** - Evaluate multiple hooks at once. "Here are 5 headline options, rank them by Hook Stack score."

- [ ] **Platform-Specific Weights** - Different platforms care about different layers. Video hooks need stronger "Earn the Stop" (3 seconds to grab). Newsletter can lean harder on "Make It Yours" (readers already know you).

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **Performance Tracking** - Log hooks + scores + eventual engagement metrics. Build a personal database of what works.

- **Swipe File Integration** - When scoring a hook, show high-scoring examples from your swipe file for inspiration.

- **Voice Mode** - Evaluate spoken hooks for video. "Read this out loud in 3 seconds - does it still work?"

- **A/B Test Generator** - Given one hook, generate a variant that tests a different layer. "Same hook but test Curiosity vs Clarity emphasis."

- **Competitor Analysis** - Paste a competitor's hook, get a scored breakdown. See what layers they're hitting.

- **Layer Drills** - Practice mode that isolates one layer at a time. "Here are 5 hooks - which one has the strongest 'Make It Yours'?"

- **Historical Scoring** - Re-evaluate old hooks after learning more about audience. Track improvement over time.

## What We've Learned

Building this skill taught us a few things:

**Mode detection was critical.** Early versions always asked "Keep/Tweak/Trash?" even when running in a pipeline. That broke automation. The automatic/interactive split fixed it.

**Layer 4 needs audience context.** "Speak Their Lingo" can't be scored without knowing the lingo. When agents call Hook Stack, they need to pass audience info.

**The threshold matters.** 12/15 as the "ready" line isn't arbitrary. Below that, at least one layer is weak enough to hurt. Above that, all layers are at least functional.

**Metaphors make the framework stick.** "Three-legged stool" for the Three C's. "Cover band" for Make It Yours. "Street performer" for Earn the Stop. These analogies help people internalize the concepts.

**Personal stories unlock Layer 5.** When people are stuck on "Make It Yours," prompting questions help: "What happened in a client session recently?" "What childhood incident connects?" These surface the specific details that make hooks uncopyable.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
