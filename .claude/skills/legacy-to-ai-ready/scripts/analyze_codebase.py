#!/usr/bin/env python3
"""
Codebase Analyzer for Legacy-to-AI-Ready Skill

Analyzes a codebase to extract patterns, conventions, and structure
for generating Claude Code configurations.

Usage:
    python analyze_codebase.py [path] [--output json|markdown]
"""

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# Directories to ignore
IGNORE_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv', 'env',
    'dist', 'build', '.next', '.nuxt', 'coverage', '.pytest_cache',
    '.mypy_cache', '.tox', 'eggs', '*.egg-info', '.idea', '.vscode',
    'vendor', 'target', 'out', 'bin', 'obj'
}

# File extensions by category
EXTENSIONS = {
    'typescript': {'.ts', '.tsx'},
    'javascript': {'.js', '.jsx', '.mjs', '.cjs'},
    'python': {'.py', '.pyi'},
    'go': {'.go'},
    'rust': {'.rs'},
    'java': {'.java'},
    'ruby': {'.rb'},
    'php': {'.php'},
    'csharp': {'.cs'},
    'cpp': {'.cpp', '.cc', '.cxx', '.hpp', '.h'},
    'c': {'.c'},
    'swift': {'.swift'},
    'kotlin': {'.kt', '.kts'},
    'scala': {'.scala'},
    'markdown': {'.md', '.mdx'},
    'yaml': {'.yml', '.yaml'},
    'json': {'.json'},
    'css': {'.css', '.scss', '.sass', '.less'},
    'html': {'.html', '.htm'},
    'sql': {'.sql'},
    'shell': {'.sh', '.bash', '.zsh'},
}

# Config files to detect
CONFIG_FILES = {
    'package.json': 'nodejs',
    'pyproject.toml': 'python',
    'setup.py': 'python',
    'requirements.txt': 'python',
    'Cargo.toml': 'rust',
    'go.mod': 'go',
    'pom.xml': 'java',
    'build.gradle': 'java',
    'Gemfile': 'ruby',
    'composer.json': 'php',
    '.csproj': 'csharp',
    'Package.swift': 'swift',
    'Makefile': 'make',
    'CMakeLists.txt': 'cmake',
}

# Formatter/linter configs
TOOL_CONFIGS = {
    '.eslintrc': 'eslint',
    '.eslintrc.js': 'eslint',
    '.eslintrc.json': 'eslint',
    '.eslintrc.yml': 'eslint',
    'eslint.config.js': 'eslint',
    '.prettierrc': 'prettier',
    '.prettierrc.js': 'prettier',
    '.prettierrc.json': 'prettier',
    'prettier.config.js': 'prettier',
    'tsconfig.json': 'typescript',
    '.editorconfig': 'editorconfig',
    'pyproject.toml': 'python-tools',
    '.flake8': 'flake8',
    '.pylintrc': 'pylint',
    'setup.cfg': 'python-tools',
    '.rubocop.yml': 'rubocop',
    'rustfmt.toml': 'rustfmt',
    '.golangci.yml': 'golangci',
}


def should_ignore(path: Path) -> bool:
    """Check if path should be ignored."""
    parts = path.parts
    return any(part in IGNORE_DIRS or part.startswith('.') for part in parts)


def detect_language(ext: str) -> str:
    """Detect language from extension."""
    for lang, exts in EXTENSIONS.items():
        if ext in exts:
            return lang
    return 'other'


def analyze_directory_structure(root: Path) -> dict:
    """Analyze the directory structure."""
    structure = {
        'root_dirs': [],
        'patterns': [],
        'depth': 0,
    }

    try:
        for item in root.iterdir():
            if item.is_dir() and not should_ignore(item):
                structure['root_dirs'].append(item.name)
    except PermissionError:
        pass

    # Detect common patterns
    common_patterns = {
        'src': 'source code',
        'lib': 'library code',
        'app': 'application code',
        'pages': 'page components (Next.js/Nuxt)',
        'components': 'UI components',
        'hooks': 'React hooks',
        'utils': 'utilities',
        'helpers': 'helper functions',
        'services': 'service layer',
        'api': 'API routes/handlers',
        'routes': 'routing',
        'controllers': 'MVC controllers',
        'models': 'data models',
        'views': 'view templates',
        'tests': 'test files',
        'test': 'test files',
        '__tests__': 'Jest tests',
        'spec': 'spec files',
        'docs': 'documentation',
        'scripts': 'build/utility scripts',
        'config': 'configuration',
        'public': 'static assets',
        'static': 'static assets',
        'assets': 'assets',
    }

    for dir_name in structure['root_dirs']:
        if dir_name in common_patterns:
            structure['patterns'].append({
                'dir': dir_name,
                'purpose': common_patterns[dir_name]
            })

    return structure


def analyze_files(root: Path) -> dict:
    """Analyze file distribution and patterns."""
    stats = {
        'total_files': 0,
        'by_language': Counter(),
        'by_extension': Counter(),
        'test_files': 0,
        'config_files': [],
        'tool_configs': [],
    }

    for path in root.rglob('*'):
        if path.is_file() and not should_ignore(path.relative_to(root)):
            stats['total_files'] += 1
            ext = path.suffix.lower()
            stats['by_extension'][ext] += 1
            stats['by_language'][detect_language(ext)] += 1

            # Detect test files
            name = path.name.lower()
            if 'test' in name or 'spec' in name or path.parent.name in ('tests', 'test', '__tests__', 'spec'):
                stats['test_files'] += 1

            # Detect config files
            if path.name in CONFIG_FILES:
                stats['config_files'].append({
                    'file': path.name,
                    'type': CONFIG_FILES[path.name]
                })

            # Detect tool configs
            if path.name in TOOL_CONFIGS:
                stats['tool_configs'].append({
                    'file': path.name,
                    'tool': TOOL_CONFIGS[path.name]
                })

    # Convert counters to dicts for JSON serialization
    stats['by_language'] = dict(stats['by_language'].most_common())
    stats['by_extension'] = dict(stats['by_extension'].most_common(20))

    return stats


def analyze_package_json(root: Path) -> dict | None:
    """Analyze package.json for Node.js projects."""
    pkg_path = root / 'package.json'
    if not pkg_path.exists():
        return None

    try:
        with open(pkg_path) as f:
            pkg = json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

    analysis = {
        'name': pkg.get('name', 'unknown'),
        'scripts': {},
        'dependencies': [],
        'devDependencies': [],
        'frameworks': [],
    }

    # Extract scripts
    scripts = pkg.get('scripts', {})
    important_scripts = ['build', 'test', 'lint', 'format', 'start', 'dev', 'deploy']
    for script in important_scripts:
        if script in scripts:
            analysis['scripts'][script] = scripts[script]

    # Detect frameworks
    all_deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}

    frameworks = {
        'react': 'React',
        'next': 'Next.js',
        'vue': 'Vue.js',
        'nuxt': 'Nuxt.js',
        '@angular/core': 'Angular',
        'svelte': 'Svelte',
        'express': 'Express.js',
        'fastify': 'Fastify',
        'nest': 'NestJS',
        'prisma': 'Prisma ORM',
        'drizzle-orm': 'Drizzle ORM',
        'typeorm': 'TypeORM',
        'jest': 'Jest',
        'vitest': 'Vitest',
        'mocha': 'Mocha',
        'cypress': 'Cypress',
        'playwright': 'Playwright',
        'tailwindcss': 'Tailwind CSS',
        'eslint': 'ESLint',
        'prettier': 'Prettier',
        'typescript': 'TypeScript',
    }

    for dep, framework in frameworks.items():
        if dep in all_deps:
            analysis['frameworks'].append(framework)

    return analysis


def analyze_pyproject(root: Path) -> dict | None:
    """Analyze pyproject.toml for Python projects."""
    pyproject_path = root / 'pyproject.toml'
    if not pyproject_path.exists():
        return None

    try:
        import tomllib
        with open(pyproject_path, 'rb') as f:
            pyproject = tomllib.load(f)
    except ImportError:
        # Python < 3.11
        return {'note': 'pyproject.toml exists but tomllib not available'}
    except Exception:
        return None

    analysis = {
        'name': pyproject.get('project', {}).get('name', 'unknown'),
        'tools': [],
        'frameworks': [],
    }

    # Detect tools
    tool_section = pyproject.get('tool', {})
    if 'black' in tool_section:
        analysis['tools'].append('black')
    if 'isort' in tool_section:
        analysis['tools'].append('isort')
    if 'ruff' in tool_section:
        analysis['tools'].append('ruff')
    if 'pytest' in tool_section:
        analysis['tools'].append('pytest')
    if 'mypy' in tool_section:
        analysis['tools'].append('mypy')

    # Detect frameworks from dependencies
    deps = pyproject.get('project', {}).get('dependencies', [])
    deps_str = ' '.join(deps) if isinstance(deps, list) else str(deps)

    if 'django' in deps_str.lower():
        analysis['frameworks'].append('Django')
    if 'flask' in deps_str.lower():
        analysis['frameworks'].append('Flask')
    if 'fastapi' in deps_str.lower():
        analysis['frameworks'].append('FastAPI')
    if 'sqlalchemy' in deps_str.lower():
        analysis['frameworks'].append('SQLAlchemy')
    if 'pytest' in deps_str.lower():
        analysis['frameworks'].append('pytest')

    return analysis


def analyze_git(root: Path) -> dict | None:
    """Analyze git configuration."""
    git_dir = root / '.git'
    if not git_dir.exists():
        return None

    analysis = {
        'has_git': True,
        'hooks': [],
        'commit_patterns': [],
        'branch_pattern': None,
    }

    # Check for git hooks
    hooks_dir = git_dir / 'hooks'
    if hooks_dir.exists():
        for hook in hooks_dir.iterdir():
            if hook.is_file() and not hook.name.endswith('.sample'):
                analysis['hooks'].append(hook.name)

    # Check for husky
    husky_dir = root / '.husky'
    if husky_dir.exists():
        analysis['hooks'].append('husky (pre-commit hooks)')

    # Analyze recent commit messages (via subprocess)
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'log', '--oneline', '-20', '--format=%s'],
            cwd=root, capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            commits = result.stdout.strip().split('\n')
            # Detect conventional commits pattern
            conventional = sum(1 for c in commits if re.match(r'^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?:', c))
            if conventional > len(commits) * 0.5:
                analysis['commit_patterns'].append('conventional-commits')
            # Detect other patterns
            if any('[' in c and ']' in c for c in commits):
                analysis['commit_patterns'].append('bracketed-prefix')
    except Exception:
        pass

    return analysis


def analyze_sensitive_files(root: Path) -> dict:
    """Detect potentially sensitive files that should be protected."""
    sensitive = {
        'found': [],
        'patterns_detected': [],
        'claudeignore_suggestions': [],
    }

    sensitive_patterns = [
        ('.env', 'Environment variables'),
        ('.env.local', 'Local environment'),
        ('.env.production', 'Production secrets'),
        ('credentials.json', 'Credentials file'),
        ('service-account.json', 'Service account'),
        ('*.pem', 'SSL certificate'),
        ('*.key', 'Private key'),
        ('kubeconfig', 'Kubernetes config'),
        ('.aws/', 'AWS credentials'),
        ('secrets/', 'Secrets directory'),
    ]

    for path in root.rglob('*'):
        if should_ignore(path.relative_to(root)):
            continue
        if not path.is_file():
            continue

        name = path.name.lower()
        rel_path = str(path.relative_to(root))

        # Check for sensitive patterns
        if name.startswith('.env'):
            sensitive['found'].append(rel_path)
            sensitive['patterns_detected'].append('env-files')
        elif 'secret' in name or 'credential' in name:
            sensitive['found'].append(rel_path)
            sensitive['patterns_detected'].append('secrets')
        elif name.endswith(('.pem', '.key', '.p12', '.keystore')):
            sensitive['found'].append(rel_path)
            sensitive['patterns_detected'].append('certificates')
        elif 'kubeconfig' in name:
            sensitive['found'].append(rel_path)
            sensitive['patterns_detected'].append('k8s-config')

    # Generate .claudeignore suggestions
    sensitive['patterns_detected'] = list(set(sensitive['patterns_detected']))
    if sensitive['patterns_detected']:
        sensitive['claudeignore_suggestions'] = [
            '# Auto-detected sensitive patterns',
            '.env*',
            '*.pem',
            '*.key',
            '*secret*',
            '*credential*',
        ]

    return sensitive


def analyze_gitignore(root: Path) -> dict:
    """Analyze .gitignore for .claudeignore suggestions."""
    analysis = {
        'has_gitignore': False,
        'patterns': [],
        'claudeignore_additions': [],
    }

    gitignore_path = root / '.gitignore'
    if not gitignore_path.exists():
        return analysis

    analysis['has_gitignore'] = True

    try:
        content = gitignore_path.read_text()
        lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
        analysis['patterns'] = lines[:20]  # First 20 patterns

        # Patterns that should also be in .claudeignore
        claude_additions = []
        for line in lines:
            # Large directories Claude shouldn't read
            if any(p in line for p in ['node_modules', 'dist', 'build', '.next', 'coverage']):
                continue  # Already in default ignore
            # Binary/generated files
            if line.endswith(('.min.js', '.bundle.js', '.map', '.lock')):
                claude_additions.append(line)
            # Data files
            if line.endswith(('.sql', '.db', '.sqlite', '.dump')):
                claude_additions.append(line)

        analysis['claudeignore_additions'] = claude_additions[:10]
    except Exception:
        pass

    return analysis


def analyze_cicd(root: Path) -> dict:
    """Detect CI/CD configuration."""
    cicd = {
        'detected': [],
        'files': [],
    }

    ci_patterns = {
        '.github/workflows': 'GitHub Actions',
        '.gitlab-ci.yml': 'GitLab CI',
        'Jenkinsfile': 'Jenkins',
        '.circleci': 'CircleCI',
        '.travis.yml': 'Travis CI',
        'azure-pipelines.yml': 'Azure DevOps',
        'bitbucket-pipelines.yml': 'Bitbucket Pipelines',
        '.drone.yml': 'Drone CI',
        'cloudbuild.yaml': 'Google Cloud Build',
        'appveyor.yml': 'AppVeyor',
    }

    for pattern, name in ci_patterns.items():
        check_path = root / pattern
        if check_path.exists():
            cicd['detected'].append(name)
            if check_path.is_file():
                cicd['files'].append(pattern)
            elif check_path.is_dir():
                # List workflow files
                for f in check_path.glob('*.yml'):
                    cicd['files'].append(str(f.relative_to(root)))
                for f in check_path.glob('*.yaml'):
                    cicd['files'].append(str(f.relative_to(root)))

    return cicd


def analyze_env_files(root: Path) -> dict:
    """Analyze environment variable usage."""
    analysis = {
        'env_files': [],
        'env_vars': [],
    }

    # Check for .env files
    env_patterns = ['.env', '.env.example', '.env.local', '.env.development', '.env.production']
    for pattern in env_patterns:
        env_file = root / pattern
        if env_file.exists():
            analysis['env_files'].append(pattern)
            # Extract variable names from .env.example if exists
            if pattern == '.env.example':
                try:
                    content = env_file.read_text()
                    vars_found = re.findall(r'^([A-Z][A-Z0-9_]+)=', content, re.MULTILINE)
                    analysis['env_vars'] = vars_found[:20]  # Limit to 20
                except Exception:
                    pass

    return analysis


def analyze_code_samples(root: Path, language: str) -> dict:
    """Extract representative code samples for style analysis."""
    samples = {
        'import_style': None,
        'comment_style': None,
        'sample_files': [],
    }

    # Find representative files
    extensions = EXTENSIONS.get(language, set())
    if not extensions:
        return samples

    sample_files = []
    for ext in extensions:
        for path in root.rglob(f'*{ext}'):
            if not should_ignore(path.relative_to(root)):
                sample_files.append(path)
                if len(sample_files) >= 5:
                    break
        if len(sample_files) >= 5:
            break

    if not sample_files:
        return samples

    # Analyze first file for patterns
    try:
        content = sample_files[0].read_text(errors='ignore')[:5000]

        # Detect import style
        if language in ('typescript', 'javascript'):
            if "import type" in content:
                samples['import_style'] = 'type-imports-separate'
            elif "from '" in content:
                samples['import_style'] = 'single-quotes'
            elif 'from "' in content:
                samples['import_style'] = 'double-quotes'
        elif language == 'python':
            if 'from __future__' in content:
                samples['import_style'] = 'future-imports'

        # Detect comment style
        if language in ('typescript', 'javascript'):
            if '/**' in content and '@param' in content:
                samples['comment_style'] = 'jsdoc'
            elif '/**' in content:
                samples['comment_style'] = 'block-comments'
        elif language == 'python':
            if '"""' in content:
                if ':param' in content:
                    samples['comment_style'] = 'sphinx-docstring'
                elif 'Args:' in content:
                    samples['comment_style'] = 'google-docstring'
                else:
                    samples['comment_style'] = 'docstring'

        samples['sample_files'] = [str(f.relative_to(root)) for f in sample_files[:3]]
    except Exception:
        pass

    return samples


def extract_naming_conventions(root: Path) -> dict:
    """Extract naming conventions from the codebase."""
    conventions = {
        'files': {
            'patterns': [],
            'examples': []
        },
        'directories': {
            'patterns': [],
            'examples': []
        }
    }

    file_names = []
    dir_names = set()

    for path in root.rglob('*'):
        if should_ignore(path.relative_to(root)):
            continue
        if path.is_file():
            file_names.append(path.stem)
        elif path.is_dir():
            dir_names.add(path.name)

    # Analyze file naming patterns
    patterns = {
        'kebab-case': re.compile(r'^[a-z]+(-[a-z]+)+$'),
        'camelCase': re.compile(r'^[a-z]+([A-Z][a-z]+)+$'),
        'PascalCase': re.compile(r'^[A-Z][a-z]+([A-Z][a-z]+)*$'),
        'snake_case': re.compile(r'^[a-z]+(_[a-z]+)+$'),
    }

    pattern_counts = Counter()
    for name in file_names[:200]:  # Sample first 200
        for pattern_name, regex in patterns.items():
            if regex.match(name):
                pattern_counts[pattern_name] += 1
                break

    if pattern_counts:
        most_common = pattern_counts.most_common(2)
        conventions['files']['patterns'] = [p[0] for p in most_common]

    return conventions


def generate_report(root: Path) -> dict:
    """Generate a complete analysis report."""
    report = {
        'path': str(root.absolute()),
        'structure': analyze_directory_structure(root),
        'files': analyze_files(root),
        'naming': extract_naming_conventions(root),
        'git': analyze_git(root),
        'env': analyze_env_files(root),
        'sensitive': analyze_sensitive_files(root),
        'gitignore': analyze_gitignore(root),
        'cicd': analyze_cicd(root),
    }

    # Add language-specific analysis
    if (root / 'package.json').exists():
        report['nodejs'] = analyze_package_json(root)

    if (root / 'pyproject.toml').exists():
        report['python'] = analyze_pyproject(root)

    # Determine primary language and analyze code samples
    if report['files']['by_language']:
        primary = max(report['files']['by_language'].items(), key=lambda x: x[1])
        report['primary_language'] = primary[0]
        report['code_samples'] = analyze_code_samples(root, primary[0])

    # Generate recommendations
    report['recommendations'] = generate_recommendations(report)

    return report


def generate_recommendations(report: dict) -> dict:
    """Generate AI-ready configuration recommendations based on analysis."""
    recs = {
        'priority': [],  # Must-have configs
        'suggested': [],  # Nice-to-have configs
        'hooks': [],  # Recommended hooks
    }

    # Always recommend CLAUDE.md
    recs['priority'].append({
        'config': 'CLAUDE.md',
        'reason': 'Essential for project-wide coding standards'
    })

    # Check if rules are needed
    langs = report['files'].get('by_language', {})
    if len([l for l in langs if langs[l] > 10 and l != 'other']) > 1:
        recs['priority'].append({
            'config': '.claude/rules/',
            'reason': 'Multi-language project needs language-specific rules'
        })

    # Check if skills are needed based on frameworks
    frameworks = []
    if report.get('nodejs', {}).get('frameworks'):
        frameworks.extend(report['nodejs']['frameworks'])
    if report.get('python', {}).get('frameworks'):
        frameworks.extend(report['python']['frameworks'])

    if any(fw in ['Prisma ORM', 'Drizzle ORM', 'TypeORM', 'SQLAlchemy'] for fw in frameworks):
        recs['suggested'].append({
            'config': '.claude/skills/database/',
            'reason': 'ORM detected - document query patterns and migrations'
        })

    if any(fw in ['Express.js', 'Fastify', 'NestJS', 'FastAPI', 'Django', 'Flask'] for fw in frameworks):
        recs['suggested'].append({
            'config': '.claude/skills/api/',
            'reason': 'Web framework detected - document API patterns'
        })

    # Check for test framework
    test_files = report['files'].get('test_files', 0)
    if test_files > 5:
        recs['suggested'].append({
            'config': '.claude/commands/test.md',
            'reason': f'{test_files} test files detected - create test command'
        })

    # Recommend hooks based on tools
    tools = [c.get('tool') for c in report['files'].get('tool_configs', [])]
    if 'prettier' in tools or 'eslint' in tools:
        recs['hooks'].append({
            'hook': 'PostToolUse format',
            'reason': 'Auto-format on file edit'
        })
    if 'black' in tools or 'ruff' in tools:
        recs['hooks'].append({
            'hook': 'PostToolUse format',
            'reason': 'Python auto-format on file edit'
        })

    # Git workflow recommendation
    if report.get('git', {}).get('commit_patterns'):
        patterns = report['git']['commit_patterns']
        if 'conventional-commits' in patterns:
            recs['suggested'].append({
                'config': '.claude/commands/commit.md',
                'reason': 'Conventional commits detected - enforce format'
            })

    return recs


def format_markdown(report: dict) -> str:
    """Format report as markdown."""
    lines = [
        "# Codebase Analysis Report",
        "",
        f"**Path:** `{report['path']}`",
        "",
        "## Summary",
        "",
        f"- **Total Files:** {report['files']['total_files']}",
        f"- **Test Files:** {report['files']['test_files']}",
        f"- **Primary Language:** {report.get('primary_language', 'unknown')}",
        "",
        "## Languages",
        "",
    ]

    for lang, count in report['files']['by_language'].items():
        lines.append(f"- {lang}: {count} files")

    lines.extend([
        "",
        "## Directory Structure",
        "",
        "### Root Directories",
        "",
    ])

    for dir_name in report['structure']['root_dirs']:
        lines.append(f"- `{dir_name}/`")

    if report['structure']['patterns']:
        lines.extend([
            "",
            "### Detected Patterns",
            "",
        ])
        for pattern in report['structure']['patterns']:
            lines.append(f"- `{pattern['dir']}/` - {pattern['purpose']}")

    if report['files']['tool_configs']:
        lines.extend([
            "",
            "## Development Tools",
            "",
        ])
        for config in report['files']['tool_configs']:
            lines.append(f"- {config['tool']} (`{config['file']}`)")

    if report.get('nodejs'):
        lines.extend([
            "",
            "## Node.js Project",
            "",
            f"**Name:** {report['nodejs']['name']}",
            "",
            "### Scripts",
            "",
        ])
        for script, cmd in report['nodejs']['scripts'].items():
            lines.append(f"- `{script}`: `{cmd}`")

        if report['nodejs']['frameworks']:
            lines.extend([
                "",
                "### Frameworks & Libraries",
                "",
            ])
            for fw in report['nodejs']['frameworks']:
                lines.append(f"- {fw}")

    if report.get('python'):
        lines.extend([
            "",
            "## Python Project",
            "",
        ])
        if report['python'].get('tools'):
            lines.append("### Tools")
            for tool in report['python']['tools']:
                lines.append(f"- {tool}")
        if report['python'].get('frameworks'):
            lines.append("")
            lines.append("### Frameworks")
            for fw in report['python']['frameworks']:
                lines.append(f"- {fw}")

    if report.get('git'):
        lines.extend([
            "",
            "## Git Configuration",
            "",
        ])
        if report['git'].get('hooks'):
            lines.append("### Hooks")
            for hook in report['git']['hooks']:
                lines.append(f"- {hook}")
        if report['git'].get('commit_patterns'):
            lines.append("")
            lines.append("### Commit Patterns Detected")
            for pattern in report['git']['commit_patterns']:
                lines.append(f"- {pattern}")

    if report.get('env', {}).get('env_files'):
        lines.extend([
            "",
            "## Environment Files",
            "",
        ])
        for env_file in report['env']['env_files']:
            lines.append(f"- `{env_file}`")
        if report['env'].get('env_vars'):
            lines.append("")
            lines.append("### Environment Variables")
            for var in report['env']['env_vars'][:10]:
                lines.append(f"- `{var}`")

    if report.get('code_samples'):
        samples = report['code_samples']
        if samples.get('import_style') or samples.get('comment_style'):
            lines.extend([
                "",
                "## Code Style Detected",
                "",
            ])
            if samples.get('import_style'):
                lines.append(f"- **Import style:** {samples['import_style']}")
            if samples.get('comment_style'):
                lines.append(f"- **Comment style:** {samples['comment_style']}")
            if samples.get('sample_files'):
                lines.append("")
                lines.append("**Sample files for reference:**")
                for f in samples['sample_files']:
                    lines.append(f"- `{f}`")

    # CI/CD section
    if report.get('cicd', {}).get('detected'):
        lines.extend([
            "",
            "## CI/CD",
            "",
        ])
        for ci in report['cicd']['detected']:
            lines.append(f"- {ci}")
        if report['cicd'].get('files'):
            lines.append("")
            lines.append("**Config files:**")
            for f in report['cicd']['files'][:5]:
                lines.append(f"- `{f}`")

    # Security section
    if report.get('sensitive', {}).get('found'):
        lines.extend([
            "",
            "## Security Warning",
            "",
            "**Sensitive files detected** - Add to .claudeignore:",
            "",
        ])
        for f in report['sensitive']['found'][:10]:
            lines.append(f"- `{f}`")

        if report['sensitive'].get('claudeignore_suggestions'):
            lines.extend([
                "",
                "**Suggested .claudeignore:**",
                "```",
            ])
            for pattern in report['sensitive']['claudeignore_suggestions']:
                lines.append(pattern)
            lines.append("```")

    # Recommendations section
    if report.get('recommendations'):
        recs = report['recommendations']
        lines.extend([
            "",
            "---",
            "",
            "## AI-Ready Configuration Recommendations",
            "",
        ])

        if recs.get('priority'):
            lines.append("### Priority (Required)")
            for rec in recs['priority']:
                lines.append(f"- **{rec['config']}** - {rec['reason']}")
            lines.append("")

        if recs.get('suggested'):
            lines.append("### Suggested")
            for rec in recs['suggested']:
                lines.append(f"- **{rec['config']}** - {rec['reason']}")
            lines.append("")

        if recs.get('hooks'):
            lines.append("### Hooks to Configure")
            for rec in recs['hooks']:
                lines.append(f"- **{rec['hook']}** - {rec['reason']}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Analyze a codebase for AI-ready conversion')
    parser.add_argument('path', nargs='?', default='.', help='Path to analyze (default: current directory)')
    parser.add_argument('--output', '-o', choices=['json', 'markdown'], default='markdown',
                        help='Output format (default: markdown)')

    args = parser.parse_args()
    root = Path(args.path).resolve()

    if not root.exists():
        print(f"Error: Path does not exist: {root}")
        return 1

    report = generate_report(root)

    if args.output == 'json':
        print(json.dumps(report, indent=2))
    else:
        print(format_markdown(report))

    return 0


if __name__ == '__main__':
    exit(main())
