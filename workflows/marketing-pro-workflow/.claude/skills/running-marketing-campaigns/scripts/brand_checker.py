#!/usr/bin/env python3
"""
Brand Voice Compliance Checker

Validates marketing copy against brand guidelines including:
- Banned words and phrases detection
- Terminology consistency checks
- Readability scoring (Flesch-Kincaid)
- Tone analysis
- Superlative detection

Usage:
    python brand_checker.py check --text "Your marketing copy here"
    python brand_checker.py check --file copy.txt
    python brand_checker.py readability --file article.md
    python brand_checker.py terminology --text "Check our clients usage"
    python brand_checker.py full-audit --file campaign_copy.txt --output report.json

Configuration:
    Place a brand_config.json in the same directory to customize:
    - banned_words: Words/phrases to flag
    - terminology: Preferred terms and alternatives to avoid
    - tone_keywords: Words associated with different tones
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Default configuration - override with brand_config.json
DEFAULT_CONFIG = {
    "banned_words": [
        # Unsubstantiated superlatives
        {"word": "best-in-class", "reason": "Unsubstantiated superlative", "suggestion": "Specific differentiator"},
        {"word": "world-class", "reason": "Unsubstantiated superlative", "suggestion": "Specific achievement"},
        {"word": "revolutionary", "reason": "Hyperbolic", "suggestion": "Specific improvement"},
        {"word": "game-changer", "reason": "Overused cliche", "suggestion": "Specific impact"},
        {"word": "cutting-edge", "reason": "Vague buzzword", "suggestion": "Specific innovation"},
        {"word": "best ever", "reason": "Unsubstantiated superlative", "suggestion": "Specific metric"},
        {"word": "unparalleled", "reason": "Unsubstantiated superlative", "suggestion": "Specific comparison"},
        {"word": "unmatched", "reason": "Unsubstantiated superlative", "suggestion": "Specific metric"},

        # Corporate jargon
        {"word": "synergy", "reason": "Corporate jargon", "suggestion": "'work together' or specific benefit"},
        {"word": "leverage", "reason": "Overused buzzword (as verb)", "suggestion": "'use' or 'apply'"},
        {"word": "circle back", "reason": "Corporate speak", "suggestion": "'follow up' or 'revisit'"},
        {"word": "touch base", "reason": "Corporate speak", "suggestion": "'connect' or 'check in'"},
        {"word": "move the needle", "reason": "Corporate cliche", "suggestion": "Specific metric improvement"},
        {"word": "low-hanging fruit", "reason": "Corporate cliche", "suggestion": "'quick wins' or specific opportunities"},
        {"word": "paradigm shift", "reason": "Dated buzzword", "suggestion": "Specific change description"},
        {"word": "bandwidth", "reason": "Jargon (non-technical)", "suggestion": "'capacity' or 'time'"},
        {"word": "deep dive", "reason": "Overused", "suggestion": "'detailed analysis' or 'thorough review'"},

        # Vague promises
        {"word": "seamless", "reason": "Vague promise", "suggestion": "Specific integration detail"},
        {"word": "frictionless", "reason": "Vague promise", "suggestion": "Specific UX improvement"},
        {"word": "turnkey", "reason": "Vague promise", "suggestion": "Specific setup details"},
        {"word": "robust", "reason": "Vague descriptor", "suggestion": "Specific capability"},
        {"word": "scalable", "reason": "Vague without context", "suggestion": "Specific scaling capability"},
        {"word": "enterprise-grade", "reason": "Vague qualifier", "suggestion": "Specific features"},

        # Potentially problematic
        {"word": "honestly", "reason": "Implies other statements aren't honest", "suggestion": "Remove or rephrase"},
        {"word": "actually", "reason": "Can sound condescending", "suggestion": "Remove or rephrase"},
        {"word": "obviously", "reason": "Patronizing", "suggestion": "Remove"},
        {"word": "simply", "reason": "Dismissive of complexity", "suggestion": "Remove or be specific"},
        {"word": "just", "reason": "Minimizing (context-dependent)", "suggestion": "Evaluate if needed"},
    ],

    "terminology": {
        # Preferred term: [alternatives to avoid]
        "customers": ["clients", "users", "accounts", "end-users"],
        "dashboard": ["control panel", "interface", "admin panel"],
        "team members": ["employees", "staff", "workers", "personnel"],
        "campaign": ["initiative", "program", "effort"],
        "integration": ["connector", "bridge", "plugin", "add-on"],
        "API": ["interface", "endpoint"],
    },

    "tone_keywords": {
        "formal": ["therefore", "furthermore", "subsequently", "hereby", "pursuant"],
        "casual": ["gonna", "wanna", "gotta", "kinda", "yeah", "awesome", "cool"],
        "enthusiastic": ["excited", "thrilled", "amazing", "incredible", "fantastic", "love"],
        "empathetic": ["understand", "frustrating", "challenging", "difficult", "sorry"],
        "urgent": ["now", "immediately", "urgent", "critical", "deadline", "asap", "hurry"],
        "confident": ["proven", "trusted", "reliable", "guaranteed", "results"],
    },

    "readability_targets": {
        "flesch_reading_ease_min": 60,  # 60-70 is standard
        "avg_sentence_length_max": 20,
        "avg_word_length_max": 5,
    }
}


@dataclass
class Issue:
    """Represents a brand compliance issue."""
    line_number: int
    column: int
    text: str
    issue_type: str
    severity: str  # "error", "warning", "info"
    message: str
    suggestion: Optional[str] = None


@dataclass
class CheckResult:
    """Results from a brand check."""
    text: str
    issues: List[Issue] = field(default_factory=list)
    readability_score: Optional[float] = None
    avg_sentence_length: Optional[float] = None
    tone_analysis: Dict[str, int] = field(default_factory=dict)
    word_count: int = 0
    sentence_count: int = 0

    @property
    def error_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "warning")

    @property
    def passed(self) -> bool:
        return self.error_count == 0


def load_config(config_path: Optional[Path] = None) -> Dict:
    """Load brand configuration from JSON file or use defaults."""
    if config_path and config_path.exists():
        with open(config_path) as f:
            custom_config = json.load(f)
            # Merge with defaults
            config = DEFAULT_CONFIG.copy()
            config.update(custom_config)
            return config

    # Check for config in script directory
    script_dir = Path(__file__).parent
    default_config_path = script_dir / "brand_config.json"
    if default_config_path.exists():
        with open(default_config_path) as f:
            custom_config = json.load(f)
            config = DEFAULT_CONFIG.copy()
            config.update(custom_config)
            return config

    return DEFAULT_CONFIG


def count_syllables(word: str) -> int:
    """Estimate syllable count for a word."""
    word = word.lower().strip()
    if not word:
        return 0

    # Remove non-alphabetic characters
    word = re.sub(r'[^a-z]', '', word)
    if not word:
        return 0

    # Count vowel groups
    vowels = "aeiouy"
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Adjust for silent e
    if word.endswith('e') and count > 1:
        count -= 1

    # Adjust for -le endings
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1

    return max(1, count)


def calculate_flesch_reading_ease(text: str) -> Tuple[float, float, float]:
    """
    Calculate Flesch Reading Ease score.

    Returns: (score, avg_sentence_length, avg_syllables_per_word)

    Score interpretation:
    - 90-100: Very easy (5th grade)
    - 80-89: Easy (6th grade)
    - 70-79: Fairly easy (7th grade)
    - 60-69: Standard (8th-9th grade)
    - 50-59: Fairly difficult (10th-12th grade)
    - 30-49: Difficult (college)
    - 0-29: Very difficult (college graduate)
    """
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0.0, 0.0, 0.0

    # Count words and syllables
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    if not words:
        return 0.0, 0.0, 0.0

    total_syllables = sum(count_syllables(word) for word in words)

    word_count = len(words)
    sentence_count = len(sentences)

    avg_sentence_length = word_count / sentence_count
    avg_syllables_per_word = total_syllables / word_count

    # Flesch Reading Ease formula
    score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)

    return score, avg_sentence_length, avg_syllables_per_word


def find_banned_words(text: str, config: Dict) -> List[Issue]:
    """Find banned words and phrases in text."""
    issues = []
    lines = text.split('\n')

    for banned in config.get("banned_words", []):
        word = banned["word"].lower()
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)

        for line_num, line in enumerate(lines, 1):
            for match in pattern.finditer(line):
                issues.append(Issue(
                    line_number=line_num,
                    column=match.start() + 1,
                    text=match.group(),
                    issue_type="banned_word",
                    severity="warning",
                    message=f"'{match.group()}': {banned['reason']}",
                    suggestion=banned.get("suggestion")
                ))

    return issues


def check_terminology(text: str, config: Dict) -> List[Issue]:
    """Check for terminology consistency."""
    issues = []
    lines = text.split('\n')
    terminology = config.get("terminology", {})

    for preferred, alternatives in terminology.items():
        for alt in alternatives:
            pattern = re.compile(r'\b' + re.escape(alt) + r'\b', re.IGNORECASE)

            for line_num, line in enumerate(lines, 1):
                for match in pattern.finditer(line):
                    issues.append(Issue(
                        line_number=line_num,
                        column=match.start() + 1,
                        text=match.group(),
                        issue_type="terminology",
                        severity="info",
                        message=f"Consider using '{preferred}' instead of '{match.group()}'",
                        suggestion=preferred
                    ))

    return issues


def detect_superlatives(text: str) -> List[Issue]:
    """Detect potentially unsubstantiated superlatives."""
    issues = []
    lines = text.split('\n')

    # Patterns for superlatives without evidence
    superlative_patterns = [
        (r'\b(the\s+)?(best|greatest|fastest|easiest|most\s+\w+)\b(?!\s+\d)', "Superlative without evidence"),
        (r'\b(100%|guaranteed|always|never)\b', "Absolute claim - verify accuracy"),
        (r'\b(#1|number one|leading|top-rated)\b', "Ranking claim - needs citation"),
        (r'\b(\d+)x\s+(faster|better|more)\b', "Comparative claim - needs baseline"),
    ]

    for pattern, message in superlative_patterns:
        regex = re.compile(pattern, re.IGNORECASE)

        for line_num, line in enumerate(lines, 1):
            for match in regex.finditer(line):
                issues.append(Issue(
                    line_number=line_num,
                    column=match.start() + 1,
                    text=match.group(),
                    issue_type="superlative",
                    severity="warning",
                    message=message,
                    suggestion="Add supporting evidence or soften claim"
                ))

    return issues


def analyze_tone(text: str, config: Dict) -> Dict[str, int]:
    """Analyze tone based on keyword presence."""
    tone_keywords = config.get("tone_keywords", {})
    tone_counts = {}

    text_lower = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text_lower)

    for tone, keywords in tone_keywords.items():
        count = sum(1 for word in words if word in keywords)
        if count > 0:
            tone_counts[tone] = count

    return tone_counts


def check_passive_voice(text: str) -> List[Issue]:
    """Detect passive voice constructions."""
    issues = []
    lines = text.split('\n')

    # Common passive voice patterns
    passive_patterns = [
        r'\b(is|are|was|were|been|being)\s+(being\s+)?\w+ed\b',
        r'\b(is|are|was|were|been|being)\s+(being\s+)?\w+en\b',
        r'\bhas\s+been\s+\w+ed\b',
        r'\bhave\s+been\s+\w+ed\b',
    ]

    for pattern in passive_patterns:
        regex = re.compile(pattern, re.IGNORECASE)

        for line_num, line in enumerate(lines, 1):
            for match in regex.finditer(line):
                issues.append(Issue(
                    line_number=line_num,
                    column=match.start() + 1,
                    text=match.group(),
                    issue_type="passive_voice",
                    severity="info",
                    message="Consider using active voice",
                    suggestion="Rewrite with subject performing the action"
                ))

    return issues


def check_sentence_length(text: str, config: Dict) -> List[Issue]:
    """Flag sentences that exceed recommended length."""
    issues = []
    max_length = config.get("readability_targets", {}).get("avg_sentence_length_max", 20)

    sentences = re.split(r'[.!?]+', text)

    char_position = 0
    line_number = 1

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            char_position += 1
            continue

        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        word_count = len(words)

        # Find line number for this sentence
        text_before = text[:text.find(sentence)]
        line_number = text_before.count('\n') + 1

        if word_count > max_length * 1.5:  # Flag if 50% over limit
            issues.append(Issue(
                line_number=line_number,
                column=1,
                text=sentence[:50] + "..." if len(sentence) > 50 else sentence,
                issue_type="long_sentence",
                severity="warning",
                message=f"Sentence has {word_count} words (target: {max_length})",
                suggestion="Break into shorter sentences"
            ))
        elif word_count > max_length:
            issues.append(Issue(
                line_number=line_number,
                column=1,
                text=sentence[:50] + "..." if len(sentence) > 50 else sentence,
                issue_type="long_sentence",
                severity="info",
                message=f"Sentence has {word_count} words (target: {max_length})",
                suggestion="Consider breaking into shorter sentences"
            ))

    return issues


def full_check(text: str, config: Optional[Dict] = None) -> CheckResult:
    """Run all brand compliance checks on text."""
    if config is None:
        config = load_config()

    result = CheckResult(text=text)

    # Collect all issues
    result.issues.extend(find_banned_words(text, config))
    result.issues.extend(check_terminology(text, config))
    result.issues.extend(detect_superlatives(text))
    result.issues.extend(check_passive_voice(text))
    result.issues.extend(check_sentence_length(text, config))

    # Calculate readability
    score, avg_sentence, _ = calculate_flesch_reading_ease(text)
    result.readability_score = round(score, 1)
    result.avg_sentence_length = round(avg_sentence, 1)

    # Analyze tone
    result.tone_analysis = analyze_tone(text, config)

    # Word and sentence counts
    result.word_count = len(re.findall(r'\b[a-zA-Z]+\b', text))
    result.sentence_count = len([s for s in re.split(r'[.!?]+', text) if s.strip()])

    # Sort issues by line number
    result.issues.sort(key=lambda x: (x.line_number, x.column))

    return result


def format_result(result: CheckResult, verbose: bool = False) -> str:
    """Format check result for display."""
    lines = []

    # Header
    lines.append("\n" + "=" * 70)
    lines.append("BRAND VOICE COMPLIANCE REPORT")
    lines.append("=" * 70)

    # Summary stats
    lines.append(f"\nWord count: {result.word_count}")
    lines.append(f"Sentence count: {result.sentence_count}")
    lines.append(f"Average sentence length: {result.avg_sentence_length} words")
    lines.append(f"Readability score: {result.readability_score} (Flesch Reading Ease)")

    # Readability interpretation
    if result.readability_score:
        if result.readability_score >= 70:
            lines.append("  -> Easy to read (7th grade level or below)")
        elif result.readability_score >= 60:
            lines.append("  -> Standard readability (8th-9th grade)")
        elif result.readability_score >= 50:
            lines.append("  -> Fairly difficult (10th-12th grade)")
        else:
            lines.append("  -> Difficult (college level) - consider simplifying")

    # Tone analysis
    if result.tone_analysis:
        lines.append("\nTone indicators detected:")
        for tone, count in sorted(result.tone_analysis.items(), key=lambda x: -x[1]):
            lines.append(f"  {tone}: {count} keywords")

    # Issues
    lines.append("\n" + "-" * 70)

    if result.issues:
        error_count = result.error_count
        warning_count = result.warning_count
        info_count = len(result.issues) - error_count - warning_count

        lines.append(f"Issues found: {len(result.issues)} total")
        lines.append(f"  Errors: {error_count} | Warnings: {warning_count} | Info: {info_count}")
        lines.append("-" * 70)

        for issue in result.issues:
            icon = {"error": "X", "warning": "!", "info": "i"}[issue.severity]
            lines.append(f"\n[{icon}] Line {issue.line_number}, Col {issue.column}: {issue.issue_type.upper()}")
            lines.append(f"    Text: \"{issue.text}\"")
            lines.append(f"    {issue.message}")
            if issue.suggestion:
                lines.append(f"    Suggestion: {issue.suggestion}")
    else:
        lines.append("No issues found!")

    # Final verdict
    lines.append("\n" + "=" * 70)
    if result.passed:
        lines.append("RESULT: PASSED - No errors found")
    else:
        lines.append(f"RESULT: NEEDS REVIEW - {result.error_count} error(s) found")
    lines.append("=" * 70 + "\n")

    return "\n".join(lines)


def result_to_json(result: CheckResult) -> Dict:
    """Convert result to JSON-serializable dict."""
    return {
        "word_count": result.word_count,
        "sentence_count": result.sentence_count,
        "avg_sentence_length": result.avg_sentence_length,
        "readability_score": result.readability_score,
        "tone_analysis": result.tone_analysis,
        "passed": result.passed,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
        "issues": [
            {
                "line": i.line_number,
                "column": i.column,
                "text": i.text,
                "type": i.issue_type,
                "severity": i.severity,
                "message": i.message,
                "suggestion": i.suggestion
            }
            for i in result.issues
        ]
    }


def main():
    parser = argparse.ArgumentParser(
        description="Brand Voice Compliance Checker - Validate marketing copy against brand guidelines"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Check command
    check_parser = subparsers.add_parser("check", help="Run full brand compliance check")
    check_parser.add_argument("--text", help="Text to check (inline)")
    check_parser.add_argument("--file", help="File to check")
    check_parser.add_argument("--config", help="Path to brand_config.json")
    check_parser.add_argument("--json", action="store_true", help="Output as JSON")
    check_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # Readability command
    read_parser = subparsers.add_parser("readability", help="Calculate readability score")
    read_parser.add_argument("--text", help="Text to analyze")
    read_parser.add_argument("--file", help="File to analyze")

    # Terminology command
    term_parser = subparsers.add_parser("terminology", help="Check terminology consistency")
    term_parser.add_argument("--text", help="Text to check")
    term_parser.add_argument("--file", help="File to check")
    term_parser.add_argument("--config", help="Path to brand_config.json")

    # Banned words command
    banned_parser = subparsers.add_parser("banned", help="Check for banned words")
    banned_parser.add_argument("--text", help="Text to check")
    banned_parser.add_argument("--file", help="File to check")
    banned_parser.add_argument("--config", help="Path to brand_config.json")

    # Full audit command
    audit_parser = subparsers.add_parser("full-audit", help="Run full audit with JSON output")
    audit_parser.add_argument("--file", required=True, help="File to audit")
    audit_parser.add_argument("--output", help="Output JSON file")
    audit_parser.add_argument("--config", help="Path to brand_config.json")

    # List banned words command
    list_parser = subparsers.add_parser("list-banned", help="List all banned words")
    list_parser.add_argument("--config", help="Path to brand_config.json")

    args = parser.parse_args()

    # Load config if specified
    config_path = Path(args.config) if hasattr(args, 'config') and args.config else None
    config = load_config(config_path)

    # Get text from file or argument
    def get_text():
        if hasattr(args, 'file') and args.file:
            try:
                with open(args.file) as f:
                    return f.read()
            except FileNotFoundError:
                print(f"Error: File not found: {args.file}", file=sys.stderr)
                sys.exit(1)
        elif hasattr(args, 'text') and args.text:
            return args.text
        else:
            print("Error: Provide --text or --file", file=sys.stderr)
            sys.exit(1)

    if args.command == "check":
        text = get_text()
        result = full_check(text, config)

        if args.json:
            print(json.dumps(result_to_json(result), indent=2))
        else:
            print(format_result(result, args.verbose))

        sys.exit(0 if result.passed else 1)

    elif args.command == "readability":
        text = get_text()
        score, avg_sentence, avg_syllables = calculate_flesch_reading_ease(text)

        print(f"\nReadability Analysis")
        print("=" * 40)
        print(f"Flesch Reading Ease: {score:.1f}")
        print(f"Average sentence length: {avg_sentence:.1f} words")
        print(f"Average syllables per word: {avg_syllables:.2f}")

        if score >= 70:
            print("\nInterpretation: Easy to read")
        elif score >= 60:
            print("\nInterpretation: Standard readability")
        elif score >= 50:
            print("\nInterpretation: Fairly difficult")
        else:
            print("\nInterpretation: Difficult - consider simplifying")

    elif args.command == "terminology":
        text = get_text()
        issues = check_terminology(text, config)

        if issues:
            print(f"\nTerminology suggestions: {len(issues)}")
            print("-" * 40)
            for issue in issues:
                print(f"Line {issue.line_number}: '{issue.text}' -> '{issue.suggestion}'")
        else:
            print("\nNo terminology issues found!")

    elif args.command == "banned":
        text = get_text()
        issues = find_banned_words(text, config)

        if issues:
            print(f"\nBanned words found: {len(issues)}")
            print("-" * 40)
            for issue in issues:
                print(f"Line {issue.line_number}: '{issue.text}'")
                print(f"  Reason: {issue.message}")
                if issue.suggestion:
                    print(f"  Suggestion: {issue.suggestion}")
        else:
            print("\nNo banned words found!")

    elif args.command == "full-audit":
        with open(args.file) as f:
            text = f.read()

        result = full_check(text, config)
        output = result_to_json(result)

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(output, f, indent=2)
            print(f"Audit saved to {args.output}")
        else:
            print(json.dumps(output, indent=2))

    elif args.command == "list-banned":
        print("\nBanned Words & Phrases")
        print("=" * 60)
        for banned in config.get("banned_words", []):
            print(f"\n'{banned['word']}'")
            print(f"  Reason: {banned['reason']}")
            print(f"  Use instead: {banned.get('suggestion', 'N/A')}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
