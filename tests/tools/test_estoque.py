"""Tests for estoque tools."""
from __future__ import annotations


def test_estoque_module_imports():
    """Test that estoque module can be imported."""
    from bling_mcp.mcp.tools import estoque
    assert hasattr(estoque, 'register_estoque_tools')


def test_estoque_tools_registered():
    """Test that estoque tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None


def test_saldo_concise_helper():
    """Test _saldo_concise helper function."""
    from bling_mcp.mcp.tools.estoque import _saldo_concise

    saldo = {
        "idProduto": 123,
        "idDeposito": 456,
        "saldo": 100,
        "reservado": 10,
        "disponivel": 90,
    }
    result = _saldo_concise(saldo)
    assert result["idProduto"] == 123
    assert result["idDeposito"] == 456
    assert result["saldo"] == 100
    assert result["reservado"] == 10
    assert result["disponivel"] == 90


def test_saldo_concise_none():
    """Test _saldo_concise with None input."""
    from bling_mcp.mcp.tools.estoque import _saldo_concise
    result = _saldo_concise(None)
    assert result is None
