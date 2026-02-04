"""Bling pedidos (vendas) tools."""

from __future__ import annotations

from typing import Annotated, Any

from bling_mcp.utils.bling_client import get_bling_client
from bling_mcp.mcp.app import get_mcp
from bling_mcp.mcp.tool_helpers import (
    READ_ONLY_ANNOTATIONS,
    build_tool_envelope,
    build_error_result,
    unwrap_data_array,
    unwrap_data_object,
    infer_next_page,
)
from bling_mcp.mcp.tool_models import (
    PedidoDetail,
    PedidoInclude,
    PedidosListData,
    ResponseFormat,
    SituacoesListData,
    ToolEnvelope,
)
from pydantic import Field


def _pedido_concise(pedido: dict[str, Any] | None) -> dict[str, Any] | None:
    if not pedido:
        return None
    contato = pedido.get("contato") or pedido.get("cliente")
    return {
        "id": pedido.get("id") or pedido.get("idPedido"),
        "numero": pedido.get("numero") or pedido.get("numeroPedido"),
        "data": pedido.get("data") or pedido.get("dataEmissao"),
        "situacao": pedido.get("situacao", {}).get("descricao") if isinstance(pedido.get("situacao"), dict) else pedido.get("situacao"),
        "total": pedido.get("total") or pedido.get("totalVenda") or pedido.get("valor"),
        "cliente": {"id": contato.get("id"), "nome": contato.get("nome")} if contato else None,
    }


def _params_pedidos_list(args: dict[str, Any]) -> list[tuple[str, Any]]:
    params = [("pagina", args.get("pagina", 1)), ("limite", args.get("limite", 50))]
    for key in ["idContato", "dataInicial", "dataFinal", "dataAlteracaoInicial", "dataAlteracaoFinal",
                "dataPrevistaInicial", "dataPrevistaFinal", "numero", "idLoja", "idVendedor", "idControleCaixa"]:
        if args.get(key) is not None:
            params.append((key, args[key]))
    if args.get("idsSituacoes"):
        for i in args["idsSituacoes"]:
            params.append(("idsSituacoes[]", i))
    if args.get("numerosLojas"):
        for n in args["numerosLojas"]:
            params.append(("numerosLojas[]", n))
    return params


def register_pedidos_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    client = get_bling_client()

    @mcp.tool(
        description="Lista pedidos de venda com filtros.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_pedidos_list(
        pagina: Annotated[int, Field(ge=1, description="Numero da pagina.")] = 1,
        limite: Annotated[int, Field(ge=1, description="Quantidade de registros por pagina.")] = 50,
        idContato: Annotated[int | None, Field(description="ID do contato.")] = None,
        idsSituacoes: Annotated[
            list[int] | None,
            Field(description="Conjunto de IDs de situacoes."),
        ] = None,
        idSituacao: Annotated[
            int | None,
            Field(description="Alias para idsSituacoes (um unico ID)."),
        ] = None,
        dataInicial: Annotated[str | None, Field(description="Data inicial (YYYY-MM-DD).")] = None,
        dataFinal: Annotated[str | None, Field(description="Data final (YYYY-MM-DD).")] = None,
        dataAlteracaoInicial: Annotated[
            str | None,
            Field(description="Data inicial da alteracao (YYYY-MM-DD)."),
        ] = None,
        dataAlteracaoFinal: Annotated[
            str | None,
            Field(description="Data final da alteracao (YYYY-MM-DD)."),
        ] = None,
        dataPrevistaInicial: Annotated[
            str | None,
            Field(description="Data inicial prevista (YYYY-MM-DD)."),
        ] = None,
        dataPrevistaFinal: Annotated[
            str | None,
            Field(description="Data final prevista (YYYY-MM-DD)."),
        ] = None,
        numero: Annotated[int | None, Field(description="Numero do pedido de venda.")] = None,
        idLoja: Annotated[int | None, Field(description="ID da loja.")] = None,
        idVendedor: Annotated[int | None, Field(description="ID do vendedor.")] = None,
        idControleCaixa: Annotated[int | None, Field(description="ID do controle de caixa.")] = None,
        numerosLojas: Annotated[
            list[str] | None,
            Field(description="Conjunto de numeros de pedidos nas lojas."),
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
    ) -> ToolEnvelope[PedidosListData]:
        """Lista pedidos de venda paginados. Prefira idsSituacoes/numero/idContato e limite menor."""
        try:
            args = {k: v for k, v in locals().items() if v is not None and k != 'client'}
            args["idsSituacoes"] = idsSituacoes or ([idSituacao] if idSituacao is not None else None)
            params = _params_pedidos_list(args)
            raw = client.get("/pedidos/vendas", params=params if params else None)
            items = unwrap_data_array(raw)
            data = {"items": [_pedido_concise(p) for p in items if isinstance(p, dict)]}
            next_page = infer_next_page(raw, {"pagina": pagina, "limite": limite})
            return build_tool_envelope(
                name="bling_pedidos_list",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                next_page=next_page,
                hint="Use bling_pedidos_get para detalhes. Ajuste limite/maxItems para reduzir tokens.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem um pedido de venda pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_pedidos_get(
        idPedido: Annotated[int, Field(ge=1, description="ID do pedido de venda.")],
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        include: Annotated[
            list[PedidoInclude] | None,
            Field(description="Inclui blocos adicionais: itens, parcelas, transporte."),
        ] = None,
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
    ) -> ToolEnvelope[PedidoDetail | None]:
        """Obtem um pedido de venda pelo ID. Use include apenas quando necessario."""
        try:
            raw = client.get(f"/pedidos/vendas/{idPedido}")
            pedido = unwrap_data_object(raw)
            data = _pedido_concise(pedido) if pedido else None
            if data and pedido and include:
                inc = set(include)
                if "itens" in inc:
                    data["itens"] = pedido.get("itens") or pedido.get("itensPedido")
                if "parcelas" in inc:
                    data["parcelas"] = pedido.get("parcelas") or pedido.get("financeiro")
                if "transporte" in inc:
                    data["transporte"] = pedido.get("transporte")
            return build_tool_envelope(
                name="bling_pedidos_get",
                raw=raw,
                data=data,
                response_format=responseFormat,
                include=list(include or []),
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Lista situacoes de um modulo do sistema.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_situacoes_list(
        idModuloSistema: Annotated[
            int | None,
            Field(description="ID do modulo do sistema (OpenAPI: idModuloSistema)."),
        ] = None,
        idModulo: Annotated[
            int | None,
            Field(description="Alias legado para idModuloSistema."),
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
    ) -> ToolEnvelope[SituacoesListData]:
        """Lista situacoes disponiveis para um modulo do sistema."""
        try:
            modulo_id = idModuloSistema if idModuloSistema is not None else idModulo
            if modulo_id is None:
                modulo_id = 9835
            raw = client.get(f"/situacoes/modulos/{modulo_id}")
            items = unwrap_data_array(raw)
            data = {"items": [{"id": s.get("id"), "descricao": s.get("descricao"), "cor": s.get("cor")} for s in items if isinstance(s, dict)]}
            return build_tool_envelope(
                name="bling_situacoes_list",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                hint="Se necessario, obtenha o ID do modulo em /situacoes/modulos.",
            )
        except Exception as e:
            return build_error_result(str(e))
