# INDEPENDENT_RESERVE Documentation

## English

Welcome to the INDEPENDENT_RESERVE documentation for bt_api.

### Quick Start

```bash
pip install bt_api_independent_reserve
```

```python
from bt_api_independent_reserve import IndependentReserveApi
feed = IndependentReserveApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## 中文

欢迎使用 bt_api 的 INDEPENDENT_RESERVE 文档。

### 快速开始

```bash
pip install bt_api_independent_reserve
```

```python
from bt_api_independent_reserve import IndependentReserveApi
feed = IndependentReserveApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## API Reference

See source code in `src/bt_api_independent_reserve/` for detailed API documentation.
