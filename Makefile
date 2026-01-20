# AI Workflow - Skill Management
#
# Usage:
#   make list                                    # List all workflows and skills
#   make update-skill W=content-creator S=docx  # Update single skill
#   make update-workflow W=content-creator      # Update all skills in workflow
#   make update-all                             # Update all workflows
#   make dry-run W=content-creator              # Preview what would be updated
#
# Variables:
#   W = workflow name (e.g., content-creator, marketing-pro)
#   S = skill name (e.g., docx, canvas-design)

.PHONY: help list update-skill update-workflow update-all dry-run clean validate validate-fast crawl-claude-docs merge-claude-docs

PYTHON := python3
SCRIPTS_DIR := scripts
UPDATE_SCRIPT := $(SCRIPTS_DIR)/update_skills.py
VALIDATE_SCRIPT := $(SCRIPTS_DIR)/validate_sources.py

# Default target
help:
	@echo "AI Workflow - Skill Management"
	@echo ""
	@echo "Usage:"
	@echo "  make list                                    # List all workflows and skills"
	@echo "  make validate                               # Validate all skill sources"
	@echo "  make validate-fast                          # Fast validation (repos only)"
	@echo "  make validate W=<workflow>                  # Validate one workflow"
	@echo "  make update-skill W=<workflow> S=<skill>    # Update single skill"
	@echo "  make update-workflow W=<workflow>           # Update all skills in workflow"
	@echo "  make update-all                             # Update all workflows"
	@echo "  make dry-run W=<workflow>                   # Preview what would be updated"
	@echo ""
	@echo "Examples:"
	@echo "  make validate"
	@echo "  make validate W=content-creator"
	@echo "  make update-skill W=content-creator S=docx"
	@echo "  make update-workflow W=marketing-pro"
	@echo "  make update-all"
	@echo ""
	@echo "Available workflows:"
	@ls -d workflows/*-workflow 2>/dev/null | sed 's#workflows/##' | sed 's/-workflow//' | sed 's/^/  - /'

# List all workflows and their skills
list:
	@$(PYTHON) $(UPDATE_SCRIPT) --list

# Update a single skill in a workflow
# Usage: make update-skill W=content-creator S=docx
update-skill:
ifndef W
	$(error W is not set. Usage: make update-skill W=<workflow> S=<skill>)
endif
ifndef S
	$(error S is not set. Usage: make update-skill W=<workflow> S=<skill>)
endif
	@echo "Updating skill '$(S)' in workflow '$(W)'..."
	@$(PYTHON) $(UPDATE_SCRIPT) --workflow $(W) --skill $(S)

# Update all skills in a workflow
# Usage: make update-workflow W=content-creator
update-workflow:
ifndef W
	$(error W is not set. Usage: make update-workflow W=<workflow>)
endif
	@echo "Updating all skills in workflow '$(W)'..."
	@$(PYTHON) $(UPDATE_SCRIPT) --workflow $(W) --all

# Update all skills in all workflows
update-all:
	@echo "Updating all workflows..."
	@$(PYTHON) $(UPDATE_SCRIPT) --all-workflows

# Dry run - show what would be updated
# Usage: make dry-run W=content-creator
dry-run:
ifndef W
	$(error W is not set. Usage: make dry-run W=<workflow>)
endif
	@echo "Dry run for workflow '$(W)'..."
	@$(PYTHON) $(UPDATE_SCRIPT) --workflow $(W) --all --dry-run

# Dry run for all workflows
dry-run-all:
	@echo "Dry run for all workflows..."
	@$(PYTHON) $(UPDATE_SCRIPT) --all-workflows --dry-run

# Shortcuts for common workflows
update-content-creator:
	@$(MAKE) update-workflow W=content-creator

update-marketing-pro:
	@$(MAKE) update-workflow W=marketing-pro

update-video-creator:
	@$(MAKE) update-workflow W=video-creator

update-stock-trader:
	@$(MAKE) update-workflow W=stock-trader

update-product-manager:
	@$(MAKE) update-workflow W=product-manager

update-slidev:
	@$(MAKE) update-workflow W=talk-to-slidev

# Validate all skill sources
# Usage: make validate [W=<workflow>]
validate:
ifdef W
	@echo "Validating workflow '$(W)'..."
	@$(PYTHON) $(VALIDATE_SCRIPT) --workflow $(W) --verbose
else
	@echo "Validating all workflows..."
	@$(PYTHON) $(VALIDATE_SCRIPT) --verbose
endif

# Fast validation (repos only, skip path checks)
validate-fast:
ifdef W
	@echo "Fast validating workflow '$(W)'..."
	@$(PYTHON) $(VALIDATE_SCRIPT) --workflow $(W) --no-paths --verbose
else
	@echo "Fast validating all workflows..."
	@$(PYTHON) $(VALIDATE_SCRIPT) --no-paths --verbose
endif

# Validate and output as JSON
validate-json:
	@$(PYTHON) $(VALIDATE_SCRIPT) --json

# Clean __pycache__ directories
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned __pycache__ directories"

# Crawl Claude Code documentation
crawl-claude-docs:
	@echo "Crawling Claude Code documentation..."
	@cd claude-code-docs && uv run --with requests --with beautifulsoup4 --with markdownify python crawl_docs.py

# Merge Claude Code docs into single file for LLMs
merge-claude-docs:
	@echo "Merging Claude Code documentation..."
	@cd claude-code-docs && { \
		echo "# Claude Code Documentation"; \
		echo ""; \
		echo "Source: https://code.claude.com/docs"; \
		echo "Generated: $$(date -u +%Y-%m-%dT%H:%M:%SZ)"; \
		echo ""; \
		echo "---"; \
		echo ""; \
		for f in docs/*.md; do \
			[ -f "$$f" ] && [ "$$(basename $$f)" != "INDEX.md" ] && { \
				cat "$$f"; \
				echo ""; \
				echo "---"; \
				echo ""; \
			}; \
		done; \
	} > claude-code-llms.txt
	@echo "Created claude-code-docs/claude-code-llms.txt"
