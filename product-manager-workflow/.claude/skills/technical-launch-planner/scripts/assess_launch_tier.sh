#!/bin/bash

# Technical Launch Tier Assessment
# Helps determine the appropriate launch tier based on scope and impact

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Technical Launch Tier Assessment          ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}This assessment will help determine your launch tier.${NC}"
echo ""

# Scoring system
SCORE=0

# Question 1: What are you launching?
echo -e "${YELLOW}Question 1: What are you launching?${NC}"
echo "  1) New product/platform (GA)"
echo "  2) Major version update (v2.0, v3.0)"
echo "  3) New feature/integration"
echo "  4) Enhancement/improvement"
echo "  5) Bug fix/patch"
echo ""
read -p "Your answer (1-5): " Q1

case $Q1 in
    1) SCORE=$((SCORE + 10));;
    2) SCORE=$((SCORE + 8));;
    3) SCORE=$((SCORE + 5));;
    4) SCORE=$((SCORE + 2));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Question 2: Target audience size
echo -e "${YELLOW}Question 2: How many developers/users will this impact?${NC}"
echo "  1) All users (100%)"
echo "  2) Most users (50-99%)"
echo "  3) Segment of users (25-50%)"
echo "  4) Small segment (<25%)"
echo "  5) Beta/limited group"
echo ""
read -p "Your answer (1-5): " Q2

case $Q2 in
    1) SCORE=$((SCORE + 10));;
    2) SCORE=$((SCORE + 7));;
    3) SCORE=$((SCORE + 5));;
    4) SCORE=$((SCORE + 2));;
    5) SCORE=$((SCORE + 1));;
esac
echo ""

# Question 3: Revenue impact
echo -e "${YELLOW}Question 3: What's the revenue/business impact?${NC}"
echo "  1) New revenue stream"
echo "  2) Major revenue driver"
echo "  3) Moderate impact"
echo "  4) Minor impact"
echo "  5) No direct revenue impact"
echo ""
read -p "Your answer (1-5): " Q3

case $Q3 in
    1) SCORE=$((SCORE + 10));;
    2) SCORE=$((SCORE + 7));;
    3) SCORE=$((SCORE + 4));;
    4) SCORE=$((SCORE + 2));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Question 4: Competitive differentiation
echo -e "${YELLOW}Question 4: Is this competitively differentiated?${NC}"
echo "  1) Industry first / unique capability"
echo "  2) Significant differentiation"
echo "  3) Some differentiation"
echo "  4) Parity feature"
echo "  5) No competitive angle"
echo ""
read -p "Your answer (1-5): " Q4

case $Q4 in
    1) SCORE=$((SCORE + 8));;
    2) SCORE=$((SCORE + 6));;
    3) SCORE=$((SCORE + 4));;
    4) SCORE=$((SCORE + 1));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Question 5: Technical complexity
echo -e "${YELLOW}Question 5: How complex is this technically?${NC}"
echo "  1) New platform/architecture"
echo "  2) Significant technical undertaking"
echo "  3) Moderate complexity"
echo "  4) Simple feature"
echo "  5) Minor change"
echo ""
read -p "Your answer (1-5): " Q5

case $Q5 in
    1) SCORE=$((SCORE + 7));;
    2) SCORE=$((SCORE + 5));;
    3) SCORE=$((SCORE + 3));;
    4) SCORE=$((SCORE + 1));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Question 6: Documentation/enablement needed
echo -e "${YELLOW}Question 6: What documentation/enablement is required?${NC}"
echo "  1) Complete new documentation set + SDKs"
echo "  2) Major documentation updates + samples"
echo "  3) New guides + code samples"
echo "  4) Documentation updates"
echo "  5) Release notes only"
echo ""
read -p "Your answer (1-5): " Q6

case $Q6 in
    1) SCORE=$((SCORE + 6));;
    2) SCORE=$((SCORE + 5));;
    3) SCORE=$((SCORE + 3));;
    4) SCORE=$((SCORE + 1));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Question 7: External interest
echo -e "${YELLOW}Question 7: Expected external interest (press, analysts, community)?${NC}"
echo "  1) High (industry news)"
echo "  2) Moderate (tech press interest)"
echo "  3) Some (developer community)"
echo "  4) Low (niche interest)"
echo "  5) Minimal (internal mainly)"
echo ""
read -p "Your answer (1-5): " Q7

case $Q7 in
    1) SCORE=$((SCORE + 7));;
    2) SCORE=$((SCORE + 5));;
    3) SCORE=$((SCORE + 3));;
    4) SCORE=$((SCORE + 1));;
    5) SCORE=$((SCORE + 0));;
esac
echo ""

# Calculate tier
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${CYAN}Analyzing your responses...${NC}"
echo ""

sleep 1

# Determine tier based on score
if [ $SCORE -ge 40 ]; then
    TIER="Tier 1"
    COLOR=$RED
    TIMELINE="12-16 weeks"
    INVESTMENT="Full GTM"
elif [ $SCORE -ge 20 ]; then
    TIER="Tier 2"
    COLOR=$YELLOW
    TIMELINE="6-8 weeks"
    INVESTMENT="Selective GTM"
else
    TIER="Tier 3"
    COLOR=$GREEN
    TIMELINE="2-4 weeks"
    INVESTMENT="Minimal GTM"
fi

# Display results
echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║              Assessment Results                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Your Score:  ${CYAN}$SCORE / 58${NC}"
echo -e "Launch Tier: ${COLOR}$TIER${NC}"
echo -e "Timeline:    ${CYAN}$TIMELINE${NC}"
echo -e "Investment:  ${CYAN}$INVESTMENT${NC}"
echo ""

# Tier-specific recommendations
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${COLOR}$TIER Recommendations:${NC}"
echo ""

if [ "$TIER" = "Tier 1" ]; then
    echo -e "${YELLOW}Major Launch - Full GTM Treatment${NC}"
    echo ""
    echo "Required:"
    echo "  ✓ Complete documentation set"
    echo "  ✓ Multiple SDKs/client libraries"
    echo "  ✓ Sample applications"
    echo "  ✓ Video tutorials"
    echo "  ✓ Interactive demos/playground"
    echo "  ✓ Press release"
    echo "  ✓ Launch event/webinar"
    echo "  ✓ Partner coordination"
    echo "  ✓ Paid promotion"
    echo "  ✓ Analyst briefings"
    echo ""
    echo "Channels:"
    echo "  • Developer blog (launch post)"
    echo "  • Email (entire developer list)"
    echo "  • Social media (coordinated campaign)"
    echo "  • Hacker News / Reddit"
    echo "  • Tech press outreach"
    echo "  • Developer communities"
    echo "  • Conference talks"
    echo ""
    echo "Team involvement:"
    echo "  • Product Marketing (lead)"
    echo "  • Product Management"
    echo "  • Developer Relations"
    echo "  • Engineering"
    echo "  • Sales Engineering"
    echo "  • Partners"
    echo "  • PR/Comms"
    echo ""

elif [ "$TIER" = "Tier 2" ]; then
    echo -e "${YELLOW}Standard Launch - Selective GTM${NC}"
    echo ""
    echo "Required:"
    echo "  ✓ Feature documentation"
    echo "  ✓ Code samples"
    echo "  ✓ Blog post"
    echo "  ✓ Demo video"
    echo "  ✓ Email announcement"
    echo "  ✓ Updated API reference"
    echo ""
    echo "Channels:"
    echo "  • Developer blog"
    echo "  • Email (targeted segment)"
    echo "  • Social media"
    echo "  • Changelog"
    echo "  • Developer newsletter"
    echo "  • Relevant communities"
    echo ""
    echo "Team involvement:"
    echo "  • Product Marketing (lead)"
    echo "  • Developer Relations"
    echo "  • Product Management"
    echo "  • Engineering (docs)"
    echo ""

else
    echo -e "${GREEN}Minor Launch - Documentation Focus${NC}"
    echo ""
    echo "Required:"
    echo "  ✓ Release notes"
    echo "  ✓ Updated documentation"
    echo "  ✓ Changelog entry"
    echo "  ✓ In-app notification (if applicable)"
    echo ""
    echo "Channels:"
    echo "  • Changelog"
    echo "  • Documentation"
    echo "  • Social media (single post)"
    echo "  • Email (if significant)"
    echo ""
    echo "Team involvement:"
    echo "  • Product Marketing or PM"
    echo "  • Engineering (docs)"
    echo ""
fi

echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""

# Next steps
echo -e "${CYAN}Next Steps:${NC}"
echo ""
echo "1. Generate detailed launch plan:"
echo -e "   ${YELLOW}scripts/generate_launch_plan.sh${NC}"
echo ""
echo "2. Review tier framework:"
echo -e "   ${YELLOW}cat references/launch_tiers.md${NC}"
echo ""
echo "3. Check developer enablement checklist:"
echo -e "   ${YELLOW}cat references/developer_enablement.md${NC}"
echo ""

# Save results
read -p "Save results to file? (y/n): " SAVE
if [[ "$SAVE" =~ ^[Yy]$ ]]; then
    OUTPUT_FILE="launch_assessment_$(date +%Y%m%d_%H%M%S).txt"
    {
        echo "Technical Launch Tier Assessment"
        echo "Date: $(date)"
        echo ""
        echo "Score: $SCORE / 58"
        echo "Tier: $TIER"
        echo "Timeline: $TIMELINE"
        echo "Investment: $INVESTMENT"
        echo ""
        echo "Responses:"
        echo "Q1: $Q1"
        echo "Q2: $Q2"
        echo "Q3: $Q3"
        echo "Q4: $Q4"
        echo "Q5: $Q5"
        echo "Q6: $Q6"
        echo "Q7: $Q7"
    } > "$OUTPUT_FILE"

    echo -e "${GREEN}✓ Results saved to: $OUTPUT_FILE${NC}"
fi

echo ""
echo -e "${GREEN}✓ Assessment complete!${NC}"
