# Troubleshooting

> Part of the whisperkit-transcriber skill

Common issues and solutions.

---

## Missing Dependencies

Script checks for yt-dlp and whisperkit-cli automatically.

**yt-dlp not found:**
```bash
pip install yt-dlp
# or
brew install yt-dlp
```

**whisperkit-cli not found:**
- Install from: https://github.com/argmaxinc/WhisperKit
- Requires macOS with Apple Silicon

---

## Download Failures

If media download fails:

1. **Verify URL is accessible** - open in browser first
2. **Check authentication** - some content requires login
3. **Try alternative URL format** - youtube.com vs youtu.be
4. **Check yt-dlp version** - `pip install --upgrade yt-dlp`

---

## Transcription Errors

If WhisperKit fails:

1. **Verify installation** - `whisperkit-cli --help`
2. **Try smaller model** - `--model tiny` or `--model base`
3. **Check audio extracted** - look for temp files
4. **Ensure enough disk space** - models need room

---

## File Write Errors

If output file cannot be written:

1. **Verify directory exists** - script creates `whisper-transcriptions/` if missing
2. **Check permissions** - `ls -la` on output directory
3. **Check disk space** - `df -h`
4. **Try different output dir** - `--output-dir ~/Desktop`

---

## Performance Issues

For slow transcription:

1. **Use smaller model** - `tiny` or `base`
2. **Close other apps** - WhisperKit uses significant CPU/GPU
3. **Check thermal throttling** - let machine cool down

---

## Analysis Issues

### Missing API Key

Error: `OPENAI_API_KEY environment variable not set`

Solution:
```bash
export OPENAI_API_KEY='sk-...'
```

Add to `~/.zshrc` or `~/.bashrc` for persistence.

### API Errors

Error: `Error calling OpenAI API: ...`

Common causes:
- Invalid API key
- Rate limiting (wait and retry)
- Network connectivity issues
- Model not available

### Large Transcripts

For very large transcripts (>100k tokens):
- Consider splitting into sections
- Use more concise custom prompts
- Monitor token usage and costs
