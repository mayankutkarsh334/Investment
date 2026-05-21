import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

NIFTY_SYMBOLS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS", 
    "HINDUNILVR.NS", "SBIN.NS", "BAJFINANCE.NS", "BHARTIARTL.NS", "ITC.NS"
]

def backtest_symbol(symbol):
    print(f"Backtesting {symbol}...")
    try:
        # Fetch 3 years of data to have enough history
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="3y")
        if data.empty:
            return 0, 0
            
        close_series = data['Close']

        data['RSI'] = RSIIndicator(close=close_series, window=14).rsi()
        data['SMA50'] = SMAIndicator(close=close_series, window=50).sma_indicator()
        data['SMA200'] = SMAIndicator(close=close_series, window=200).sma_indicator()
        
        trades_taken = 0
        successful_trades = 0
        
        # We need at least 200 days to calculate SMA200, and we stop 63 days before the end
        # so we have 3 months (approx 63 trading days) to check the outcome.
        for i in range(200, len(data) - 63):
            # To avoid multiple trades close to each other, we can skip ahead if a trade was taken,
            # but for simplicity, we just check every day.
            
            current_price = data['Close'].iloc[i]
            sma50 = data['SMA50'].iloc[i]
            sma200 = data['SMA200'].iloc[i]
            rsi = data['RSI'].iloc[i]
            
            # Entry condition
            if current_price > sma50 and sma50 > sma200 and 55 <= rsi <= 75:
                # Check next 63 days for a 10% gain
                target_price = current_price * 1.10
                stop_loss = current_price * 0.90 # Optional 10% stop loss
                
                future_prices = data['Close'].iloc[i+1:i+64]
                
                trade_success = False
                for price in future_prices:
                    if price >= target_price:
                        trade_success = True
                        break
                    elif price <= stop_loss:
                        # hit stop loss before target
                        break
                        
                trades_taken += 1
                if trade_success:
                    successful_trades += 1
                    
        return trades_taken, successful_trades

    except Exception as e:
        print(f"Error backtesting {symbol}: {e}")
        return 0, 0

def main():
    total_trades = 0
    total_success = 0
    
    for symbol in NIFTY_SYMBOLS:
        trades, success = backtest_symbol(symbol)
        total_trades += trades
        total_success += success
        
    if total_trades > 0:
        win_rate = (total_success / total_trades) * 100
        print(f"\n--- Backtest Results ---")
        print(f"Total Signals found in 3 years: {total_trades}")
        print(f"Trades hitting 10% target within 3 months: {total_success}")
        print(f"Win Rate: {win_rate:.2f}%")
    else:
        print("No trades triggered.")

if __name__ == "__main__":
    main()
