import yfinance as yf
import pandas as pd
import numpy as np
from math import log, sqrt, exp
from scipy import stats
from matplotlib import pyplot as plt
from yahoo_fin import stock_info as si
import datetime
import time

def d1_(S, K, t, r, iv):
    return (log(S/K) + ((iv*iv)/2.0 + r)*t)/(iv*sqrt(t))

def BS_call(S, K , t, r, iv):
    S = float(S)
    d1 = d1_(S, K, t, r, iv)
    d2 = d1 - iv*sqrt(t)
    price = S * stats.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * t) * stats.norm.cdf(d2, 0.0, 1.0)

    delta = stats.norm.cdf(d1, 0.0, 1.0)
    return price, delta



tick = 'AAPL'

apple = yf.Ticker(tick)
dates = apple.options
expiry = dates[0]


options = apple.option_chain(expiry)


#exp = input("Days Until Expiration: ")

r = .026
exp = 3.0
exp = exp/252
price = si.get_live_price(tick)

call_price = options.calls.lastPrice
implied_vol = options.calls.impliedVolatility
call_strike = options.calls.strike



##

for i in range (len(call_strike)):

    calculated_call , calculated_delta= BS_call(price, call_strike[i], exp, r, implied_vol[i])

    print("Stike: ", call_strike[i], "Calculated: ", calculated_call, "Yfin Price: ", call_price[0])
    print("Delta: ", calculated_delta)
    print("")
