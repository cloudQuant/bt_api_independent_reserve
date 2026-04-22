from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData
from bt_api_base.functions.utils import from_dict_get_float


class IndependentReserveOrderBookData(OrderBookData):
    def __init__(
        self,
        orderbook_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(orderbook_info, has_been_json_encoded)
        self.exchange_name = "INDEPENDENT_RESERVE"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.orderbook_data: dict[str, Any] | None = (
            orderbook_info if has_been_json_encoded and isinstance(orderbook_info, dict) else None
        )
        self.bids: list[list[float]] | None = None
        self.asks: list[list[float]] | None = None
        self.has_been_init_data = False

    def init_data(self) -> IndependentReserveOrderBookData:
        if not self.has_been_json_encoded:
            self.orderbook_data = (
                json.loads(self.orderbook_info) if isinstance(self.orderbook_info, str) else {}
            )
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.orderbook_data, dict):
            data = self.orderbook_data
            bid_list = data.get("Bids", []) if isinstance(data.get("Bids", []), list) else []
            ask_list = data.get("Asks", []) if isinstance(data.get("Asks", []), list) else []
            self.bids = [
                [
                    from_dict_get_float(item, "Price") or 0.0,
                    from_dict_get_float(item, "Volume") or 0.0,
                ]
                for item in bid_list
            ]
            self.asks = [
                [
                    from_dict_get_float(item, "Price") or 0.0,
                    from_dict_get_float(item, "Volume") or 0.0,
                ]
                for item in ask_list
            ]

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name or ""

    def get_symbol_name(self) -> str:
        return self.symbol_name or ""

    def get_asset_type(self) -> str:
        return self.asset_type or ""

    def get_bids(self) -> list[list[float]]:
        self.init_data()
        return self.bids or []

    def get_asks(self) -> list[list[float]]:
        self.init_data()
        return self.asks or []

    def get_local_update_time(self) -> float:
        return float(self.local_update_time or 0.0)


class IndependentReserveRequestOrderBookData(IndependentReserveOrderBookData):
    pass


class IndependentReserveWssOrderBookData(IndependentReserveOrderBookData):
    pass
