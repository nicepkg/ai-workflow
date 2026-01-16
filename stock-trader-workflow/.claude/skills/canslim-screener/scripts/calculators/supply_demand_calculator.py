#!/usr/bin/env python3
"""
S Component - Supply and Demand Calculator

Calculates CANSLIM 'S' component score based on volume accumulation/distribution patterns.

O'Neil's Rule: "Volume is the gas in the tank of a stock. Without gas, the car doesn't
go anywhere. Look for stocks where volume expands on up days and contracts on down days."

Key Principle:
- UP-DAY VOLUME > DOWN-DAY VOLUME = Accumulation (institutions buying)
- DOWN-DAY VOLUME > UP-DAY VOLUME = Distribution (institutions selling)

Scoring:
- 100 points: Up/down ratio ≥ 2.0 (Strong Accumulation)
- 80 points: Ratio 1.5-2.0 (Accumulation)
- 60 points: Ratio 1.0-1.5 (Neutral/Weak Accumulation)
- 40 points: Ratio 0.7-1.0 (Neutral/Weak Distribution)
- 20 points: Ratio 0.5-0.7 (Distribution)
- 0 points: Ratio < 0.5 (Strong Distribution)
"""

from typing import Dict, List


def calculate_supply_demand(historical_prices: Dict) -> Dict:
    """
    Calculate supply/demand dynamics based on volume patterns

    Args:
        historical_prices: Historical price data from FMP API
                          Dict with keys: 'historical' (list of daily price/volume data)
                          Each entry should have: date, close, volume

    Returns:
        Dict with:
            - score: 0-100 points
            - up_down_ratio: Average up-day volume / average down-day volume
            - accumulation_detected: True if ratio ≥ 1.5
            - avg_up_volume: Average volume on up days
            - avg_down_volume: Average volume on down days
            - up_days_count: Number of up days in analysis period
            - down_days_count: Number of down days
            - interpretation: Human-readable interpretation
            - quality_warning: Warning if data quality issues
            - error: Error message if calculation failed

    Example:
        >>> prices = client.get_historical_prices("NVDA", days=90)
        >>> result = calculate_supply_demand(prices)
        >>> print(f"S Score: {result['score']}, Ratio: {result['up_down_ratio']:.2f}")
    """
    # Validate input
    if not historical_prices or "historical" not in historical_prices:
        return {
            "score": 0,
            "error": "No historical price data provided",
            "up_down_ratio": None,
            "accumulation_detected": False,
            "avg_up_volume": None,
            "avg_down_volume": None,
            "up_days_count": 0,
            "down_days_count": 0,
            "interpretation": "Data unavailable"
        }

    prices = historical_prices["historical"]

    if not prices or len(prices) < 60:
        return {
            "score": 0,
            "error": f"Insufficient data (need 60+ days, got {len(prices)})",
            "up_down_ratio": None,
            "accumulation_detected": False,
            "avg_up_volume": None,
            "avg_down_volume": None,
            "up_days_count": 0,
            "down_days_count": 0,
            "interpretation": "Data unavailable",
            "quality_warning": "Less than 60 days of historical data available"
        }

    # Analyze last 60 days (prices are typically newest first, so take first 60)
    analysis_period = prices[:60]

    # Classify days as up or down
    up_days = []
    down_days = []
    previous_close = None

    for day in reversed(analysis_period):  # Process chronologically
        current_close = day.get("close")
        current_volume = day.get("volume")

        if current_close is None or current_volume is None:
            continue  # Skip incomplete data

        if previous_close is not None:
            if current_close > previous_close:
                up_days.append(current_volume)
            elif current_close < previous_close:
                down_days.append(current_volume)
            # Unchanged days are ignored

        previous_close = current_close

    # Validate we have enough classified days
    if len(up_days) < 10 or len(down_days) < 10:
        return {
            "score": 0,
            "error": "Insufficient up/down days for analysis",
            "up_down_ratio": None,
            "accumulation_detected": False,
            "avg_up_volume": None,
            "avg_down_volume": None,
            "up_days_count": len(up_days),
            "down_days_count": len(down_days),
            "interpretation": "Data quality issues",
            "quality_warning": f"Too few classified days (up: {len(up_days)}, down: {len(down_days)})"
        }

    # Calculate average volumes
    avg_up_volume = sum(up_days) / len(up_days)
    avg_down_volume = sum(down_days) / len(down_days)

    # Calculate accumulation/distribution ratio
    if avg_down_volume == 0:
        # Edge case: no volume on down days (extremely bullish, but rare)
        ratio = 5.0  # Cap at 5.0 to avoid infinity
    else:
        ratio = avg_up_volume / avg_down_volume

    # Determine accumulation status
    accumulation_detected = ratio >= 1.5

    # Score based on ratio
    score = score_supply_demand(ratio)

    # Generate interpretation
    interpretation = interpret_supply_demand(ratio, accumulation_detected)

    return {
        "score": score,
        "up_down_ratio": ratio,
        "accumulation_detected": accumulation_detected,
        "avg_up_volume": int(avg_up_volume),
        "avg_down_volume": int(avg_down_volume),
        "up_days_count": len(up_days),
        "down_days_count": len(down_days),
        "interpretation": interpretation
    }


def score_supply_demand(ratio: float) -> int:
    """
    Score accumulation/distribution ratio

    Args:
        ratio: Up-day volume / down-day volume

    Returns:
        int: Score from 0-100
    """
    if ratio >= 2.0:
        return 100  # Strong Accumulation
    elif ratio >= 1.5:
        return 80   # Accumulation
    elif ratio >= 1.0:
        return 60   # Neutral/Weak Accumulation
    elif ratio >= 0.7:
        return 40   # Neutral/Weak Distribution
    elif ratio >= 0.5:
        return 20   # Distribution
    else:
        return 0    # Strong Distribution


def interpret_supply_demand(ratio: float, accumulation: bool) -> str:
    """
    Generate human-readable interpretation of supply/demand dynamics

    Args:
        ratio: Up-day volume / down-day volume
        accumulation: True if accumulation detected

    Returns:
        str: Interpretation string
    """
    if ratio >= 2.0:
        return f"Strong Accumulation (ratio: {ratio:.2f}x) - Institutions aggressively buying. Volume precedes price."
    elif ratio >= 1.5:
        return f"Accumulation (ratio: {ratio:.2f}x) - Bullish volume pattern. Institutional interest building."
    elif ratio >= 1.0:
        return f"Neutral/Weak Accumulation (ratio: {ratio:.2f}x) - Slightly positive volume trend."
    elif ratio >= 0.7:
        return f"Neutral/Weak Distribution (ratio: {ratio:.2f}x) - Slightly negative volume trend. Monitor closely."
    elif ratio >= 0.5:
        return f"Distribution (ratio: {ratio:.2f}x) - Bearish volume pattern. Institutions may be selling."
    else:
        return f"Strong Distribution (ratio: {ratio:.2f}x) - Heavy selling pressure. Volume leads price lower."


# Example usage
if __name__ == "__main__":
    # Test with sample data
    sample_data = {
        "historical": [
            {"date": "2024-12-10", "close": 150.0, "volume": 80000000},  # up day
            {"date": "2024-12-09", "close": 148.0, "volume": 50000000},  # down day
            {"date": "2024-12-06", "close": 149.0, "volume": 75000000},  # up day
            {"date": "2024-12-05", "close": 147.0, "volume": 45000000},  # down day
        ] * 15  # Repeat to get 60 days
    }

    result = calculate_supply_demand(sample_data)

    print("S Component Test Results:")
    print(f"  Score: {result['score']}/100")
    print(f"  Up/Down Ratio: {result['up_down_ratio']:.2f}")
    print(f"  Accumulation: {result['accumulation_detected']}")
    print(f"  Interpretation: {result['interpretation']}")
