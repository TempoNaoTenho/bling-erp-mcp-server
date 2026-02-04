"""Tests for dependency injection."""
from __future__ import annotations
import pytest
from bling_mcp.mcp.dependencies import (
    get_bling_client_dep,
    get_settings_dep,
    BlingClientDep,
    SettingsDep,
)
from bling_mcp.utils.bling_client import BlingClient
from bling_mcp.config import Settings


def test_get_bling_client_dep():
    """Test BlingClient factory returns instance."""
    client = get_bling_client_dep()
    assert isinstance(client, BlingClient)


def test_get_settings_dep():
    """Test Settings factory returns instance."""
    settings = get_settings_dep()
    assert isinstance(settings, Settings)


def test_bling_client_dep_type_alias():
    """Test BlingClientDep type alias is defined."""
    assert BlingClientDep is not None


def test_settings_dep_type_alias():
    """Test SettingsDep type alias is defined."""
    assert SettingsDep is not None
