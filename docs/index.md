# INDEPENDENT_RESERVE Documentation

## English

Welcome to the INDEPENDENT_RESERVE documentation for bt_api.

### Quick Start

```bash
pip install bt_api_independent_reserve
```

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "INDEPENDENT_RESERVE___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)
ticker = api.get_tick("INDEPENDENT_RESERVE___SPOT", "BTCUSDT")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 INDEPENDENT_RESERVE 文档。

### 快速开始

```bash
pip install bt_api_independent_reserve
```

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "INDEPENDENT_RESERVE___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)
ticker = api.get_tick("INDEPENDENT_RESERVE___SPOT", "BTCUSDT")
print(ticker)
```

## API Reference

See source code in `src/bt_api_independent_reserve/` for detailed API documentation.
