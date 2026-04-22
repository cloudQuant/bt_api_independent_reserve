from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.bars.bar import BarData
from bt_api_base.functions.utils import from_dict_get_float


class IndependentReserveBarData(BarData):
    def __init__(
        self,
        bar_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(bar_info, has_been_json_encoded)
        self.exchange_name = "INDEPENDENT_RESERVE"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.bar_data: dict[str, Any] | None = (
            bar_info if has_been_json_encoded and isinstance(bar_info, dict) else None
        )
        self.open_time: int | None = None
        self.open_price: float | None = None
        self.high_price: float | None = None
        self.low_price: float | None = None
        self.close_price: float | None = None
        self.volume: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> IndependentReserveBarData:
        if not self.has_been_json_encoded:
            self.bar_data = json.loads(self.bar_info) if isinstance(self.bar_info, str) else {}
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.bar_data, list) and len(self.bar_data) >= 5:
            data_list = list(self.bar_data)
            self.open_time = int(float(data_list[0]) if len(data_list) > 0 else 0)
            self.open_price = float(data_list[1]) if len(data_list) > 1 else 0.0
            self.high_price = float(data_list[2]) if len(data_list) > 2 else 0.0
            self.low_price = float(data_list[3]) if len(data_list) > 3 else 0.0
            self.close_price = float(data_list[4]) if len(data_list) > 4 else 0.0
            if len(data_list) > 5:
                self.volume = float(data_list[5])
        elif isinstance(self.bar_data, dict):
            data = self.bar_data
            self.open_time = int(from_dict_get_float(data, "Timestamp") or 0)
            self.open_price = from_dict_get_float(data, "OpenPrice")
            self.high_price = from_dict_get_float(data, "HighPrice")
            self.low_price = from_dict_get_float(data, "LowPrice")
            self.close_price = from_dict_get_float(data, "ClosePrice")
            self.volume = from_dict_get_float(data, "Volume")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name or ""

    def get_symbol_name(self) -> str:
        return self.symbol_name or ""

    def get_asset_type(self) -> str:
        return self.asset_type or ""

    def get_open_time(self) -> float | int:
        self.init_data()
        return self.open_time or 0

    def get_open_price(self) -> float | int:
        self.init_data()
        return self.open_price or 0.0

    def get_high_price(self) -> float | int:
        self.init_data()
        return self.high_price or 0.0

    def get_low_price(self) -> float | int:
        self.init_data()
        return self.low_price or 0.0

    def get_close_price(self) -> float | int:
        self.init_data()
        return self.close_price or 0.0

    def get_volume(self) -> float | int:
        self.init_data()
        return self.volume or 0.0


class IndependentReserveRequestBarData(IndependentReserveBarData):
    pass


class IndependentReserveWssBarData(IndependentReserveBarData):
    pass
