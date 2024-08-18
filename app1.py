import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
         
Shown are the stock closing price and volume of Google!
         
""")

# Define the ticker symbol
tickersymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickersymbol)

# Get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2024-01-31')

# Use the correct column name 'Close' for closing prices
st.write("""
         ## closing price""")
st.line_chart(tickerDF['Close'])
st.write(""" 
    ## volume price
""")
st.line_chart(tickerDF['Volume'])
