"""Bling estoque (saldos) tools."""

from __future__ import annotations

from typing import Annotated, Any

from bling_mcp.utils.bling_client import get_bling_client
from bling_mcp.mcp.app import get_mcp
from bling_mcp.mcp.tool_helpers import (
    READ_ONLY_ANNOTATIONS,
    build_tool_envelope,
    build_error_result,
    unwrap_data_array,
)
from bling_mcp.mcp.tool_models import (
    EstoqueSaldosData,
    ResponseFormat,
    SaldoFiltro,
    ToolEnvelope,
)
from pydantic import Field


def _saldo_concise(saldo: dict[str, Any] | None) -> dict[str, Any] | None:
    if not saldo:
        return None
    return {
        "idProduto": saldo.get("idProduto") or (saldo.get("produto") or {}).get("id"),
        "idDeposito": saldo.get("idDeposito") or (saldo.get("deposito") or {}).get("id"),
        "saldo": saldo.get("saldo") or saldo.get("quantidade"),
        "reservado": saldo.get("reservado"),
        "disponivel": saldo.get("disponivel"),
    }


def register_estoque_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    client = get_bling_client()

    @mcp.tool(
        description="Consulta saldos de estoque em todos os depositos.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_estoque_saldos(
        idsProdutos: Annotated[
            list[int],
            Field(description="IDs dos produtos (obrigatorio)."),
        ],
        codigos: Annotated[
            list[str] | None,
            Field(description="Codigos dos produtos (SKU)."),
        ] = None,
        filtroSaldoEstoque: Annotated[
            SaldoFiltro | None,
            Field(description="Filtro de saldo (0=zerado, 1=positivo, 2=negativo)."),
        ] = None,
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        maxItems: Annotated[
            int,
            Field(ge=1, description="Limite de itens em arrays retornados."),
        ] = 50,
        maxChars: Annotated[
            int,
            Field(ge=1000, description="Limite de caracteres no payload final."),
        ] = 30000,
        rawAsResource: Annotated[
            bool,
            Field(description="Se true e responseFormat=raw, retorna um resourceUri."),
        ] = True,
    ) -> ToolEnvelope[EstoqueSaldosData]:
        """Consulta saldos de estoque em todos os depositos. idsProdutos e obrigatorio."""
        try:
            if not idsProdutos:
                return build_error_result("idsProdutos e obrigatorio. Informe ao menos um ID.")
            params: list[tuple[str, Any]] = []
            for i in idsProdutos:
                params.append(("idsProdutos[]", i))
            if codigos:
                for c in codigos:
                    params.append(("codigos[]", c))
            if filtroSaldoEstoque is not None:
                params.append(("filtroSaldoEstoque", filtroSaldoEstoque))
            raw = client.get("/estoques/saldos", params=params if params else None)
            items = unwrap_data_array(raw)
            data = {"items": [_saldo_concise(s) for s in items if isinstance(s, dict)]}
            return build_tool_envelope(
                name="bling_estoque_saldos",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Consulta saldos de estoque por deposito.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_estoque_saldos_por_deposito(
        idDeposito: Annotated[int, Field(description="ID do deposito (obrigatorio).")],
        idsProdutos: Annotated[
            list[int],
            Field(description="IDs dos produtos (obrigatorio)."),
        ],
        codigos: Annotated[
            list[str] | None,
            Field(description="Codigos dos produtos (SKU)."),
        ] = None,
        filtroSaldoEstoque: Annotated[
            SaldoFiltro | None,
            Field(description="Filtro de saldo (0=zerado, 1=positivo, 2=negativo)."),
        ] = None,
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        maxItems: Annotated[
            int,
            Field(ge=1, description="Limite de itens em arrays retornados."),
        ] = 50,
        maxChars: Annotated[
            int,
            Field(ge=1000, description="Limite de caracteres no payload final."),
        ] = 30000,
        rawAsResource: Annotated[
            bool,
            Field(description="Se true e responseFormat=raw, retorna um resourceUri."),
        ] = True,
    ) -> ToolEnvelope[EstoqueSaldosData]:
        """Consulta saldos de estoque para um deposito. idsProdutos e obrigatorio."""
        try:
            if not idsProdutos:
                return build_error_result("idsProdutos e obrigatorio. Informe ao menos um ID.")
            params: list[tuple[str, Any]] = []
            for i in idsProdutos:
                params.append(("idsProdutos[]", i))
            if codigos:
                for c in codigos:
                    params.append(("codigos[]", c))
            if filtroSaldoEstoque is not None:
                params.append(("filtroSaldoEstoque", filtroSaldoEstoque))
            raw = client.get(f"/estoques/saldos/{idDeposito}", params=params if params else None)
            items = unwrap_data_array(raw)
            data = {"items": [_saldo_concise(s) for s in items if isinstance(s, dict)]}
            return build_tool_envelope(
                name="bling_estoque_saldos_por_deposito",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
            )
        except Exception as e:
            return build_error_result(str(e))
