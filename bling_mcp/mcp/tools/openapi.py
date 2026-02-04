"""Bling OpenAPI reference search tool."""

from __future__ import annotations

from typing import Annotated

from bling_mcp.utils.openapi_search import search_openapi_reference
from bling_mcp.mcp.app import get_mcp
from bling_mcp.mcp.tool_helpers import (
    READ_ONLY_INTERNAL_ANNOTATIONS,
    build_tool_envelope,
    build_error_result,
)
from bling_mcp.mcp.tool_models import HttpMethod, OpenApiSearchResult, ResponseFormat, ToolEnvelope
from pydantic import Field


def register_openapi_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return

    @mcp.tool(
        description="Busca endpoints no bling-openapi-reference.md.",
        annotations=READ_ONLY_INTERNAL_ANNOTATIONS,
    )
    def bling_openapi_search(
        query: Annotated[str, Field(description="Termos de busca (ex: produto estoque).")],
        methods: Annotated[
            list[HttpMethod] | None,
            Field(description="Filtra por metodos HTTP."),
        ] = None,
        limit: Annotated[int, Field(ge=1, description="Limite de resultados retornados.")] = 10,
        include: Annotated[
            list[str] | None,
            Field(description="Inclui campos extras: snippet, description."),
        ] = None,
        snippetLines: Annotated[
            int,
            Field(ge=1, description="Numero de linhas para snippet quando include=snippet."),
        ] = 5,
        matchAll: Annotated[
            bool,
            Field(description="Se true, exige que todos os termos aparecam no bloco."),
        ] = True,
        filePath: Annotated[
            str | None,
            Field(description="Caminho do arquivo de referencia (opcional)."),
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
    ) -> ToolEnvelope[OpenApiSearchResult]:
        """Busca endpoints no bling-openapi-reference.md. Retorna lista enxuta; use include/responseFormat para detalhes."""
        try:
            raw = search_openapi_reference(
                query=query,
                methods=methods,
                limit=limit,
                include=include or [],
                snippet_lines=snippetLines,
                match_all=matchAll,
                file_path=filePath,
            )
            return build_tool_envelope(
                name="bling_openapi_search",
                raw=raw,
                data=raw,
                response_format=responseFormat,
                include=list(include or []),
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                hint="Use include=['snippet','description'] para detalhes. Para trechos completos, use responseFormat=raw com rawAsResource=true.",
            )
        except Exception as e:
            return build_error_result(str(e))
