# YouTube Processor - How It Works

## The One-Sentence Version

It's like having a research assistant who watches videos for you and hands you the notes.

## Why This Exists

You come across an interesting YouTube video. Could be a tutorial. Could be an interview. Could be something relevant to your newsletter.

Watching takes 20 minutes. But you don't have 20 minutes right now. The video goes in a "watch later" list that you never actually get to.

This skill changes the equation. Share the link, get the summary. In 30 seconds you know whether the video is worth your time - and you've captured the key insights either way.

## The Mental Model: The Video Summarizer

Think of it like having a smart assistant who:
1. Watches the video
2. Takes detailed notes
3. Summarizes the key points
4. Highlights what's actionable

You get the essence without the time investment.

## How You Actually Use It

Share a YouTube link with any of these:
- "Summarize this video: [URL]"
- "What's this video about?"
- "Turn this into notes"

The skill extracts the transcript (most videos have captions), then summarizes based on what you need:

**Quick Summary:** One sentence headline, 3-5 key bullets, main takeaway. Takes 30 seconds to read.

**Detailed Analysis:** Full breakdown with context, action items, and how it relates to your work.

**Newsletter Mining:** If you're looking for content ideas - hooks, core insights, story beats, potential angles for The Little Blue Report.

## Why Claude Does The Summarizing

Here's an important design choice: the Python script just extracts the transcript. Claude (you) does the actual summarization.

Why? Because Claude can use context. If the video is about AI for coaches, Claude knows about Ed's work and can highlight relevant connections. If it's for the newsletter, Claude can pull out the story beats that would work for The Little Blue Report.

A generic summarizer would miss all of that.

## Two Ways to Extract

**In Claude Code (terminal):** Runs a local Python script. Faster, works offline.

**In Claude.ai (browser):** Hits an API endpoint on Vercel. Works from anywhere.

Same result either way. The skill auto-detects which environment you're in.

## What Gets Saved

When you ask to save the notes, they go to your Zettelkasten in this format:

```
YT - [Topic] - 2026-01-08.md
```

With frontmatter for the source URL, date, and tags. Plus the full transcript at the bottom if you want to search it later.

## What It's NOT

This isn't transcription. It uses the existing captions (most videos have them).

This isn't a replacement for actually watching. Some videos need to be watched - visual demos, emotional content, things you want to experience. This is for information extraction.

This isn't magic. If a video has no captions or they're disabled, it can't work.

## The Newsletter Connection

Here's where it gets powerful: combine with newsletter-coach.

You see an interesting video. Process it with youtube-processor. The mining mode pulls out hooks and story beats. Then hand off to newsletter-coach to develop those into an article.

Video → notes → newsletter draft. The insights flow through your system.

## The Time Arbitrage

A 20-minute video becomes a 30-second read. That's 40x time savings.

Multiply that across all the videos you might watch in a week. That's hours reclaimed - and you still get the key insights.
