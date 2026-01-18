# Capture Triage - How It Works

## The One-Sentence Version

It's like having an assistant who empties your mental inbox every day, turning fleeting thoughts into tasks you can actually do something about.

## Why This Exists

Throughout the day, you capture things. A call you need to make. An idea that popped into your head. A link worth reading later. A question worth researching.

These all land in Drafts Pro on your phone. Quick captures. Friction-free.

But then what?

Without a system, they pile up. You forget what you captured. The urgent stuff gets lost in the noise. The great ideas never get acted on.

This skill is the system. It reads your captures, figures out what each one actually is, and routes it to the right place - your Ready queue - where it becomes a task you'll actually see and decide on.

## The Mental Model: The Mail Room

Think of your captures like incoming mail. Some of it is bills (tasks that need doing). Some of it is magazines (stuff to read later). Some of it is letters from friends (people to follow up with). Some of it is junk (stuff you can delete).

A good mail room sorts everything before it hits your desk. Bills go in one pile. Magazines in another. Important letters get flagged.

This skill is your digital mail room. It sorts captures by intent so you can deal with them efficiently.

## How You Actually Use It

Throughout the day, capture whatever comes to mind in Drafts Pro. Don't think about organization - just capture.

Then, once a day (usually morning), say "triage captures."

The skill shows you what it found:

| # | Capture | Classification | Suggested Action |
|---|---------|----------------|------------------|
| 1 | "Call dentist..." | TASK | → Ready |
| 2 | "What if we did..." | IDEA | → Ready: Consider: |
| 3 | "Research: how do..." | RESEARCH | → Spawn research-swarm? |

You approve, modify, or skip. Then everything gets routed to your Ready queue in today's daily note.

From there, task-clarity-scanner helps you decide what's actually important today.

## The Preview Pattern

Notice you always see what's happening before anything changes? That's deliberate.

Early versions just processed everything automatically. But that felt out of control - suddenly your Ready queue had 15 new items you didn't expect.

The preview step takes 10 seconds but gives you back control. You see exactly what's about to happen. You can skip items that aren't ready. You can correct misclassifications. You approve before any changes happen.

## Classification: How It Knows What Things Are

The skill looks for signals:

**Verbs mean tasks.** "Call dentist" starts with a verb - that's clearly something to do.

**"What if" means ideas.** Speculative language signals something to consider, not something to do right now.

**Questions needing investigation mean research.** If you'd need to look stuff up to answer it, that's research.

**People's names mean contacts.** "Email Sarah about the project" - that's a follow-up with a person.

You can also use inline hints to override the auto-detection:
- `IDEA:` forces idea classification
- `Research:` triggers the research swarm option
- `Task:` forces task classification

The skill respects explicit hints over guesses.

## What Happens to Each Type

**TASK** → Goes straight to Ready as a checkbox item. "Call dentist Monday (01-08)"

**IDEA** → Goes to Ready with "Consider:" prefix. Signals it's something to think about, not necessarily do.

**REFERENCE** → Goes to Ready with "Review:" prefix. Stuff to read, watch, or process later.

**RESEARCH** → Optionally spawns a research-swarm agent. You approve this explicitly - no automatic spawning.

**CONTACT** → Creates or updates a CONTACT note, adds follow-up task to Ready.

## The "Everything to Ready" Philosophy

Notice everything goes to the Ready section? That's intentional.

The Ready queue is your "things I might do today" list. Capture triage loads it up. Then task-clarity-scanner helps you pick what actually matters.

The alternative - routing things to different places - creates "out of sight, out of mind" problems. If an idea goes to some Ideas folder, you'll never see it again.

By putting everything in Ready, you're forced to look at it. Then you consciously decide: do this today, defer to tomorrow, or move to Someday/Maybe.

## What It's NOT

This isn't a filing system. It doesn't organize things into elaborate folder structures. It routes everything to one place - Ready - and lets you decide what to do with it.

This isn't automatic. It shows you what it plans to do and waits for approval.

This isn't a research tool. If something needs research, it can spawn a research-swarm - but that's opt-in, not automatic.

Think of it as triage, not treatment. It sorts the incoming. You decide what gets attention.
