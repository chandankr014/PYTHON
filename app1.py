import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
## SIMPLE STOCK PRICE APP
MADE USING STREAMLIT\n

STOCK = GOOGLE\n
""")

#define ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this stock
#Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#~Intraday data cannot extend last 60 days
#start='YYYY-MM-DD'
#end = 'YYYY-MM-DD'

tickerDf = tickerData.history(start='2022-01-01', end='2022-06-01', period='1m', interval='1h')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
