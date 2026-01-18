# Configuration

> Part of the whisperkit-transcriber skill

Detailed configuration options for transcription.

---

## Model Selection

WhisperKit supports multiple model sizes:

| Model | Speed | Accuracy | Use Case |
|-------|-------|----------|----------|
| `tiny` | Fastest | Lowest | Quick drafts, testing |
| `base` | Fast | Reasonable | Simple content |
| `small` | Balanced | Good | **Default - most use cases** |
| `medium` | Slower | High | Lectures, important content |
| `large` | Slowest | Highest | Critical accuracy needed |

**Recommendation:** Use `small` unless user specifically requests higher accuracy.

---

## Output Format

Transcriptions save as markdown (`.md`) files.

**With timestamps (default):**
```markdown
# Transcription

**Source:** https://youtube.com/watch?v=example
**Transcribed:** 2025-11-06 14:30:00
**Tool:** WhisperKit

---

[00:00:00.000 --> 00:00:05.000] Welcome to this video...
[00:00:05.000 --> 00:00:10.000] Today we'll discuss...
```

**Without timestamps (`--no-timestamps`):**
```markdown
# Transcription

**Source:** https://youtube.com/watch?v=example
**Transcribed:** 2025-11-06 14:30:00
**Tool:** WhisperKit

---

Welcome to this video...
Today we'll discuss...
```

---

## File Naming

- **Auto-generated:** Derived from URL or video title
- **Custom:** Use `--filename "name.md"`
- **Conflict handling:** Appends timestamp if file exists

---

## Output Location

- **Default:** `./whisper-transcriptions/` in current working directory
- **Custom:** Use `--output-dir "/path/to/dir"`
