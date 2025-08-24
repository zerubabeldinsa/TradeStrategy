# trade_strategy

[![PyPI - Version](https://img.shields.io/pypi/v/trade-strategy.svg)](https://pypi.org/project/trade-strategy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/trade-strategy.svg)](https://pypi.org/project/trade-strategy)

-----

## Table of Contents

- [Installation](#installation)
- [How to Run `allocations.py`](#how-to-run-allocationspy)
- [License](#license)

## Installation

```console
pip install trade-strategy
```

## How to Run

To use the `risk_return` function, you can use the following Python code:

```python
from trade_strategy import risk_return

tickers = ["AAPL", "MSFT"]
start_date = '2013-03-07'
end_date = '2025-04-05'

risk_return(tickers, start_date, end_date)
```

- **Assets:** `["AAPL", "MSFT"]`
- **Start Date:** `2013-03-07`
- **End Date:** `2025-04-05`

### Expected Output

The script will output the lowest risk, highest returns, and highest Sharpe ratio allocations for the specified tickers and date range.

```
Lowest risk Allocation
Returns                    0.248073
Risk                       0.234054
Sharpe Ratio               1.059898
Weights         [0.347, 0.352, 0.3]
Name: 69, dtype: object
['AAPL', 'MSFT', 'GOOG']

Highest Returns Allocation
Returns                      0.268417
Risk                         0.262248
Sharpe Ratio                 1.023524
Weights         [0.003, 0.986, 0.011]
Name: 116, dtype: object
['AAPL', 'MSFT', 'GOOG']

Highest Sharpe Allocation
Returns                      0.258282
Risk                         0.238805
Sharpe Ratio                 1.081562
Weights         [0.301, 0.588, 0.111]
Name: 128, dtype: object
['AAPL', 'MSFT', 'GOOG']
```

## License

`trade-strategy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.