from matplotlib import pyplot as plt
import math
import numpy as np
import numpy.random as npr
import pandas
import yfinance as yf
data = yf.Ticker('MSFT').history(period = '7d', interval = '1m')
close = data['Close'].values
#plt.plot(close)
#plt.show()
#exit(1)

S0 = 100
r = 0.05
sigma = 0.25
lamb = 0.75
mu = -.6
delta = .25
T = 1
I = 100     #Iterations
M = 10      #steps
dt = np.float(T)/M
rj = lamb*(np.exp(mu+0.5*delta**2) - 1)
S = np.zeros((M+1, I))
S[0] = S0

z1 = npr.standard_normal((M+1, I))
z2 = npr.standard_normal((M+1, I))
y = npr.poisson(lamb*dt, (M+1, I))

prices = []
for t in range(1, M+1):
 #   S[t] = S[t-1] * np.exp((r-0.5*sigma**2) * dt + sigma*np.sqrt(dt)*npr.randn(I))


    #Metron Jump
    S[t] = S[t-1]*(np.exp((r-rj-0.5*sigma**2) * dt + sigma*np.sqrt(dt) *
                          z1[t]) + (np.exp(mu+delta*z2[t]) - 1) * y[t])

    S[t] = np.maximum(S[t], 0)

    print(S[t])

    plt.plot(S[t])

    break

plt.show()












