import streamlit as st
import pandas as pd
from data import get_stock_prices

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

st.subheader("Microsoft Stock Prices")

msft = get_stock_prices("MSFT")
if msft.empty:
    st.warning("No data available")
else:
    st.dataframe(msft.tail())
    st.line_chart(msft["Close"])



st.subheader("Telsa Stock Prices")

tesla = get_stock_prices("TSLA")
if tesla.empty:
    st.warning("No data available")
else:
    st.dataframe(tesla.tail())
    st.line_chart(tesla["Close"])


st.subheader("Apple Stock Prices")

apple = get_stock_prices("AAPL")

if apple.empty:
    st.warning("No data available")
else:
    st.dataframe(apple.tail())
    st.line_chart(apple["Close"])