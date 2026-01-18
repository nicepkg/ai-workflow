# Usage Patterns

> Part of the whisperkit-transcriber skill

Common transcription scenarios and workflows.

---

## Simple YouTube Transcription

User: "Transcribe this YouTube video: https://youtube.com/watch?v=abc123"

```bash
python3 scripts/transcribe.py "https://youtube.com/watch?v=abc123"
```

Inform user:
- Transcription saved to `./whisper-transcriptions/`
- Includes timestamps and metadata
- Uses small model (good balance)

---

## High-Quality Transcription

User: "I need a very accurate transcription of this lecture"

```bash
python3 scripts/transcribe.py "URL" --model medium
```

Note: medium/large models take longer but provide better accuracy.

---

## Custom Output Location

User: "Save the transcription in my Documents folder"

```bash
python3 scripts/transcribe.py "URL" --output-dir "/Users/username/Documents"
```

---

## Clean Text Only

User: "Just give me the text without timestamps"

```bash
python3 scripts/transcribe.py "URL" --no-timestamps
```

---

## Batch Processing

User: "Transcribe these three videos"

Execute sequentially:
```bash
python3 scripts/transcribe.py "URL1"
python3 scripts/transcribe.py "URL2"
python3 scripts/transcribe.py "URL3"
```

All transcriptions save to the same output directory with unique filenames.

---

## Best Practices

1. **Start with defaults** - small model with timestamps works for most cases
2. **Warn on long videos** - videos >1 hour take significant time
3. **Preserve metadata** - keep source URL and timestamp for reference
4. **Batch sequentially** - avoid overwhelming the system
