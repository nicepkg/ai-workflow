#!/bin/bash

# Content Brief Generation Script
# Interactive workflow for creating comprehensive content briefs

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# Header
echo -e "${BLUE}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║       Content Brief Generator                    ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════╝${NC}"
echo ""

# Helper function for prompts
prompt_input() {
    local prompt_text="$1"
    local var_name="$2"
    local required="$3"

    while true; do
        echo -e "${CYAN}${prompt_text}${NC}"
        read -r input

        if [ -n "$input" ]; then
            eval "$var_name=\"$input\""
            break
        elif [ "$required" != "true" ]; then
            eval "$var_name=\"\""
            break
        else
            echo -e "${RED}This field is required.${NC}"
        fi
    done
}

prompt_multiline() {
    local prompt_text="$1"
    local var_name="$2"

    echo -e "${CYAN}${prompt_text}${NC}"
    echo -e "${YELLOW}(Type your response, press Enter twice when done)${NC}"

    local input=""
    local line
    local empty_count=0

    while true; do
        read -r line
        if [ -z "$line" ]; then
            ((empty_count++))
            if [ $empty_count -ge 2 ]; then
                break
            fi
            input="${input}\n"
        else
            empty_count=0
            if [ -n "$input" ]; then
                input="${input}\n${line}"
            else
                input="${line}"
            fi
        fi
    done

    eval "$var_name=\"$input\""
}

# Step 1: Content Type and Basics
echo -e "${MAGENTA}━━━ Step 1: Content Basics ━━━${NC}"
echo ""

echo "Select content type:"
echo "1) Blog Post / Article"
echo "2) Technical Documentation"
echo "3) Landing Page"
echo "4) Case Study"
echo "5) Social Media"
echo "6) Email Campaign"
echo "7) Video Script"
echo "8) Whitepaper / Report"
echo "9) Product Description"
echo ""

prompt_input "Enter number (1-9):" CONTENT_TYPE_NUM true

case $CONTENT_TYPE_NUM in
    1) CONTENT_TYPE="Blog Post / Article" ;;
    2) CONTENT_TYPE="Technical Documentation" ;;
    3) CONTENT_TYPE="Landing Page" ;;
    4) CONTENT_TYPE="Case Study" ;;
    5) CONTENT_TYPE="Social Media" ;;
    6) CONTENT_TYPE="Email Campaign" ;;
    7) CONTENT_TYPE="Video Script" ;;
    8) CONTENT_TYPE="Whitepaper / Report" ;;
    9) CONTENT_TYPE="Product Description" ;;
    *) CONTENT_TYPE="Blog Post / Article" ;;
esac

echo ""
prompt_input "Working title or topic:" TITLE true
prompt_input "Target word count (or duration for video):" WORD_COUNT false
prompt_input "Target publication date (YYYY-MM-DD):" PUB_DATE false

# Step 2: Audience and Goals
echo ""
echo -e "${MAGENTA}━━━ Step 2: Audience & Goals ━━━${NC}"
echo ""

prompt_input "Primary target audience (e.g., 'Junior developers', 'Marketing managers'):" AUDIENCE true
prompt_input "Reader's knowledge level (Beginner/Intermediate/Advanced):" KNOWLEDGE_LEVEL false
prompt_multiline "What problem or question does this content solve for them?" PROBLEM

echo ""
echo "Primary content goal:"
echo "1) Educate / Inform"
echo "2) Convert / Generate leads"
echo "3) Entertain / Engage"
echo "4) Support / Help"
echo "5) Build authority / Thought leadership"
echo ""

prompt_input "Enter number (1-5):" GOAL_NUM true

case $GOAL_NUM in
    1) PRIMARY_GOAL="Educate / Inform" ;;
    2) PRIMARY_GOAL="Convert / Generate leads" ;;
    3) PRIMARY_GOAL="Entertain / Engage" ;;
    4) PRIMARY_GOAL="Support / Help" ;;
    5) PRIMARY_GOAL="Build authority / Thought leadership" ;;
    *) PRIMARY_GOAL="Educate / Inform" ;;
esac

prompt_input "Key takeaway (what should readers remember):" KEY_TAKEAWAY true

# Step 3: SEO & Keywords
echo ""
echo -e "${MAGENTA}━━━ Step 3: SEO Strategy ━━━${NC}"
echo ""

prompt_input "Primary keyword:" PRIMARY_KEYWORD true
prompt_input "Secondary keywords (comma-separated):" SECONDARY_KEYWORDS false
prompt_input "Search intent (Informational/Commercial/Transactional/Navigational):" SEARCH_INTENT false
prompt_input "Target search volume (if known):" SEARCH_VOLUME false

# Step 4: Structure and Content
echo ""
echo -e "${MAGENTA}━━━ Step 4: Content Structure ━━━${NC}"
echo ""

echo "Content structure framework:"
echo "1) AIDA (Attention, Interest, Desire, Action)"
echo "2) PAS (Problem, Agitate, Solve)"
echo "3) Inverted Pyramid (Most important first)"
echo "4) Storytelling Arc (Setup, Conflict, Resolution)"
echo "5) How-to / Tutorial"
echo "6) Listicle"
echo "7) Custom"
echo ""

prompt_input "Enter number (1-7):" FRAMEWORK_NUM false

case $FRAMEWORK_NUM in
    1) FRAMEWORK="AIDA (Attention, Interest, Desire, Action)" ;;
    2) FRAMEWORK="PAS (Problem, Agitate, Solve)" ;;
    3) FRAMEWORK="Inverted Pyramid" ;;
    4) FRAMEWORK="Storytelling Arc" ;;
    5) FRAMEWORK="How-to / Tutorial" ;;
    6) FRAMEWORK="Listicle" ;;
    7) FRAMEWORK="Custom" ;;
    *) FRAMEWORK="Custom" ;;
esac

prompt_multiline "Key sections or outline (one per line):" KEY_SECTIONS

prompt_input "Number of examples/case studies to include:" NUM_EXAMPLES false
prompt_input "Data/statistics required (Yes/No):" NEEDS_DATA false
prompt_input "Code examples needed (Yes/No - for technical content):" NEEDS_CODE false

# Step 5: Tone, Voice, and Style
echo ""
echo -e "${MAGENTA}━━━ Step 5: Tone & Voice ━━━${NC}"
echo ""

echo "Tone:"
echo "1) Professional and formal"
echo "2) Professional but conversational"
echo "3) Casual and friendly"
echo "4) Technical and authoritative"
echo "5) Playful and creative"
echo ""

prompt_input "Enter number (1-5):" TONE_NUM false

case $TONE_NUM in
    1) TONE="Professional and formal" ;;
    2) TONE="Professional but conversational" ;;
    3) TONE="Casual and friendly" ;;
    4) TONE="Technical and authoritative" ;;
    5) TONE="Playful and creative" ;;
    *) TONE="Professional but conversational" ;;
esac

prompt_input "Point of view (1st person 'we', 2nd person 'you', 3rd person):" POV false
prompt_input "Specific style notes or voice attributes:" STYLE_NOTES false

# Step 6: Media and Visuals
echo ""
echo -e "${MAGENTA}━━━ Step 6: Visuals & Media ━━━${NC}"
echo ""

prompt_input "Number of images needed:" NUM_IMAGES false
prompt_input "Hero image requirements:" HERO_IMAGE false
prompt_input "Screenshots or diagrams needed (describe):" SCREENSHOTS false
prompt_input "Video or embedded media (describe):" VIDEO_NEEDS false

# Step 7: CTAs and Conversion
echo ""
echo -e "${MAGENTA}━━━ Step 7: CTAs & Conversion ━━━${NC}"
echo ""

prompt_input "Primary call-to-action:" PRIMARY_CTA false
prompt_input "Secondary CTA (if any):" SECONDARY_CTA false
prompt_input "Conversion goal (e.g., 'Sign up', 'Download', 'Contact sales'):" CONVERSION_GOAL false

# Step 8: Research and References
echo ""
echo -e "${MAGENTA}━━━ Step 8: Research Requirements ━━━${NC}"
echo ""

prompt_input "Competitor content to reference (URLs, comma-separated):" COMPETITOR_URLS false
prompt_input "SME interviews required (Yes/No):" NEEDS_SME false
prompt_input "Primary sources or research needed:" RESEARCH_SOURCES false

# Step 9: Success Metrics
echo ""
echo -e "${MAGENTA}━━━ Step 9: Success Metrics ━━━${NC}"
echo ""

prompt_input "Primary success metric (e.g., 'Organic traffic', 'Conversions'):" PRIMARY_METRIC true
prompt_input "Secondary metrics (comma-separated):" SECONDARY_METRICS false
prompt_input "Target goal for primary metric:" METRIC_TARGET false

# Step 10: Additional Details
echo ""
echo -e "${MAGENTA}━━━ Step 10: Additional Details ━━━${NC}"
echo ""

prompt_input "Internal links to include (comma-separated URLs/pages):" INTERNAL_LINKS false
prompt_input "External links to include:" EXTERNAL_LINKS false
prompt_input "Legal or compliance requirements:" COMPLIANCE false
prompt_multiline "Any other special requirements or notes:" SPECIAL_NOTES

# Generate filename
FILENAME="${TITLE// /_}"
FILENAME="${FILENAME//[^a-zA-Z0-9_-]/}"
FILENAME="$(echo "$FILENAME" | tr '[:upper:]' '[:lower:]')"
FILENAME="content_brief_${FILENAME}.md"

# Output directory
OUTPUT_DIR="."
if [ ! -z "$1" ]; then
    OUTPUT_DIR="$1"
fi

OUTPUT_FILE="$OUTPUT_DIR/$FILENAME"

# Generate the brief
echo ""
echo -e "${BLUE}Generating content brief...${NC}"
echo ""

cat > "$OUTPUT_FILE" << EOF
# Content Brief: ${TITLE}

**Content Type:** ${CONTENT_TYPE}
**Target Word Count:** ${WORD_COUNT:-TBD}
**Target Publication Date:** ${PUB_DATE:-TBD}
**Status:** Draft
**Created:** $(date +%Y-%m-%d)

---

## Overview

### Key Information
- **Primary Goal:** ${PRIMARY_GOAL}
- **Target Audience:** ${AUDIENCE}
- **Knowledge Level:** ${KNOWLEDGE_LEVEL:-General}
- **Key Takeaway:** ${KEY_TAKEAWAY}

### Problem Statement
${PROBLEM}

---

## Audience

### Primary Audience
${AUDIENCE}

**Knowledge Level:** ${KNOWLEDGE_LEVEL:-General}

**Pain Points:**
${PROBLEM}

**What They Need:**
${KEY_TAKEAWAY}

---

## SEO Strategy

### Keywords
- **Primary Keyword:** ${PRIMARY_KEYWORD}
- **Secondary Keywords:** ${SECONDARY_KEYWORDS:-TBD}
- **Search Intent:** ${SEARCH_INTENT:-Informational}
- **Target Search Volume:** ${SEARCH_VOLUME:-TBD}

### SEO Requirements
- [ ] Include primary keyword in title
- [ ] Use primary keyword in first 100 words
- [ ] Include keywords in headings (H2, H3)
- [ ] Write compelling meta description (150-160 chars)
- [ ] Add alt text to all images
- [ ] Internal linking strategy
- [ ] External authoritative links

### Meta Description (Draft)
[Write a compelling 150-160 character description including primary keyword]

---

## Content Structure

### Framework
${FRAMEWORK}

### Outline / Key Sections
${KEY_SECTIONS}

### Content Requirements
- **Examples needed:** ${NUM_EXAMPLES:-TBD}
- **Data/statistics:** ${NEEDS_DATA:-No}
- **Code examples:** ${NEEDS_CODE:-No}

---

## Tone & Voice

### Writing Style
- **Tone:** ${TONE}
- **Point of View:** ${POV:-Second person (you/your)}
- **Style Notes:** ${STYLE_NOTES:-Follow brand voice guidelines}

### Writing Guidelines
- Use active voice
- Short paragraphs (2-4 sentences)
- Bullet points for scanability
- Subheadings every 300-400 words
- Clear, concise language
- Avoid jargon (or explain when necessary)

---

## Visual & Media Requirements

### Images
- **Number of images:** ${NUM_IMAGES:-3-5}
- **Hero image:** ${HERO_IMAGE:-Featured image at top}
- **In-content images:** ${SCREENSHOTS:-Relevant screenshots or diagrams}

### Other Media
${VIDEO_NEEDS}

### Image Specifications
- Format: PNG or JPG
- Max file size: 500KB (optimize)
- Alt text for all images
- Relevant to content
- High quality (no stock photos if possible)

---

## Research & Sources

### Competitor Analysis
${COMPETITOR_URLS:-Research top-ranking content for target keyword}

### Research Requirements
- **SME Interviews:** ${NEEDS_SME:-No}
- **Primary Sources:** ${RESEARCH_SOURCES:-TBD}
- **Citation Standards:** Link to original sources, use recent data (< 2 years)

### Required Research
- [ ] Analyze top 5 ranking articles for primary keyword
- [ ] Gather relevant statistics and data
- [ ] Collect examples and case studies
- [ ] Interview SMEs (if required)
- [ ] Compile list of authoritative sources

---

## Calls-to-Action

### Primary CTA
${PRIMARY_CTA:-TBD}

### Secondary CTA
${SECONDARY_CTA:-None}

### Conversion Goal
${CONVERSION_GOAL:-TBD}

### CTA Placement
- [ ] In introduction (soft CTA)
- [ ] Mid-content (contextual)
- [ ] End of article (primary CTA)
- [ ] Sidebar or floating (if applicable)

---

## Links & References

### Internal Links
${INTERNAL_LINKS:-Link to relevant internal content (3-5 links)}

### External Links
${EXTERNAL_LINKS:-Link to authoritative external sources (2-3 links)}

### Linking Strategy
- Link to relevant internal content (3-5 links)
- Link to authoritative external sources
- Use descriptive anchor text
- Open external links in new tabs

---

## Success Metrics

### Primary Metric
**${PRIMARY_METRIC}** - Target: ${METRIC_TARGET:-TBD}

### Secondary Metrics
${SECONDARY_METRICS:-Time on page, scroll depth, social shares}

### How We'll Measure Success
- Track metrics in Google Analytics / analytics tool
- Review performance after 30 days
- A/B test headlines/CTAs if needed
- Compare to existing similar content

### Benchmarks
- [Add relevant benchmarks from similar content]

---

## Legal & Compliance

${COMPLIANCE:-No special requirements}

### Checklist
- [ ] Copyright for all images
- [ ] Proper attribution for quotes
- [ ] Fact-checking completed
- [ ] Legal disclaimers (if needed)
- [ ] Privacy policy linked (if collecting data)

---

## Special Requirements / Notes

${SPECIAL_NOTES:-None}

---

## Workflow & Timeline

### Process
1. **Brief Review** - Writer reviews brief with stakeholders
2. **Research** - Gather sources, data, examples (est: ___ hours)
3. **Outline** - Create detailed outline for review (est: ___ hours)
4. **First Draft** - Write content following brief (est: ___ hours)
5. **Self-Edit** - Writer reviews and edits (est: ___ hours)
6. **Peer Review** - Editor reviews against brief (est: ___ hours)
7. **Revisions** - Incorporate feedback (est: ___ hours)
8. **SEO Review** - Optimize for search (est: ___ hours)
9. **Final Approval** - Stakeholder sign-off
10. **Publish** - Schedule and publish
11. **Promote** - Distribution across channels
12. **Track** - Monitor success metrics

### Key Dates
- **Brief Finalized:** $(date +%Y-%m-%d)
- **First Draft Due:** ${PUB_DATE:-TBD}
- **Final Approval:** ${PUB_DATE:-TBD}
- **Publication Date:** ${PUB_DATE:-TBD}

---

## Stakeholders

### Content Team
- **Writer:** [Name]
- **Editor:** [Name]
- **SEO Specialist:** [Name]

### Reviewers
- **Subject Matter Expert:** [Name]
- **Brand Review:** [Name]
- **Final Approver:** [Name]

---

## References & Resources

### Templates & Guidelines
- [Brand voice guide]
- [Style guide]
- [SEO guidelines]
- [Content templates]

### Research Links
- [Link to research document]
- [Link to keyword research]
- [Link to competitor analysis]

---

## Approval

- [ ] Writer reviewed brief
- [ ] Stakeholders aligned
- [ ] Ready to begin writing

**Approved by:** ___________
**Date:** ___________

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | $(date +%Y-%m-%d) | [Auto-generated] | Initial brief |

EOF

echo -e "${GREEN}✅ Content brief generated successfully!${NC}"
echo ""
echo -e "File location: ${BLUE}$OUTPUT_FILE${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Review the brief with stakeholders"
echo "2. Conduct research and gather sources"
echo "3. Create detailed outline"
echo "4. Begin writing first draft"
echo ""
echo -e "${CYAN}Tip: Use validate_brief.sh to check completeness${NC}"
echo ""
