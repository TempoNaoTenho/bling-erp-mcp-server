"""Pydantic models and shared types for MCP tool schemas."""

from __future__ import annotations

from typing import Any, Generic, Literal, TypeVar

from pydantic import BaseModel, ConfigDict, Field

ResponseFormat = Literal["concise", "raw", "detailed"]
HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]

ProdutoCriterio = Literal[1, 2, 3, 4, 5]
ProdutoTipo = Literal["T", "P", "S", "E", "PS", "C", "V"]
SaldoFiltro = Literal[0, 1, 2]

ContatoCriterio = Literal[1, 2, 3, 4]
TipoPessoa = Literal[1, 2, 3]

NfeSituacao = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
NfeTipo = Literal[0, 1, "0", "1"]

ProdutoInclude = Literal["estoque", "fornecedor", "categoria", "tributacao", "midia", "variacoes"]
ContatoInclude = Literal["enderecos", "financeiro"]
PedidoInclude = Literal["itens", "parcelas", "transporte"]
NfeInclude = Literal["itens", "duplicatas"]


class ToolMeta(BaseModel):
    model_config = ConfigDict(extra="allow")

    responseFormat: str
    include: list[str] = Field(default_factory=list)
    truncated: bool = False
    hint: str | None = None
    nextPage: int | None = None
    truncatedReason: str | None = None
    error: bool | None = None


T = TypeVar("T")


class ToolEnvelope(BaseModel, Generic[T]):
    meta: ToolMeta
    data: T


class ProdutoConcise(BaseModel):
    id: int | None = None
    nome: str | None = None
    codigo: str | None = None
    preco: float | int | None = None
    tipo: str | None = None
    situacao: str | None = None
    unidade: str | None = None
    gtin: str | None = None
    marca: str | None = None
    imagemURL: str | None = None


class ProdutosListData(BaseModel):
    items: list[ProdutoConcise]


class ProdutoVariacaoInfo(BaseModel):
    nome: str | None = None
    ordem: int | None = None


class ProdutoVariacaoPreview(BaseModel):
    id: int | None = None
    codigo: str | None = None
    preco: float | int | None = None
    situacao: str | None = None
    variacao: ProdutoVariacaoInfo | None = None


class VariacoesPreviewData(BaseModel):
    total: int
    preview: list[ProdutoVariacaoPreview]
    truncated: bool


class ProdutoDetail(ProdutoConcise):
    model_config = ConfigDict(extra="allow")

    estoque: Any | None = None
    fornecedor: Any | None = None
    categoria: Any | None = None
    tributacao: Any | None = None
    midia: Any | None = None
    variacoes: Any | None = None


class ProdutoEstoqueData(BaseModel):
    idProduto: int | None = None
    estoque: Any | None = None


class ProdutoTributacaoData(BaseModel):
    idProduto: int | None = None
    tributacao: Any | None = None


class ProdutoLotesSaldoTotalData(BaseModel):
    idProduto: int
    idDeposito: int | None = None
    saldoTotal: float | int | None = None


class ContatoConcise(BaseModel):
    id: int | None = None
    nome: str | None = None
    codigo: str | None = None
    tipo: str | None = None
    situacao: str | None = None
    documento: str | None = None
    email: str | None = None
    telefone: str | None = None


class ContatosListData(BaseModel):
    items: list[ContatoConcise]


class ContatoDetail(ContatoConcise):
    model_config = ConfigDict(extra="allow")

    enderecos: Any | None = None
    financeiro: Any | None = None


class ClienteRef(BaseModel):
    id: int | None = None
    nome: str | None = None


class PedidoConcise(BaseModel):
    id: int | None = None
    numero: int | None = None
    data: str | None = None
    situacao: str | None = None
    total: float | int | None = None
    cliente: ClienteRef | None = None


class PedidosListData(BaseModel):
    items: list[PedidoConcise]


class PedidoDetail(PedidoConcise):
    model_config = ConfigDict(extra="allow")

    itens: Any | None = None
    parcelas: Any | None = None
    transporte: Any | None = None


class SituacaoItem(BaseModel):
    id: int | None = None
    descricao: str | None = None
    cor: str | None = None


class SituacoesListData(BaseModel):
    items: list[SituacaoItem]


class NotaConcise(BaseModel):
    id: int | None = None
    numero: int | None = None
    serie: int | None = None
    dataEmissao: str | None = None
    situacao: str | None = None
    chaveAcesso: str | None = None
    total: float | int | None = None


class NfeListData(BaseModel):
    items: list[NotaConcise]


class NfeDetail(NotaConcise):
    model_config = ConfigDict(extra="allow")

    itens: Any | None = None
    duplicatas: Any | None = None


class EstoqueSaldoItem(BaseModel):
    idProduto: int | None = None
    idDeposito: int | None = None
    saldo: float | int | None = None
    reservado: float | int | None = None
    disponivel: float | int | None = None


class EstoqueSaldosData(BaseModel):
    items: list[EstoqueSaldoItem]


class OpenApiSearchMatch(BaseModel):
    method: HttpMethod
    path: str
    section: str | None = None
    description: str | None = None
    snippet: str | None = None


class OpenApiSearchResult(BaseModel):
    query: str
    totalMatches: int
    returned: int
    limit: int
    filePath: str
    matches: list[OpenApiSearchMatch]


class BlingAuthStartData(BaseModel):
    status: str
    message: str
    localUiUrl: str
    publicUrl: str | None = None


class BlingAuthStatusData(BaseModel):
    authenticated: bool
    refreshTokenPresent: bool | None = None
    accessTokenExpiresAt: int | None = None
    accessTokenExpiresAtFormatted: str | None = None
    scopes: str | None = None
    autoRefresh: bool | None = None
    message: str | None = None
