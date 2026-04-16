# trade_strategy

[![PyPI - Version](https://img.shields.io/pypi/v/trade-strategy.svg)](https://pypi.org/project/trade-strategy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/trade-strategy.svg)](https://pypi.org/project/trade-strategy)

-----

## Table of Contents

- [Installation](#installation)
- [How to Run `example.py`](#how-to-run-example.py)
- [License](#license)

## Installation

```console
pip install trade-strategy
```

## How to Run

To use the `risk_return` function, you can use the following Python code:

```python
from trade_strategy import risk_return

tickers = ["AAPL", "MSFT", "GOOG"]
start_date = '2013-03-07'
end_date = '2025-04-05'

risk_return(tickers, start_date, end_date)
```

- **Assets:** `["AAPL", "MSFT", "GOOG"]`
- **Start Date:** `2013-03-07`
- **End Date:** `2025-04-05`

### Expected Output

The script will output a JSON payload containing the lowest risk, highest returns, and highest Sharpe ratio allocations for the specified tickers and date range. The `returns` and `volatility` fields are expressed as percentages.

```json
{
  "lowest_risk_allocation": {
    "returns": 24.8073,
    "volatility": 23.4054,
    "sharpe_ratio": 1.059898,
    "weights": [0.347, 0.352, 0.3],
    "assets": ["AAPL", "MSFT", "GOOG"]
  },
  "highest_returns_allocation": {
    "returns": 26.8417,
    "volatility": 26.2248,
    "sharpe_ratio": 1.023524,
    "weights": [0.003, 0.986, 0.011],
    "assets": ["AAPL", "MSFT", "GOOG"]
  },
  "highest_sharpe_allocation": {
    "returns": 25.8282,
    "volatility": 23.8805,
    "sharpe_ratio": 1.081562,
    "weights": [0.301, 0.588, 0.111],
    "assets": ["AAPL", "MSFT", "GOOG"]
  }
}
```

## License

`trade-strategy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
