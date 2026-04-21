# bt_api_independent_reserve

Independent Reserve exchange plugin for bt_api framework.

## Installation

```bash
pip install bt_api_independent_reserve
```

## Usage

```python
from bt_api_independent_reserve import IndependentReserveExchangeDataSpot, IndependentReserveRequestDataSpot
```

## Features

- REST API support
- HMAC-SHA256 authentication (POST JSON body)
- Symbol format: `BTC/AUD`, `ETH/USD` etc.
- Primary/secondary currency code mapping (BTC→Xbt, ETH→Eth, etc.)
