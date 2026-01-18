#!/usr/bin/env python3
"""
Creates final markdown file from template and component files, cleans up intermediate work files
Usage: finalize.py [--debug] <BASE_NAME> <OUTPUT_DIR>
Keeps: {BASE_NAME}.md
Removes: all intermediate files including _metadata.md, _summary.md, _summary_tight.md, _description.md, _transcript.md (unless --debug)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shared_types import FileSystem, RealFileSystem, clean_title_for_filename, FileOperationError


class Finalizer:
    """Finalizes YouTube to Markdown conversion."""

    def __init__(self, fs: FileSystem = RealFileSystem()):
        """
        Initialize finalizer with dependencies.

        Args:
            fs: File system implementation
        """
        self.fs = fs

    def read_template(self, script_dir: Path, template_name: str = "template.md") -> str:
        """
        Read template file.

        Args:
            script_dir: Directory containing this script
            template_name: Name of template file

        Returns:
            Template content

        Raises:
            FileOperationError: If template not found
        """
        template_file = script_dir / template_name
        if not self.fs.exists(template_file):
            raise FileOperationError(f"{template_file} not found")
        return self.fs.read_text(template_file)

    def read_component_or_empty(self, path: Path) -> str:
        """
        Read component file or return empty string if not found.

        Args:
            path: Path to component file

        Returns:
            File content or empty string
        """
        if self.fs.exists(path):
            return self.fs.read_text(path)
        return ""

    def strip_leading_header(self, content: str, header: str) -> str:
        """
        Strip leading markdown header if present.

        Args:
            content: Content that may start with header
            header: Header text to strip (e.g., "## Quick Summary")

        Returns:
            Content with leading header removed
        """
        stripped = content.strip()
        if stripped.startswith(header):
            stripped = stripped[len(header):].lstrip()
        return stripped

    def create_final_filename(self, base_name: str, output_dir: Path) -> str:
        """
        Create human-readable filename from title.

        Args:
            base_name: Base name (youtube_{VIDEO_ID})
            output_dir: Output directory

        Returns:
            Final filename
        """
        title_path = output_dir / f"{base_name}_title.txt"
        title = self.read_component_or_empty(title_path).strip()

        if title:
            cleaned_title = clean_title_for_filename(title)
            video_id = base_name.replace('youtube_', '')
            return f"youtube - {cleaned_title} ({video_id}).md"
        else:
            # Fallback to old format if title not found
            return f"{base_name}.md"

    def assemble_final_content(
        self,
        template: str,
        base_name: str,
        output_dir: Path
    ) -> str:
        """
        Assemble final content from template and components.

        Args:
            template: Template content
            base_name: Base name
            output_dir: Output directory

        Returns:
            Final assembled content
        """
        # Read component files
        quick_summary = self.read_component_or_empty(output_dir / f"{base_name}_quick_summary.md")
        metadata = self.read_component_or_empty(output_dir / f"{base_name}_metadata.md")
        summary = self.read_component_or_empty(output_dir / f"{base_name}_summary_tight.md")

        # Strip duplicate headers from components
        quick_summary = self.strip_leading_header(quick_summary, "## Quick Summary")
        summary = self.strip_leading_header(summary, "## Summary")

        # Replace placeholders
        final_content = template.replace("{quick_summary}", quick_summary.strip())
        final_content = final_content.replace("{metadata}", metadata.strip())
        final_content = final_content.replace("{summary}", summary.strip())

        return final_content

    def assemble_transcript_content(
        self,
        template: str,
        base_name: str,
        output_dir: Path
    ) -> str:
        """
        Assemble transcript content from template and components.

        Args:
            template: Template content
            base_name: Base name
            output_dir: Output directory

        Returns:
            Assembled transcript content
        """
        # Read component files
        description = self.read_component_or_empty(output_dir / f"{base_name}_description.md")
        transcription = self.read_component_or_empty(output_dir / f"{base_name}_transcript.md")

        # Replace placeholders
        transcript_content = template.replace("{description}", description.strip())
        transcript_content = transcript_content.replace("{transcription}", transcription.strip())

        return transcript_content

    def cleanup_work_files(self, base_name: str, output_dir: Path) -> None:
        """
        Remove intermediate work files.

        Args:
            base_name: Base name
            output_dir: Output directory
        """
        work_files = [
            f"{base_name}_title.txt",
            f"{base_name}_metadata.md",
            f"{base_name}_summary.md",
            f"{base_name}_summary_tight.md",
            f"{base_name}_description.md",
            f"{base_name}_chapters.json",
            f"{base_name}_transcript.vtt",
            f"{base_name}_transcript_dedup.md",
            f"{base_name}_transcript_no_timestamps.txt",
            f"{base_name}_transcript_paragraphs.txt",
            f"{base_name}_transcript_paragraphs.md",
            f"{base_name}_transcript_cleaned.md",
            f"{base_name}_transcript.md"
        ]

        for work_file in work_files:
            file_path = output_dir / work_file
            if self.fs.exists(file_path):
                self.fs.remove(file_path)

        print("Cleaned up intermediate work files")

    def finalize(
        self,
        base_name: str,
        output_dir: Path,
        debug: bool = False
    ) -> tuple[Path, Path]:
        """
        Create final markdown files and cleanup.

        Args:
            base_name: Base name (youtube_{VIDEO_ID})
            output_dir: Output directory
            debug: If True, keep intermediate files

        Returns:
            Tuple of (summary_path, transcript_path)

        Raises:
            FileOperationError: If finalization fails
        """
        # Get script directory for templates
        script_dir = Path(__file__).parent

        # Read templates
        summary_template = self.read_template(script_dir, "template.md")
        transcript_template = self.read_template(script_dir, "template_transcript.md")

        # Assemble content
        summary_content = self.assemble_final_content(summary_template, base_name, output_dir)
        transcript_content = self.assemble_transcript_content(transcript_template, base_name, output_dir)

        # Create filenames
        title_path = output_dir / f"{base_name}_title.txt"
        title = self.read_component_or_empty(title_path).strip()
        video_id = base_name.replace('youtube_', '')

        if title:
            cleaned_title = clean_title_for_filename(title)
            summary_filename = f"youtube - {cleaned_title} ({video_id}).md"
            transcript_filename = f"youtube - {cleaned_title} - transcript ({video_id}).md"
        else:
            summary_filename = f"{base_name}.md"
            transcript_filename = f"{base_name}_transcript.md"

        summary_path = output_dir / summary_filename
        transcript_path = output_dir / transcript_filename

        # Write files
        self.fs.write_text(summary_path, summary_content)
        print(f"Created summary file: {summary_filename}")

        self.fs.write_text(transcript_path, transcript_content)
        print(f"Created transcript file: {transcript_filename}")

        # Clean up intermediate work files unless --debug is set
        if debug:
            print("Debug mode: keeping intermediate work files")
        else:
            self.cleanup_work_files(base_name, output_dir)

        return summary_path, transcript_path


def main() -> None:
    """CLI entry point."""
    # Parse options
    debug = False
    args = []
    for arg in sys.argv[1:]:
        if arg == '--debug':
            debug = True
        else:
            args.append(arg)

    # Parse arguments
    if len(args) < 1:
        print("ERROR: No BASE_NAME provided", file=sys.stderr)
        print("Usage: finalize.py [--debug] <BASE_NAME> <OUTPUT_DIR>", file=sys.stderr)
        sys.exit(1)

    base_name = args[0]
    output_dir = Path(args[1]) if len(args) > 1 else Path(".")

    try:
        finalizer = Finalizer()
        finalizer.finalize(base_name, output_dir, debug)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
