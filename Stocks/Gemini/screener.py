import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

# Top NIFTY 50 companies by weight as a sample set.
NIFTY_SYMBOLS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS", 
    "HINDUNILVR.NS", "SBIN.NS", "BAJFINANCE.NS", "BHARTIARTL.NS", "ITC.NS",
    "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS", "ASIANPAINT.NS", "MARUTI.NS"
]

def analyze_stock(symbol):
    try:
        # Fetch 1 year of data
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1y")
        if data.empty:
            return None
            
        # Calculate technical indicators
        close_series = data['Close']
            
        data['RSI'] = RSIIndicator(close=close_series, window=14).rsi()
        data['SMA50'] = SMAIndicator(close=close_series, window=50).sma_indicator()
        data['SMA200'] = SMAIndicator(close=close_series, window=200).sma_indicator()
        
        last_row = data.iloc[-1]
        
        # Momentum criteria: Price > SMA50 > SMA200, and RSI between 55 and 75
        current_price = last_row['Close']
        sma50 = last_row['SMA50']
        sma200 = last_row['SMA200']
        rsi = last_row['RSI']
        
        if pd.isna(current_price) or pd.isna(sma50) or pd.isna(sma200) or pd.isna(rsi):
            return None

        # Check conditions for momentum breakout
        if current_price > sma50 and sma50 > sma200 and 55 <= rsi <= 75:
            return {
                'Symbol': symbol,
                'Price': round(float(current_price), 2),
                'RSI': round(float(rsi), 2),
                'SMA50': round(float(sma50), 2),
                'SMA200': round(float(sma200), 2)
            }
        return None
    except Exception as e:
        print(f"Error analyzing {symbol}: {e}")
        return None

def main():
    print("Running stock screener for NIFTY sample...")
    candidates = []
    
    for symbol in NIFTY_SYMBOLS:
        result = analyze_stock(symbol)
        if result:
            candidates.append(result)
            
    if not candidates:
        print("No stocks met the criteria today.")
    else:
        print(f"Found {len(candidates)} candidates for a potential short-term momentum trade:")
        df = pd.DataFrame(candidates)
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()
