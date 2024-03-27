import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt

# class to contain testing and visualization functions
class backtest:


    data = {'Ticker': [],
        'Amount': [],
        'Date': []}
    # trades = []
    portfolioVal = []

    def __init__(self) -> None:
        pass

    # function should step through the algorithm time step by time
    # step and record relevant information, including trades and the
    # value of the portfolio at each step
    def run(self, algo, start, end):
        print(algo.ticker.index)
        for day in algo.ticker.index:#change this
            
            algo.buy("AAPL", day)
            algo.sell("AAPL", day)
            self.portfolioVal.append(algo.getCurrVal(day))
            print(algo.getCurrVal(day))
            
        print("End portfolio value: ", algo.getCurrVal(day))
            #algo.buy("AAPL")
        pass

    def graphReturns(): 
        pass

    def calculateVol():
        pass

    def calculateSharpe():
        pass
