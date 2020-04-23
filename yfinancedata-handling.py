
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


data=yf.download('AAPL',start="2017-04-01", end="2019-04-30")
data.head()

data=pd.read_csv('FB.csv')
data.head()

data=pd.read_csv('FB.csv',index_col=0)
data.index=pd.to_datetime(data.index,dayfirst=true)

plt.figure(figsize=(10,5))
data[close].plot(figsize=(10,5))
plt.legend()
plt.show()

