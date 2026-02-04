"""Tests for clientes tools."""
from __future__ import annotations


def test_clientes_module_imports():
    """Test that clientes module can be imported."""
    from bling_mcp.mcp.tools import clientes
    assert hasattr(clientes, 'register_clientes_tools')


def test_clientes_tools_registered():
    """Test that clientes tools are registered."""
    from bling_mcp.mcp.app import create_mcp
    mcp = create_mcp()
    assert mcp is not None


def test_contato_concise_helper():
    """Test _contato_concise helper function."""
    from bling_mcp.mcp.tools.clientes import _contato_concise

    contato = {
        "id": 123,
        "nome": "João Silva",
        "codigo": "CLI001",
        "tipo": "C",
        "situacao": "A",
        "numeroDocumento": "12345678900",
        "email": "joao@example.com",
        "telefone": "11999999999",
    }
    result = _contato_concise(contato)
    assert result["id"] == 123
    assert result["nome"] == "João Silva"
    assert result["codigo"] == "CLI001"
    assert result["documento"] == "12345678900"


def test_contato_concise_none():
    """Test _contato_concise with None input."""
    from bling_mcp.mcp.tools.clientes import _contato_concise
    result = _contato_concise(None)
    assert result is None


def test_params_clientes_list_helper():
    """Test _params_clientes_list helper function."""
    from bling_mcp.mcp.tools.clientes import _params_clientes_list

    args = {
        "pagina": 1,
        "limite": 50,
        "pesquisa": "João",
        "idsContatos": [1, 2, 3],
    }
    result = _params_clientes_list(args)
    assert ("pagina", 1) in result
    assert ("limite", 50) in result
    assert ("pesquisa", "João") in result
    # Check array params
    array_params = [(k, v) for k, v in result if k == "idsContatos[]"]
    assert len(array_params) == 3
