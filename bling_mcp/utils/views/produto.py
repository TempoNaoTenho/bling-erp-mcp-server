"""Produto view helpers (concise, detailed, includes, variacoes)."""

from __future__ import annotations

from typing import Any


def _first_defined(value: dict[str, Any] | None, keys: list[str]) -> Any:
    if not value:
        return None
    for key in keys:
        if value.get(key) is not None:
            return value[key]
    return None


def produto_concise(produto: dict[str, Any] | None) -> dict[str, Any] | None:
    if not produto:
        return None
    return {
        "id": _first_defined(produto, ["id", "idProduto"]),
        "nome": produto.get("nome"),
        "codigo": produto.get("codigo"),
        "preco": _first_defined(produto, ["preco", "precoVenda", "precoVenda1", "valorVenda"]),
        "tipo": produto.get("tipo"),
        "situacao": produto.get("situacao"),
        "unidade": _first_defined(produto, ["unidade", "un"]),
        "gtin": produto.get("gtin"),
        "marca": _first_defined(produto, ["marca", "marcaDescricao", "marcaProduto"]),
        "imagemURL": _first_defined(produto, ["imagemURL", "imagemUrl", "urlImagem", "imagem"]),
    }


def extract_variacoes(produto: dict[str, Any] | None) -> list[Any]:
    if not produto:
        return []
    variacoes = produto.get("variacoes") or produto.get("variacoesProduto")
    if isinstance(variacoes, list):
        return variacoes
    if isinstance(variacoes, dict):
        if isinstance(variacoes.get("data"), list):
            return variacoes["data"]
        if isinstance(variacoes.get("items"), list):
            return variacoes["items"]
        if isinstance(variacoes.get("variacoes"), list):
            return variacoes["variacoes"]
    return []


def variacoes_preview(variacoes: list[Any], limite: int) -> dict[str, Any]:
    preview = []
    for v in variacoes[:limite]:
        var = v.get("variacao") if isinstance(v, dict) else None
        preview.append({
            "id": v.get("id") or v.get("idVariacao") or v.get("idProduto") if isinstance(v, dict) else None,
            "codigo": v.get("codigo") if isinstance(v, dict) else None,
            "preco": v.get("preco") or v.get("precoVenda") if isinstance(v, dict) else None,
            "situacao": v.get("situacao") if isinstance(v, dict) else None,
            "variacao": {"nome": var.get("nome"), "ordem": var.get("ordem")} if isinstance(var, dict) else None,
        })
    return {"total": len(variacoes), "preview": preview, "truncated": len(variacoes) > limite}


def apply_produto_includes(
    base: dict[str, Any] | None,
    produto: dict[str, Any] | None,
    include: list[str],
    preview_items: int = 5,
) -> dict[str, Any] | None:
    if not base or not produto:
        return base
    inc = set(include)
    if "estoque" in inc:
        base["estoque"] = produto.get("estoque") or produto.get("saldoEstoque") or produto.get("estoques")
    if "fornecedor" in inc:
        base["fornecedor"] = produto.get("fornecedor") or produto.get("fornecedores")
    if "categoria" in inc:
        base["categoria"] = produto.get("categoria") or produto.get("categorias")
    if "tributacao" in inc:
        base["tributacao"] = produto.get("tributacao") or produto.get("tributos")
    if "midia" in inc:
        base["midia"] = produto.get("midia") or produto.get("imagens") or produto.get("fotos")
    if "variacoes" in inc:
        base["variacoes"] = variacoes_preview(extract_variacoes(produto), preview_items)
    return base
