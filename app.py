import streamlit as st
import pandas as pd
from data import get_stock_prices


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
    st.dataframe(history.tail())
    st.line_chart(history["Close"])

