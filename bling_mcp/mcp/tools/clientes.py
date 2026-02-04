"""Bling clientes (contatos) tools."""

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
    ContatoCriterio,
    ContatoDetail,
    ContatoInclude,
    ContatosListData,
    ResponseFormat,
    TipoPessoa,
    ToolEnvelope,
)
from pydantic import Field


def _contato_concise(contato: dict[str, Any] | None) -> dict[str, Any] | None:
    if not contato:
        return None
    return {
        "id": contato.get("id") or contato.get("idContato"),
        "nome": contato.get("nome"),
        "codigo": contato.get("codigo"),
        "tipo": contato.get("tipo"),
        "situacao": contato.get("situacao"),
        "documento": contato.get("numeroDocumento") or contato.get("documento"),
        "email": contato.get("email"),
        "telefone": contato.get("telefone") or contato.get("fone"),
    }


def _params_clientes_list(args: dict[str, Any]) -> list[tuple[str, Any]]:
    params = [
        ("pagina", args.get("pagina", 1)),
        ("limite", args.get("limite", 50)),
    ]
    pesquisa = args.get("pesquisa") or args.get("nome") or args.get("codigo")
    if pesquisa:
        params.append(("pesquisa", pesquisa))
    if args.get("criterio") is not None:
        params.append(("criterio", args["criterio"]))
    for key in ["dataInclusaoInicial", "dataInclusaoFinal", "dataAlteracaoInicial", "dataAlteracaoFinal",
                 "idTipoContato", "idVendedor", "uf", "telefone", "numeroDocumento", "tipoPessoa"]:
        if args.get(key) is not None:
            params.append((key, args[key]))
    ids = args.get("idsContatos")
    if ids:
        for i in ids:
            params.append(("idsContatos[]", i))
    return params


def register_clientes_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    client = get_bling_client()

    @mcp.tool(
        description="Lista contatos (clientes/fornecedores) com filtros.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_clientes_list(
        pagina: Annotated[int, Field(ge=1, description="Numero da pagina.")] = 1,
        limite: Annotated[int, Field(ge=1, description="Quantidade de registros por pagina.")] = 50,
        pesquisa: Annotated[
            str | None,
            Field(description="Nome, CPF/CNPJ, fantasia, e-mail ou codigo do contato."),
        ] = None,
        nome: Annotated[
            str | None,
            Field(description="Alias para pesquisa (nome do contato)."),
        ] = None,
        codigo: Annotated[
            str | None,
            Field(description="Alias para pesquisa (codigo do contato)."),
        ] = None,
        criterio: Annotated[
            ContatoCriterio | None,
            Field(description="Criterio de listagem (1=Todos, 2=Excluidos, 3=Ultimos, 4=Sem movimento)."),
        ] = None,
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
        idTipoContato: Annotated[int | None, Field(description="ID do tipo do contato.")] = None,
        idVendedor: Annotated[int | None, Field(description="ID do vendedor associado.")] = None,
        uf: Annotated[str | None, Field(description="UF do contato.")] = None,
        telefone: Annotated[str | None, Field(description="Telefone do contato.")] = None,
        idsContatos: Annotated[
            list[int] | None,
            Field(description="IDs dos contatos."),
        ] = None,
        numeroDocumento: Annotated[
            str | None,
            Field(description="CPF/CNPJ sem pontuacao."),
        ] = None,
        tipoPessoa: Annotated[
            TipoPessoa | None,
            Field(description="Tipo de pessoa (1=Fisica, 2=Juridica, 3=Estrangeiro)."),
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
    ) -> ToolEnvelope[ContatosListData]:
        """Lista contatos paginados. Prefira pesquisa/idsContatos e limite menor para reduzir tokens."""
        try:
            args = {k: v for k, v in locals().items() if v is not None and k != 'client'}
            params_list = _params_clientes_list(args)
            # Bling client accepts list of (key, value) for array params
            raw = client.get("/contatos", params=params_list if params_list else None)
            items = unwrap_data_array(raw)
            data = {"items": [_contato_concise(c) for c in items if isinstance(c, dict)]}
            next_page = infer_next_page(raw, {"pagina": pagina, "limite": limite})
            return build_tool_envelope(
                name="bling_clientes_list",
                raw=raw,
                data=data,
                response_format=responseFormat,
                max_items=maxItems,
                max_chars=maxChars,
                raw_as_resource=rawAsResource,
                next_page=next_page,
                hint="Use bling_clientes_get para detalhes. Ajuste limite/maxItems para reduzir tokens.",
            )
        except Exception as e:
            return build_error_result(str(e))

    @mcp.tool(
        description="Obtem detalhes de um contato pelo ID.",
        annotations=READ_ONLY_ANNOTATIONS,
    )
    def bling_clientes_get(
        idContato: Annotated[int, Field(ge=1, description="ID do contato.")],
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        include: Annotated[
            list[ContatoInclude] | None,
            Field(description="Inclui blocos adicionais: enderecos, financeiro."),
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
    ) -> ToolEnvelope[ContatoDetail | None]:
        """Obtem detalhes de um contato pelo ID. Use include para enderecos/financeiro."""
        try:
            raw = client.get(f"/contatos/{idContato}")
            contato = unwrap_data_object(raw)
            data = _contato_concise(contato) if contato else None
            if include:
                include_set = set(include or [])
                if data and contato:
                    if "enderecos" in include_set:
                        data["enderecos"] = contato.get("enderecos") or contato.get("endereco")
                    if "financeiro" in include_set:
                        data["financeiro"] = contato.get("financeiro")
            return build_tool_envelope(
                name="bling_clientes_get",
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
