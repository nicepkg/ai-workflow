#!/usr/bin/env python3
"""
A Component - Annual EPS Growth Calculator

Calculates CANSLIM 'A' component score based on multi-year EPS CAGR and growth stability.

O'Neil's Rule: "Annual earnings per share should be up 25% or more in each
of the last three years."

Scoring:
- 90-100: CAGR 40%+, stable growth (no down years)
- 70-89: CAGR 30-39%, stable
- 50-69: CAGR 25-29% (meets CANSLIM minimum)
- 30-49: CAGR 15-24% (below threshold)
- 0-29: CAGR <15% or erratic growth

Bonus: +10 points for stability (no down years)
Penalty: -20% if revenue CAGR significantly lags EPS CAGR (buyback-driven growth)
"""

from typing import Dict, List, Optional


def calculate_annual_growth(income_statements: List[Dict]) -> Dict:
    """
    Calculate 3-year EPS CAGR and growth stability

    Args:
        income_statements: List of annual income statements from FMP API
                          (most recent year first, needs at least 4 years for 3-year CAGR)

    Returns:
        Dict with:
            - score: 0-100 points
            - eps_cagr_3yr: 3-year EPS compound annual growth rate (%)
            - revenue_cagr_3yr: 3-year revenue CAGR (%) for validation
            - stability: "stable" or "erratic"
            - eps_values: List of EPS values (chronological)
            - interpretation: Human-readable interpretation
            - error: Error message if calculation failed
    """
    # Validate input
    if not income_statements or len(income_statements) < 4:
        return {
            "score": 50,  # Default for insufficient data (neutral)
            "error": "Insufficient annual data (need at least 4 years for 3-year CAGR)",
            "eps_cagr_3yr": None,
            "revenue_cagr_3yr": None,
            "stability": "unknown",
            "eps_values": None,
            "interpretation": "Data unavailable"
        }

    # Extract EPS for last 4 years (most recent first in API response)
    eps_values = []
    revenue_values = []

    for i in range(4):
        stmt = income_statements[i]
        eps = stmt.get("eps") or stmt.get("epsdiluted")
        revenue = stmt.get("revenue")

        if eps is None:
            return {
                "score": 0,
                "error": f"Missing EPS data for year {stmt.get('date', 'unknown')}",
                "eps_cagr_3yr": None,
                "revenue_cagr_3yr": None,
                "stability": "unknown",
                "eps_values": None,
                "interpretation": "EPS data incomplete"
            }

        if eps <= 0:
            return {
                "score": 0,
                "error": f"Negative or zero EPS in year {stmt.get('date', 'unknown')} - cannot calculate CAGR",
                "eps_cagr_3yr": None,
                "revenue_cagr_3yr": None,
                "stability": "unknown",
                "eps_values": None,
                "interpretation": "Negative EPS - not a CANSLIM candidate"
            }

        eps_values.append(eps)
        revenue_values.append(revenue if revenue else 0)

    # Reverse to chronological order (oldest first)
    eps_values_chrono = eps_values[::-1]
    revenue_values_chrono = revenue_values[::-1]

    # Calculate 3-year CAGR
    # CAGR = ((Ending Value / Beginning Value) ^ (1 / Number of Years)) - 1
    eps_start = eps_values_chrono[0]  # 3 years ago
    eps_end = eps_values_chrono[3]    # Current year
    years = 3

    eps_cagr = (((eps_end / eps_start) ** (1 / years)) - 1) * 100

    # Calculate revenue CAGR for validation
    revenue_start = revenue_values_chrono[0]
    revenue_end = revenue_values_chrono[3]

    if revenue_start > 0:
        revenue_cagr = (((revenue_end / revenue_start) ** (1 / years)) - 1) * 100
    else:
        revenue_cagr = 0

    # Check growth stability (no down years)
    stable = all(eps_values_chrono[i] >= eps_values_chrono[i - 1]
                 for i in range(1, len(eps_values_chrono)))

    # Calculate score
    score = score_annual_growth(eps_cagr, revenue_cagr, stable)

    # Generate interpretation
    interpretation = interpret_growth_score(score, eps_cagr, stable)

    # Quality warning
    quality_warning = None
    if revenue_cagr < (eps_cagr * 0.5) and eps_cagr > 20:
        quality_warning = ("Revenue CAGR significantly lags EPS CAGR - "
                          "growth may be buyback-driven rather than organic")

    return {
        "score": score,
        "eps_cagr_3yr": round(eps_cagr, 1),
        "revenue_cagr_3yr": round(revenue_cagr, 1),
        "stability": "stable" if stable else "erratic",
        "eps_values": [round(eps, 2) for eps in eps_values_chrono],
        "revenue_values": [int(rev) for rev in revenue_values_chrono],
        "years_analyzed": len(eps_values_chrono),
        "interpretation": interpretation,
        "quality_warning": quality_warning,
        "error": None
    }


def score_annual_growth(eps_cagr: float, revenue_cagr: float, stable: bool) -> int:
    """
    Score A component based on EPS CAGR, revenue validation, and stability

    Args:
        eps_cagr: 3-year EPS compound annual growth rate (%)
        revenue_cagr: 3-year revenue CAGR (%)
        stable: True if no down years, False if erratic

    Returns:
        Score (0-100)

    Scoring Logic:
    - Base score from EPS CAGR:
      - 40%+: 90 points
      - 30-39%: 70 points
      - 25-29%: 50 points (meets CANSLIM minimum)
      - 15-24%: 30 points
      - <15%: 0 points
    - Penalty: -20% if revenue CAGR < 50% of EPS CAGR (buyback concern)
    - Bonus: +10 points if stable growth (no down years)
    """
    # Base score from EPS CAGR
    if eps_cagr >= 40:
        base_score = 90
    elif eps_cagr >= 30:
        base_score = 70
    elif eps_cagr >= 25:
        base_score = 50  # Meets CANSLIM minimum
    elif eps_cagr >= 15:
        base_score = 30
    else:
        base_score = 0

    # Revenue growth validation penalty
    if revenue_cagr < (eps_cagr * 0.5):
        base_score = int(base_score * 0.8)  # 20% penalty

    # Stability bonus
    if stable:
        base_score += 10

    # Cap at 100
    return min(base_score, 100)


def interpret_growth_score(score: int, eps_cagr: float, stable: bool) -> str:
    """
    Generate human-readable interpretation of A component score

    Args:
        score: Component score (0-100)
        eps_cagr: 3-year EPS CAGR (%)
        stable: Growth stability flag

    Returns:
        Interpretation string
    """
    stability_text = "stable" if stable else "erratic"

    if score >= 90:
        return (f"Exceptional - {eps_cagr:.1f}% CAGR, {stability_text} growth trajectory")

    elif score >= 70:
        return (f"Strong - {eps_cagr:.1f}% CAGR, well above CANSLIM 25% threshold ({stability_text})")

    elif score >= 50:
        return (f"Acceptable - {eps_cagr:.1f}% CAGR meets CANSLIM minimum ({stability_text})")

    elif score >= 30:
        return (f"Below threshold - {eps_cagr:.1f}% CAGR insufficient (<25% required)")

    else:
        return (f"Weak - {eps_cagr:.1f}% CAGR does not meet CANSLIM criteria")


def check_consistency(income_statements: List[Dict]) -> Dict:
    """
    Check year-over-year growth consistency (no down years is ideal)

    Args:
        income_statements: List of annual income statements (recent first)

    Returns:
        Dict with:
            - down_years: Count of years with YoY decline
            - consecutive_growth_years: Max consecutive years of growth
            - growth_pattern: List of YoY growth rates
    """
    if len(income_statements) < 2:
        return {
            "down_years": None,
            "consecutive_growth_years": None,
            "growth_pattern": None,
            "interpretation": "Insufficient data"
        }

    eps_values = []
    for stmt in income_statements:
        eps = stmt.get("eps") or stmt.get("epsdiluted")
        if eps:
            eps_values.append(eps)

    # Reverse to chronological order
    eps_values = eps_values[::-1]

    # Calculate YoY growth rates
    growth_pattern = []
    for i in range(1, len(eps_values)):
        if eps_values[i - 1] > 0:
            yoy_growth = ((eps_values[i] - eps_values[i - 1]) / eps_values[i - 1]) * 100
            growth_pattern.append(round(yoy_growth, 1))

    # Count down years
    down_years = sum(1 for g in growth_pattern if g < 0)

    # Find max consecutive growth years
    consecutive = 0
    max_consecutive = 0
    for g in growth_pattern:
        if g >= 0:
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 0

    interpretation = f"{max_consecutive} consecutive years of growth, {down_years} down years"

    return {
        "down_years": down_years,
        "consecutive_growth_years": max_consecutive,
        "growth_pattern": growth_pattern,
        "interpretation": interpretation
    }


# Example usage and testing
if __name__ == "__main__":
    print("Testing Growth Calculator (A Component)...\n")

    # Test case 1: Exceptional growth (NVDA-like, 40%+ CAGR, stable)
    test_data_exceptional = [
        {"date": "2023-01-31", "eps": 4.02, "revenue": 26974000000},  # FY2023
        {"date": "2022-01-31", "eps": 4.44, "revenue": 26914000000},  # FY2022
        {"date": "2021-01-31", "eps": 1.93, "revenue": 16675000000},  # FY2021
        {"date": "2020-01-31", "eps": 1.67, "revenue": 10918000000},  # FY2020
    ]

    result1 = calculate_annual_growth(test_data_exceptional)
    print("Test 1: Exceptional Growth (40%+ CAGR)")
    print(f"  Score: {result1['score']}/100")
    print(f"  EPS CAGR: {result1['eps_cagr_3yr']}%")
    print(f"  Revenue CAGR: {result1['revenue_cagr_3yr']}%")
    print(f"  Stability: {result1['stability']}")
    print(f"  Interpretation: {result1['interpretation']}\n")

    # Test case 2: Meets minimum (25-29% CAGR, stable)
    test_data_minimum = [
        {"date": "2023-12-31", "eps": 2.00, "revenue": 50000000000},
        {"date": "2022-12-31", "eps": 1.60, "revenue": 45000000000},
        {"date": "2021-12-31", "eps": 1.28, "revenue": 40000000000},
        {"date": "2020-12-31", "eps": 1.02, "revenue": 36000000000},  # ~25% CAGR
    ]

    result2 = calculate_annual_growth(test_data_minimum)
    print("Test 2: Meets CANSLIM Minimum (25% CAGR)")
    print(f"  Score: {result2['score']}/100")
    print(f"  EPS CAGR: {result2['eps_cagr_3yr']}%")
    print(f"  Revenue CAGR: {result2['revenue_cagr_3yr']}%")
    print(f"  Stability: {result2['stability']}")
    print(f"  Interpretation: {result2['interpretation']}\n")

    # Test case 3: Erratic growth (one down year)
    test_data_erratic = [
        {"date": "2023-12-31", "eps": 2.50, "revenue": 50000000000},
        {"date": "2022-12-31", "eps": 1.80, "revenue": 45000000000},  # Down year
        {"date": "2021-12-31", "eps": 2.00, "revenue": 48000000000},
        {"date": "2020-12-31", "eps": 1.60, "revenue": 42000000000},
    ]

    result3 = calculate_annual_growth(test_data_erratic)
    print("Test 3: Erratic Growth (One Down Year)")
    print(f"  Score: {result3['score']}/100")
    print(f"  EPS CAGR: {result3['eps_cagr_3yr']}%")
    print(f"  Stability: {result3['stability']}")
    print(f"  Interpretation: {result3['interpretation']}\n")

    # Test consistency check
    print("Test 4: Consistency Check")
    consistency = check_consistency(test_data_exceptional)
    print(f"  Down years: {consistency['down_years']}")
    print(f"  Consecutive growth: {consistency['consecutive_growth_years']} years")
    print(f"  Growth pattern: {consistency['growth_pattern']}")
    print(f"  Interpretation: {consistency['interpretation']}")

    print("\n✓ All tests completed")
