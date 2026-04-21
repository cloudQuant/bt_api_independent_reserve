from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


_CODE_MAP = {
    "BTC": "Xbt",
    "ETH": "Eth",
    "USDT": "Usdt",
    "USDC": "Usdc",
    "LTC": "Ltc",
    "XRP": "Xrp",
    "BCH": "Bch",
    "EOS": "Eos",
    "XLM": "Xlm",
    "BAT": "Bat",
    "ETC": "Etc",
    "LINK": "Link",
    "GNT": "Gnt",
    "OMG": "Omg",
    "ZRX": "Zrx",
    "PMGT": "Pmgt",
    "AUD": "Aud",
    "NZD": "Nzd",
    "USD": "Usd",
    "SGD": "Sgd",
}

_FALLBACK_REST_PATHS = {
    "get_tick": "GET /Public/GetMarketSummary",
    "get_depth": "GET /Public/GetOrderBook",
    "get_deals": "GET /Public/GetRecentTrades",
    "get_exchange_info": "GET /Public/GetValidPrimaryCurrencyCodes",
    "get_secondary_currencies": "GET /Public/GetValidSecondaryCurrencyCodes",
    "make_order_limit": "POST /Private/PlaceLimitOrder",
    "make_order_market": "POST /Private/PlaceMarketOrder",
    "cancel_order": "POST /Private/CancelOrder",
    "get_open_orders": "POST /Private/GetOpenOrders",
    "get_order_details": "POST /Private/GetOrderDetails",
    "get_account": "POST /Private/GetAccounts",
    "get_balance": "POST /Private/GetAccounts",
    "get_trades": "POST /Private/GetTrades",
}


class IndependentReserveExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "INDEPENDENT_RESERVE___SPOT"
        self.rest_url = "https://api.independentreserve.com"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "4h": "4h",
            "1d": "1d",
            "1w": "1w",
        }
        self.reverse_kline_periods = {v: k for k, v in self.kline_periods.items()}
        self.legal_currency = ["AUD", "NZD", "USD", "SGD", "USDT", "BTC", "ETH"]

    @staticmethod
    def get_symbol(symbol):
        parts = symbol.split("/") if "/" in symbol else symbol.split("-")
        if len(parts) == 2:
            base = _CODE_MAP.get(parts[0].upper(), parts[0].capitalize())
            quote = _CODE_MAP.get(parts[1].upper(), parts[1].capitalize())
            return base, quote
        return "Xbt", "Aud"

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]


class IndependentReserveExchangeDataSpot(IndependentReserveExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
