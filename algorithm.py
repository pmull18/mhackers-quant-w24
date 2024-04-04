import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta



class algorithm:
    portfolio = 0 #list of ticker, amt
    cash = 1000000
    ticker_symbols = "AAPL"
    ticker = yf.download(ticker_symbols, "2022-12-13", "2024-01-01")
    fourteen_day_ma = [] #just AAPL for now
    trades = []

    def __init__(self, day):
        #put first 14 values into RSI list
        # average_gain()
        # set_rsi()

        first_day = "2022-12-13"
        for i in range(14):
            price_on_day = self.ticker.loc[day]["Close"]
            #iterate through the table
            fourteen_day_ma += price_on_day



        
        # ticker = yf.download(tick, start_date, end_date)
        pass

    def buy(self, tick, day):
        # print(self.ticker.loc[day]["Close"])
        price_on_day = self.ticker.loc[day]["Close"]
        
        buy_amt = 0
        if price_on_day < 175:
            buy_amt = self.cash / price_on_day
        self.portfolio += buy_amt
        self.cash -= buy_amt * price_on_day
        data = {"AAPL", buy_amt, day}
        self.trades.append(data)
        pass

    def sell(self, tick, day):
        # print(ticker[day])
        # print(self.ticker.loc[day])
        price_on_day = self.ticker.loc[day]["Close"]
        sell_amt = 0
        if price_on_day > 190:
            sell_amt = self.portfolio
        self.portfolio -= sell_amt
        self.cash += sell_amt + price_on_day
        data = {"AAPL", -sell_amt, day}
        self.trades.append(data)
        pass

    def RSI_val(self, day):
        # push/pop values on day
        fourteen_day_ma.pop(0)
        fourteen_day_ma.append(self.ticker.loc[day]["Close"])

        pass

    def getCurrVal(self, day):
        price_on_day = self.ticker.loc[day]["Close"]
        portfolio_val = price_on_day*self.portfolio + self.cash
        return portfolio_val
        pass

    def decide(self, tick, day):
        self.buy("AAPL", day)
        self.sell("AAPL", day)