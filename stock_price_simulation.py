from matplotlib import pyplot as plt
import math
import numpy as np
import numpy.random as npr
import pandas
import yfinance as yf
data = yf.Ticker('MSFT').history(period = '7d', interval = '1m')



S0 = 100
r = 0.05
sigma = 0.25
T = 2
I = 100
M = 50
dt = np.float(T)/M
S = np.zeros((M+1, I))
S[0] = S0

prices = []
for t in range(1, M+1):
    S[t] = S[t-1] * np.exp((r-0.5*sigma**2) * dt + sigma*np.sqrt(dt)*npr.randn(I))

    plt.plot(S[t])

plt.show()


