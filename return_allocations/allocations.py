import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from trade_strategy.portfolio_construction.efficient_frontier import risk_return

# Dates
start_date = '2013-01-01' 
end_date = '2025-03-27' 

# tickers
symbols = ["AAPL", "MSFT", "GOOG"]

# Calling function
risk_return(symbols, start_date, end_date)

