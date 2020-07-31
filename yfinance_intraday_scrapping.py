import sys
import yfinance as yf 
import math 

tick = 'AAPL' 
stock = yf.Ticker(tick) 

#Daily 
daily_ = stock.history(period = '5y', interval = '1d') 
daily_close = daily_['Close'].values

#Hourly
hourly_ = stock.history(period = '2y', interval = '1h')
hourly_close = hourly_['Close'].values

#5 Minutes
5_minute_ = stock.history(period = '60d', interval = '5m') 
5_minute_close = 5_minute['Close'].values

