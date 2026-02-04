"""Bling produtos tools."""

from __future__ import annotations

from typing import Annotated, Any

from bling_mcp.utils.views.produto import (
    apply_produto_includes,
    produto_concise,
    variacoes_preview,
)
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
    ProdutoCriterio,
    ProdutoDetail,
    ProdutoInclude,
    ProdutoLotesSaldoTotalData,
    ProdutoTipo,
    ProdutoTributacaoData,
    ProdutoEstoqueData,
    ProdutosListData,
    ResponseFormat,
    SaldoFiltro,
    ToolEnvelope,
    VariacoesPreviewData,
)
from pydantic import Field


def register_produtos_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    client = get_bling_client()

    @mcp.tool(
        description="Lista produtos com filtros e paginacao.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_list(
        pagina: Annotated[int, Field(ge=1, description="Numero da pagina.")] = 1,
        limite: Annotated[int, Field(ge=1, description="Quantidade de registros por pagina.")] = 50,
        criterio: Annotated[
            ProdutoCriterio | None,
            Field(description="Criterio de listagem (1..5)."),
        ] = None,
        tipo: Annotated[
            ProdutoTipo | None,
            Field(description="Tipo do produto (T, P, S, E, PS, C, V)."),
        ] = None,
        idComponente: Annotated[int | None, Field(description="ID do componente (usado quando tipo=E).")] = None,
        dataInclusaoInicial: Annotated[
            str | None,
            Field(description="Data de inclusao inicial (YYYY-MM-DD)."),
        ] = None,
        dataInclusaoFinal: Annotated[
            str | None,
            Field(description="Data de inclusao final (YYYY-MM-DD)."),
        ] = None,
        dataAlteracaoInicial: Annotated[
            str | None,
            Field(description="Data de alteracao inicial (YYYY-MM-DD)."),
        ] = None,
        dataAlteracaoFinal: Annotated[
            str | None,
            Field(description="Data de alteracao final (YYYY-MM-DD)."),
        ] = None,
        idCategoria: Annotated[int | None, Field(description="ID da categoria do produto.")] = None,
        idLoja: Annotated[int | None, Field(description="ID da loja.")] = None,
        nome: Annotated[str | None, Field(description="Nome do produto.")] = None,
        idsProdutos: Annotated[
            list[int] | None,
            Field(description="IDs dos produtos."),
        ] = None,
        codigos: Annotated[
            list[str] | None,
            Field(description="Codigos (SKU) dos produtos."),
        ] = None,
        codigo: Annotated[
            str | None,
            Field(description="Alias para um unico codigo (SKU)."),
        ] = None,
        gtins: Annotated[
            list[str] | None,
            Field(description="GTINs/EANs dos produtos."),
        ] = None,
        filtroSaldoEstoque: Annotated[
            SaldoFiltro | None,
            Field(description="Filtro de saldo em estoque (0=zerado, 1=positivo, 2=negativo)."),
        ] = None,
        filtroSaldoEstoqueDeposito: Annotated[
            int | None,
            Field(description="ID do deposito para considerar no filtro de saldo."),
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
    ) -> ToolEnvelope[ProdutosListData]:
        """Lista produtos paginados. Prefira filtros por ID/codigo/GTIN e limite menor."""
        try:
            params: list[tuple[str, Any]] = [("pagina", pagina), ("limite", limite)]
            if criterio is not None:
                params.append(("criterio", criterio))
            if tipo:
                params.append(("tipo", tipo))
            if idComponente is not None:
                params.append(("idComponente", idComponente))
            if dataInclusaoInicial:
                params.append(("dataInclusaoInicial", dataInclusaoInicial))
            if dataInclusaoFinal:
                params.append(("dataInclusaoFinal", dataInclusaoFinal))
            if dataAlteracaoInicial:
                params.append(("dataAlteracaoInicial", dataAlteracaoInicial))
            if dataAlteracaoFinal:
                params.append(("dataAlteracaoFinal", dataAlteracaoFinal))
            if idCategoria is not None:
                params.append(("idCategoria", idCategoria))
            if idLoja is not None:
                params.append(("idLoja", idLoja))
            if nome:
                params.append(("nome", nome))
            cods = codigos or ([codigo] if codigo else None)
            if idsProdutos:
                for i in idsProdutos:
                    params.append(("idsProdutos[]", i))
            if cods:
                for c in cods:
                    params.append(("codigos[]", c))
            if gtins:
                for g in gtins:
                    params.append(("gtins[]", g))
            if filtroSaldoEstoque is not None:
                params.append(("filtroSaldoEstoque", filtroSaldoEstoque))
            if filtroSaldoEstoqueDeposito is not None:
                params.append(("filtroSaldoEstoqueDeposito", filtroSaldoEstoqueDeposito))
            raw = client.get("/produtos", params=params)
            items = unwrap_data_array(raw)
            data = {"items": [produto_concise(p) for p in items if isinstance(p, dict)]}
            next_page = infer_next_page(raw, {"pagina": pagina, "limite": limite})
            return build_tool_envelope(
                name="bling_produtos_list",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                next_page=next_page,
                hint="Use bling_produtos_get para detalhes. Ajuste limite/maxItems para reduzir tokens.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem detalhes de um produto pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_get(
        idProduto: Annotated[int, Field(ge=1, description="ID do produto.")],
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        include: Annotated[
            list[ProdutoInclude] | None,
            Field(description="Inclui blocos adicionais (estoque, fornecedor, categoria, tributacao, midia, variacoes)."),
        ] = None,
        previewItems: Annotated[
            int,
            Field(ge=1, description="Limite de variacoes no preview (quando include=variacoes)."),
        ] = 5,
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
    ) -> ToolEnvelope[ProdutoDetail | None]:
        """Obtem detalhes de um produto pelo ID. Use include para trazer apenas blocos necessarios."""
        try:
            raw = client.get(f"/produtos/{idProduto}")
            produto = unwrap_data_object(raw)
            base = produto_concise(produto) if produto else None
            if base and produto:
                base = apply_produto_includes(base, produto, include or [], previewItems)
            return build_tool_envelope(
                name="bling_produtos_get",
                raw=raw,
                data=base,
                response_format=responseFormat,
                include=list(include or []),
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                hint="Use include=['estoque','fornecedor','categoria','tributacao','midia','variacoes'] para detalhar.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem estoque resumido de um produto pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_get_estoque(
        idProduto: Annotated[int, Field(ge=1, description="ID do produto.")],
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
    ) -> ToolEnvelope[ProdutoEstoqueData]:
        """Obtem estoque resumido de um produto pelo ID (economiza tokens)."""
        try:
            raw = client.get(f"/produtos/{idProduto}")
            produto = unwrap_data_object(raw)
            data = {
                "idProduto": (produto or {}).get("id") or idProduto,
                "estoque": (produto or {}).get("estoque") or (produto or {}).get("saldoEstoque") or (produto or {}).get("estoques"),
            }
            return build_tool_envelope(
                name="bling_produtos_get_estoque",
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
        description="Obtem tributacao resumida de um produto pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_get_tributacao(
        idProduto: Annotated[int, Field(ge=1, description="ID do produto.")],
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
    ) -> ToolEnvelope[ProdutoTributacaoData]:
        """Obtem tributacao resumida de um produto pelo ID (economiza tokens)."""
        try:
            raw = client.get(f"/produtos/{idProduto}")
            produto = unwrap_data_object(raw)
            data = {
                "idProduto": (produto or {}).get("id") or idProduto,
                "tributacao": (produto or {}).get("tributacao") or (produto or {}).get("tributos"),
            }
            return build_tool_envelope(
                name="bling_produtos_get_tributacao",
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
        description="Lista variacoes de um produto com preview limitado.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_list_variacoes(
        idProduto: Annotated[int, Field(ge=1, description="ID do produto pai.")],
        previewItems: Annotated[
            int,
            Field(ge=1, description="Limite de variacoes no preview."),
        ] = 5,
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
    ) -> ToolEnvelope[VariacoesPreviewData]:
        """Lista variacoes de um produto com preview limitado."""
        try:
            raw = client.get(f"/produtos/variacoes/{idProduto}")
            items = unwrap_data_array(raw)
            data = variacoes_preview(items, previewItems)
            return build_tool_envelope(
                name="bling_produtos_list_variacoes",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                hint="Use previewItems para ajustar o limite.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem o saldo total de lotes de um produto (opcionalmente por deposito).",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_produtos_lotes_saldo_total(
        idProduto: Annotated[int, Field(ge=1, description="ID do produto.")],
        idDeposito: Annotated[int | None, Field(description="ID do deposito (opcional).")] = None,
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
    ) -> ToolEnvelope[ProdutoLotesSaldoTotalData]:
        """Obtem o saldo total de lotes de um produto (opcionalmente por deposito)."""
        try:
            if idDeposito is not None:
                raw = client.get(f"/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma")
            else:
                raw = client.get(f"/produtos/{idProduto}/lotes/saldo/soma")
            data_obj = raw if isinstance(raw, dict) else {}
            data = {
                "idProduto": idProduto,
                "idDeposito": idDeposito,
                "saldoTotal": data_obj.get("saldoTotal") or data_obj.get("saldo") or data_obj.get("total"),
            }
            return build_tool_envelope(
                name="bling_produtos_lotes_saldo_total",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
            )
        except Exception as e:
            return build_error_result(str(e))
