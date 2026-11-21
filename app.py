import streamlit as st
import pandas as pd

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
st.dataframe(df)