"""Bling NFe (notas fiscais) tools."""

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
    NfeDetail,
    NfeInclude,
    NfeListData,
    NfeSituacao,
    NfeTipo,
    ResponseFormat,
    ToolEnvelope,
)
from pydantic import Field


def _nota_concise(nota: dict[str, Any] | None) -> dict[str, Any] | None:
    if not nota:
        return None
    return {
        "id": nota.get("id") or nota.get("idNota"),
        "numero": nota.get("numero"),
        "serie": nota.get("serie"),
        "dataEmissao": nota.get("dataEmissao") or nota.get("data"),
        "situacao": nota.get("situacao", {}).get("descricao") if isinstance(nota.get("situacao"), dict) else nota.get("situacao"),
        "chaveAcesso": nota.get("chaveAcesso") or nota.get("chave"),
        "total": nota.get("total") or nota.get("valorTotal"),
    }


def register_notas_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    client = get_bling_client()

    @mcp.tool(
        description="Lista notas fiscais eletronicas (NFe) com filtros.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_nfe_list(
        pagina: Annotated[int, Field(ge=1, description="Numero da pagina.")] = 1,
        limite: Annotated[int, Field(ge=1, description="Quantidade de registros por pagina.")] = 50,
        numeroLoja: Annotated[str | None, Field(description="Numero do pedido na loja.")] = None,
        idTransportador: Annotated[int | None, Field(description="ID do transportador.")] = None,
        chaveAcesso: Annotated[str | None, Field(description="Chave de acesso da NFe.")] = None,
        numero: Annotated[int | None, Field(description="Numero da nota fiscal.")] = None,
        serie: Annotated[int | None, Field(description="Serie da nota fiscal.")] = None,
        situacao: Annotated[
            NfeSituacao | None,
            Field(description="Situacao da NFe (1..11)."),
        ] = None,
        tipo: Annotated[
            NfeTipo | None,
            Field(description="Tipo da nota fiscal (0=Entrada, 1=Saida)."),
        ] = None,
        dataEmissaoInicial: Annotated[
            str | None,
            Field(description="Data/hora inicial de emissao (YYYY-MM-DD ou ISO)."),
        ] = None,
        dataEmissaoFinal: Annotated[
            str | None,
            Field(description="Data/hora final de emissao (YYYY-MM-DD ou ISO)."),
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
    ) -> ToolEnvelope[NfeListData]:
        """Lista NFe paginadas. Prefira numero/serie/chave e limite menor para reduzir tokens."""
        try:
            params: list[tuple[str, Any]] = [("pagina", pagina), ("limite", limite)]
            for k, v in [("numeroLoja", numeroLoja), ("idTransportador", idTransportador),
                         ("chaveAcesso", chaveAcesso), ("numero", numero),
                         ("serie", serie), ("situacao", situacao), ("tipo", tipo),
                         ("dataEmissaoInicial", dataEmissaoInicial), ("dataEmissaoFinal", dataEmissaoFinal)]:
                if v is not None:
                    params.append((k, v))
            raw = client.get("/nfe", params=params)
            items = unwrap_data_array(raw)
            data = {"items": [_nota_concise(n) for n in items if isinstance(n, dict)]}
            next_page = infer_next_page(raw, {"pagina": pagina, "limite": limite})
            return build_tool_envelope(
                name="bling_nfe_list",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                next_page=next_page,
                hint="Use bling_nfe_get para detalhes. Ajuste limite/maxItems para reduzir tokens.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem uma NFe pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_nfe_get(
        idNota: Annotated[int, Field(ge=1, description="ID da nota fiscal.")],
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        include: Annotated[
            list[NfeInclude] | None,
            Field(description="Inclui blocos adicionais: itens, duplicatas."),
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
    ) -> ToolEnvelope[NfeDetail | None]:
        """Obtem uma NFe pelo ID. Use include apenas quando necessario."""
        try:
            raw = client.get(f"/nfe/{idNota}")
            nota = unwrap_data_object(raw)
            data = _nota_concise(nota) if nota else None
            if data and nota and include:
                inc = set(include or [])
                if "itens" in inc:
                    data["itens"] = nota.get("itens")
                if "duplicatas" in inc:
                    data["duplicatas"] = nota.get("duplicatas") or nota.get("financeiro")
            return build_tool_envelope(
                name="bling_nfe_get",
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
