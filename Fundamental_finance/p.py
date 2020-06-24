import yfinance as yf
from yahoofinancials import YahooFinancials
import numexpr as ne
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/income-statement/AAPL?apikey=demo")

data = get_jsonparsed_data(url)
size = len(data)
#print(data)

dates = []
revenue = []
cogs = []
grossprofit = []
research = []
general = []
marketing = []
otherexpenses = []
operatingexpenses = []
costandexpenses = []
interestexpense = []
depreciation = []
ebitda = []
operatingincome = []
otherincome = []
pretaxincome = []
incomeTaxExpense = []
netincome = []
shares = []
sharesDiluted = []

for i in range (size):
    dates.append(data[i]['date'])
    revenue.append(data[i]['revenue'])
    cogs.append(data[i]['costOfRevenue'])
    grossprofit.append(data[i]['grossProfit'])
    research.append(data[i]['researchAndDevelopmentExpenses'])
    general.append(data[i]['generalAndAdministrativeExpenses'])
    marketing.append(data[i]['sellingAndMarketingExpenses'])
    otherexpenses.append(data[i]['otherExpenses'])
    operatingexpenses.append(data[i]['operatingExpenses'])
    costandexpenses.append(data[i]['costAndExpenses'])
    interestexpense.append(data[i]['interestExpense'])
    depreciation.append(data[i]['depreciationAndAmortization'])
    ebitda.append(data[i]['ebitda'])
    operatingincome.append(data[i]['operatingIncome'])
    otherincome.append(data[i]['totalOtherIncomeExpensesNet'])
    pretaxincome.append(data[i]['incomeBeforeTax'])
    incomeTaxExpense.append(data[i]['incomeTaxExpense'])
    netincome.append(data[i]['netIncome'])
    shares.append(data[i]['weightedAverageShsOut'])
    sharesDiluted.append(data[i]['weightedAverageShsOutDil'])


#building Projections
revenue_change = 0
for i in range(4):
    change  = (revenue[i] - revenue[i+1])/(revenue[i+1]) *100
    print(revenue[i+1], "    ", change, "   ", revenue[i])
    revenue_change += change

revenue_change = revenue_change/4.0

print("Projection percentage constant change of revenue: " ,revenue_change, "%")




















