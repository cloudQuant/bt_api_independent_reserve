"""Tests for IndependentReserveExchangeData container."""

from __future__ import annotations

from bt_api_independent_reserve.exchange_data import (
    IndependentReserveExchangeData,
)


class TestIndependentReserveExchangeData:
    """Tests for IndependentReserveExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = IndependentReserveExchangeData()

        assert exchange.exchange_name == "INDEPENDENT_RESERVE___SPOT"
