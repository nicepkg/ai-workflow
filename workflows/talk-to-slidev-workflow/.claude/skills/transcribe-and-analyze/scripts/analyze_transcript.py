#!/usr/bin/env python3
"""
Transcript Analysis Script

Analyzes transcripts using either OpenAI API or local Ollama to provide:
- Executive summary
- Key insights
- Topic breakdown with summaries
- Notable quotes and highlights

Supports both cloud (OpenAI) and local (Ollama) inference.
"""

import argparse
import os
import sys
from pathlib import Path
from openai import OpenAI


DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
DEFAULT_OLLAMA_MODEL = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434/v1"


def read_transcript(file_path):
    """Read transcript file content."""
    try:
        return Path(file_path).read_text()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


def get_client(local=False):
    """Get OpenAI client configured for API or local Ollama."""
    if local:
        # Ollama uses OpenAI-compatible API
        return OpenAI(
            base_url=OLLAMA_BASE_URL,
            api_key="ollama"  # Ollama doesn't need a real key
        )
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
            print("Set it with: export OPENAI_API_KEY='your-key-here'", file=sys.stderr)
            print("Or use --local to run with Ollama instead", file=sys.stderr)
            sys.exit(1)
        return OpenAI(api_key=api_key)


def analyze_transcript(transcript_text, model, local=False, custom_prompt=None):
    """
    Analyze transcript using OpenAI API or local Ollama.

    Args:
        transcript_text: The transcript content to analyze
        model: Model to use
        local: If True, use Ollama instead of OpenAI
        custom_prompt: Custom analysis prompt (if None, uses default comprehensive analysis)

    Returns:
        Analysis results as a dictionary
    """
    client = get_client(local=local)
    provider = "Ollama" if local else "OpenAI"

    print(f"Analyzing transcript with {model} ({provider})...")

    # Use custom prompt or default
    if custom_prompt:
        system_prompt = "You are an expert content analyzer. Analyze the provided transcript according to the user's request."
        user_message = f"{custom_prompt}\n\nTranscript:\n\n{transcript_text}"
    else:
        # Default comprehensive analysis prompt
        system_prompt = """You are an expert content analyzer. Analyze the provided transcript and create a comprehensive analysis with the following sections:

1. EXECUTIVE SUMMARY: A concise 2-3 paragraph overview of the entire content

2. KEY INSIGHTS: 5-7 bullet points highlighting the most important takeaways

3. TOPICS DISCUSSED: Break down the major topics covered, with:
   - Topic name
   - Brief summary (2-3 sentences)
   - Key points discussed

4. NOTABLE QUOTES: 3-5 memorable or impactful quotes from the transcript

5. ACTION ITEMS: Any concrete actions, recommendations, or next steps mentioned

6. ADDITIONAL NOTES: Any other relevant observations, context, or interesting details

Format your response in clear markdown with headers and bullet points for readability."""
        user_message = f"Please analyze this transcript:\n\n{transcript_text}"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        analysis = response.choices[0].message.content

        # Get usage stats (may not be available for all providers)
        usage = response.usage
        tokens_used = usage.total_tokens if usage else 0
        prompt_tokens = usage.prompt_tokens if usage else 0
        completion_tokens = usage.completion_tokens if usage else 0

        print(f"Analysis complete!")
        if tokens_used:
            print(f"   Tokens used: {tokens_used:,} (prompt: {prompt_tokens:,}, completion: {completion_tokens:,})")

        return {
            "analysis": analysis,
            "model": model,
            "provider": provider,
            "tokens_used": tokens_used,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens
        }

    except Exception as e:
        print(f"Error calling {provider} API: {e}", file=sys.stderr)
        if local:
            print("Make sure Ollama is running: ollama serve", file=sys.stderr)
        sys.exit(1)


def save_analysis(analysis_data, output_path, transcript_path):
    """Save analysis to markdown file."""

    # Create header with metadata
    tokens_line = f"**Tokens Used:** {analysis_data['tokens_used']:,}\n" if analysis_data['tokens_used'] else ""

    header = f"""# Transcript Analysis

**Source Transcript:** {transcript_path}
**Analysis Model:** {analysis_data['model']} ({analysis_data['provider']})
{tokens_line}
---

"""

    output_content = header + analysis_data['analysis']

    # Save to file
    output_file = Path(output_path)
    output_file.write_text(output_content)

    print(f"Analysis saved to: {output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Analyze transcripts using OpenAI or local Ollama'
    )
    parser.add_argument(
        'transcript',
        help='Path to transcript file to analyze'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output file path (default: transcript_name_analysis.md)'
    )
    parser.add_argument(
        '--model', '-m',
        help=f'Model to use (default: {DEFAULT_OPENAI_MODEL} for API, {DEFAULT_OLLAMA_MODEL} for local)'
    )
    parser.add_argument(
        '--local', '-l',
        action='store_true',
        help='Use local Ollama instead of OpenAI API'
    )
    parser.add_argument(
        '--print', '-p',
        action='store_true',
        dest='print_output',
        help='Print analysis to stdout instead of saving to file'
    )
    parser.add_argument(
        '--prompt',
        help='Custom analysis prompt (overrides default comprehensive analysis)'
    )

    args = parser.parse_args()

    # Set default model based on provider
    if args.model:
        model = args.model
    else:
        model = DEFAULT_OLLAMA_MODEL if args.local else DEFAULT_OPENAI_MODEL

    # Read transcript
    print(f"Reading transcript: {args.transcript}")
    transcript_text = read_transcript(args.transcript)

    # Analyze
    analysis_data = analyze_transcript(
        transcript_text,
        model=model,
        local=args.local,
        custom_prompt=args.prompt
    )

    # Output results
    if args.print_output:
        print("\n" + "="*80)
        print(analysis_data['analysis'])
        print("="*80)
    else:
        # Determine output path
        if args.output:
            output_path = args.output
        else:
            # Auto-generate output filename
            transcript_path = Path(args.transcript)
            output_path = transcript_path.parent / f"{transcript_path.stem}_analysis.md"

        save_analysis(analysis_data, output_path, args.transcript)

    return 0


if __name__ == '__main__':
    sys.exit(main())
