import yfinance as yf
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def std_(returns):
    if len(returns) >1:
        sigmasum = 0
        d=0
        total = 0
        avg = 0
        for i in range(len(returns)):
            total += returns[i]
        avg = total/len(returns)
        for i in range(len(returns)):
            d = returns[i] - avg
            sigmasum += d*d
        sigma  = 0
        sigma = math.sqrt((1/(len(returns) -1)) * sigmasum)
        return sigma
    else:
        return None


stock = 'gld'

obj = yf.Ticker(stock)
data = obj.history(period = '1y', interval = '1d')
close = data['Close'].values

sx = []
lowers = []
uppers = []
actuals = []
close_ = []


upper_bound = 0
lower_bound = 0

yes = 0
no = 0

for i in range(30, len(close)):

    for j in range(i-15, i):
        
        prices = []

        standard_devs = []

        for k in range(j-30, j+1):
            prices.append(close[k])

        sigma = std_(prices)

        standard_devs.append(sigma)
        
    sx.append(np.mean(standard_devs))


    upper_bound = close[i-1]+sx[-1]
    lower_bound = close[i-1]-sx[-1]

    if close[i] < upper_bound and close[i] > lower_bound:
        yes = yes+1
    else:
        no = no + 1

    print("Close: ", close[i-1])
    print("LOWER: " , lower_bound)
    print("UPPER: ", upper_bound)
    print("[*]Actual: ", close[i])
    print("*************")

    lowers.append(lower_bound)
    uppers.append(upper_bound)
    actuals.append(close[i])
    close_.append(close[i-1])



#plt.plot(close_, label = 'Prices')
plt.plot(lowers, label = 'Lowerbound')
plt.plot(uppers, label = 'Upperbound')
plt.plot(actuals, label = 'Actual')


#plt.plot(sx)
#plt.show()

print("Mean Sigma: ", np.mean(sx))
print("Yes: ", yes)
print("No : ", no)
print("Percentage Range(Expected 68%): ", round(yes/(yes+no)*100,2), "%")


plt.legend()
plt.show()
