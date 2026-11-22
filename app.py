import streamlit as st
import pandas as pd
from data import get_stock_prices
import math

@st.cache_data(ttl=3600)
def get_cached_prices(symbol):
    print(f"Downloading {symbol}...")
    return get_stock_prices(symbol)

prices = {
    "Date": [
        "2026-11-16",
        "2026-11-17",
        "2026-11-18",
        "2026-11-19",
        "2026-11-20",
        "2026-11-23"
    ],
    "Close": [100, 102, 101, 104, 103, 106]
}

df = pd.DataFrame(prices)

st.subheader("Historical Stock Prices")

df["Return (%)"] = df["Close"].pct_change() * 100
df["Date"] = pd.to_datetime(df["Date"])

st.dataframe(df.round(2))


st.subheader("Stock Price Evolution")
st.line_chart(df, x="Date", y="Close")

st.subheader("Real Market Data")

selected_symbol = st.selectbox(
    "Choose a stock",
    ["MSFT", "AAPL", "TSLA", "NVDA"]
)

history = get_cached_prices(selected_symbol)

if history.empty:
    st.warning("No data available")
else:
    prices = history[["Close"]].copy()
    
    prices["Daily_Return"] = prices["Close"].pct_change()
    st.dataframe(prices.tail())

    latest_return = prices["Daily_Return"].iloc[-1]

    st.metric(
        "Latest Daily Return",
        f"{latest_return:+.2%}"
    )

    daily_volatility = prices["Daily_Return"].std()
    annual_volatility = daily_volatility * math.sqrt(252)

    st.metric(
        "Daily Volatility",
        f"{daily_volatility:.2%}"
    )

    st.metric(
        "Annual Volatility",
        f"{annual_volatility:.2%}"
    )
    
    prices["SMA_20"] = prices["Close"].rolling(window=20).mean()
    prices["SMA_50"] = prices["Close"].rolling(window=50).mean()
    
    st.line_chart(
        prices[["Close", "SMA_20", "SMA_50"]]
    )

    

