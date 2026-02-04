"""FastMCP 3.x dependency injection."""
from __future__ import annotations
from typing import Annotated
from fastmcp import Context
from bling_mcp.utils.bling_client import BlingClient
from bling_mcp.config import Settings, get_config


def get_bling_client_dep() -> BlingClient:
    """Factory for BlingClient."""
    return BlingClient()


def get_settings_dep() -> Settings:
    """Factory for Settings."""
    return get_config()


# Type aliases for tool parameters
BlingClientDep = Annotated[BlingClient, Context(get_bling_client_dep)]
SettingsDep = Annotated[Settings, Context(get_settings_dep)]
