#!/usr/bin/env python3
"""
Validate skill sources without downloading.

Checks:
- GitHub repos: Uses git ls-remote to verify repo exists
- GitHub paths: Uses GitHub API to verify path exists in repo
- Archive URLs: Uses HEAD request to verify URL is reachable

Usage:
    python scripts/validate_sources.py                     # Validate all
    python scripts/validate_sources.py -w content-creator  # Validate one workflow
    python scripts/validate_sources.py --verbose           # Show details
"""

import argparse
import json
import subprocess
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of validating a skill source."""
    skill_name: str
    workflow: str
    source_type: str
    valid: bool
    message: str
    repo: str = ""
    path: str = ""


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_workflows_root() -> Path:
    """Get the workflows root directory."""
    root = get_project_root()
    workflows_root = root / "workflows"
    return workflows_root if workflows_root.exists() else root


def get_workflows() -> list[Path]:
    """Get all workflow directories."""
    root = get_workflows_root()
    workflows = []
    for item in root.iterdir():
        if item.is_dir() and item.name.endswith('-workflow'):
            skill_source = item / '.claude' / 'skill-source.json'
            if skill_source.exists():
                workflows.append(item)
    return sorted(workflows)


def load_skill_source(workflow_path: Path) -> dict[str, Any]:
    """Load skill-source.json from workflow."""
    skill_source_path = workflow_path / '.claude' / 'skill-source.json'
    with open(skill_source_path) as f:
        return json.load(f)


def check_github_repo(repo_url: str) -> tuple[bool, str]:
    """
    Check if a GitHub repo exists using git ls-remote.

    Returns:
        Tuple of (exists, message)
    """
    # Normalize URL
    if not repo_url.endswith('.git'):
        repo_url = repo_url + '.git'

    try:
        result = subprocess.run(
            ['git', 'ls-remote', '--exit-code', '-h', repo_url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return True, "Repo exists"
        else:
            return False, f"Repo not found or not accessible"
    except subprocess.TimeoutExpired:
        return False, "Timeout checking repo"
    except Exception as e:
        return False, f"Error: {e}"


def check_github_path(repo_url: str, path: str) -> tuple[bool, str]:
    """
    Check if a path exists in a GitHub repo using GitHub API.

    Returns:
        Tuple of (exists, message)
    """
    # Extract owner/repo from URL
    # https://github.com/owner/repo -> owner/repo
    repo_url = repo_url.rstrip('/')
    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]

    parts = repo_url.replace('https://github.com/', '').split('/')
    if len(parts) < 2:
        return False, "Invalid GitHub URL"

    owner, repo = parts[0], parts[1]

    # Use GitHub API to check contents
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    try:
        request = urllib.request.Request(
            api_url,
            headers={
                'User-Agent': 'skill-validator',
                'Accept': 'application/vnd.github.v3+json'
            }
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status == 200:
                return True, "Path exists"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, f"Path not found: {path}"
        elif e.code == 403:
            return None, "Rate limited (path not verified)"  # None = unknown
        else:
            return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, f"URL error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"

    return False, "Unknown error"


def check_archive_url(url: str) -> tuple[bool, str]:
    """
    Check if an archive URL is reachable using HEAD request.

    Returns:
        Tuple of (reachable, message)
    """
    # Skip local files
    if not url.startswith('http'):
        path = Path(url)
        if path.exists():
            return True, "Local file exists"
        else:
            return False, "Local file not found"

    try:
        request = urllib.request.Request(
            url,
            method='HEAD',
            headers={'User-Agent': 'skill-validator'}
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            content_length = response.headers.get('Content-Length', 'unknown')
            return True, f"Reachable (size: {content_length})"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, f"URL error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"


def validate_skill(
    skill: dict[str, Any],
    workflow_name: str,
    check_paths: bool = True
) -> ValidationResult:
    """
    Validate a single skill source.

    Args:
        skill: Skill configuration
        workflow_name: Name of the workflow
        check_paths: Whether to check paths (uses GitHub API, may rate limit)

    Returns:
        ValidationResult
    """
    name = skill.get('name', 'unknown')
    source_type = skill.get('type', 'github')

    if source_type == 'github':
        repo = skill.get('repo', '')
        path = skill.get('path', name)

        # First check if repo exists
        repo_valid, repo_msg = check_github_repo(repo)

        if not repo_valid:
            return ValidationResult(
                skill_name=name,
                workflow=workflow_name,
                source_type=source_type,
                valid=False,
                message=repo_msg,
                repo=repo,
                path=path
            )

        # Optionally check if path exists
        if check_paths:
            path_valid, path_msg = check_github_path(repo, path)
            if path_valid is None:  # Rate limited
                return ValidationResult(
                    skill_name=name,
                    workflow=workflow_name,
                    source_type=source_type,
                    valid=True,  # Repo valid, path unknown
                    message=f"Repo OK, {path_msg}",
                    repo=repo,
                    path=path
                )
            elif not path_valid:
                return ValidationResult(
                    skill_name=name,
                    workflow=workflow_name,
                    source_type=source_type,
                    valid=False,
                    message=path_msg,
                    repo=repo,
                    path=path
                )

        return ValidationResult(
            skill_name=name,
            workflow=workflow_name,
            source_type=source_type,
            valid=True,
            message="OK",
            repo=repo,
            path=path
        )

    elif source_type == 'archive':
        url = skill.get('url', '')

        url_valid, url_msg = check_archive_url(url)

        return ValidationResult(
            skill_name=name,
            workflow=workflow_name,
            source_type=source_type,
            valid=url_valid,
            message=url_msg,
            repo=url
        )

    else:
        return ValidationResult(
            skill_name=name,
            workflow=workflow_name,
            source_type=source_type,
            valid=False,
            message=f"Unknown source type: {source_type}"
        )


def validate_workflow(
    workflow_path: Path,
    check_paths: bool = True,
    verbose: bool = False,
    parallel: bool = True
) -> list[ValidationResult]:
    """
    Validate all skills in a workflow.

    Args:
        workflow_path: Path to workflow directory
        check_paths: Whether to check paths in repos
        verbose: Print progress
        parallel: Use parallel validation

    Returns:
        List of ValidationResults
    """
    workflow_name = workflow_path.name.replace('-workflow', '')
    config = load_skill_source(workflow_path)
    skills = config.get('skills', [])

    results = []

    if parallel:
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(validate_skill, skill, workflow_name, check_paths): skill
                for skill in skills
            }
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                if verbose:
                    status = "✓" if result.valid else "✗"
                    print(f"  {status} {result.skill_name}: {result.message}")
    else:
        for skill in skills:
            result = validate_skill(skill, workflow_name, check_paths)
            results.append(result)
            if verbose:
                status = "✓" if result.valid else "✗"
                print(f"  {status} {result.skill_name}: {result.message}")

    return results


def print_summary(results: list[ValidationResult], verbose: bool = False):
    """Print validation summary."""
    valid_count = sum(1 for r in results if r.valid)
    invalid_count = len(results) - valid_count

    # Group by workflow
    by_workflow: dict[str, list[ValidationResult]] = {}
    for r in results:
        if r.workflow not in by_workflow:
            by_workflow[r.workflow] = []
        by_workflow[r.workflow].append(r)

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    for workflow, workflow_results in sorted(by_workflow.items()):
        w_valid = sum(1 for r in workflow_results if r.valid)
        w_invalid = len(workflow_results) - w_valid

        status = "✓" if w_invalid == 0 else "✗"
        print(f"\n{status} {workflow}: {w_valid}/{len(workflow_results)} valid")

        # Show invalid ones
        invalid = [r for r in workflow_results if not r.valid]
        for r in invalid:
            print(f"    ✗ {r.skill_name}: {r.message}")
            if verbose and r.repo:
                print(f"      repo: {r.repo}")
                if r.path:
                    print(f"      path: {r.path}")

    print("\n" + "-" * 60)
    print(f"Total: {valid_count}/{len(results)} valid")

    if invalid_count > 0:
        print(f"\n⚠️  {invalid_count} skills have invalid sources!")
        return 1
    else:
        print(f"\n✅ All {valid_count} skills have valid sources!")
        return 0


def main():
    parser = argparse.ArgumentParser(
        description="Validate skill sources without downloading"
    )
    parser.add_argument(
        '--workflow', '-w',
        help="Validate specific workflow (e.g., 'content-creator')"
    )
    parser.add_argument(
        '--no-paths',
        action='store_true',
        help="Skip path validation (faster, avoids rate limits)"
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Show detailed progress"
    )
    parser.add_argument(
        '--no-parallel',
        action='store_true',
        help="Disable parallel validation"
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help="Output results as JSON"
    )

    args = parser.parse_args()

    root = get_workflows_root()

    # Determine workflows to validate
    if args.workflow:
        workflow_name = args.workflow
        if not workflow_name.endswith('-workflow'):
            workflow_name = f"{workflow_name}-workflow"

        workflow_path = root / workflow_name
        if not workflow_path.exists():
            print(f"❌ Workflow not found: {workflow_name}")
            sys.exit(1)

        workflows = [workflow_path]
    else:
        workflows = get_workflows()

    all_results = []

    for workflow_path in workflows:
        workflow_name = workflow_path.name.replace('-workflow', '')

        if args.verbose:
            print(f"\n📦 Validating: {workflow_name}")

        results = validate_workflow(
            workflow_path,
            check_paths=not args.no_paths,
            verbose=args.verbose,
            parallel=not args.no_parallel
        )
        all_results.extend(results)

    if args.json:
        import json
        output = [
            {
                'skill': r.skill_name,
                'workflow': r.workflow,
                'type': r.source_type,
                'valid': r.valid,
                'message': r.message,
                'repo': r.repo,
                'path': r.path
            }
            for r in all_results
        ]
        print(json.dumps(output, indent=2))
        sys.exit(0 if all(r.valid for r in all_results) else 1)
    else:
        exit_code = print_summary(all_results, args.verbose)
        sys.exit(exit_code)


if __name__ == "__main__":
    main()
