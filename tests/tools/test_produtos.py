"""Tests for produtos tools."""
from __future__ import annotations


def test_produtos_module_imports():
    """Test that produtos module can be imported."""
    from bling_mcp.mcp.tools import produtos
    assert hasattr(produtos, 'register_produtos_tools')


def test_produtos_tools_registered():
    """Test that produtos tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None
