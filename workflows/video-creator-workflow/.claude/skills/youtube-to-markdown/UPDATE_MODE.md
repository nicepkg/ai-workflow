# Update Mode

Video already exists. Follow these steps to analyze changes and selectively refresh.

## Step U1: Fetch fresh metadata

```bash
python3 ./extract_data.py "<YOUTUBE_URL>" "<output_directory>"
```

Read the new metadata from `youtube_{VIDEO_ID}_metadata.md`.

## Step U2: Compare and show changes

Display comparison table to user:

| Field | Stored | Current | Change |
|-------|--------|---------|--------|
| Views | {old_views} | {new_views} | {diff} |
| Likes | {old_likes} | {new_likes} | {diff} |
| Comments | {old_comments} | {new_comments} | {diff} |
| Summary Format | {v1.0/v2.0} | - | {Outdated if v1.0} |
| Comment Format | {v1.0/v2.0} | - | {Outdated if v1.0} |

## Step U3: Ask what to refresh

Use AskUserQuestion with multiSelect=true:

Options based on what changed:
- **Re-summarize** - If summary_v1=true (outdated format)
- **Re-analyze comments** - If comments_v1=true OR comment count increased
- **Update metadata only** - Always available
- **Full refresh** - Redo everything from scratch
- **Stop** - Keep existing files unchanged and stop process

## Step U4: Execute selected refreshes

Move aside = `python3 ./file_ops.py backup {file}` then delete original (file replaced)
Backup = `python3 ./file_ops.py backup {file}` (file modified in place, keep original)

### Re-summarize
1. Move summary aside
2. Move transcript aside
3. Run Steps 2-9 from main SKILL.md
4. If comment file exists: move comment-file aside, run youtube-comment-analysis

### Re-analyze comments
If comment file exists:
1. Move comment-file aside
2. Backup summary (copy)
3. Remove `## Comment Insights` section from summary (to next `##` or end)
4. Run youtube-comment-analysis

If no comment file:
1. Ask user: "No comment analysis exists. Run now?"
2. If yes: run youtube-comment-analysis

### Update metadata only
1. Backup summary (copy)
2. Replace metadata section with new metadata
3. Write back

### Full refresh
1. Move all existing files aside (summary, transcript, comments)
2. Run complete pipeline from Step 1

### Stop
1. Clean up temp files, exit

## Cleanup

Remove intermediate files created during update:
```bash
python3 ./file_ops.py cleanup "<output_directory>" "{VIDEO_ID}"
```
