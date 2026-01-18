# YouTube Processor - Roadmap

## What's Shipped

| Version | Date | What Changed |
|---------|------|--------------|
| v1.0 | 2026-01-02 | Initial build with transcript extraction |
| v1.1 | 2026-01-03 | Added Vercel API for Claude.ai/Mac client support |
| v1.2 | 2026-01-08 | Added docs/ folder (README, GUIDE, ROADMAP) |

## The Vision

Right now, you share a link, get a summary. One video at a time.

The vision: video research pipelines. "Process these 5 videos about AI for coaches and synthesize the key themes." Batch processing with cross-video analysis.

## Planned Improvements

These are on the list. Not "someday maybe" - actually planned.

- [ ] **Batch Processing** - Process multiple URLs at once. "Summarize these 5 videos" → get individual summaries plus synthesis.

- [ ] **Newsletter Coach Integration** - One-click handoff from video summary to newsletter development. Video → notes → article draft.

- [ ] **Timestamp Extraction** - When key moments are identified, include timestamps. "The main insight is at 12:34."

## Ideas (Not Committed)

These are interesting but not proven necessary yet. Parking lot stuff.

- **Video Library** - Track all processed videos. "What videos have I processed about X topic?"

- **Playlist Processing** - Given a YouTube playlist, process all videos and synthesize themes.

- **Speaker Identification** - For interview videos, identify who said what. Separate the host's questions from the guest's insights.

- **Quote Extraction** - Pull the most quotable moments. Ready-to-use quotes for social or newsletter.

- **Visual Description** - For videos where visuals matter (demos, tutorials), describe what's being shown, not just said.

- **Comparison Mode** - "Compare these two videos on the same topic. Where do they agree? Disagree?"

- **Auto-Categorization** - Based on content, suggest tags and which project this relates to.

- **MCP Server** - Package as MCP server so it works natively in Claude.ai (currently hits API which has sandbox limitations).

## What We've Learned

Building this skill taught us a few things:

**youtube-transcript-api just works.** No API keys needed. Most videos have auto-generated English captions. Extraction takes 3-5 seconds.

**Claude summarizing beats API summarizing.** Having Claude do the summarization (instead of a separate API) means it can use context - Ed's terminology, newsletter style, relevant connections.

**Two methods needed.** Claude Code has Python access. Claude.ai doesn't. The Vercel API bridges that gap, though sandbox restrictions in Claude.ai limit some functionality.

**Newsletter mining is the killer use case.** Quick summary is useful, but pulling out hooks, story beats, and angles for articles - that's where the real value is.

**Save the transcript.** Even after summarizing, keep the full transcript. You'll want to search it later or quote specific parts.

## Decision Log

When we make significant changes, the plan lives in `plans/` and the decision rationale gets archived in `plans/archive/`. That way we remember WHY we did things, not just what we did.
