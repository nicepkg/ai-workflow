#!/bin/bash

# Content Brief Validation Script
# Checks content brief completeness and quality

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if file provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <brief_file.md>"
    exit 1
fi

BRIEF_FILE="$1"

# Check if file exists
if [ ! -f "$BRIEF_FILE" ]; then
    echo -e "${RED}✗ Error: File not found: $BRIEF_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Content Brief Validation Report           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "File: ${BLUE}$BRIEF_FILE${NC}"
echo ""

# Counters
ISSUES_FOUND=0
WARNINGS=0
CHECKS_PASSED=0

# Function to check section exists
check_section() {
    local section_name="$1"
    local section_pattern="$2"
    local required="$3"

    if grep -q "$section_pattern" "$BRIEF_FILE"; then
        echo -e "${GREEN}✓${NC} $section_name section found"
        ((CHECKS_PASSED++))
        return 0
    else
        if [ "$required" = "true" ]; then
            echo -e "${RED}✗${NC} $section_name section missing (REQUIRED)"
            ((ISSUES_FOUND++))
        else
            echo -e "${YELLOW}⚠${NC} $section_name section missing (recommended)"
            ((WARNINGS++))
        fi
        return 1
    fi
}

echo -e "${BLUE}━━━ Required Sections ━━━${NC}"
echo ""

# Check required sections
check_section "Overview" "##.*Overview" true
check_section "Audience" "##.*Audience" true
check_section "SEO Strategy" "##.*SEO.*Strategy\|##.*SEO\|##.*Keywords" true
check_section "Content Structure" "##.*Content Structure\|##.*Structure\|##.*Outline" true
check_section "Success Metrics" "##.*Success Metrics\|##.*Metrics" true

echo ""
echo -e "${BLUE}━━━ Recommended Sections ━━━${NC}"
echo ""

# Check recommended sections
check_section "Tone & Voice" "##.*Tone.*Voice\|##.*Voice\|##.*Writing Style" false
check_section "Visual & Media" "##.*Visual\|##.*Media\|##.*Images" false
check_section "Research & Sources" "##.*Research\|##.*Sources" false
check_section "CTAs" "##.*CTA\|##.*Call.*Action" false
check_section "Timeline" "##.*Timeline\|##.*Workflow" false

echo ""
echo -e "${BLUE}━━━ Content Quality Checks ━━━${NC}"
echo ""

# Check for placeholder text
if grep -q "\[.*\]\|TBD" "$BRIEF_FILE"; then
    PLACEHOLDER_COUNT=$(grep -c "\[.*\]\|TBD" "$BRIEF_FILE")
    echo -e "${YELLOW}⚠${NC} Contains $PLACEHOLDER_COUNT placeholder(s) - fill in all details"
    ((WARNINGS++))
else
    echo -e "${GREEN}✓${NC} No placeholders remaining"
    ((CHECKS_PASSED++))
fi

# Check for primary keyword
if grep -qi "Primary Keyword" "$BRIEF_FILE"; then
    if grep -A 1 "Primary Keyword" "$BRIEF_FILE" | grep -qv "TBD\|^\s*$"; then
        echo -e "${GREEN}✓${NC} Primary keyword specified"
        ((CHECKS_PASSED++))
    else
        echo -e "${RED}✗${NC} Primary keyword not specified"
        ((ISSUES_FOUND++))
    fi
else
    echo -e "${RED}✗${NC} Primary keyword section missing"
    ((ISSUES_FOUND++))
fi

# Check for target audience
if grep -qi "Target Audience\|Primary Audience" "$BRIEF_FILE"; then
    if grep -A 2 "Target Audience\|Primary Audience" "$BRIEF_FILE" | grep -qv "TBD\|^\s*$"; then
        echo -e "${GREEN}✓${NC} Target audience defined"
        ((CHECKS_PASSED++))
    else
        echo -e "${RED}✗${NC} Target audience not defined"
        ((ISSUES_FOUND++))
    fi
else
    echo -e "${RED}✗${NC} Target audience section missing"
    ((ISSUES_FOUND++))
fi

# Check for word count
if grep -qi "Word Count" "$BRIEF_FILE"; then
    if grep "Word Count" "$BRIEF_FILE" | grep -qv "TBD"; then
        echo -e "${GREEN}✓${NC} Word count specified"
        ((CHECKS_PASSED++))
    else
        echo -e "${YELLOW}⚠${NC} Word count not specified"
        ((WARNINGS++))
    fi
else
    echo -e "${YELLOW}⚠${NC} Word count not mentioned"
    ((WARNINGS++))
fi

# Check for content structure/outline
if grep -qi "Outline\|Key Sections\|Structure" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Content structure provided"
    ((CHECKS_PASSED++))
else
    echo -e "${RED}✗${NC} Content structure/outline missing"
    ((ISSUES_FOUND++))
fi

echo ""
echo -e "${BLUE}━━━ SEO Checks ━━━${NC}"
echo ""

# Check for keyword strategy
KEYWORD_SCORE=0

if grep -qi "Primary Keyword" "$BRIEF_FILE"; then
    if grep -A 1 "Primary Keyword" "$BRIEF_FILE" | grep -qv "TBD\|^\s*$"; then
        ((KEYWORD_SCORE++))
    fi
fi

if grep -qi "Secondary Keyword" "$BRIEF_FILE"; then
    ((KEYWORD_SCORE++))
fi

if grep -qi "Search Intent" "$BRIEF_FILE"; then
    ((KEYWORD_SCORE++))
fi

if [ $KEYWORD_SCORE -eq 3 ]; then
    echo -e "${GREEN}✓${NC} Complete keyword strategy defined"
    ((CHECKS_PASSED++))
elif [ $KEYWORD_SCORE -eq 2 ]; then
    echo -e "${YELLOW}⚠${NC} Partial keyword strategy (add more details)"
    ((WARNINGS++))
elif [ $KEYWORD_SCORE -eq 1 ]; then
    echo -e "${YELLOW}⚠${NC} Minimal keyword strategy (needs expansion)"
    ((WARNINGS++))
else
    echo -e "${RED}✗${NC} No keyword strategy defined"
    ((ISSUES_FOUND++))
fi

# Check for meta description
if grep -qi "Meta Description" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Meta description section included"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Meta description not mentioned"
    ((WARNINGS++))
fi

# Check for internal links
if grep -qi "Internal Link" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Internal linking strategy mentioned"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Internal linking not addressed"
    ((WARNINGS++))
fi

echo ""
echo -e "${BLUE}━━━ Content-Specific Checks ━━━${NC}"
echo ""

# Check for tone/voice
if grep -qi "Tone\|Voice\|Writing Style" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Tone and voice specified"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Tone and voice not specified"
    ((WARNINGS++))
fi

# Check for CTAs
if grep -qi "CTA\|Call.*Action" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Call-to-action defined"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} No call-to-action specified"
    ((WARNINGS++))
fi

# Check for success metrics
if grep -qi "Success Metric\|Primary Metric" "$BRIEF_FILE"; then
    if grep -A 3 "Success Metric\|Primary Metric" "$BRIEF_FILE" | grep -qv "TBD"; then
        echo -e "${GREEN}✓${NC} Success metrics defined"
        ((CHECKS_PASSED++))
    else
        echo -e "${RED}✗${NC} Success metrics not defined"
        ((ISSUES_FOUND++))
    fi
else
    echo -e "${RED}✗${NC} Success metrics section missing"
    ((ISSUES_FOUND++))
fi

# Check for target audience pain points/problem
if grep -qi "Problem\|Pain Point" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Audience problem/pain points addressed"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Audience problem/pain points not explicitly stated"
    ((WARNINGS++))
fi

# Check for research requirements
if grep -qi "Research\|Source" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Research requirements mentioned"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Research requirements not specified"
    ((WARNINGS++))
fi

# Check for visual/media requirements
if grep -qi "Image\|Visual\|Media\|Screenshot" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Visual/media requirements included"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Visual/media requirements not specified"
    ((WARNINGS++))
fi

# Document quality
echo ""
echo -e "${BLUE}━━━ Document Quality ━━━${NC}"
echo ""

# Check word count
WORD_COUNT=$(wc -w < "$BRIEF_FILE")
echo -e "Brief word count: $WORD_COUNT"

if [ "$WORD_COUNT" -lt 200 ]; then
    echo -e "${RED}✗${NC} Brief is too short (< 200 words) - needs more detail"
    ((ISSUES_FOUND++))
elif [ "$WORD_COUNT" -lt 400 ]; then
    echo -e "${YELLOW}⚠${NC} Brief is short (< 400 words) - consider adding more detail"
    ((WARNINGS++))
elif [ "$WORD_COUNT" -gt 2000 ]; then
    echo -e "${YELLOW}⚠${NC} Brief is very long (> 2000 words) - ensure it's scannable"
    ((WARNINGS++))
else
    echo -e "${GREEN}✓${NC} Brief length appropriate"
    ((CHECKS_PASSED++))
fi

# Check for proper heading structure
if grep -q "^#\s" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Proper heading structure"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Check heading hierarchy (should start with # not ##)"
    ((WARNINGS++))
fi

# Check for content type
if grep -qi "Content Type" "$BRIEF_FILE"; then
    echo -e "${GREEN}✓${NC} Content type specified"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Content type not specified"
    ((WARNINGS++))
fi

# Final Summary
echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║           Validation Summary                   ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Checks passed:  ${GREEN}$CHECKS_PASSED${NC}"
echo -e "Warnings:       ${YELLOW}$WARNINGS${NC}"
echo -e "Issues found:   ${RED}$ISSUES_FOUND${NC}"
echo ""

# Calculate completeness score
TOTAL_CHECKS=$((CHECKS_PASSED + WARNINGS + ISSUES_FOUND))
if [ $TOTAL_CHECKS -gt 0 ]; then
    COMPLETENESS=$((CHECKS_PASSED * 100 / TOTAL_CHECKS))
    echo -e "Completeness: ${BLUE}${COMPLETENESS}%${NC}"
    echo ""
fi

# Recommendations
echo -e "${BLUE}━━━ Key Recommendations ━━━${NC}"
echo ""
echo "1. Fill in all TBD placeholders with specific information"
echo "2. Ensure primary keyword and SEO strategy are complete"
echo "3. Define clear, measurable success metrics"
echo "4. Specify tone, voice, and writing style guidelines"
echo "5. Include research sources and competitor analysis"
echo "6. Add visual/media requirements with specifications"
echo "7. Define clear CTAs aligned with content goals"
echo "8. Review with stakeholders before writer begins"
echo ""

# Priority issues
if [ "$ISSUES_FOUND" -gt 0 ]; then
    echo -e "${RED}⚠ Critical Issues to Address:${NC}"
    if ! grep -qi "Primary Keyword" "$BRIEF_FILE" || grep -A 1 "Primary Keyword" "$BRIEF_FILE" | grep -q "TBD"; then
        echo "   • Define primary keyword for SEO"
    fi
    if ! grep -qi "Target Audience\|Primary Audience" "$BRIEF_FILE" || grep -A 2 "Target Audience\|Primary Audience" "$BRIEF_FILE" | grep -q "TBD"; then
        echo "   • Specify target audience clearly"
    fi
    if ! grep -qi "Success Metric" "$BRIEF_FILE" || grep -A 3 "Success Metric" "$BRIEF_FILE" | grep -q "TBD"; then
        echo "   • Define success metrics and targets"
    fi
    if ! grep -qi "Outline\|Key Sections\|Structure" "$BRIEF_FILE"; then
        echo "   • Add content structure or outline"
    fi
    if [ "$WORD_COUNT" -lt 200 ]; then
        echo "   • Add more detail to brief (currently too short)"
    fi
    echo ""
fi

# Exit code
if [ "$ISSUES_FOUND" -gt 0 ]; then
    echo -e "${RED}❌ Content brief validation failed${NC}"
    echo -e "   Address $ISSUES_FOUND critical issue(s) before proceeding"
    exit 1
elif [ "$WARNINGS" -gt 3 ]; then
    echo -e "${YELLOW}⚠ Content brief validation passed with warnings${NC}"
    echo -e "   Consider addressing $WARNINGS warning(s) to improve quality"
    exit 0
else
    echo -e "${GREEN}✅ Content brief validation passed!${NC}"
    echo -e "   Brief looks ready for writer to begin"
    exit 0
fi
