import yfinance as yf
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = yf.Ticker('AAPL')
hist = data.history(period = '1y', interval = '1d')
close = hist['Close'].values

close = np.asarray(close)

close_fft = np.fft.fft(np.asarray(close.tolist()))
close_fft_list = np.asarray(close_fft.tolist())

num_ = 50
fft_list_m10 = np.copy(close_fft_list); fft_list_m10[num_:-num_]=0
ft = np.fft.ifft(fft_list_m10)

plt.plot(close)
plt.plot(ft)
plt.show()





