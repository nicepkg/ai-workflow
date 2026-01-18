#!/usr/bin/env python3
"""
Test FMP institutional-holder endpoint availability
Critical decision point for Phase 2 implementation
"""

import os
import sys
import requests

def test_institutional_endpoint():
    """
    Test if institutional-holder endpoint is available with current API key

    Returns:
        bool: True if endpoint available (Full Implementation)
              False if endpoint restricted (Fallback Implementation)
    """
    # Get API key
    api_key = os.environ.get('FMP_API_KEY')

    if not api_key:
        print("ERROR: FMP_API_KEY environment variable not set")
        print("Please set it with: export FMP_API_KEY=your_key")
        return False

    print(f"Testing institutional-holder endpoint with API key (length: {len(api_key)})...")
    print()

    # Test institutional-holder endpoint
    test_symbol = "AAPL"
    url = f"https://financialmodelingprep.com/api/v3/institutional-holder/{test_symbol}"
    params = {"apikey": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)

        print(f"Status Code: {response.status_code}")
        print(f"Response length: {len(response.text)} bytes")
        print()

        if response.status_code == 200:
            # Parse JSON
            data = response.json()

            # Check if it's an error message
            if isinstance(data, dict) and "Error Message" in data:
                print("❌ RESULT: Endpoint RESTRICTED")
                print(f"   Error: {data['Error Message']}")
                print()
                print("DECISION: Use Fallback Implementation (Step 3B)")
                print("  - I component will use Profile API institutionalOwnership field only")
                print("  - Score capped at 70/100")
                print("  - Quality warning will be added to all results")
                return False

            # Check if data is valid
            if isinstance(data, list) and len(data) > 0:
                print("✅ RESULT: Endpoint AVAILABLE")
                print(f"   Found {len(data)} institutional holders for {test_symbol}")
                print()
                print("Sample data:")
                for i, holder in enumerate(data[:3]):
                    print(f"  {i+1}. {holder.get('holder', 'N/A')}: "
                          f"{holder.get('shares', 0):,} shares")
                print()
                print("DECISION: Use Full Implementation (Step 3A)")
                print("  - Full institutional analysis with holder count and ownership %")
                print("  - Superinvestor detection")
                print("  - Score range: 0-100")
                return True
            else:
                print("⚠️  RESULT: Unexpected response format")
                print(f"   Data type: {type(data)}")
                print(f"   Data: {data}")
                print()
                print("DECISION: Use Fallback Implementation (Step 3B) as precaution")
                return False

        elif response.status_code == 401 or response.status_code == 403:
            print("❌ RESULT: Endpoint RESTRICTED (401/403)")
            print()
            print("DECISION: Use Fallback Implementation (Step 3B)")
            return False
        else:
            print(f"⚠️  RESULT: Unexpected status code {response.status_code}")
            print()
            print("DECISION: Use Fallback Implementation (Step 3B) as precaution")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Request failed - {e}")
        print()
        print("DECISION: Use Fallback Implementation (Step 3B)")
        return False


if __name__ == "__main__":
    print("=" * 70)
    print("FMP Institutional-Holder Endpoint Availability Test")
    print("=" * 70)
    print()

    result = test_institutional_endpoint()

    print()
    print("=" * 70)

    sys.exit(0 if result else 1)
