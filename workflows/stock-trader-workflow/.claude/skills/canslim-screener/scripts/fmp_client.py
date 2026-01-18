#!/usr/bin/env python3
"""
FMP API Client for CANSLIM Screener

Provides rate-limited access to Financial Modeling Prep API endpoints
required for CANSLIM component analysis (C, A, N, M).

Features:
- Rate limiting (0.3s between requests)
- Automatic retry on 429 errors
- Session caching for duplicate requests
- Error handling and logging
"""

import os
import sys
import time
from typing import Dict, List, Optional
from datetime import datetime

try:
    import requests
except ImportError:
    print("ERROR: requests library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


class FMPClient:
    """Client for Financial Modeling Prep API with rate limiting and caching"""

    BASE_URL = "https://financialmodelingprep.com/api/v3"
    RATE_LIMIT_DELAY = 0.3  # 300ms between requests (200 requests/minute max)

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize FMP API client

        Args:
            api_key: FMP API key (defaults to FMP_API_KEY environment variable)

        Raises:
            ValueError: If API key not provided and not in environment
        """
        self.api_key = api_key or os.getenv("FMP_API_KEY")
        if not self.api_key:
            raise ValueError(
                "FMP API key required. Set FMP_API_KEY environment variable "
                "or pass api_key parameter."
            )

        self.session = requests.Session()
        self.cache = {}  # Simple in-memory cache for session
        self.last_call_time = 0
        self.rate_limit_reached = False
        self.retry_count = 0
        self.max_retries = 1

    def _rate_limited_get(self, url: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make rate-limited GET request with retry logic

        Args:
            url: Full endpoint URL
            params: Query parameters (apikey added automatically)

        Returns:
            JSON response dict, or None on error
        """
        if self.rate_limit_reached:
            return None

        if params is None:
            params = {}
        params['apikey'] = self.api_key

        # Enforce rate limit
        elapsed = time.time() - self.last_call_time
        if elapsed < self.RATE_LIMIT_DELAY:
            time.sleep(self.RATE_LIMIT_DELAY - elapsed)

        try:
            response = self.session.get(url, params=params, timeout=30)
            self.last_call_time = time.time()

            if response.status_code == 200:
                self.retry_count = 0  # Reset on success
                return response.json()

            elif response.status_code == 429:
                # Rate limit exceeded
                self.retry_count += 1
                if self.retry_count <= self.max_retries:
                    print(f"WARNING: Rate limit exceeded. Waiting 60 seconds...", file=sys.stderr)
                    time.sleep(60)
                    return self._rate_limited_get(url, params)
                else:
                    print(f"ERROR: Daily API rate limit reached. Stopping analysis.", file=sys.stderr)
                    self.rate_limit_reached = True
                    return None

            else:
                print(f"ERROR: API request failed: {response.status_code} - {response.text[:200]}",
                      file=sys.stderr)
                return None

        except requests.exceptions.RequestException as e:
            print(f"ERROR: Request exception: {e}", file=sys.stderr)
            return None

    def get_income_statement(self,
                            symbol: str,
                            period: str = "quarter",
                            limit: int = 8) -> Optional[List[Dict]]:
        """
        Fetch income statement data (quarterly or annual)

        Args:
            symbol: Stock ticker (e.g., "AAPL")
            period: "quarter" or "annual"
            limit: Number of periods to fetch (default 8 for quarterly, 5 for annual)

        Returns:
            List of income statement records (most recent first), or None on error

        Example:
            quarterly = client.get_income_statement("AAPL", period="quarter", limit=8)
            # Returns last 8 quarters (2 years) for YoY comparison
        """
        cache_key = f"income_{symbol}_{period}_{limit}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"{self.BASE_URL}/income-statement/{symbol}"
        params = {"period": period, "limit": limit}

        data = self._rate_limited_get(url, params)

        if data:
            self.cache[cache_key] = data

        return data

    def get_quote(self, symbols: str) -> Optional[List[Dict]]:
        """
        Fetch real-time quote data

        Args:
            symbols: Single ticker or comma-separated list (e.g., "AAPL" or "AAPL,MSFT,GOOGL")

        Returns:
            List of quote records, or None on error

        Example:
            quote = client.get_quote("AAPL")
            # Returns [{"symbol": "AAPL", "price": 185.92, "yearHigh": 198.23, ...}]

            quotes = client.get_quote("^GSPC,^VIX")
            # Batch fetch S&P 500 and VIX
        """
        cache_key = f"quote_{symbols}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"{self.BASE_URL}/quote/{symbols}"

        data = self._rate_limited_get(url)

        if data:
            self.cache[cache_key] = data

        return data

    def get_historical_prices(self,
                             symbol: str,
                             days: int = 365) -> Optional[Dict]:
        """
        Fetch historical daily price data

        Args:
            symbol: Stock ticker (e.g., "AAPL")
            days: Number of days of history to fetch (default 365 for 52-week analysis)

        Returns:
            Dict with 'symbol' and 'historical' (list of daily OHLCV records), or None

        Example:
            prices = client.get_historical_prices("AAPL", days=365)
            # prices['historical'][0] = most recent day
            # prices['historical'][251] = 252 trading days ago (~1 year)
        """
        cache_key = f"prices_{symbol}_{days}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"{self.BASE_URL}/historical-price-full/{symbol}"
        params = {"timeseries": days}

        data = self._rate_limited_get(url, params)

        if data:
            self.cache[cache_key] = data

        return data

    def get_profile(self, symbol: str) -> Optional[List[Dict]]:
        """
        Fetch company profile (sector, industry, description)

        Args:
            symbol: Stock ticker

        Returns:
            List with single profile dict, or None on error

        Example:
            profile = client.get_profile("AAPL")
            # profile[0] = {"symbol": "AAPL", "companyName": "Apple Inc.", "sector": "Technology", ...}
        """
        cache_key = f"profile_{symbol}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"{self.BASE_URL}/profile/{symbol}"

        data = self._rate_limited_get(url)

        if data:
            self.cache[cache_key] = data

        return data

    def get_institutional_holders(self, symbol: str) -> Optional[List[Dict]]:
        """
        Fetch institutional holder data (Phase 2: I component)

        Args:
            symbol: Stock ticker

        Returns:
            List of institutional holders with:
                - holder: Institution name (str)
                - shares: Number of shares held (int)
                - dateReported: Reporting date (str)
                - change: Change in shares from previous quarter (int)
            Returns None on error

        Example:
            holders = client.get_institutional_holders("AAPL")
            # holders[0] = {"holder": "Vanguard Group Inc", "shares": 1234567890, ...}

        Note:
            This endpoint provides 13F filing data. Free tier may have limited access.
            Typical response contains hundreds to thousands of institutional holders.
        """
        cache_key = f"institutional_{symbol}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"{self.BASE_URL}/institutional-holder/{symbol}"

        data = self._rate_limited_get(url)

        if data:
            self.cache[cache_key] = data

        return data

    def calculate_ema(self, prices: List[float], period: int = 50) -> float:
        """
        Calculate Exponential Moving Average

        Args:
            prices: List of prices (most recent first)
            period: EMA period (default 50)

        Returns:
            EMA value

        Note:
            This is a helper method for market direction (M component).
            Uses standard EMA formula: EMA = Price * k + EMA_prev * (1-k)
            where k = 2 / (period + 1)
        """
        if len(prices) < period:
            return sum(prices) / len(prices)  # Fallback to simple average

        # Reverse to oldest-first for calculation
        prices_reversed = prices[::-1]

        # Initialize with SMA
        sma = sum(prices_reversed[:period]) / period
        ema = sma

        # Calculate EMA
        k = 2 / (period + 1)
        for price in prices_reversed[period:]:
            ema = price * k + ema * (1 - k)

        return ema

    def clear_cache(self):
        """Clear session cache (useful for refreshing data)"""
        self.cache = {}
        print("Cache cleared", file=sys.stderr)

    def get_api_stats(self) -> Dict:
        """
        Get API usage statistics for current session

        Returns:
            Dict with cache size and estimated API calls made
        """
        return {
            "cache_entries": len(self.cache),
            "rate_limit_reached": self.rate_limit_reached,
            "retry_count": self.retry_count
        }


def test_client():
    """Test FMP client with sample queries"""
    print("Testing FMP Client...")

    client = FMPClient()

    # Test 1: Quote
    print("\n1. Testing quote endpoint (AAPL)...")
    quote = client.get_quote("AAPL")
    if quote:
        print(f"✓ Quote: {quote[0]['symbol']} @ ${quote[0]['price']:.2f}")
    else:
        print("✗ Quote failed")

    # Test 2: Quarterly income statement
    print("\n2. Testing quarterly income statement (AAPL)...")
    quarterly = client.get_income_statement("AAPL", period="quarter", limit=8)
    if quarterly:
        latest = quarterly[0]
        print(f"✓ Latest quarter: {latest['date']}, EPS: ${latest.get('eps', 'N/A')}")
    else:
        print("✗ Quarterly income statement failed")

    # Test 3: Annual income statement
    print("\n3. Testing annual income statement (AAPL)...")
    annual = client.get_income_statement("AAPL", period="annual", limit=5)
    if annual:
        latest = annual[0]
        print(f"✓ Latest year: {latest['date']}, EPS: ${latest.get('eps', 'N/A')}")
    else:
        print("✗ Annual income statement failed")

    # Test 4: Historical prices
    print("\n4. Testing historical prices (AAPL)...")
    prices = client.get_historical_prices("AAPL", days=365)
    if prices and 'historical' in prices:
        print(f"✓ Fetched {len(prices['historical'])} days of price history")
        if len(prices['historical']) > 0:
            latest = prices['historical'][0]
            print(f"  Latest: {latest['date']}, Close: ${latest['close']:.2f}")
    else:
        print("✗ Historical prices failed")

    # Test 5: Market indices (batch)
    print("\n5. Testing market indices (^GSPC, ^VIX)...")
    indices = client.get_quote("^GSPC,^VIX")
    if indices:
        for idx in indices:
            print(f"✓ {idx['symbol']}: {idx['price']:.2f}")
    else:
        print("✗ Market indices failed")

    # Test 6: Cache
    print("\n6. Testing cache (repeat AAPL quote)...")
    quote2 = client.get_quote("AAPL")
    if quote2:
        print(f"✓ Cache working (no API call made)")

    # Stats
    stats = client.get_api_stats()
    print(f"\nAPI Stats:")
    print(f"  Cache entries: {stats['cache_entries']}")
    print(f"  Rate limit reached: {stats['rate_limit_reached']}")

    print("\n✓ All tests completed")


if __name__ == "__main__":
    test_client()
