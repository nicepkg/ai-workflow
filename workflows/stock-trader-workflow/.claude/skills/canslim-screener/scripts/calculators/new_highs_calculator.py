#!/usr/bin/env python3
"""
N Component - Newness / New Highs Calculator

Calculates CANSLIM 'N' component score based on price position relative to
52-week high and momentum indicators.

O'Neil's Rule: "Stocks making new price highs have no overhead supply.
New products, services, or management catalyze major moves."

Scoring:
- 100: Within 5% of 52-week high + breakout + new product catalyst
- 80: Within 10% of 52-week high + breakout
- 60: Within 15% of 52-week high OR breakout
- 40: Within 25% of 52-week high
- 20: >25% from 52-week high (lacks momentum)
"""

from typing import Dict, List, Optional


def calculate_newness(quote: Dict, historical_prices: Optional[Dict] = None) -> Dict:
    """
    Calculate N component score based on price position and momentum

    Args:
        quote: Stock quote data from FMP API (contains yearHigh, price, volume)
        historical_prices: Optional historical price data for detailed analysis

    Returns:
        Dict with:
            - score: 0-100 points
            - distance_from_high_pct: Distance from 52-week high (%)
            - current_price: Current stock price
            - week_52_high: 52-week high price
            - week_52_low: 52-week low price
            - breakout_detected: Boolean
            - interpretation: Human-readable interpretation
    """
    # Validate input
    if not quote:
        return {
            "score": 0,
            "error": "Quote data missing",
            "distance_from_high_pct": None,
            "interpretation": "Data unavailable"
        }

    # Extract price data
    current_price = quote.get("price")
    week_52_high = quote.get("yearHigh")
    week_52_low = quote.get("yearLow")
    current_volume = quote.get("volume")
    avg_volume = quote.get("avgVolume")

    if not current_price or not week_52_high:
        return {
            "score": 0,
            "error": "Price or 52-week high data missing",
            "distance_from_high_pct": None,
            "interpretation": "Data unavailable"
        }

    # Calculate distance from 52-week high
    distance_from_high_pct = ((current_price / week_52_high) - 1) * 100

    # Detect breakout (new high on elevated volume)
    breakout_detected = False
    if current_volume and avg_volume:
        # Within 0.5% of high AND volume 40%+ above average
        if current_price >= week_52_high * 0.995 and current_volume > avg_volume * 1.4:
            breakout_detected = True

    # Calculate score
    score = score_newness(distance_from_high_pct, breakout_detected)

    # Generate interpretation
    interpretation = interpret_newness_score(score, distance_from_high_pct, breakout_detected)

    return {
        "score": score,
        "distance_from_high_pct": round(distance_from_high_pct, 1),
        "current_price": current_price,
        "week_52_high": week_52_high,
        "week_52_low": week_52_low,
        "breakout_detected": breakout_detected,
        "current_volume": current_volume,
        "avg_volume": avg_volume,
        "volume_ratio": round(current_volume / avg_volume, 2) if avg_volume else None,
        "interpretation": interpretation,
        "error": None
    }


def score_newness(distance_from_high_pct: float, breakout_detected: bool) -> int:
    """
    Score N component based on price position and breakout

    Args:
        distance_from_high_pct: Distance from 52-week high (negative = below high)
        breakout_detected: Boolean indicating volume-confirmed breakout

    Returns:
        Score (0-100)

    Scoring Logic:
    - Within 5% of high + breakout: 100
    - Within 10% of high + breakout: 80
    - Within 15% of high OR breakout: 60
    - Within 25% of high: 40
    - >25% from high: 20
    """
    if distance_from_high_pct >= -5 and breakout_detected:
        return 100  # Perfect setup - at new highs with volume
    elif distance_from_high_pct >= -10 and breakout_detected:
        return 80   # Strong momentum
    elif distance_from_high_pct >= -15 or breakout_detected:
        return 60   # Acceptable
    elif distance_from_high_pct >= -25:
        return 40   # Weak momentum
    else:
        return 20   # Too far from highs, lacks sponsorship


def interpret_newness_score(score: int, distance: float, breakout: bool) -> str:
    """
    Generate human-readable interpretation

    Args:
        score: Component score
        distance: Distance from 52-week high (%)
        breakout: Breakout detected flag

    Returns:
        Interpretation string
    """
    breakout_text = " with volume breakout" if breakout else ""

    if score >= 90:
        return f"Exceptional - At new highs{breakout_text} ({distance:+.1f}% from high)"
    elif score >= 70:
        return f"Strong - Near 52-week high{breakout_text} ({distance:+.1f}% from high)"
    elif score >= 50:
        return f"Acceptable - Within 15% of high ({distance:+.1f}% from high)"
    elif score >= 30:
        return f"Weak - Lacks momentum ({distance:+.1f}% from high)"
    else:
        return f"Poor - Too far from highs, overhead resistance ({distance:+.1f}% from high)"


# Example usage
if __name__ == "__main__":
    print("Testing New Highs Calculator (N Component)...\n")

    # Test 1: At new high with breakout (score 100)
    test_quote_1 = {
        "symbol": "NVDA",
        "price": 495.50,
        "yearHigh": 496.00,
        "yearLow": 280.00,
        "volume": 60000000,
        "avgVolume": 40000000
    }
    result1 = calculate_newness(test_quote_1)
    print(f"Test 1: New High + Breakout - Score: {result1['score']}")
    print(f"  {result1['interpretation']}\n")

    # Test 2: Within 10% of high, no breakout (score 60)
    test_quote_2 = {
        "symbol": "META",
        "price": 450.00,
        "yearHigh": 490.00,
        "yearLow": 320.00,
        "volume": 15000000,
        "avgVolume": 16000000
    }
    result2 = calculate_newness(test_quote_2)
    print(f"Test 2: Near High, No Breakout - Score: {result2['score']}")
    print(f"  {result2['interpretation']}\n")

    # Test 3: Far from high (score 20)
    test_quote_3 = {
        "symbol": "XYZ",
        "price": 50.00,
        "yearHigh": 80.00,
        "yearLow": 45.00,
        "volume": 1000000,
        "avgVolume": 1200000
    }
    result3 = calculate_newness(test_quote_3)
    print(f"Test 3: Far from High - Score: {result3['score']}")
    print(f"  {result3['interpretation']}\n")

    print("✓ All tests completed")
