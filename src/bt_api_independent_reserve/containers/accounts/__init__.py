"""Module-level docstring."""

from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.accounts.account import AccountData


class IndependentReserveAccountData(AccountData):
    """Class IndependentReserveAccountData"""

    def __init__(
        self,
        account_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        """__init__ method"""
        super().__init__(account_info, has_been_json_encoded)
        self.exchange_name = "INDEPENDENT_RESERVE"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.account_data: dict[str, Any] | str | None = (
            account_info if has_been_json_encoded and isinstance(account_info, dict) else None
        )
        self.balances: list[Any] = []
        self.all_data: dict[str, Any] | None = None
        self.has_been_init_data = False

    def init_data(self) -> IndependentReserveAccountData:
        """init_data method"""
        if not self.has_been_json_encoded:
            self.account_data = json.loads(self.account_info) if isinstance(self.account_info, str) else {}
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.account_data, dict):
            data = self.account_data
            balances = data.get("Accounts", [])
            self.balances = balances if isinstance(balances, list) else []

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        """get_exchange_name method"""
        return self.exchange_name or ""

    def get_symbol_name(self) -> str:
        """get_symbol_name method"""
        return self.symbol_name or ""

    def get_asset_type(self) -> str:
        """get_asset_type method"""
        return self.asset_type or ""

    def get_balances(self) -> list[Any]:
        """get_balances method"""
        self.init_data()
        return self.balances

    def get_all_data(self) -> dict[str, Any]:
        """get_all_data method"""
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "balances": self.balances,
            }
        return self.all_data

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class IndependentReserveRequestAccountData(IndependentReserveAccountData):
    """Class IndependentReserveRequestAccountData"""

    pass


class IndependentReserveWssAccountData(IndependentReserveAccountData):
    """Class IndependentReserveWssAccountData"""

    pass
