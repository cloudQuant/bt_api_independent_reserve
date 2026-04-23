from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _independent_reserve_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_independent_reserve.exchange_data import IndependentReserveExchangeDataSpot
from bt_api_independent_reserve.feeds.live_independent_reserve.spot import (
    IndependentReserveRequestDataSpot,
)


def register_independent_reserve(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("INDEPENDENT_RESERVE___SPOT", IndependentReserveRequestDataSpot)
    registry.register_exchange_data("INDEPENDENT_RESERVE___SPOT", IndependentReserveExchangeDataSpot)
    registry.register_balance_handler("INDEPENDENT_RESERVE___SPOT", _independent_reserve_balance_handler)
