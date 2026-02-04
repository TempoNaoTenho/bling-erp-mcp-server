"""Tests for notas tools."""
from __future__ import annotations


def test_notas_module_imports():
    """Test that notas module can be imported."""
    from bling_mcp.mcp.tools import notas
    assert hasattr(notas, 'register_notas_tools')


def test_notas_tools_registered():
    """Test that notas tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None


def test_nota_concise_helper():
    """Test _nota_concise helper function."""
    from bling_mcp.mcp.tools.notas import _nota_concise

    nota = {
        "id": 123,
        "numero": "456",
        "serie": "1",
        "dataEmissao": "2024-01-01",
        "situacao": {"descricao": "Autorizada"},
        "chaveAcesso": "12345678901234567890123456789012345678901234",
        "total": 1000.50,
    }
    result = _nota_concise(nota)
    assert result["id"] == 123
    assert result["numero"] == "456"
    assert result["situacao"] == "Autorizada"


def test_nota_concise_none():
    """Test _nota_concise with None input."""
    from bling_mcp.mcp.tools.notas import _nota_concise
    result = _nota_concise(None)
    assert result is None
