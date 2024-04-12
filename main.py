import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from backtest import backtest
from algorithm import algorithm



tester = backtest()

# start_date = "2023-01-01"
# end_date = "2024-01-01"

algo = algorithm()

tester.run(algo)
plt.figure(figsize=(10, 6))
tester.calculateVol(algo)
tester.graphReturns(algo)
tester.graphRSI(algo)
tester.calculate_tot_returns(algo)
tester.calculate_market_return(algo)
plt.tight_layout()
plt.show()