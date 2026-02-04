"""Tests for pedidos tools."""
from __future__ import annotations


def test_pedidos_module_imports():
    """Test that pedidos module can be imported."""
    from bling_mcp.mcp.tools import pedidos
    assert hasattr(pedidos, 'register_pedidos_tools')


def test_pedidos_tools_registered():
    """Test that pedidos tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None


def test_pedido_concise_helper():
    """Test _pedido_concise helper function."""
    from bling_mcp.mcp.tools.pedidos import _pedido_concise

    pedido = {
        "id": 123,
        "numero": "456",
        "data": "2024-01-01",
        "situacao": {"descricao": "Em andamento"},
        "total": 1000.50,
        "contato": {"id": 789, "nome": "Cliente Teste"},
    }
    result = _pedido_concise(pedido)
    assert result["id"] == 123
    assert result["numero"] == "456"
    assert result["situacao"] == "Em andamento"
    assert result["cliente"]["id"] == 789


def test_pedido_concise_none():
    """Test _pedido_concise with None input."""
    from bling_mcp.mcp.tools.pedidos import _pedido_concise
    result = _pedido_concise(None)
    assert result is None


def test_params_pedidos_list_helper():
    """Test _params_pedidos_list helper function."""
    from bling_mcp.mcp.tools.pedidos import _params_pedidos_list

    args = {
        "pagina": 1,
        "limite": 50,
        "idContato": 123,
        "idsSituacoes": [1, 2, 3],
        "numero": 456,
    }
    result = _params_pedidos_list(args)
    assert ("pagina", 1) in result
    assert ("limite", 50) in result
    assert ("idContato", 123) in result
    assert ("numero", 456) in result
    # Check array params
    array_params = [(k, v) for k, v in result if k == "idsSituacoes[]"]
    assert len(array_params) == 3
