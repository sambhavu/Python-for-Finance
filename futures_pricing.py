import math
import yfinance

def futures_price(S, r, t):
    return math.exp(r*t) * S

def main():


    r = .05
    times = [.1, .2, .3, .4, .5]
    Stock = 100

    for t in times:
        price = futures_price(Stock, r, t)
        print("Time: ", t, "Futures Price: ", price, "Stock Price: ", Stock , "Interest Rate: ", r)


    
main()
