#!/bin/bash

# Launch Readiness Validator
# Checks if technical launch is ready

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║      Technical Launch Readiness Check         ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════╝${NC}"
echo ""

# Counters
PASSED=0
FAILED=0
WARNINGS=0

# Helper functions
check_yes_no() {
    local question="$1"
    local critical="$2"

    read -p "$question (y/n): " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        echo -e "  ${GREEN}✓${NC} Pass"
        ((PASSED++))
        return 0
    else
        if [ "$critical" = "true" ]; then
            echo -e "  ${RED}✗${NC} FAIL (Critical)"
            ((FAILED++))
        else
            echo -e "  ${YELLOW}⚠${NC} Warning"
            ((WARNINGS++))
        fi
        return 1
    fi
}

# Documentation Check
echo -e "${CYAN}━━━ Documentation ━━━${NC}"
echo ""

check_yes_no "Getting started guide complete and reviewed?" true
check_yes_no "API reference up to date?" true
check_yes_no "At least 3 code samples ready?" true
check_yes_no "Integration guide written?" false
check_yes_no "Migration guide (if needed)?" false
check_yes_no "Troubleshooting FAQ added?" false

echo ""

# Code Assets
echo -e "${CYAN}━━━ Code Assets ━━━${NC}"
echo ""

check_yes_no "SDKs built and tested?" false
check_yes_no "Sample applications functional?" false
check_yes_no "Interactive demo/playground ready?" false
check_yes_no "Code snippets library created?" false

echo ""

# Technical Infrastructure
echo -e "${CYAN}━━━ Technical Infrastructure ━━━${NC}"
echo ""

check_yes_no "Production environment tested?" true
check_yes_no "Monitoring/analytics instrumented?" true
check_yes_no "Error tracking configured?" true
check_yes_no "Rate limiting verified?" false
check_yes_no "Load testing completed?" false

echo ""

# Marketing Assets
echo -e "${CYAN}━━━ Marketing Assets ━━━${NC}"
echo ""

check_yes_no "Launch blog post written and reviewed?" true
check_yes_no "Demo video recorded?" false
check_yes_no "Email template created?" true
check_yes_no "Social media posts scheduled?" true
check_yes_no "Product page updated?" true

echo ""

# Sales Enablement
echo -e "${CYAN}━━━ Sales Enablement ━━━${NC}"
echo ""

check_yes_no "Sales team briefed?" false
check_yes_no "Demo script prepared?" false
check_yes_no "FAQ/objections documented?" false
check_yes_no "Pricing materials ready?" false

echo ""

# Team Readiness
echo -e "${CYAN}━━━ Team Readiness ━━━${NC}"
echo ""

check_yes_no "Support team trained?" true
check_yes_no "On-call rotation set?" true
check_yes_no "Escalation path defined?" true
check_yes_no "Launch day roles assigned?" true

echo ""

# Final Checks
echo -e "${CYAN}━━━ Final Checks ━━━${NC}"
echo ""

check_yes_no "All stakeholders approved?" true
check_yes_no "Legal/compliance review (if needed)?" true
check_yes_no "Rollback plan documented?" true
check_yes_no "Launch day playbook ready?" true

echo ""

# Results
echo -e "${BLUE}╔═══════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║             Readiness Summary                  ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Checks Passed: ${GREEN}$PASSED${NC}"
echo -e "Warnings:      ${YELLOW}$WARNINGS${NC}"
echo -e "Failed:        ${RED}$FAILED${NC}"
echo ""

# Decision
if [ $FAILED -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ READY TO LAUNCH!${NC}"
        echo ""
        echo "All critical checks passed. You're good to go!"
    else
        echo -e "${YELLOW}⚠ LAUNCH WITH CAUTION${NC}"
        echo ""
        echo "Critical checks passed, but $WARNINGS warnings remain."
        echo "Consider addressing warnings before launch."
    fi
    exit 0
else
    echo -e "${RED}❌ NOT READY TO LAUNCH${NC}"
    echo ""
    echo "You have $FAILED critical failures that must be addressed."
    echo "Do not launch until these are resolved."
    exit 1
fi
