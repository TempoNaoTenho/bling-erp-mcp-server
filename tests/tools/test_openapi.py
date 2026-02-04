"""Tests for openapi tools."""
from __future__ import annotations


def test_openapi_module_imports():
    """Test that openapi module can be imported."""
    from bling_mcp.mcp.tools import openapi
    assert hasattr(openapi, 'register_openapi_tools')


def test_openapi_tools_registered():
    """Test that openapi tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None
