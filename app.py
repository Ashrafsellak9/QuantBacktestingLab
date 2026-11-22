import streamlit as st
import pandas as pd
from data import get_stock_prices # import this function from data.py file
import math

# implement a function that store result of stock price in cache 
@st.cache_data(ttl=3600)
def get_cached_prices(symbol):
    print(f"Downloading {symbol}...")
    return get_stock_prices(symbol)

st.subheader("Real Market Data")

# user choose which stock 
selected_symbol = st.selectbox(
    "Choose a stock",
    ["MSFT", "AAPL", "TSLA", "NVDA"]
)

history = get_cached_prices(selected_symbol)

if history.empty:
    st.warning("No data available")
else:
    # Select "Close" Dataframe and make a copy to keep original one
    prices = history[["Close"]].copy()
    
    # Calculate Daily Return using pct_change()
    prices["Daily_Return"] = prices["Close"].pct_change()
    # Display the last 5 lines 
    st.dataframe(prices.tail())
    
    # Calculate latest Return based on Daily Return using iloc
    latest_return = prices["Daily_Return"].iloc[-1]
    
    # Display Latest Daily Return Result
    st.metric(
        "Latest Daily Return",
        f"{latest_return:+.2%}"
    )
    
    # Calculate Daily Volatility based on Daily Return
    daily_volatility = prices["Daily_Return"].std()
    # Calculate Annual Volatility based on Daily Volatility
    annual_volatility = daily_volatility * math.sqrt(252)
    
    # Display Daily Volatility result
    st.metric(
        "Daily Volatility",
        f"{daily_volatility:.2%}"
    )
    # Display Annual Volatility result
    st.metric(
        "Annual Volatility",
        f"{annual_volatility:.2%}"
    )
    
    # Calculate Simple moving average, SMA20 and SMA50
    prices["SMA_20"] = prices["Close"].rolling(window=20).mean()
    prices["SMA_50"] = prices["Close"].rolling(window=50).mean()
    
    prices["Signal"] = (
        # if SMA20 is above SMA50, sign of bullish trend but not 100% buy position
        (prices["SMA_20"] > prices["SMA_50"]) & prices["SMA_50"].notna() # to verify if SMA50 is calculated or not
    ).astype(int) # to convert boolean to int , True => 1 False => 0
    
    st.subheader("Trading Signals")

    # display dataframe table with 3 columns 
    st.dataframe(
        prices[["Close", "SMA_50", "Signal"]].tail(15)
    )
    # display 3 graphs (close, SMA20, SMA50)
    st.line_chart(
        prices[["Close", "SMA_20", "SMA_50"]]
    )

    

