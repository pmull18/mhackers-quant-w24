import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt

from backtest import backtest
from algorithm import algorithm



tester = backtest()

start_date = "2022-01-01"
end_date = "2023-01-01"

algo = algorithm(start_date)

tester.run(algo, start_date, end_date)
tester.graphReturns(algo)