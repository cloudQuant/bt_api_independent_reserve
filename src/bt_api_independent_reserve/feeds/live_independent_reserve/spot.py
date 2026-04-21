from __future__ import annotations

from typing import Any

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_independent_reserve.feeds.live_independent_reserve.request_base import (
    IndependentReserveRequestData,
)


class IndependentReserveRequestDataSpot(IndependentReserveRequestData):
    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        kwargs.setdefault("exchange_name", "INDEPENDENT_RESERVE___SPOT")
        kwargs.setdefault("asset_type", "SPOT")
        super().__init__(data_queue, **kwargs)

    def get_tick(self, symbol: Any, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_tick(
        self, symbol: Any, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    get_ticker = get_tick
    async_get_ticker = async_get_tick

    def get_depth(
        self, symbol: Any, count: int = 20, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_depth(symbol, extra_data, count=count, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_depth(
        self, symbol: Any, count: int = 20, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_depth(symbol, extra_data, count=count, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_exchange_info(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_exchange_info(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_balance(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_balance(
        self, symbol: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_account(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_account(
        self, symbol: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_account(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_open_orders(
        self, symbol: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_open_orders(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_open_orders(
        self, symbol: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_open_orders(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def make_order(
        self,
        symbol: Any,
        volume: Any,
        price: Any = None,
        order_type: Any = "buy-limit",
        offset: str = "open",
        post_only: bool = False,
        client_order_id: Any = None,
        extra_data: Any = None,
        **kwargs: Any,
    ) -> RequestData:
        side = "buy" if "buy" in str(order_type).lower() else "sell"
        path, params, extra = self._make_order(
            symbol, side, order_type, volume, price, extra_data, **kwargs
        )
        return self.request(path, params, extra_data=extra)

    async def async_make_order(
        self,
        symbol: Any,
        volume: Any,
        price: Any = None,
        order_type: Any = "buy-limit",
        offset: str = "open",
        post_only: bool = False,
        client_order_id: Any = None,
        extra_data: Any = None,
        **kwargs: Any,
    ) -> RequestData:
        side = "buy" if "buy" in str(order_type).lower() else "sell"
        path, params, extra = self._make_order(
            symbol, side, order_type, volume, price, extra_data, **kwargs
        )
        return await self.async_request(path, params, extra_data=extra)

    def cancel_order(
        self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_cancel_order(
        self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)
