# Bling API

**Version:** 3.0

A sessão abaixo contém a documentação das API's que o Bling disponibiliza.

## Base URLs
- `https://api.bling.com.br/Api/v3`: Ambiente de produção
- `https://developer.bling.com.br/api/bling`: Ambiente de teste da documentação

## Anúncios

### GET `/anuncios`

**Obtém anúncios**

Obtém anúncios paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer | Situação do anúncio <br> `1` Publicado <br> `2` Rascunho <br> `3` Com problema <br> `4` Pausado |
| idProduto | query | No | integer | ID do produto |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/anuncios`

**Cria um anúncio**

Cria um anúncio.

#### Request Body

**Content-Type:** `application/json`

Schema: [AnunciosSaveRequest](#schema-anunciossaverequest)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/anuncios/{idAnuncio}`

**Obtém um anúncio**

Obtém os detalhes de um anúncio específico pelo seu ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/anuncios/{idAnuncio}`

**Altera um anúncio**

Altera um anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |

#### Request Body

**Content-Type:** `application/json`

Schema: [AnunciosSaveRequest](#schema-anunciossaverequest)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/anuncios/{idAnuncio}`

**Remove um anúncio**

Remove um anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/anuncios/{idAnuncio}/publicar`

**Publica um anúncio**

Altera o status do anúncio para publicado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/anuncios/{idAnuncio}/pausar`

**Pausa um anúncio**

Altera o status do anúncio para pausado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Anúncios - Categorias

### GET `/anuncios/categorias`

**Obtém categorias de anúncios**

Obtém categorias de anúncios.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |
| idCategoria | query | No | integer | ID da categoria |
| tipoProduto | query | No | string | Tipo do produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/anuncios/categorias/{idCategoria}`

**Obtém uma categoria de anúncio**

Obtém uma categoria de anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Borderôs

### GET `/borderos/{idBordero}`

**Obtém um borderô**

Obtém um borderô pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idBordero | path | **Yes** | integer | ID do bordero |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/borderos/{idBordero}`

**Remove um borderô**

Remove um borderô pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idBordero | path | **Yes** | integer | ID do bordero |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Caixas e Bancos

### GET `/caixas`

**Obtém lista de lançamentos de caixas e bancos.**

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| dataInicial | query | No | string | Data inicial de consulta de movimentações, só serão retornados os lançamento a partir dessa data. Caso não informado, o padrão será o primeiro dia do mês atual. |
| dataFinal | query | No | string | Data final de consulta de movimentações, só serão retornados os lançamento até essa data. Caso não informado, o padrão será o último dia do mês atual. |
| idsCategorias | query | No | Array<integer> | IDs das categorias de movimentações. |
| idContaFinanceira | query | No | integer | ID da conta financeira. |
| pesquisa | query | No | string | Pesquisa por descrição do lançamento. |
| valor | query | No | number | Valor do lançamento. |
| situacaoConciliacao | query | No | integer | Situação da conciliação do lançamento <br> `1` Registros conciliados <br> `2` Registros não conciliados <br> `3` Todos os registros |
| situacao | query | No | string | Situação do lançamento.<br>'R' para registros<br>'E' para excluídos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 | Valor de filtro inválido. | [ErrorResponse](#schema-errorresponse) |

---

### POST `/caixas`

**Cria um novo lançamento de caixa e banco.**

Cria um novo lançamento de caixa e banco com os dados fornecidos.

#### Request Body

**Content-Type:** `application/json`

Schema: [CaixasBancosSalvarLancamentoDTO](#schema-caixasbancossalvarlancamentodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 | Lançamento criado com sucesso | [CaixasBancosSalvarLancamentoResponseDTO](#schema-caixasbancossalvarlancamentoresponsedto) |
| 400 | Dados inválidos ou campos obrigatórios não informados | [ErrorResponse](#schema-errorresponse) |

---

### GET `/caixas/{idCaixa}`

**Obtém um lançamento de caixa e banco.**

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixas e bancos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [CaixasBancosLancamentoDTO](#schema-caixasbancoslancamentodto) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/caixas/{idCaixa}`

**Atualiza um lançamento de caixa e banco.**

Atualiza um lançamento de caixa e banco existente com os dados fornecidos.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixas e bancos |

#### Request Body

**Content-Type:** `application/json`

Schema: [CaixasBancosSalvarLancamentoDTO](#schema-caixasbancossalvarlancamentodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 | Lançamento atualizado com sucesso | [CaixasBancosSalvarLancamentoResponseDTO](#schema-caixasbancossalvarlancamentoresponsedto) |
| 400 | Dados inválidos ou campos obrigatórios não informados | [ErrorResponse](#schema-errorresponse) |
| 404 | Lançamento não encontrado | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/caixas/{idCaixa}`

**Remove um lançamento de caixa e banco**

Remove um lançamento de caixa e banco pelo ID. O registro não é excluído permanentemente, apenas marcado como excluído (exclusão lógica).

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixa e banco a ser excluído. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. O lançamento foi excluído com sucesso. | - |
| 400 | Erro de validação. | [ErrorResponse](#schema-errorresponse) |
| 404 | Lançamento não encontrado. | [ErrorResponse](#schema-errorresponse) |

---

## Campos Customizados

### GET `/campos-customizados/modulos`

**Obtém módulos que possuem campos customizados**

Obtém módulos que possuem campos customizados.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/campos-customizados/tipos`

**Obtém tipos de campos customizados**

Obtém tipos de campos customizados.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/campos-customizados/modulos/{idModulo}`

**Obtém campos customizados por módulo**

Obtém campos customizados por módulo paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModulo | path | **Yes** | integer |  |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/campos-customizados/{idCampoCustomizado}`

**Obtém um campo customizado**

Obtém um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/campos-customizados/{idCampoCustomizado}`

**Altera um campo customizado**

Altera um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Request Body

**Content-Type:** `application/json`

Schema: [CamposCustomizadosDadosBaseDTO](#schema-camposcustomizadosdadosbasedto) & [CamposCustomizadosDadosEdicaoDTO](#schema-camposcustomizadosdadosedicaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/campos-customizados/{idCampoCustomizado}`

**Remove um campo customizado**

Remove um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/campos-customizados`

**Cria um campo customizado**

Cria um campo customizado.

#### Request Body

**Content-Type:** `application/json`

Schema: [CamposCustomizadosDadosBaseDTO](#schema-camposcustomizadosdadosbasedto) & [CamposCustomizadosDadosEdicaoDTO](#schema-camposcustomizadosdadosedicaodto) & [CamposCustomizadosDadosDTO](#schema-camposcustomizadosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/campos-customizados/{idCampoCustomizado}/situacoes`

**Altera a situação de um campo customizado**

Altera a situação de um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Canais de Venda

### GET `/canais-venda`

**Obtém canais de venda**

Obtém canais de venda paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipos[] | query | No | Array<string> | Parâmetro para filtrar os registros através de uma lista de tipos de canal de venda. |
| situacao | query | No | integer | Parâmetro para filtrar os registros através da situação<br> `1` Habilitado<br> `2` Desabilitado |
| agrupador | query | No | integer | Agrupador do canal de venda<br> `1` Loja virtual<br> `2` Hub<br> `3` Marketplace<br> `4` API |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/canais-venda/{idCanalVenda}`

**Obtém um canal de venda**

Obtém uma canal de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCanalVenda | path | **Yes** | integer | ID do canal de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/canais-venda/tipos`

**Obtém os tipos de canais de venda**

Obtém os tipos de canais de venda paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| agrupador | query | No | integer | Agrupador do canal de venda<br> `1` Loja virtual<br> `2` Hub<br> `3` Marketplace<br> `4` API |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

## Categorias - Lojas

### GET `/categorias/lojas`

**Obtém categorias de lojas virtuais vinculadas a de produtos**

Obtém categorias de lojas virtuais vinculadas a de produtos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idLoja | query | No | integer | ID da loja |
| idCategoriaProduto | query | No | integer | ID da categoria do produto |
| idCategoriaProdutoPai | query | No | integer | ID da categoria do produto pai |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/categorias/lojas`

**Cria o vínculo de uma categoria da loja com a de produto**

Cria o vínculo de uma categoria da loja com a de produto.

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasLojasDadosDTO](#schema-categoriaslojasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/categorias/lojas/{idCategoriaLoja}`

**Obtém uma categoria da loja vinculada a de produto**

Obtém uma categoria da loja vinculada a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/categorias/lojas/{idCategoriaLoja}`

**Altera o vínculo de uma categoria da loja com a de produto**

Altera o vínculo de uma categoria da loja com a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasLojasDadosDTO](#schema-categoriaslojasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/categorias/lojas/{idCategoriaLoja}`

**Remove o vínculo de uma categoria da loja com a de produto**

Remove o vínculo de uma categoria da loja com a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Categorias - Produtos

### GET `/categorias/produtos`

**Obtém categorias de produtos**

Obtém categorias de produtos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/categorias/produtos`

**Cria uma categoria de produto**

Cria uma categoria de produto.

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasProdutosDadosDTO](#schema-categoriasprodutosdadosdto) & object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/categorias/produtos/{idCategoriaProduto}`

**Obtém uma categoria de produto**

Obtém uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/categorias/produtos/{idCategoriaProduto}`

**Altera uma categoria de produto**

Altera uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasProdutosDadosDTO](#schema-categoriasprodutosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/categorias/produtos/{idCategoriaProduto}`

**Remove uma categoria de produto**

Remove uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Categorias - Receitas e Despesas

### GET `/categorias/receitas-despesas`

**Obtém categorias de receitas e despesas**

Obtém categorias de receitas e despesas paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipo | query | No | integer | `0` Todas<br>`1` Despesa<br>`2` Receita<br>`3` Receita e despesa |
| situacao | query | No | integer | `0` Ativas e Inativas<br>`1` Ativas<br>`2` Inativas |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/categorias/receitas-despesas`

**Cria uma categoria de receita e despesa**

Cria uma categoria de receita e despesa.

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasReceitasDespesasDadosPostDTO](#schema-categoriasreceitasdespesasdadospostdto) & [CategoriasReceitasDespesasDadosBaseDTO](#schema-categoriasreceitasdespesasdadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/categorias/receitas-despesas`

**Remove múltiplas categorias de receita e despesa**

Remove múltiplas categorias de receita e despesa a partir de uma lista de IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsCategorias[] | query | **Yes** | Array<integer> | IDs das categorias a serem removidas |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |

---

### GET `/categorias/receitas-despesas/{idCategoria}`

**Obtém uma categoria de receita e despesa**

Obtém uma categoria de receita e despesa pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/categorias/receitas-despesas/{idCategoria}`

**Atualiza uma categoria de receita e despesa**

Atualiza uma categoria de receita e despesa a partir do ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Request Body

**Content-Type:** `application/json`

Schema: [CategoriasReceitasDespesasDadosPostDTO](#schema-categoriasreceitasdespesasdadospostdto) & [CategoriasReceitasDespesasDadosBaseDTO](#schema-categoriasreceitasdespesasdadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/categorias/receitas-despesas/{idCategoria}`

**Remove uma categoria de receita e despesa**

Remove uma categoria de receita e despesa pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Contas Financeiras

### GET `/contas-contabeis`

**Obtém contas financeiras**

Obtém contas financeiras paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| ocultarInvisiveis | query | No | boolean | Oculta contas financeiras invisíveis |
| ocultarTipoContaBancaria | query | No | boolean | Oculta contas financeiras do tipo conta bancária |
| situacoes | query | No | Array<integer> | Situação da conta financeira<br> `1` Ativo<br> `2` Inativo<br> `3` Pendente<br> `4` Cancelada |
| aliasIntegracao | query | No | string | Alias da integração |
| aliasIntegracao | path | No | string | Alias da integração |
| ordenacao | query | No | string | Ordenação da obtenção pelos campos: <br> `descricao` |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/contas-contabeis/{idContaContabil}`

**Obtém uma conta financeira**

Obtém uma conta financeira pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaContabil | path | **Yes** | integer | ID da conta financeira |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Contas a Pagar

### GET `/contas/pagar`

**Obtém contas a pagar**

Obtém contas a pagar paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| dataEmissaoInicial | query | No | string | Data de emissão inicial da conta a pagar |
| dataEmissaoFinal | query | No | string | Data de emissão final da conta a pagar |
| dataVencimentoInicial | query | No | string | Data de vencimento inicial da conta a pagar |
| dataVencimentoFinal | query | No | string | Data de vencimento final da conta a pagar |
| dataPagamentoInicial | query | No | string | Data de pagamento inicial da conta |
| dataPagamentoFinal | query | No | string | Data de pagamento final da conta |
| situacao | query | No | integer | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Cancelado |
| idContato | query | No | integer | ID do contato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/contas/pagar`

**Cria uma conta a pagar**

Cria uma conta a pagar.

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasDadosBaseDTO](#schema-contasdadosbasedto) & [ContasPagarDadosDTO](#schema-contaspagardadosdto) & [ContasPagarDadosPostDTO](#schema-contaspagardadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | [BasePostResponse](#schema-basepostresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contas/pagar/{idContaPagar}`

**Obtém uma conta a pagar**

Obtém uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/contas/pagar/{idContaPagar}`

**Atualiza uma conta a pagar**

Atualiza uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasDadosBaseDTO](#schema-contasdadosbasedto) & [ContasPagarDadosDTO](#schema-contaspagardadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [BasePostResponse](#schema-basepostresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/contas/pagar/{idContaPagar}`

**Remove uma conta a pagar**

Remove uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/contas/pagar/{idContaPagar}/baixar`

**Cria o recebimento de uma conta a pagar**

Cria o recebimento de uma conta a pagar.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasBaixarContaDTO](#schema-contasbaixarcontadto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Contas a Receber

### GET `/contas/receber`

**Obtém contas a receber**

Obtém contas a receber paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacoes[] | query | No | Array<integer> | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Cancelado |
| tipoFiltroData | query | No | string | Referente ao campo que será considerado ao filtrar por data inicial e final<br>`E` Data de emissão <br> `V` Data de vencimento <br> `R` Data de recebimento |
| dataInicial | query | No | string | Data inicial. Por padrão, um ano antes da data atual. |
| dataFinal | query | No | string | Data final. Por padrão, a data atual. |
| idsCategorias[] | query | No | Array<integer> | IDs das categorias de receitas e despesas |
| idPortador | query | No | integer | ID da conta financeira |
| idContato | query | No | integer | ID do contato |
| idVendedor | query | No | integer | ID do vendedor |
| idFormaPagamento | query | No | integer | ID da forma de pagamento |
| boletoGerado | query | No | integer | Obtém contas com ou sem boletos emitidos via integração, `0` para boletos não emitidos e `1` para boletos emitidos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/contas/receber`

**Cria uma conta a receber**

Cria uma conta a receber.

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasDadosBaseDTO](#schema-contasdadosbasedto) & [ContasReceberDadosBaseDTO](#schema-contasreceberdadosbasedto) & [ContasReceberDadosDTO](#schema-contasreceberdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contas/receber/{idContaReceber}`

**Obtém uma conta a receber**

Obtém uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/contas/receber/{idContaReceber}`

**Altera uma conta a receber**

Altera uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasDadosBaseDTO](#schema-contasdadosbasedto) & [ContasReceberDadosBaseDTO](#schema-contasreceberdadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/contas/receber/{idContaReceber}`

**Remove uma conta a receber**

Remove uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/contas/receber/{idContaReceber}/baixar`

**Cria o recebimento de uma conta a receber**

Cria o recebimento de uma conta a receber.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasBaixarContaDTO](#schema-contasbaixarcontadto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contas/receber/boletos`

**Obtém boletos de contas a receber**

Obtém os boletos vinculados a um idOrigem, o qual corresponde ao ID de uma venda ou nota fiscal.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrigem | query | **Yes** | integer | ID da venda ou nota fiscal |
| situacoes[] | query | No | Array<integer> | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Parcialmente devolvido <br>`6` Cancelado |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [ContasReceberBoletosDadosBaseDTO](#schema-contasreceberboletosdadosbasedto) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | object |

---

### POST `/contas/receber/boletos/cancelar`

**Cancela boletos de contas a receber**

Cancela um ou todos os boletos em aberto vinculados a uma venda ou nota fiscal.

#### Request Body

**Content-Type:** `application/json`

Schema: [ContasReceberBoletosCancelarDTO](#schema-contasreceberboletoscancelardto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | object |

---

## Contatos

### GET `/contatos`

**Obtém contatos**

Obtém contatos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| pesquisa | query | No | string | Nome, CPF/CNPJ, fantasia, e-mail ou código do contato |
| criterio | query | No | integer | Criterio de listagem <br> `1` Todos <br> `2` Excluídos <br> `3` Últimos incluídos <br> `4` Sem movimento |
| dataInclusaoInicial | query | No | string | Data de inclusão inicial |
| dataInclusaoFinal | query | No | string | Data de inclusão final |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |
| idTipoContato | query | No | integer | ID do tipo do contato |
| idVendedor | query | No | integer | ID do vendedor relacionado ao contato |
| uf | query | No | string | UF do contato |
| telefone | query | No | string | Telefone do contato |
| idsContatos[] | query | No | Array<integer> | IDs dos contatos |
| numeroDocumento | query | No | string |  CPF/CNPJ, desconsiderando a pontuação |
| tipoPessoa | query | No | integer | Tipo de pessoa <br> `1` Física <br> `2` Jurídica <br> `3` Estrangeiro |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/contatos`

**Cria um contato**

Cria um contato.

#### Request Body

**Content-Type:** `application/json`

Schema: [ContatosDadosBaseDTO](#schema-contatosdadosbasedto) & [ContatosDadosDTO](#schema-contatosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/contatos`

**Remove múltiplos contatos**

Remove múltiplos contatos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsContatos[] | query | **Yes** | Array<integer> | IDs dos contatos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contatos/{idContato}`

**Obtém um contato**

Obtém um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/contatos/{idContato}`

**Altera um contato**

Altera um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContatosDadosBaseDTO](#schema-contatosdadosbasedto) & [ContatosDadosDTO](#schema-contatosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/contatos/{idContato}`

**Remove um contato**

Remove um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contatos/{idContato}/tipos`

**Obtém os tipos de contato de um contato**

Obtém os tipos de contato de um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contatos/consumidor-final`

**Obtém os dados do contato Consumidor Final**

Obtém os dados do contato Consumidor Final. O consumidor final é um contato padrão do sistema que é criado automaticamente e não pode ser alterado.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### PATCH `/contatos/{idContato}/situacoes`

**Altera a situação de um contato**

Altera a situação de um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/contatos/situacoes`

**Altera a situação de múltiplos contatos**

Altera a situação de múltiplos contatos pelos IDs.

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Contatos - Tipos

### GET `/contatos/tipos`

**Obtém tipos de contato**

Obtém tipos de contato pelo ID.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

## Contratos

### GET `/contratos`

**Obtém contratos**

Obtém contratos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| dataCriacaoInicio | query | No | string | Data inicial de criação |
| dataCriacaoFinal | query | No | string | Data final de criação |
| dataBaseInicio | query | No | string | Data base inicial para geração de cobranças |
| dataBaseFinal | query | No | string | Data base final para geração de cobranças |
| situacao | query | No | string | `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento |
| idContato | query | No | integer | ID do contato |
| idContatoCobranca | query | No | integer | ID do contato de cobrança |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/contratos`

**Cria um contrato**

Cria um contrato.

#### Request Body

**Content-Type:** `application/json`

Schema: [ContratosDadosBaseDTO](#schema-contratosdadosbasedto) & [ContratosDadosDTO](#schema-contratosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/contratos/{idContrato}`

**Obtém um contrato**

Obtém um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/contratos/{idContrato}`

**Altera um contrato**

Altera um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Request Body

**Content-Type:** `application/json`

Schema: [ContratosDadosBaseDTO](#schema-contratosdadosbasedto) & [ContratosDadosDTO](#schema-contratosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/contratos/{idContrato}`

**Remove um contrato**

Remove um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Depósitos

### GET `/depositos`

**Obtém depósitos**

Obtém depósitos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| descricao | query | No | string | Descrição do depósito |
| situacao | query | No | integer | `0` Inativo <br> `1` Ativo |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/depositos`

**Cria um depósito**

Cria um depósito. Até 100 depósitos podem ser criados.

#### Request Body

**Content-Type:** `application/json`

Schema: [DepositosDadosDTO](#schema-depositosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/depositos/{idDeposito}`

**Obtém um depósito**

Obtém um depósito pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/depositos/{idDeposito}`

**Altera um depósito**

Altera um depósito pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Request Body

**Content-Type:** `application/json`

Schema: [DepositosDadosDTO](#schema-depositosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [BasePostResponse](#schema-basepostresponse) & object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Empresas

### GET `/empresas/me/dados-basicos`

**Obtém dados básicos da empresa**

Obtém CNPJ, razão social e e-mail da empresa.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

## Estoques

### GET `/estoques/saldos/{idDeposito}`

**Obtém o saldo em estoque de produtos por depósito**

Obtém o saldo em estoque de produtos pelo ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |
| codigos[] | query | No | Array<string> | Códigos dos produtos |
| filtroSaldoEstoque | query | No | integer | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/estoques/saldos`

**Obtém o saldo em estoque de produtos**

Obtém o saldo em estoque de produtos, em todos os depósitos.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |
| codigos[] | query | No | Array<string> | Códigos dos produtos |
| filtroSaldoEstoque | query | No | integer | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/estoques`

**Cria um registro de estoque**

Cria um registro de estoque.

#### Request Body

**Content-Type:** `application/json`

Schema: [EstoquesDadosDTO](#schema-estoquesdadosdto) & [EstoquesDadosBaseDTO](#schema-estoquesdadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Formas de Pagamentos

### GET `/formas-pagamentos`

**Obtém formas de pagamentos**

Obtém formas de pagamentos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| descricao | query | No | string | Descrição da forma de pagamento |
| tiposPagamentos[] | query | No | Array<integer> | `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Presente<br>`13` Vale Combustível<br>`14` Duplicata Mercantil<br>`15` Boleto Bancário<br>`16` Depósito Bancário<br>`17` Pagamento Instantâneo (PIX) - Dinâmico<br>`18` Transferência Bancária, Carteira Digital<br>`19` Programa de Fidelidade, Cashback, Crédito Virtual<br>`20` Pagamento Instantâneo (PIX) – Estático<br>`21` Crédito em loja<br>`22` Pagamento Eletrônico não Informado - falha de hardware do sistema emissor<br>`90` Sem pagamento<br>`99` Outros |
| situacao | query | No | integer | `0` Inativa<br>`1` Ativa |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/formas-pagamentos`

**Cria uma forma de pagamento**

Cria uma forma de pagamento.

#### Request Body

**Content-Type:** `application/json`

Schema: [FormasPagamentosDadosBaseDTO](#schema-formaspagamentosdadosbasedto) & [FormasPagamentosDadosDTO](#schema-formaspagamentosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/formas-pagamentos/{idFormaPagamento}`

**Obtém uma forma de pagamento**

Obtém uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/formas-pagamentos/{idFormaPagamento}`

**Altera uma forma de pagamento**

Altera uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

Schema: [FormasPagamentosDadosBaseDTO](#schema-formaspagamentosdadosbasedto) & [FormasPagamentosDadosDTO](#schema-formaspagamentosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/formas-pagamentos/{idFormaPagamento}`

**Remove uma forma de pagamento**

Remove uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/formas-pagamentos/{idFormaPagamento}/padrao`

**Altera o padrão de uma forma de pagamento**

Altera o padrão de uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

Schema: [FormasPagamentosDefinirPadraoDTO](#schema-formaspagamentosdefinirpadraodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/formas-pagamentos/{idFormaPagamento}/situacao`

**Altera a situação de uma forma de pagamento**

Altera a situação de uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

Schema: [FormasPagamentosAlterarSituacaoDTO](#schema-formaspagamentosalterarsituacaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Grupos de Produtos

### GET `/grupos-produtos`

**Obtém grupos de produtos**

Obtém grupos de produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| nome | query | No | string | O nome do grupo |
| nomePai | query | No | string | O nome do grupo pai |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/grupos-produtos`

**Cria um grupo de produtos**

Cria um grupo de produtos.

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/grupos-produtos`

**Remove múltiplos grupos de produtos**

Remove múltiplos grupos de produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsGruposProdutos[] | query | **Yes** | Array<integer> | IDs dos grupos de produtos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/grupos-produtos/{idGrupoProduto}`

**Obtém um grupo de produtos**

Obtém um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/grupos-produtos/{idGrupoProduto}`

**Altera um grupo de produtos**

Altera um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/grupos-produtos/{idGrupoProduto}`

**Remove um grupo de produtos**

Remove um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Homologação

### GET `/homologacao/produtos`

**Obtém o produto da homologação**

Obtém o produto que será utilizado durante os demais passos da homologação, e, inicia o processo de validação, o qual deve ser acompanhando via interface do cadastro de aplicativos.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/homologacao/produtos`

**Cria o produto da homologação**

Cria o produto da homologação.

#### Request Body

**Content-Type:** `application/json`

Schema: [HomologacaoDadosBaseDTO](#schema-homologacaodadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/homologacao/produtos/{idProdutoHomologacao}`

**Altera o produto da homologação**

Altera o produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Request Body

**Content-Type:** `application/json`

Schema: [HomologacaoDadosBaseDTO](#schema-homologacaodadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/homologacao/produtos/{idProdutoHomologacao}`

**Remove o produto da homologação**

Remove o produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/homologacao/produtos/{idProdutoHomologacao}/situacoes`

**Altera a situação do produto da homologação**

Altera a situação do produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Request Body

**Content-Type:** `application/json`

Schema: [HomologacaoSituacaoDTO](#schema-homologacaosituacaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Logísticas

### GET `/logisticas`

**Obtém logísticas**

Obtém logísticas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipoIntegracao | query | No | string | Parâmetro para filtrar os registros através do tipo da logística. |
| tiposIntegracoes[] | query | No | Array<string> | Parâmetro para filtrar os registros através de uma lista de tipos de logística. |
| situacao | query | No | string | Parâmetro para filtrar os registros através da situação<br> `H` Habilitado<br> `D` Desabilitado |
| logisticasReversas | query | No | boolean | Parâmetro para filtrar apenas as logísticas que possuem serviço de reversão. É sobrescrito pelo parâmetro tipoIntegracao, caso enviado junto. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/logisticas`

**Cria logística**

Cria uma logística.

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasDadosPostDTO](#schema-logisticasdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/logisticas/{idLogistica}`

**Obtém uma logística**

Obtém uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |
| listarServicosInativos | query | No | boolean | Parâmetro para incluir serviços inativos na resposta.<br> `true` Inclui serviços ativos e inativos<br> `false` Inclui apenas serviços ativos (padrão) |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/logisticas/{idLogistica}`

**Altera uma logística**

Altera uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasDadosPutDTO](#schema-logisticasdadosputdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/logisticas/{idLogistica}`

**Remove uma logística**

Remove uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Logísticas - Etiquetas

### GET `/logisticas/etiquetas`

**Obtém etiquetas das vendas**

Obtém as etiquetas dos pedidos de venda a partir dos ID's dos pedidos. No momento, o filtro está limitado para apenas um ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| formato | query | **Yes** | string | Parâmetro para definir o formato do arquivo de impressão.<br> `PDF` - Formato PDF<br> `ZPL` - Formato ZPL |
| idsVendas[] | query | **Yes** | Array<integer> | IDs dos pedidos de venda para impressão |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Logísticas - Objetos

### GET `/logisticas/objetos/{idObjeto}`

**Obtém um objeto de logística**

Obtém um objeto de logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/logisticas/objetos/{idObjeto}`

**Altera um objeto de logística pelo ID**

Altera dados de um objeto de logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasObjetosUpdateRequestDTO](#schema-logisticasobjetosupdaterequestdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/logisticas/objetos/{idObjeto}`

**Remove um objeto de logística personalizada**

Remove um objeto de logística personalizada que não esteja em uma PLP.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 |  | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/logisticas/objetos`

**Cria um objeto de logística**

Cria um objeto de logística personalizada.

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasObjetosDadosCreateRequestDTO](#schema-logisticasobjetosdadoscreaterequestdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Logísticas - Remessas

### GET `/logisticas/remessas/{idRemessa}`

**Obtém uma remessa de postagem**

Obtém uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/logisticas/remessas/{idRemessa}`

**Altera uma remessa de postagem**

Altera uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasRemessasDadosBaseDTOCommon](#schema-logisticasremessasdadosbasedtocommon)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/logisticas/remessas/{idRemessa}`

**Remove uma remessa de postagem**

Remove uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 |  | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/logisticas/{idLogistica}/remessas`

**Obtém as remessas de postagem de uma logística**

Obtém as remessas de postagem de uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/logisticas/remessas`

**Cria uma remessa de postagem de uma logística**

Cria uma remessa de postagem de uma logística.

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasRemessasDadosPostDTO](#schema-logisticasremessasdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Logísticas - Serviços

### GET `/logisticas/servicos`

**Obtém serviços de logísticas**

Obtém serviços de logísticas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipoIntegracao | query | No | string | Parâmetro para filtrar os registros através do tipo da logística. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/logisticas/servicos`

**Cria um serviço de logística**

Cria um serviço de logística personalizada.

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasServicosDadosCreateRequestDTO](#schema-logisticasservicosdadoscreaterequestdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/logisticas/servicos/{idLogisticaServico}`

**Obtém um servico de logística**

Obtém um servico de logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/logisticas/servicos/{idLogisticaServico}`

**Altera um serviço de logística pelo ID**

Altera dados de um serviço de logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasServicosDadosSaveRequestDTO](#schema-logisticasservicosdadossaverequestdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/logisticas/{idLogisticaServico}/situacoes`

**Desativa ou ativa um serviço de uma logística**

Desativa ou ativa um serviço de uma logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Request Body

**Content-Type:** `application/json`

Schema: [LogisticasServicosDadosSituationDTO](#schema-logisticasservicosdadossituationdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 |  | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Naturezas de Operações

### GET `/naturezas-operacoes`

**Obtém naturezas de operações**

Obtém naturezas de operação paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer | `0` Inativo <br> `1` Ativo |
| descricao | query | No | string | Descrição da natureza de operação |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao`

**Obtém regras de tributação da natureza de operação**

Obtém regras de tributação que incidem sobre o item, dada uma natureza de operação.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNaturezaOperacao | path | **Yes** | integer | ID da natureza de operação |

#### Request Body

**Content-Type:** `application/json`

Schema: [CalculosImpostosCalculoDTO](#schema-calculosimpostoscalculodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Notas Fiscais Eletrônicas

### GET `/nfe`

**Obtém notas fiscais**

Obtém notas fiscais paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| numeroLoja | query | No | string | Número do pedido na loja |
| idTransportador | query | No | integer | ID do contato do transportador |
| chaveAcesso | query | No | integer | Chave de acesso |
| numero | query | No | integer | Número da nota fiscal |
| serie | query | No | integer | Série |
| situacao | query | No | integer | `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada<br><br>**Observação:** Caso este parâmetro não seja informado, as notas canceladas não serão incluídas na consulta.<br><br> |
| tipo | query | No | string | `0` Entrada <br> `1` Saída |
| dataEmissaoInicial | query | No | string | Data e hora incial de emissão |
| dataEmissaoFinal | query | No | string | Data e hora final de emissão |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/nfe`

**Cria uma nota fiscal**

Cria uma nota fiscal.

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasFiscaisDadosBaseDTO](#schema-notasfiscaisdadosbasedto) & [NotasFiscaisDadosPostDTO](#schema-notasfiscaisdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/nfe`

**Remove múltiplas notas fiscais**

Remove múltiplas notas fiscais por IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsNotas[] | query | **Yes** | Array<integer> | IDs das notas fiscais |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/nfe/{idNotaFiscal}`

**Obtém uma nota fiscal**

Obtém uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/nfe/{idNotaFiscal}`

**Altera uma nota fiscal**

Altera uma nota fiscal pelo ID. Notas com vínculos possuem restrições de atualização. Notas autorizadas não podem ter dados fiscais alterados: valores, impostos, informações do destinatário e qualquer outro dado transmitido no XML da nota.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasFiscaisDadosBaseDTO](#schema-notasfiscaisdadosbasedto) & [NotasFiscaisDadosPostDTO](#schema-notasfiscaisdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/enviar`

**Envia uma nota fiscal**

Envia uma nota fiscal pelo ID para emissão na Sefaz.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |
| enviarEmail | query | No | boolean | Define se deve enviar email após a emissão da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/lancar-contas`

**Lança as contas de uma nota fiscal**

Lança as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/estornar-contas`

**Estorna as contas de uma nota fiscal**

Estorna as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/lancar-estoque`

**Lança o estoque de uma nota fiscal no depósito padrão**

Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}`

**Lança o estoque de uma nota fiscal especificando o depósito**

Lança o estoque de uma nota fiscal pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfe/{idNotaFiscal}/estornar-estoque`

**Estorna o estoque de uma nota fiscal**

Estorna o estoque de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Notas Fiscais de Consumidor Eletrônicas

### GET `/nfce`

**Obtém notas fiscais de consumidor**

Obtém notas fiscais de consumidor paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idTransportador | query | No | integer | ID do contato do transportador |
| chaveAcesso | query | No | integer | Chave de acesso |
| numero | query | No | integer | Número da nota fiscal de consumidor |
| serie | query | No | integer | Série |
| situacao | query | No | integer | `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada |
| dataEmissaoInicial | query | No | string | Data e hora inicial de emissão |
| dataEmissaoFinal | query | No | string | Data e hora final de emissão |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce`

**Cria uma nota fiscal de consumidor**

Cria uma nota fiscal de consumidor.

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasFiscaisDadosBaseDTO](#schema-notasfiscaisdadosbasedto) & [NotasFiscaisDadosPostDTO](#schema-notasfiscaisdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/nfce/{idNotaFiscalConsumidor}`

**Obtém uma nota fiscal de consumidor**

Obtém uma nota fiscal de consumidor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/nfce/{idNotaFiscalConsumidor}`

**Altera uma nota fiscal de consumidor**

Altera uma nota fiscal de consumidor.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasFiscaisDadosBaseDTO](#schema-notasfiscaisdadosbasedto) & [NotasFiscaisDadosPostDTO](#schema-notasfiscaisdadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/enviar`

**Envia uma nota de consumidor**

Envia uma nota de consumidor pelo ID para emissão na Sefaz.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-contas`

**Lança as contas de uma nota fiscal**

Lança as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/estornar-contas`

**Estorna as contas de uma nota fiscal**

Estorna as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-estoque`

**Lança o estoque de uma nota fiscal no depósito padrão**

Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}`

**Lança o estoque de uma nota fiscal especificando o depósito**

Lança o estoque de uma nota fiscal pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfce/{idNotaFiscalConsumidor}/estornar-estoque`

**Estorna o estoque de uma nota fiscal**

Estorna o estoque de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Notas Fiscais de Serviço Eletrônicas

### GET `/nfse`

**Obtém notas de serviços**

Obtém notas de serviços paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer | `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada |
| dataEmissaoInicial | query | No | string | Data incial do período de emissão |
| dataEmissaoFinal | query | No | string | Data final do período de emissão |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfse`

**Cria uma nota de serviço**

Cria uma nota de serviço.

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasServicosDadosBaseDTO_POST](#schema-notasservicosdadosbasedto_post) & [NotasServicosDadosDTO_POST](#schema-notasservicosdadosdto_post)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/nfse/{idNotaServico}`

**Obtém uma nota de serviço**

Obtém uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/nfse/{idNotaServico}`

**Exclui uma nota de serviço**

Exclui uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfse/{idNotaServico}/enviar`

**Envia uma nota de serviço**

Envia uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/nfse/{idNotaServico}/cancelar`

**Cancela uma nota de serviço**

Cancela uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Request Body

**Content-Type:** `application/json`

Schema: [NotasServicosCancelamentoDTO](#schema-notasservicoscancelamentodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/nfse/configuracoes`

**Configurações de nota de serviço**

Obtém todas as configurações de nota de serviço.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [ConfiguracaoNotaServicoDadosBaseDTO](#schema-configuracaonotaservicodadosbasedto) |

---

### PUT `/nfse/configuracoes`

**Configurações de nota de serviço**

Cria e altera configurações para emissão de notas de serviço.

#### Request Body

**Content-Type:** `application/json`

Schema: [ConfiguracaoNotaServicoDadosBaseDTO](#schema-configuracaonotaservicodadosbasedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Notificações

### GET `/notificacoes`

**Obtém todas as notificações de uma empresa em um período**

Obtém todas as notificações de uma empresa no período informado. Caso período não seja informado, será considerado o ano atual.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| periodo | query | No | string | Apenas ano ou ano e mês em que a empresa foi notificada. Caso não informado, será utilizado o ano atual. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/notificacoes/{idNotificacao}/confirmar-leitura`

**Marca notificação como lida**

Marca a notificação relacionada à empresa como lida.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotificacao | path | **Yes** | string | ULID da notificação. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/notificacoes/quantidade`

**Obtém a quantidade de notificações de uma empresa em um período**

Obtém a quantidade de notificações de uma empresa no período informado. Caso período não seja informado, será considerado o ano atual.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| periodo | query | No | string | Apenas ano ou ano e mês em que a empresa foi notificada. Caso não informado, será utilizado o ano atual. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Ordens de Produção

### GET `/ordens-producao`

**Obtém ordens de produção**

Obtém ordens de produção paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idsSituacoes[] | query | No | Array<integer> | IDs das situações |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/ordens-producao`

**Cria uma ordem de produção**

Cria uma ordem de produção.

#### Request Body

**Content-Type:** `application/json`

Schema: [OrdensProducaoDadosBaseDTO](#schema-ordensproducaodadosbasedto) & [OrdensProducaoDadosPostDTO](#schema-ordensproducaodadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/ordens-producao/{idOrdemProducao}`

**Obtém uma ordem de produção**

Obtém uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [OrdensProducaoDadosBaseDTO](#schema-ordensproducaodadosbasedto) & [OrdensProducaoDadosDTO](#schema-ordensproducaodadosdto) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/ordens-producao/{idOrdemProducao}`

**Altera uma ordem de produção**

Altera uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Request Body

**Content-Type:** `application/json`

Schema: [OrdensProducaoDadosBaseDTO](#schema-ordensproducaodadosbasedto) & [OrdensProducaoDadosPostDTO](#schema-ordensproducaodadospostdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/ordens-producao/{idOrdemProducao}`

**Remove uma ordem de produção**

Remove uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/ordens-producao/{idOrdemProducao}/situacoes`

**Altera a situação de uma ordem de produção**

Altera a situação de uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Request Body

**Content-Type:** `application/json`

Schema: [OrdensProducaoSituacaoDadosDTO](#schema-ordensproducaosituacaodadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/ordens-producao/gerar-sob-demanda`

**Gera ordens de produção sob demanda**

Gera ordens de produção sob demanda (abaixo do estoque mínimo).

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |

---

## Pedidos - Compras

### GET `/pedidos/compras`

**Obtém pedidos de compras**

Obtém pedidos de compras paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idFornecedor | query | No | integer | ID do contato do tipo fornecedor |
| valorSituacao | query | No | integer | Valor da situação |
| idSituacao | query | No | integer | ID da situação |
| dataInicial | query | No | string | Data inicial do período da compra |
| dataFinal | query | No | string | Data final do período da compra |
| idsNotasFiscais[] | query | No | Array<integer> | IDs das notas fiscais de entrada |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/pedidos/compras`

**Cria um pedido de compra**

Cria um pedido de compra.

#### Request Body

**Content-Type:** `application/json`

Schema: [PedidosComprasDadosBaseDTO](#schema-pedidoscomprasdadosbasedto) & [PedidosComprasDadosDTO](#schema-pedidoscomprasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/pedidos/compras/{idPedidoCompra}`

**Obtém um pedido de compra**

Obtém um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/pedidos/compras/{idPedidoCompra}`

**Altera um pedido de compra**

Altera um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Request Body

**Content-Type:** `application/json`

Schema: [PedidosComprasDadosBaseDTO](#schema-pedidoscomprasdadosbasedto) & [PedidosComprasDadosDTO](#schema-pedidoscomprasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/pedidos/compras/{idPedidoCompra}`

**Remove um pedido de compra**

Remove um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/pedidos/compras/{idPedidoCompra}/situacoes`

**Altera a situação de um pedido de compra**

Altera a situação de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Request Body

**Content-Type:** `application/json`

Schema: [PedidosComprasSituacaoDTO](#schema-pedidoscomprassituacaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/compras/{idPedidoCompra}/lancar-contas`

**Lança as contas de um pedido de compra**

Lança as contas de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/compras/{idPedidoCompra}/estornar-contas`

**Estorna as contas de um pedido de compra**

Estorna as contas de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/compras/{idPedidoCompra}/lancar-estoque`

**Lança o estoque de um pedido de compra**

Lança o estoque de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/compras/{idPedidoCompra}/estornar-estoque`

**Estorna o estoque de um pedido de compra**

Estorna o estoque de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Pedidos - Vendas

### GET `/pedidos/vendas`

**Obtém pedidos de vendas**

Obtém pedidos de vendas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idContato | query | No | integer | ID do contato |
| idsSituacoes[] | query | No | Array<integer> | Conjunto de situações |
| dataInicial | query | No | string | Data incial |
| dataFinal | query | No | string | Data final |
| dataAlteracaoInicial | query | No | string | Data inicial da alteração |
| dataAlteracaoFinal | query | No | string | Data final da alteração |
| dataPrevistaInicial | query | No | string | Data inicial prevista |
| dataPrevistaFinal | query | No | string | Data final prevista |
| numero | query | No | integer | Número do pedido de venda |
| idLoja | query | No | integer | ID da loja |
| idVendedor | query | No | integer | ID do vendedor |
| idControleCaixa | query | No | integer | ID do controle de caixa |
| numerosLojas[] | query | No | Array<string> | Conjunto de números de pedidos nas lojas |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/pedidos/vendas`

**Cria um pedido de venda**

Cria um pedido de venda.

#### Request Body

**Content-Type:** `application/json`

Schema: [VendasDadosBaseDTO](#schema-vendasdadosbasedto) & [VendasDadosDTO](#schema-vendasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/pedidos/vendas`

**Remove pedidos de vendas**

Remove pedidos de vendas pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsPedidosVendas[] | query | **Yes** | Array<integer> | IDs dos pedidos de vendas |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |

---

### GET `/pedidos/vendas/{idPedidoVenda}`

**Obtém um pedido de venda**

Obtém um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/pedidos/vendas/{idPedidoVenda}`

**Altera um pedido de venda**

Altera um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Request Body

**Content-Type:** `application/json`

Schema: [VendasDadosBaseDTO_PUT](#schema-vendasdadosbasedto_put) & [VendasDadosDTO](#schema-vendasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/pedidos/vendas/{idPedidoVenda}`

**Remove um pedido de venda**

Remove um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}`

**Altera a situação de um pedido de venda**

Altera a situação de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |
| idSituacao | path | **Yes** | integer | ID da situação do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}`

**Lança o estoque de um pedido de venda especificando o depósito**

Lança o estoque de um pedido de venda pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |
| idDeposito | path | **Yes** | integer | ID do depósito de estoque |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-estoque`

**Lança o estoque de um pedido de venda no depósito padrão**

Lança o estoque de um pedido de venda pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/estornar-estoque`

**Estorna o estoque de um pedido de venda**

Estorna o estoque de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-contas`

**Lança as contas de um pedido de venda**

Lança as contas de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/estornar-contas`

**Estorna as contas de um pedido de venda**

Estorna as contas de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/gerar-nfe`

**Gera nota fiscal eletrônica a partir do pedido de venda**

Gera nota fiscal eletrônica a partir do pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | [VendasCreateInvoiceResponseDTO](#schema-vendascreateinvoiceresponsedto) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/pedidos/vendas/{idPedidoVenda}/gerar-nfce`

**Gera nota fiscal de consumidor eletrônica a partir do pedido de venda**

Gera nota fiscal de consumidor eletrônica a partir do pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | [VendasCreateInvoiceResponseDTO](#schema-vendascreateinvoiceresponsedto) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos

### GET `/produtos`

**Obtém produtos**

Obtém produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| criterio | query | No | integer | Critério de listagem <br> `1` Últimos incluídos <br> `2` Ativos <br> `3` Inativos <br> `4` Excluídos <br> `5` Todos |
| tipo | query | No | string | `T` Todos <br> `P` Produtos <br> `S` Serviços <br> `E` Composições <br> `PS` Produtos simples <br> `C` Com variações <br> `V` Variações |
| idComponente | query | No | integer | ID do componente. Utilizado quando o filtro **tipo** for `E`. |
| dataInclusaoInicial | query | No | string | Data de inclusão inicial |
| dataInclusaoFinal | query | No | string | Data de inclusão final |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |
| idCategoria | query | No | integer | ID da categoria do produto |
| idLoja | query | No | integer | ID da loja |
| nome | query | No | string | Nome do produto |
| idsProdutos[] | query | No | Array<integer> | IDs dos produtos |
| codigos[] | query | No | Array<string> | Códigos (SKU) dos produtos |
| gtins[] | query | No | Array<string> | GTINs/EANs dos produtos |
| filtroSaldoEstoque | query | No | integer | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |
| filtroSaldoEstoqueDeposito | query | No | integer | ID do depósito para considerar no filtro de saldo em estoque. Se omitido, considera todos os depósitos. |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/produtos`

**Cria um produto**

Cria um produto.

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosDadosDTO](#schema-produtosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | [ProdutosResponse_POST_PUT](#schema-produtosresponse_post_put) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 403 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos`

**Remove múltiplos produtos**

Remove múltiplos produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/{idProduto}`

**Obtém um produto**

Obtém um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 403 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/{idProduto}`

**Altera um produto**

Altera um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosDadosDTO](#schema-produtosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [ProdutosResponse_POST_PUT](#schema-produtosresponse_post_put) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 403 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/{idProduto}`

**Remove um produto**

Remove um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/{idProduto}`

**Altera parcialmente um produto**

Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosDadosDTO](#schema-produtosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [ProdutosResponse_POST_PUT](#schema-produtosresponse_post_put) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 403 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/{idProduto}/situacoes`

**Altera a situação de um produto**

Altera a situação de um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/situacoes`

**Altera a situação de múltiplos produtos**

Altera a situação de múltiplos produtos pelos IDs.

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Estruturas

### GET `/produtos/estruturas/{idProdutoEstrutura}`

**Obtém a estrutura de um produto com composição**

Obtém a estrutura de um produto com composição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/estruturas/{idProdutoEstrutura}`

**Altera a estrutura de um produto com composição**

Altera a estrutura de um produto com composição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosEstruturaDTO](#schema-produtosestruturadto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/estruturas/{idProdutoEstrutura}/componentes`

**Adiciona componente(s) a uma estrutura**

Adiciona múltiplos componentes a uma estrutura pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Request Body

**Content-Type:** `application/json`

Schema: Array<[ProdutosComponenteDTO](#schema-produtoscomponentedto)>

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/estruturas/{idProdutoEstrutura}/componentes`

**Remove componentes específicos de um produto com composição**

Remove os componentes de um produto com composição pelos IDs dos componentes.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |
| idsComponentes[] | query | **Yes** | Array<integer> | IDs dos produtos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}`

**Altera um componente de uma estrutura**

Altera um componente de uma estrutura pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |
| idComponente | path | **Yes** | integer | ID do componente |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosComponenteDTO](#schema-produtoscomponentedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/estruturas`

**Remove a estrutura de múltiplos produtos**

Remove a estrutura de múltiplos produtos com composição pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Fornecedores

### GET `/produtos/fornecedores`

**Obtém produtos fornecedores**

Obtém produtos fornecedores paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idProduto | query | No | integer | ID do produto |
| idFornecedor | query | No | integer | ID do contato do tipo fornecedor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/produtos/fornecedores`

**Cria um produto fornecedor**

Cria um produto fornecedor.

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosFornecedoresDadosBaseDTO](#schema-produtosfornecedoresdadosbasedto) & [ProdutosFornecedoresDadosDTO](#schema-produtosfornecedoresdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/fornecedores/{idProdutoFornecedor}`

**Obtém um produto fornecedor**

Obtém um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/fornecedores/{idProdutoFornecedor}`

**Altera um produto fornecedor**

Altera um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosFornecedoresDadosBaseUpdateDTO](#schema-produtosfornecedoresdadosbaseupdatedto) & [ProdutosFornecedoresDadosUpdateDTO](#schema-produtosfornecedoresdadosupdatedto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/fornecedores/{idProdutoFornecedor}`

**Remove um produto fornecedor**

Remove um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Lojas

### GET `/produtos/lojas`

**Obtém vínculos de produtos com lojas**

Obtém vínculos de produtos com lojas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idProduto | query | No | integer | ID do produto |
| idLoja | query | No | integer | ID da loja |
| idCategoriaProduto | query | No | integer | ID da categoria do produto vinculada à loja |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/lojas`

**Cria o vínculo de um produto com uma loja**

Cria o vínculo de um produto com uma loja.

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosLojasDadosBaseDTO](#schema-produtoslojasdadosbasedto) & [ProdutosLojasDadosDTO](#schema-produtoslojasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/lojas/{idProdutoLoja}`

**Obtém um vínculo de produto com loja**

Obtém um vínculo de produto com loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/lojas/{idProdutoLoja}`

**Altera o vínculo de um produto com uma loja**

Altera o vínculo de um produto com uma loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosLojasDadosBaseDTO](#schema-produtoslojasdadosbasedto) & [ProdutosLojasDadosDTO](#schema-produtoslojasdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/lojas/{idProdutoLoja}`

**Remove o vínculo de um produto com uma loja**

Remove o vínculo de um produto com uma loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Lotes

### GET `/produtos/lotes`

**Obtém lotes de produtos**

Obtém lotes de produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |
| idsLotes[] | query | No | Array<string> | IDs dos lotes |
| idsDepositos[] | query | No | Array<integer> | IDs dos depósitos |
| codigosLotes[] | query | No | Array<string> | Códigos dos lotes |
| status | query | No | string | Status do lote |
| dataValidadeInicial | query | No | string | Data de validade inicial |
| dataValidadeFinal | query | No | string | Data de validade final |
| dataFabricacaoInicial | query | No | string | Data de fabricação inicial |
| dataFabricacaoFinal | query | No | string | Data de fabricação final |
| dataCriacaoInicial | query | No | string | Data de inclusão inicial |
| dataCriacaoFinal | query | No | string | Data de inclusão final |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/lotes`

**Salva lotes de produtos**

Cria/altera lotes de produtos.

#### Request Body

**Content-Type:** `application/json`

Schema: Array<[LotesDTO](#schema-lotesdto)>

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/produtos/lotes`

**Remove lotes de produtos**

Remove lotes de produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsLotes[] | query | **Yes** | Array<integer> | IDs dos lotes |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/lotes/{idLote}`

**Obtém um lote de um produto**

Obtém um lote de um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/produtos/lotes/{idLote}`

**Altera um lote de um produto**

Altera um lote de um produto pelo ID.

#### Request Body

**Content-Type:** `application/json`

Schema: [LotePutRequestDTO](#schema-loteputrequestdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/lotes/controla-lote`

**Obtém a informação se determinados produtos possuem controle de lote**

Obtém a informação se determinados produtos possuem controle de lote.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | Array<integer> | IDs dos produtos |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/{idProduto}/lotes/controla-lote/desativar`

**Desativa controle de lotes para o produto**

Desativa controle de lotes para o produto pelo ID do produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/lotes/{idLote}/status`

**Altera o status de um lote do produto**

Altera o status de um lote do produto pelo ID.

#### Request Body

**Content-Type:** `application/json`

Schema: [LoteStatusDTO](#schema-lotestatusdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Lotes Lançamentos

### GET `/produtos/lotes/{idLote}/lancamentos`

**Obtém os lançamentos de um lote de produto**

Obtém os lançamentos de um lote de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/lotes/{idLote}/lancamentos`

**Cria um lançamento de um lote**

Inclui lançamento de um lote.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Request Body

**Content-Type:** `application/json`

Schema: [LoteLancamentoDTO](#schema-lotelancamentodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/lotes/lancamentos/{idLancamento}`

**Obtém um lançamento de um lote de produto**

Obtém um lançamento de um lote de produto pelo ID do lançamento.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLancamento | path | **Yes** | integer | ID do lançamento |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/lotes/lancamentos/{idLancamento}`

**Altera a observação de um lançamento de um lote de um produto**

Altera a observação de um lançamento de um lote de um produto pelo ID do lançamento.

#### Request Body

**Content-Type:** `application/json`

Schema: [LoteLancamentoObservacaoDTO](#schema-lotelancamentoobservacaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo`

**Obtém o saldo de um lote de produto**

Obtém o saldo de um lote de produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo`

**Obtém os saldos dos lotes de um produto por depósito**

Obtém os saldos dos lotes de um produto por depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsLotes[] | query | **Yes** | Array<integer> | IDs dos lotes |
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma`

**Obtém a soma dos saldos dos lotes de um produto em um depósito**

Obtém a soma dos saldos dos lotes de um produto em um depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/produtos/{idProduto}/lotes/saldo/soma`

**Obtém o saldo total dos lotes de um produto**

Obtém o saldo total dos lotes de um produto pelo ID do produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Produtos - Variações

### GET `/produtos/variacoes/{idProdutoPai}`

**Obtém o produto e variações**

Obtém o produto e variações pelo ID do produto pai.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoPai | path | **Yes** | integer | ID do produto pai |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/produtos/variacoes/atributos/gerar-combinacoes`

**Retorna o produto pai com combinações de novas variações**

Ação responsável por retornar o produto pai com combinação de novas variações a partir dos atributos. Esta ação não persistirá os dados.

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosVariacoesCombinacaoDadosDTO](#schema-produtosvariacoescombinacaodadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/produtos/variacoes/{idProdutoPai}/atributos`

**Altera o nome do atributo nas variações**

Altera o nome do atributo nas variações de um produto pai.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoPai | path | **Yes** | integer | ID do produto pai |

#### Request Body

**Content-Type:** `application/json`

Schema: [ProdutosVariacoesDadosAtributoDTO](#schema-produtosvariacoesdadosatributodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Propostas Comerciais

### GET `/propostas-comerciais`

**Obtém propostas comerciais**

Obtém propostas comerciais paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| situacao | query | No | string | O valor referente a situação da proposta: Pendente, Aguardando, Não aprovado, Aprovado, Concluido, Rascunho. Para mais situações, pesquisar pelo número separado por vírgula. |
| idContato | query | No | integer | ID do contato |
| dataInicial | query | No | string | Data inicial |
| dataFinal | query | No | string | Data final |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### POST `/propostas-comerciais`

**Cria uma proposta comercial**

Cria uma proposta comercial.

#### Request Body

**Content-Type:** `application/json`

Schema: [OrcamentosDadosBaseDTO](#schema-orcamentosdadosbasedto) & [OrcamentosDadosDTO](#schema-orcamentosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/propostas-comerciais`

**Remove múltiplas propostas comerciais**

Remove múltiplas propostas comerciais pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsPropostasComerciais[] | query | **Yes** | Array<integer> | IDs das propostas comerciais |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/propostas-comerciais/{idPropostaComercial}`

**Obtém uma proposta comercial**

Obtém uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | [OrcamentosDadosBaseDTO](#schema-orcamentosdadosbasedto) & [OrcamentosDadosDTO](#schema-orcamentosdadosdto) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/propostas-comerciais/{idPropostaComercial}`

**Altera uma proposta comercial**

Altera uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Request Body

**Content-Type:** `application/json`

Schema: [OrcamentosDadosBaseDTO](#schema-orcamentosdadosbasedto) & [OrcamentosDadosDTO](#schema-orcamentosdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/propostas-comerciais/{idPropostaComercial}`

**Remove uma proposta comercial**

Remove uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/propostas-comerciais/{idPropostaComercial}/situacoes`

**Altera a situação de uma proposta comercial**

Altera a situação de uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Request Body

**Content-Type:** `application/json`

Schema: [OrcamentosSituacaoDTO](#schema-orcamentossituacaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Situações

### GET `/situacoes/{idSituacao}`

**Obtém uma situação**

Obtém uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/situacoes/{idSituacao}`

**Altera uma situação**

Altera uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Request Body

**Content-Type:** `application/json`

Schema: object & [SituacoesDadosDTO](#schema-situacoesdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/situacoes/{idSituacao}`

**Remove uma situação**

Remove uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/situacoes`

**Cria uma situação**

Cria uma situação.

#### Request Body

**Content-Type:** `application/json`

Schema: object & [SituacoesDadosDTO](#schema-situacoesdadosdto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Situações - Módulos

### GET `/situacoes/modulos`

**Obtém módulos**

Obtém módulos.

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/situacoes/modulos/{idModuloSistema}`

**Obtém situações de um módulo**

Obtém situações de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/situacoes/modulos/{idModuloSistema}/acoes`

**Obtém as ações de um módulo**

Obtém as ações de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/situacoes/modulos/{idModuloSistema}/transicoes`

**Obtém as transições de um módulo**

Obtém as transições de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Situações - Transições

### GET `/situacoes/transicoes/{idTransicao}`

**Obtém uma transição**

Obtém uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

### PUT `/situacoes/transicoes/{idTransicao}`

**Altera uma transição**

Altera uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Request Body

**Content-Type:** `application/json`

Schema: [SituacoesTransicaoDTO](#schema-situacoestransicaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### DELETE `/situacoes/transicoes/{idTransicao}`

**Remove uma transição**

Remove uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 404 |  | [ErrorResponse](#schema-errorresponse) |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### POST `/situacoes/transicoes`

**Cria uma transição**

Cria uma transição.

#### Request Body

**Content-Type:** `application/json`

Schema: [SituacoesTransicaoDTO](#schema-situacoestransicaodto)

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 201 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Usuários

### POST `/usuarios/recuperar-senha`

**Envia solicitação de recuperação de senha**

Envia solicitação de recuperação de senha por e-mail.

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### PATCH `/usuarios/redefinir-senha`

**Redefine senha do usuário**

Redefine senha do usuário utilizando token enviado por e-mail.

#### Request Body

**Content-Type:** `application/json`

Schema: object

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 204 | No content. | - |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

### GET `/usuarios/verificar-hash`

**Valida o hash recebido**

Valida o hash recebido por e-mail.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| hash | query | **Yes** | string |  |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 400 |  | [ErrorResponse](#schema-errorresponse) |

---

## Vendedores

### GET `/vendedores`

**Obtém vendedores**

Obtém vendedores paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| nomeContato | query | No | string | Nome do contato do vendedor |
| situacaoContato | query | No | string | Situação do contato do vendedor<br>`A` Ativo<br>`I` Inativo<br>`S` Sem movimento<br>`E` Excluído<br>`T` Todos |
| idContato | query | No | integer | ID do contato do vendedor |
| idLoja | query | No | integer | ID da loja vinculada ao vendedor |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |

---

### GET `/vendedores/{idVendedor}`

**Obtém um vendedor**

Obtém um vendedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idVendedor | path | **Yes** | integer | ID do vendedor |

#### Responses

| Status | Description | Schema |
|--------|-------------|--------|
| 200 |  | object |
| 404 |  | [ErrorResponse](#schema-errorresponse) |

---

## Component Schemas

<h3 id="schema-anunciosatributodto">AnunciosAtributoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do atributo. |
| id_externo | string | ID externo do atributo. |
| nome | string | Nome do atributo. |
| tipo | string | Tipo do atributo. |
| valor | string | Valor do atributo. |
| unidade | string | Unidade do atributo, se aplicável. |

<h3 id="schema-anuncioscategoriadto">AnunciosCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da categoria. |
| nome | string | Nome da categoria. |

<h3 id="schema-anunciosgetallresponsedto">AnunciosGetAllResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do anúncio. |
| titulo | string | Título do anúncio. |
| situacao | integer | Situação do anúncio. |

<h3 id="schema-anunciosgetattributesfromcategoryresponsedto">AnunciosGetAttributesFromCategoryResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do atributo. |
| nome | string | Nome do atributo. |
| obrigatorio | boolean | Se o atributo é obrigatório. |
| tipo | string | Tipo do atributo. |
| unidadePadrao | string | Unidade padrão do atributo. |
| minimo | integer | Mínimo do atributo. |
| maximo | integer | Máximo do atributo. |

<h3 id="schema-anunciosgetbyidresponsedto">AnunciosGetByIdResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do anúncio. |
| produto | object |  |
| titulo | string | Título do anúncio. |
| descricao | string | Descrição do anúncio. |
| status | integer | Situação do anúncio. |
| atributos | Array<[AnunciosAtributoDTO](#schema-anunciosatributodto)> |  |
| imagens | Array<[AnunciosImagemDTO](#schema-anunciosimagemdto)> |  |
| variacoes | Array<[AnunciosVariacaoDTO](#schema-anunciosvariacaodto)> |  |

<h3 id="schema-anunciosimagemdto">AnunciosImagemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da imagem. |
| url | string | URL da imagem. |
| ordem | integer | Ordem da imagem. |
| tipo | string | Tipo da imagem. |

<h3 id="schema-anunciossaverequest">AnunciosSaveRequest</h3>

**Combines:**
- [AnunciosSaveRequestBase](#schema-anunciossaverequestbase)
- object

<h3 id="schema-anunciossaverequestbase">AnunciosSaveRequestBase</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | object |  |
| integracao | object |  |
| loja | object |  |
| nome | string |  |
| descricao | string |  |
| preco | object |  |
| anuncioLoja | object |  |
| estoques | object |  |
| categoria | object |  |
| atributos | Array<object> |  |
| imagens | Array<object> |  |
| mercadoLivre | object |  |

<h3 id="schema-anunciossaveresponsedto">AnunciosSaveResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do anúncio salvo. |
| idsVariacoes | Array<integer> | Lista de IDs das variações associadas ao anúncio. |

<h3 id="schema-anunciosvariacaodto">AnunciosVariacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da variação. |
| nome | string | Nome da variação. |

<h3 id="schema-basepostresponse">BasePostResponse</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-borderoscategoriadto">BorderosCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-borderoscontatodto">BorderosContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-borderosdadosdto">BorderosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| data | string |  |
| historico | string |  |
| portador | [BorderosPortadorDTO](#schema-borderosportadordto) |  |
| categoria | [BorderosCategoriaDTO](#schema-borderoscategoriadto) |  |
| pagamentos | Array<[BorderosPagamentoDTO](#schema-borderospagamentodto)> |  |

<h3 id="schema-borderospagamentodto">BorderosPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| contato | [BorderosContatoDTO](#schema-borderoscontatodto) |  |
| numeroDocumento | string |  |
| valorPago | number |  |
| juros | number |  |
| desconto | number |  |
| acrescimo | number |  |
| tarifa | number | Tarifa da forma de pagamento |

<h3 id="schema-borderosportadordto">BorderosPortadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-caixasbancosdadosbasicocontatodto">CaixasBancosDadosBasicoContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| cnpj | string |  |

<h3 id="schema-caixasbancosdadosbasicoscategoriadto">CaixasBancosDadosBasicosCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-caixasbancosdadosbasicosorigemdto">CaixasBancosDadosBasicosOrigemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| tipo | string | Tipo da origem do lançamento <br> 'caixa' para lançamento de caixas e bancos <br> 'duplicata' para contas a receber/pagar <br> 'bordero' para pagamento/recebimento <br> 'estoque' para estoque |

<h3 id="schema-caixasbancositemlancamentodto">CaixasBancosItemLancamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | string | ID do lançamento de caixas e bancos |
| debCred | string | Débito ou crédito |
| situacao | string | Situação |
| valor | number | Valor |
| data | string | Data |
| observacoes | string | Observações |
| descricao | string | Descrição |
| origem | [CaixasBancosDadosBasicosOrigemDTO](#schema-caixasbancosdadosbasicosorigemdto) |  |
| contato | [CaixasBancosDadosBasicoContatoDTO](#schema-caixasbancosdadosbasicocontatodto) |  |
| contaFinanceira | [ContasFinanceirasDadosBasicosDTO](#schema-contasfinanceirasdadosbasicosdto) |  |

<h3 id="schema-caixasbancoslancamentoconciliacaomovimentacaodto">CaixasBancosLancamentoConciliacaoMovimentacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id da conciliação da movimentação |

<h3 id="schema-caixasbancoslancamentodto">CaixasBancosLancamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id do lançamento |
| debCred | string | Tipo de lançamento <br> `D` - Débito <br> `C` - Crédito |
| saldo | string | É ajuste de saldo após o lançamento <br> `S` - Sim <br> `N` - Não |
| situacao | string | Situação do lançamento <br> `R` - Registrado <br> `E` - Excluído <br> `H` - Escondido <br> `N` - Não registrado <br> `P` - Processando (externa) <br> `C` - Cancelado (externa) |
| transferencia | string | Indica se o lançamento é uma transferência <br> `1` - Sim <br> `0` - Não |
| tipoLancamento | string | Tipo do lançamento <br> `1` - Débito <br> `2` - Crédito |
| data | string | Data do lançamento |
| competencia | string | Data de competência do lançamento |
| valor | number | Valor do lançamento |
| observacoes | string | Observações adicionais sobre o lançamento |
| parcela | [CaixasBancosLancamentoParcelaDTO](#schema-caixasbancoslancamentoparceladto) |  |
| categoria | [CaixasBancosDadosBasicosCategoriaDTO](#schema-caixasbancosdadosbasicoscategoriadto) |  |
| conciliacaoMovimentacao | [CaixasBancosLancamentoConciliacaoMovimentacaoDTO](#schema-caixasbancoslancamentoconciliacaomovimentacaodto) |  |
| contato | [CaixasBancosDadosBasicoContatoDTO](#schema-caixasbancosdadosbasicocontatodto) |  |
| origem | [CaixasBancosDadosBasicosOrigemDTO](#schema-caixasbancosdadosbasicosorigemdto) |  |
| contaFinanceira | [ContasFinanceirasDadosBasicosDTO](#schema-contasfinanceirasdadosbasicosdto) |  |

<h3 id="schema-caixasbancoslancamentoparceladto">CaixasBancosLancamentoParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id da parcela do lançamento |

<h3 id="schema-caixasbancossalvarlancamentodto">CaixasBancosSalvarLancamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do lançamento (deve corresponder ao ID da URL) |
| data | string | Data do lançamento |
| valor | number | Valor do lançamento |
| debCred | string | Tipo de lançamento: <br> `C` - Crédito <br> `D` - Débito |
| competencia | string | Data de competência |
| observacoes | string | Observações do lançamento |
| transferencia | string | Indica se é uma transferência |
| contaFinanceira | [ContasFinanceirasDadosBasicosDTO](#schema-contasfinanceirasdadosbasicosdto) |  |
| categoria | [CaixasBancosDadosBasicosCategoriaDTO](#schema-caixasbancosdadosbasicoscategoriadto) |  |
| origem | [CaixasBancosDadosBasicosOrigemDTO](#schema-caixasbancosdadosbasicosorigemdto) |  |
| contato | [CaixasBancosDadosBasicoContatoDTO](#schema-caixasbancosdadosbasicocontatodto) |  |

<h3 id="schema-caixasbancossalvarlancamentoresponsedto">CaixasBancosSalvarLancamentoResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do lançamento criado |

<h3 id="schema-calculosimpostoscalculodto">CalculosImpostosCalculoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipoNota | integer | `0` Entrada <br> `1` Saída |
| uf | string | UF do destinatário |
| municipio | [CalculosImpostosMunicipioDTO](#schema-calculosimpostosmunicipiodto) |  |
| obterRegras | boolean | Se false, os valores das regras de tributação de cada imposto serão zerados (cst, alíquota, base, etc.) |
| crt | integer | CRT da empresa <br> `1` Simples Nacional <br> `2` Simples Nacional - excesso de sublimite de receita bruta <br> `3` Regime Normal <br> `4` MEI |
| loja | [CalculosImpostosLojaDTO](#schema-calculosimpostoslojadto) |  |
| produto | [CalculosImpostosProdutoDTO](#schema-calculosimpostosprodutodto) |  |

<h3 id="schema-calculosimpostoscbsdto">CalculosImpostosCbsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| regraOperacao | [CalculosImpostosRegraOperacaoDTO](#schema-calculosimpostosregraoperacaodto) |  |
| percentualCbs | number | Percentual CBS |
| percentualReducaoAliquota | number | % Redução Alíquota |
| aliquotaEfetiva | number | Alíquota Efetiva |
| percentualDiferimento | number | % Diferimento |
| codigoCreditoPresumido | string | Código Crédito Presumido |
| percentualCreditoPresumido | number | % Crédito Presumido CBS |

<h3 id="schema-calculosimpostoscofinsdto">CalculosImpostosCofinsDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosdadosbasedto">CalculosImpostosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| regraOperacao | [CalculosImpostosRegraOperacaoDTO](#schema-calculosimpostosregraoperacaodto) |  |
| tributacao | integer | `1` Tributado <br> `2` Isento <br> `3` Outra situação |
| cst | string |  |
| aliquota | number |  |
| base | number |  |
| valorBaseCalculo | number |  |
| valorImposto | number |  |
| observacoes | string |  |
| informacoesAdicionaisFisco | string |  |

<h3 id="schema-calculosimpostosdadosdto">CalculosImpostosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| faturada | boolean |  |
| observacoes | string |  |
| pisCofinsPresumido | boolean |  |
| somaImpostosTotal | boolean |  |
| somaIcmsTotal | boolean |  |
| aliquotaFunrural | number |  |
| descontaFunrural | boolean |  |
| consumidorFinal | boolean |  |
| retImpostoRetido | boolean |  |
| retAliquotaIr | number |  |
| retValorIr | number |  |
| retAliquotaCsll | number |  |
| retValorCsll | number |  |
| descontoCondicional | boolean |  |
| baseComissao | number |  |
| icms | [CalculosImpostosIcmsDTO](#schema-calculosimpostosicmsdto) |  |
| valorPmc | number |  |
| aliquotaValorAproxImpostos | number |  |
| informacoesAdicionaisFisco | string |  |
| incluirFreteIpi | boolean |  |
| simples | [CalculosImpostosSimplesDTO](#schema-calculosimpostossimplesdto) |  |
| ipi | [CalculosImpostosIpiDTO](#schema-calculosimpostosipidto) |  |
| issqn | [CalculosImpostosIssqnDTO](#schema-calculosimpostosissqndto) |  |
| pis | [CalculosImpostosPisDTO](#schema-calculosimpostospisdto) |  |
| cofins | [CalculosImpostosCofinsDTO](#schema-calculosimpostoscofinsdto) |  |
| icmsSt | [CalculosImpostosIcmsStDTO](#schema-calculosimpostosicmsstdto) |  |
| pisSt | [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto) |  |
| cofinsSt | [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto) |  |
| ii | [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto) |  |
| codigoBeneficioFiscal | string |  |
| porcentagemFcp | number |  |
| cfop | integer |  |
| simplesSt | [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto) |  |
| ibsCbs | [CalculosImpostosIbsCbsDTO](#schema-calculosimpostosibscbsdto) |  |
| ibs | [CalculosImpostosIbsDTO](#schema-calculosimpostosibsdto) |  |
| cbs | [CalculosImpostosCbsDTO](#schema-calculosimpostoscbsdto) |  |
| ibsCbsReg | [CalculosImpostosIbsCbsRegDTO](#schema-calculosimpostosibscbsregdto) |  |

<h3 id="schema-calculosimpostosibscbsdto">CalculosImpostosIbsCbsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| regraOperacao | [CalculosImpostosRegraOperacaoDTO](#schema-calculosimpostosregraoperacaodto) |  |
| cst | string | Código de Situação Tributária |
| classificacaoTributaria | string | Código de Classificação Tributária |
| valorBaseCalculo | number | Valor Base de Cálculo IBS/CBS |

<h3 id="schema-calculosimpostosibscbsregdto">CalculosImpostosIbsCbsRegDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| cstRegular | string | CST da Tributação Regular |
| classificacaoTributariaRegular | string | Classificação Tributária Regular |
| aliquotaEfetivaRegularIbsUf | number | Alíquota Efetiva Regular IBS UF |
| aliquotaEfetivaRegularIbsMunicipio | number | Alíquota Efetiva Regular IBS Município |
| aliquotaEfetivaRegularCbs | number | Alíquota Efetiva Regular CBS |
| valorTributacaoRegularIbsUf | number | Valor Tributação Regular IBS UF |
| valorTributacaoRegularIbsMunicipio | number | Valor Tributação Regular IBS Município |
| valorTributacaoRegularCbs | number | Valor Tributação Regular CBS |

<h3 id="schema-calculosimpostosibsdto">CalculosImpostosIbsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| regraOperacao | [CalculosImpostosRegraOperacaoDTO](#schema-calculosimpostosregraoperacaodto) |  |
| percentualIbsUf | number | Percentual IBS UF |
| percentualIbsMunicipio | number | Percentual IBS Município |
| percentualReducaoAliquotaUf | number | % Redução Alíquota UF |
| percentualReducaoAliquotaMunicipio | number | % Redução Alíquota Município |
| aliquotaEfetivaUf | number | Alíquota Efetiva UF |
| aliquotaEfetivaMunicipio | number | Alíquota Efetiva Município |
| percentualDiferimentoUf | number | % Diferimento UF |
| percentualDiferimentoMunicipio | number | % Diferimento Município |
| codigoCreditoPresumido | string | Código Crédito Presumido |
| percentualCreditoPresumido | number | % Crédito Presumido IBS |

<h3 id="schema-calculosimpostosicmsdto">CalculosImpostosIcmsDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosicmsstdto">CalculosImpostosIcmsStDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosipidto">CalculosImpostosIpiDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosissqndto">CalculosImpostosIssqnDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostoslojadto">CalculosImpostosLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| unidadeNegocio | [CalculosImpostosUnidadeNegocioDTO](#schema-calculosimpostosunidadenegociodto) |  |

<h3 id="schema-calculosimpostosmunicipiodto">CalculosImpostosMunicipioDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do município segundo a Tabela de Código de Município do IBGE |

<h3 id="schema-calculosimpostospisdto">CalculosImpostosPisDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosprodutodto">CalculosImpostosProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| valorUnitario | number |  |
| cupomFiscal | integer |  |
| origem | integer | `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br>`1` Estrangeira - Importação direta, exceto a indicada no código 6 <br>`2` Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 <br> `3` Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% <br>`4` Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes <br>`5` Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% <br>`6` Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX <br>`7` Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX <br> `8` Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |
| quantidade | number |  |

<h3 id="schema-calculosimpostosregraoperacaodto">CalculosImpostosRegraOperacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-calculosimpostossimplesdto">CalculosImpostosSimplesDTO</h3>

**Combines:**
- [CalculosImpostosDadosBaseDTO](#schema-calculosimpostosdadosbasedto)
- object

<h3 id="schema-calculosimpostosunidadenegociodto">CalculosImpostosUnidadeNegocioDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-camposcustomizadosagrupadordto">CamposCustomizadosAgrupadorDTO</h3>

Agrupadores por módulo <br> `produtos`: Categoria de produtos <br> `Contatos`: Tipos de contato

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do agrupador |

<h3 id="schema-camposcustomizadosdadosbasedto">CamposCustomizadosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string | Ignorado no método PUT |
| situacao | integer | `0` Inativo <br> `1` Ativo |

<h3 id="schema-camposcustomizadosdadosdto">CamposCustomizadosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| modulo | [CamposCustomizadosModuloBaseDTO](#schema-camposcustomizadosmodulobasedto) |  |
| tipoCampo | [CamposCustomizadosTipoBaseDTO](#schema-camposcustomizadostipobasedto) |  |

<h3 id="schema-camposcustomizadosdadosedicaodto">CamposCustomizadosDadosEdicaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| placeholder | string |  |
| obrigatorio | boolean |  |
| opcoes | Array<[CamposCustomizadosOpcaoDTO](#schema-camposcustomizadosopcaodto)> |  |
| tamanho | [CamposCustomizadosTamanhoDTO](#schema-camposcustomizadostamanhodto) |  |
| agrupadores | Array<[CamposCustomizadosAgrupadorDTO](#schema-camposcustomizadosagrupadordto)> |  |

<h3 id="schema-camposcustomizadosmodulobasedto">CamposCustomizadosModuloBaseDTO</h3>

Módulo associado ao campo customizado.

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-camposcustomizadosmodulodto">CamposCustomizadosModuloDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| modulo | string |  |
| agrupador | string | Atributo do cadastro utilizado como agrupador. |
| permissoes | Array<[CamposCustomizadosPermissaoDTO](#schema-camposcustomizadospermissaodto)> |  |

<h3 id="schema-camposcustomizadosopcaodto">CamposCustomizadosOpcaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da opção |
| nome | string | Nome da opção |

<h3 id="schema-camposcustomizadospermissaodto">CamposCustomizadosPermissaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| modulo | string |  |
| autorizado | boolean |  |

<h3 id="schema-camposcustomizadosresponse_post_put">CamposCustomizadosResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| idsVinculosAgrupadores | Array<integer> |  |
| idsOpcoes | Array<integer> |  |

<h3 id="schema-camposcustomizadostamanhodto">CamposCustomizadosTamanhoDTO</h3>

Número de caracteres ou valor mínimo e máximo

| Property | Type | Description |
|----------|------|-------------|
| minimo | integer |  |
| maximo | integer |  |

<h3 id="schema-camposcustomizadostipobasedto">CamposCustomizadosTipoBaseDTO</h3>

Tipo do campo customizado.

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-camposcustomizadostipodto">CamposCustomizadosTipoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| mascara | string |  |

<h3 id="schema-canalvendacanalvendadto">CanalVendaCanalVendaDTO</h3>

**Combines:**
- [CanalVendaDadosBaseDTO](#schema-canalvendadadosbasedto)
- object

<h3 id="schema-canalvendadadosbasedto">CanalVendaDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do canal de venda. |
| descricao | string | Descrição do canal de venda. |
| tipo | string | Tipo do canal de venda. |
| situacao | integer | Situação do canal de venda<br> `1` Habilitado<br> `2` Desabilitado |

<h3 id="schema-canalvendadepositodto">CanalVendaDepositoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-canalvendafilialdto">CanalVendaFilialDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| cnpj | string | CNPJ da filial. |
| idUnidadeNegocio | integer | ID da unidade de negócio. |
| unidadeNegocio | string | Nome da unidade de negócio. |
| deposito | [CanalVendaDepositoDTO](#schema-canalvendadepositodto) |  |
| padrao | boolean |  |

<h3 id="schema-canalvendatipointegracaodto">CanalVendaTipoIntegracaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| tipo | string |  |
| agrupador | integer | Agrupador do canal de venda |

<h3 id="schema-categoriaslojascategoriaprodutodto">CategoriasLojasCategoriaProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-categoriaslojasdadosdto">CategoriasLojasDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| loja | [CategoriasLojasLojaDTO](#schema-categoriaslojaslojadto) |  |
| descricao | string |  |
| codigo | string | Código da categoria na loja. |
| categoriaProduto | [CategoriasLojasCategoriaProdutoDTO](#schema-categoriaslojascategoriaprodutodto) |  |

<h3 id="schema-categoriaslojaslojadto">CategoriasLojasLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-categoriasprodutoscategoripaidto">CategoriasProdutosCategoriPaiDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id da categoria do produto pai. |

<h3 id="schema-categoriasprodutosdadosdto">CategoriasProdutosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string | Descrição da categoria |

<h3 id="schema-categoriasreceitasdespesasdadosbasedto">CategoriasReceitasDespesasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| idCategoriaPai | integer | Id da categoria pai. Se for a categoria raíz será 0. |
| descricao | string |  |
| tipo | integer | `1` Despesa<br>`2` Receita<br>`3` Receita e despesa |

<h3 id="schema-categoriasreceitasdespesasdadosdto">CategoriasReceitasDespesasDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| situacao | integer | `0` Inativa <br> `1` Ativa |

<h3 id="schema-categoriasreceitasdespesasdadospostdto">CategoriasReceitasDespesasDadosPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| grupoDRE | integer | `1` Não exibir DRE<br>`2` Receita Operacional Bruta<br>`3` Deduções da Receita Bruta<br>`7` Despesas Operacionais<br>`8` Receita Financeira<br>`9` Despesa Financeira<br>`10` Outras Receitas<br>`11` Outras Despesas<br>`13` IR e CSLL |

<h3 id="schema-configuracaoadicionalnotaservicodto">ConfiguracaoAdicionalNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| CFPS | string | Código Fiscal de Prestação de Serviço |
| CFOP | string | Código Fiscal de Operações e Prestações |
| AEDF | string | Autorização de Emissão de Documento Fiscal Eletrônico |
| proximoNumeroLote | integer |  |
| observacaoImpressaNota | string | Observação utilizada apenas para impressão |
| descricaoComplementar | string | Será adicionada abaixa da descrição do serviço em todas as notas |
| tipoEmissao | string | `T` Todos <br>`R` RPS e NFS-e <br>`N` Apenas NFS-e |
| campoNumeroDocContas | boolean | Escolha qual informação será utilizada como nº do documento ao lançar contas. Utilize o campo RPS caso o lançamento de contas ocorra antes do envio da nota |
| incentivadorFiscal | boolean |  |
| alterarSituacao | boolean | Permitir alteração de situação por usuários |
| incluirParcelas | boolean | Incluir informação das parcelas na descrição dos serviços na emissão da NFS-e |
| considerarDataParcela | boolean | Permite utilizar a data de vencimento da parcela da venda na geração automática de parcelas da nota de serviço |
| considerarDataOrdemServico | boolean | Permite utilizar a data de vencimento da parcela da ordem de serviço na geração automática de parcelas da nota de serviço |
| cadastroPrefeitura | [ConfiguracaoCadastroPrefeituraNotaServicoDTO](#schema-configuracaocadastroprefeituranotaservicodto) |  |

<h3 id="schema-configuracaoaproximadonotaservicodto">ConfiguracaoAproximadoNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| utilizarAliqIBPT | boolean | Utilizar alíquotas da tabela do IBPT para cálculo de tributos aproximados |
| percentualAliq | number | Alíquota para cálculo de impostos aproximados |

<h3 id="schema-configuracaobasicanotaservicodto">ConfiguracaoBasicaNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| emissorPadrao | integer |  |
| naturezaOperacao | integer |  |

<h3 id="schema-configuracaocsllpiscofinsnotaservicodto">ConfiguracaoCSLLPISCOFINSNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| calcular | boolean | Reter CSLL, PIS e COFINS para notas acima de R$ 5.000,00 (Descontinuado pela Lei 13.137) |
| reter | boolean | Reter CSLL, PIS e COFINS quando a soma desses impostos for maior que R$ 10,00(Lei 10.833) |

<h3 id="schema-configuracaocadastroprefeituranotaservicodto">ConfiguracaoCadastroPrefeituraNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| login | string |  |
| senha | string |  |

<h3 id="schema-configuracaocodigotributonotaservicodto">ConfiguracaoCodigoTributoNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| listaServico | string |  |
| tributacao | string |  |

<h3 id="schema-configuracaocontrolenotaservicodto">ConfiguracaoControleNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numeracaoRPS | [ConfiguracaoNumeracaoRPSNotaServicoDTO](#schema-configuracaonumeracaorpsnotaservicodto) |  |

<h3 id="schema-configuracaoemailpadraonotafiscalservicodto">ConfiguracaoEmailPadraoNotaFiscalServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| copia | string |  |
| resposta | string |  |

<h3 id="schema-configuracaoenvioemailnotaservicodto">ConfiguracaoEnvioEmailNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| enviarBoletoRPS | boolean | Enviar junto com o RPS o boleto das contas lançadas através do RPS ou do contrato |
| remetente | string |  |
| assunto | string |  |
| mensagem | string |  |
| padrao | [ConfiguracaoEmailPadraoNotaFiscalServicoDTO](#schema-configuracaoemailpadraonotafiscalservicodto) |  |

<h3 id="schema-configuracaoinssnotaservicodto">ConfiguracaoINSSNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| reter | boolean | Determina se o INSS deve ser retido |

<h3 id="schema-configuracaoirnotaservicodto">ConfiguracaoIRNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| percentual | number |  |
| valorMinimoAlternativoDescontol | number |  |
| descontar | boolean | Determina se o valor mínimo alternativo de desconto será aplicado |
| texto | [ConfiguracaoTextoIRNotaServicoDTO](#schema-configuracaotextoirnotaservicodto) |  |

<h3 id="schema-configuracaoissnotaservicodto">ConfiguracaoISSNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| zerar | boolean |  |
| reter | boolean |  |
| descontar | boolean |  |
| tributos | Array<[ConfiguracaoTributoNotaServicoDTO](#schema-configuracaotributonotaservicodto)> |  |

<h3 id="schema-configuracaoimpostonotaservicodto">ConfiguracaoImpostoNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| bloquearRetencaoPessoaFisica | boolean |  |
| IR | [ConfiguracaoIRNotaServicoDTO](#schema-configuracaoirnotaservicodto) |  |
| outros | [ConfiguracaoOutrosNotaServicoDTO](#schema-configuracaooutrosnotaservicodto) |  |

<h3 id="schema-configuracaonotaservicodadosbasedto">ConfiguracaoNotaServicoDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| basicas | [ConfiguracaoBasicaNotaServicoDTO](#schema-configuracaobasicanotaservicodto) |  |
| ISS | [ConfiguracaoISSNotaServicoDTO](#schema-configuracaoissnotaservicodto) |  |
| controle | [ConfiguracaoControleNotaServicoDTO](#schema-configuracaocontrolenotaservicodto) |  |
| impostos | [ConfiguracaoImpostoNotaServicoDTO](#schema-configuracaoimpostonotaservicodto) |  |
| envioEmail | [ConfiguracaoEnvioEmailNotaServicoDTO](#schema-configuracaoenvioemailnotaservicodto) |  |
| adicionais | [ConfiguracaoAdicionalNotaServicoDTO](#schema-configuracaoadicionalnotaservicodto) |  |

<h3 id="schema-configuracaonumeracaorpsnotaservicodto">ConfiguracaoNumeracaoRPSNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| cnpjEmitente | string |  |
| id | integer |  |
| numero | integer |  |
| serie | integer |  |

<h3 id="schema-configuracaooutrosnotaservicodto">ConfiguracaoOutrosNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| CSLLPISCOFINSDTO | [ConfiguracaoCSLLPISCOFINSNotaServicoDTO](#schema-configuracaocsllpiscofinsnotaservicodto) |  |
| INSS | [ConfiguracaoINSSNotaServicoDTO](#schema-configuracaoinssnotaservicodto) |  |
| aproximados | [ConfiguracaoAproximadoNotaServicoDTO](#schema-configuracaoaproximadonotaservicodto) |  |

<h3 id="schema-configuracaotextoirnotaservicodto">ConfiguracaoTextoIRNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| padrao | string |  |
| isento | string |  |

<h3 id="schema-configuracaotributonotaservicodto">ConfiguracaoTributoNotaServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID é passado apenas para tributos existentes para fins de atualização |
| percentualISS | number |  |
| CNAE | string |  |
| descricaoServico | string |  |
| padrao | boolean | Determina se o tributo em questão será o padrão para criação de notas |
| indicadorOperacao | string | Indicador de operação da reforma tributária |
| codigo | [ConfiguracaoCodigoTributoNotaServicoDTO](#schema-configuracaocodigotributonotaservicodto) |  |

<h3 id="schema-contasbaixarcontadto">ContasBaixarContaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| data | string |  |
| usarDataVencimento | boolean |  |
| portador | [ContasPortadorDTO](#schema-contasportadordto) |  |
| categoria | [ContasCategoriaDTO](#schema-contascategoriadto) |  |
| historico | string | Descriçao da conta para controle interno da empresa |
| juros | number | Valor em reais dos juros. |
| desconto | number | Valor em reais do desconto. |
| acrescimo | number | Valor em reais do acréscimo. |
| valorRecebido | number | Valor bruto da conta, incluindo a taxa do marketplace se aplicável. Se não for especificado, o valor total da conta será usado |
| tarifa | number | O valor da tarifa deve ser preenchido caso a forma de pagamento possua taxas de alíquota ou de valor fixo. |

<h3 id="schema-contascategoriadto">ContasCategoriaDTO</h3>

Categoria de receita e despesa

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contascontabeisdadosdto">ContasContabeisDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id da conta financeira |
| descricao | string | Descrição personalizada da conta financeira |
| tipo | string | `banco` Para configuração de boleto CNAB <br> `caixa` Portador caixa sem integração <br> `conta-bancaria` Contas configuradas para cashout (TED ou pix) <br>`integracao-pagamento` Configurações de integração (Bling Conta, Vindi...) |
| aliasIntegracao | string | Alias identificador da integração de pagamento |

<h3 id="schema-contascontatodto">ContasContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contasdadosbasedto">ContasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| situacao | integer | `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado |
| vencimento | string |  |
| valor | number |  |
| contato | [ContasContatoDTO](#schema-contascontatodto) |  |
| formaPagamento | [ContasFormaPagamentoDTO](#schema-contasformapagamentodto) |  |

<h3 id="schema-contasfinanceirasdadosbasicosdto">ContasFinanceirasDadosBasicosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-contasformapagamentodto">ContasFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contaspagardadosdto">ContasPagarDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| saldo | number | Valor total subtraído dos valores dos recebimentos |
| dataEmissao | string |  |
| vencimentoOriginal | string |  |
| numeroDocumento | string | Número para controle interno da empresa |
| competencia | string |  |
| historico | string | Descriçao da conta para controle interno da empresa |
| numeroBanco | string | Adicionado automaticamente com o número preenchido no cadastro do banco |
| portador | [ContasPortadorDTO](#schema-contasportadordto) |  |
| categoria | [ContasCategoriaDTO](#schema-contascategoriadto) |  |
| borderos | Array<integer> |  |
| ocorrencia | object |  |

<h3 id="schema-contaspagardadospostdto">ContasPagarDadosPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| ocorrencia | object |  |

<h3 id="schema-contasportadordto">ContasPortadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contasreceberautenticacaodto">ContasReceberAutenticacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | Tipo de autenticação:<br>`1` Código de autenticação por dois fatores<br>`4` Senha de 6 dígitos do app Bling Conta |
| codigo | string |  |

<h3 id="schema-contasreceberboletoscancelardto">ContasReceberBoletosCancelarDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| autenticacao | [ContasReceberAutenticacaoDTO](#schema-contasreceberautenticacaodto) |  |
| origem | [ContasReceberOrigemDTO](#schema-contasreceberorigemdto) |  |
| conta | [ContasReceberContaDTO](#schema-contasrecebercontadto) |  |
| motivo | string |  |

<h3 id="schema-contasreceberboletosdadosbasedto">ContasReceberBoletosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| venda | [ContasReceberVendaDTO](#schema-contasrecebervendadto) |  |
| notaFiscal | [ContasReceberNotaFiscalDTO](#schema-contasrecebernotafiscaldto) |  |
| valorTotal | number |  |
| contas | Array<[ContasReceberBoletosDadosDTO](#schema-contasreceberboletosdadosdto)> |  |

<h3 id="schema-contasreceberboletosdadosdto">ContasReceberBoletosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numeroExterno | string | Código de identificação do boleto |
| vencimento | string |  |
| valor | number |  |
| situacao | integer | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Parcialmente devolvido <br>`6` Cancelado |

<h3 id="schema-contasrecebercontacontabildto">ContasReceberContaContabilDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-contasrecebercontadto">ContasReceberContaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Para cancelar apenas uma conta, deve-se informar o ID da conta. |

<h3 id="schema-contasrecebercontatodto">ContasReceberContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| numeroDocumento | string |  |
| tipo | string |  |

<h3 id="schema-contasreceberdadosbasedto">ContasReceberDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| saldo | number | É calculado subtraindo os valores dos recebimentos do valor da conta |
| dataEmissao | string |  |
| vencimentoOriginal | string |  |
| numeroDocumento | string | Número para controle interno da empresa |
| competencia | string |  |
| historico | string | Descriçao da conta para controle interno da empresa |
| numeroBanco | string | Adicionado automaticamente com o número preenchido no cadastro do banco |
| portador | [ContasPortadorDTO](#schema-contasportadordto) |  |
| categoria | [ContasCategoriaDTO](#schema-contascategoriadto) |  |
| vendedor | [ContasReceberVendedorDTO](#schema-contasrecebervendedordto) |  |
| borderos | Array<integer> | IDs de borderos relacionados à conta caso ela possua pagamentos |

<h3 id="schema-contasreceberdadosdto">ContasReceberDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| ocorrencia | object |  |

<h3 id="schema-contasreceberdadoslistdto">ContasReceberDadosListDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| situacao | integer | `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado |
| vencimento | string |  |
| valor | number |  |
| idTransacao | string |  |
| linkQRCodePix | string |  |
| linkBoleto | string |  |
| dataEmissao | string |  |
| contato | [ContasReceberContatoDTO](#schema-contasrecebercontatodto) |  |
| formaPagamento | [ContasReceberFormaPagamentoDTO](#schema-contasreceberformapagamentodto) |  |
| contaContabil | [ContasReceberContaContabilDTO](#schema-contasrecebercontacontabildto) |  |
| origem | [ContasReceberDadosOrigemDTO](#schema-contasreceberdadosorigemdto) |  |

<h3 id="schema-contasreceberdadosorigemdto">ContasReceberDadosOrigemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| tipoOrigem | string |  |
| numero | string |  |
| dataEmissao | string |  |
| valor | number |  |
| situacao | integer | Situações da nota fiscal: <br> `1` Pendente: Situação inicial. <br> `3` Cancelada: Nota foi emitida e posteriormente cancelada. <br> `4` Aguardando recibo: Quando há uma tentativa de envio de uma nota pendente ou rejeitada. <br> `5` Rejeitada: Rejeição no envio. <br> `6` Autorizada: Sucesso no envio. <br> `7` Emitida DANFE: Após emitir a DANFE de uma nota autorizada. <br> `8` Registrada: Notas importadas no sistema. <br> `9` Aguardando protocolo: Durante uma tentativa de envio sem sucesso. <br> `10` Denegada: Devido a pendências do remetente ou destinatário junto à SEFAZ. <br> `11` Consulta situação: Quando a nota é rejeitada por duplicidade sem diferença na chave de acesso. <br> `12` Bloqueada: Quando ocorrem várias tentativas de envio que resultam na mesma rejeição. <br> `13` Contingência: Quando gerado xml e danfe em modo de contingência, aguardando envio da transmissão. Exclusiva da NFC-e. <br><br> Situações da venda: <br> `0` Em aberto <br> `1` Atendido <br> `2` Cancelado <br> `3` Em andamento <br> `5` Faturado parcialmente <br> `6` Atendido parcialmente <br> `7` Aguardando pagamento <br> `8` Pagamento confirmado <br> `10` Em digitação <br> `11` Verificado <br> `12` Checkout parcial |
| url | string |  |

<h3 id="schema-contasreceberformapagamentodto">ContasReceberFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| codigoFiscal | integer | `1` Dinheiro <br> `2` Cheque <br> `3` Cartão de crédito <br> `4` Cartão de débito <br> `5` Crédito loja <br> `10` Vale alimentação <br> `11` Vale refeição <br> `12` Vale presente <br> `13` Vale combustível <br> `14` Duplicata mercantil <br> `15` Boleto bancário <br> `16` Depósito bancário <br> `17` PIX <br> `18` Transferência bancária <br> `19` Cartão virtual <br> `90` Sem pagamento <br> `99` Outros |

<h3 id="schema-contasrecebernotafiscaldto">ContasReceberNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numero | string |  |

<h3 id="schema-contasreceberocorrenciadto">ContasReceberOcorrenciaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | `3` Mensal<br> `4` Bimestral<br> `5` Trimestral<br> `6` Semestral<br> `7` Anual<br> `8` Quinzenal<br> Ignorado no método PUT |
| considerarDiasUteis | boolean | Ignorado no método PUT |
| diaVencimento | integer |  |
| dataLimite | string |  |

<h3 id="schema-contasreceberocorrenciaparceladadto">ContasReceberOcorrenciaParceladaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | `2` Parcelada<br> Ignorado no método PUT |
| considerarDiasUteis | boolean | Ignorado no método PUT |
| diaVencimento | integer |  |
| numeroParcelas | integer | Ignorado no método PUT |

<h3 id="schema-contasreceberocorrenciasemanaldto">ContasReceberOcorrenciaSemanalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | `9` Semanal<br> Ignorado no método PUT |
| considerarDiasUteis | boolean | Ignorado no método PUT |
| diaSemanaVencimento | integer |  |
| dataLimite | string |  |

<h3 id="schema-contasreceberocorrenciaunicadto">ContasReceberOcorrenciaUnicaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | `1` Única<br> Ignorado no método PUT |

<h3 id="schema-contasreceberorigemdto">ContasReceberOrigemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da venda ou nota fiscal que originou a conta. |

<h3 id="schema-contasrecebervendadto">ContasReceberVendaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numero | string |  |

<h3 id="schema-contasrecebervendedordto">ContasReceberVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contatosalertasresponse">ContatosAlertasResponse</h3>

| Property | Type | Description |
|----------|------|-------------|
| alertas | Array<[ErrorResponse](#schema-errorresponse)> |  |

<h3 id="schema-contatosdadoadicionaldto">ContatosDadoAdicionalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| dataNascimento | string |  |
| sexo | string | `M` Masculino <br> `F` Feminino |
| naturalidade | string |  |

<h3 id="schema-contatosdadosbasedto">ContatosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| codigo | string |  |
| situacao | string | Situação do contato <br> `A` Ativo <br> `E` Excluído <br> `I` Inativo <br> `S` Sem movimentação |
| numeroDocumento | string | CPF ou CNPJ do contato |
| telefone | string |  |
| celular | string |  |

<h3 id="schema-contatosdadosdto">ContatosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| fantasia | string |  |
| tipo | string | Tipo da pessoa <br> `J` Jurídica <br> `F` Física <br> `E` Estrangeira |
| indicadorIe | integer | Indicador de inscrição estadual <br> `1` Contribuinte ICMS <br> `2` Contribuinte isento de Inscrição no cadastro de Contribuintes <br> `9` Não Contribuinte |
| ie | string | Inscrição estadual |
| rg | string | RG do contato caso for pessoa física |
| inscricaoMunicipal | string | Inscrição Municipal da empresa. Apenas para pessoa jurídica |
| orgaoEmissor | string | Órgão emissor caso for pessoa física |
| email | string |  |
| emailNotaFiscal | string | E-mail para envio da NF-e |
| numeroDocumento | string | CPF ou CNPJ do contato |
| orgaoPublico | string | Órgão público? <br> `N` Não <br> `M` Municipal <br> `E` Estadual <br> `F` Federal |
| endereco | [ContatosEnderecoDTO](#schema-contatosenderecodto) |  |
| vendedor | [ContatosVendedorDTO](#schema-contatosvendedordto) |  |
| dadosAdicionais | [ContatosDadoAdicionalDTO](#schema-contatosdadoadicionaldto) |  |
| financeiro | [ContatosFinanceiroDTO](#schema-contatosfinanceirodto) |  |
| pais | [ContatosPaisDTO](#schema-contatospaisdto) |  |
| tiposContato | Array<[ContatosTipoContatoDTO](#schema-contatostipocontatodto)> |  |
| pessoasContato | Array<[ContatosPessoaContatoDTO](#schema-contatospessoacontatodto)> |  |

<h3 id="schema-contatosenderecodto">ContatosEnderecoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| geral | [ContatosEnderecoDadosDTO](#schema-contatosenderecodadosdto) |  |
| cobranca | [ContatosEnderecoDadosDTO](#schema-contatosenderecodadosdto) |  |

<h3 id="schema-contatosenderecodadosdto">ContatosEnderecoDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| endereco | string |  |
| cep | string |  |
| bairro | string |  |
| municipio | string |  |
| uf | string |  |
| numero | string |  |
| complemento | string |  |

<h3 id="schema-contatosfinanceirocategoriadto">ContatosFinanceiroCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contatosfinanceirodto">ContatosFinanceiroDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| limiteCredito | number | Limite de crédito do cliente |
| condicaoPagamento | string | Número de parcelas ou prazos |
| categoria | [ContatosFinanceiroCategoriaDTO](#schema-contatosfinanceirocategoriadto) |  |

<h3 id="schema-contatospaisdto">ContatosPaisDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string | Nome do país do contato estrangeiro |

<h3 id="schema-contatospessoacontatodto">ContatosPessoaContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-contatostipocontatodto">ContatosTipoContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-contatosvendedordto">ContatosVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contratoscategoriadto">ContratosCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contratoscobrancacontatodto">ContratosCobrancaContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Deve ser informado apenas quando o contato de cobrança for diferente do contato vinculado ao contrato. |

<h3 id="schema-contratoscobrancadto">ContratosCobrancaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| dataBase | string |  |
| contato | [ContratosCobrancaContatoDTO](#schema-contratoscobrancacontatodto) |  |
| vencimento | [ContratosCobrancaVencimentoDTO](#schema-contratoscobrancavencimentodto) |  |

<h3 id="schema-contratoscobrancavencimentodto">ContratosCobrancaVencimentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipo | integer | `1` No mês corrente<br>`2` No mês seguinte<br>`3` Em dois meses |
| dia | integer | Caso o dia informado não exista em um determinado mês(29, 30, 31), o vencimento da cobrança utilizará o ultimo dia válido do mês. |
| periodicidade | integer | `1` Mensal<br>`2` Bimestral<br>`3` Trimestral<br>`4` Semestral<br>`5` Anual<br>`6` Bianual<br>`7` Trianual |

<h3 id="schema-contratoscontacontabildto">ContratosContaContabilDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contratoscontatodto">ContratosContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contratosdadosbasedto">ContratosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |
| data | string | Data de criação do contrato. |
| numero | string |  |
| valor | number |  |
| situacao | integer | `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento<br>`4` Em avaliação |
| contato | [ContratosContatoDTO](#schema-contratoscontatodto) |  |

<h3 id="schema-contratosdadosdto">ContratosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| dataFim | string | Formato: YYYY-MM |
| tipoManutencao | integer | `1` Valor <br> `2` Indexação |
| emitirOrdemServico | boolean |  |
| observacoes | string |  |
| vendedor | [ContratosVendedorDTO](#schema-contratosvendedordto) |  |
| categoria | [ContratosCategoriaDTO](#schema-contratoscategoriadto) |  |
| desconto | [ContratosDescontoDTO](#schema-contratosdescontodto) |  |
| contaContabil | [ContratosContaContabilDTO](#schema-contratoscontacontabildto) |  |
| formaPagamento | [ContratosFormaPagamentoDTO](#schema-contratosformapagamentodto) |  |
| notaFiscal | [ContratosNotaFiscalDTO](#schema-contratosnotafiscaldto) |  |
| cobranca | [ContratosCobrancaDTO](#schema-contratoscobrancadto) |  |

<h3 id="schema-contratosdescontodto">ContratosDescontoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valor | number |  |
| dataFim | string | Formato: YYYY-MM |

<h3 id="schema-contratosformapagamentodto">ContratosFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-contratosnotafiscaldto">ContratosNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| mes | integer | `1` Não imprime<br>`2` Mês atual<br>`3` Mês anterior<br>Período de referência da cobrança que será incluído nas informações complementares das notas fiscais e observações da conta a receber. |
| gerar | integer | `1` Não<br>`2` Ao gerar cobrança |
| descontarImpostoRenda | integer | `1` Sim<br>`2` Não<br>`3` Utilizar padrão da configuração da NFS-e<br>Reter o IR e descontar do total da NFS-e caso ultrapasse R$ 10,00. |
| texto | string | Texto a ser incluído nas informações complementares da NF-e ou como descrição do serviço na NFS-e. |
| cfop | string | Código fiscal. |
| iss | [ContratosNotaFiscalISSDTO](#schema-contratosnotafiscalissdto) |  |
| item | [ContratosNotaFiscalItemDTO](#schema-contratosnotafiscalitemdto) |  |

<h3 id="schema-contratosnotafiscalissdto">ContratosNotaFiscalISSDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descontar | boolean | Reter o ISS e descontar do total da nota. |
| aliquota | number | Percentual ISS específico para este contrato. Deixe este campo zerado para utilizar o padrão. |

<h3 id="schema-contratosnotafiscalitemdto">ContratosNotaFiscalItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigoServico | string | Código do serviço conforme tabela de serviços. |
| produto | [ContratosNotaFiscalItemProdutoDTO](#schema-contratosnotafiscalitemprodutodto) |  |

<h3 id="schema-contratosnotafiscalitemprodutodto">ContratosNotaFiscalItemProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do produto do tipo produto ou serviço. |

<h3 id="schema-contratosvendedorcomissaodto">ContratosVendedorComissaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| aliquota | number |  |
| numeroParcelas | integer |  |

<h3 id="schema-contratosvendedordto">ContratosVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| comissao | [ContratosVendedorComissaoDTO](#schema-contratosvendedorcomissaodto) |  |

<h3 id="schema-depositosdadosdto">DepositosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |
| situacao | integer | `0` Inativo <br> `1` Ativo |
| padrao | boolean |  |
| desconsiderarSaldo | boolean |  |

<h3 id="schema-empresasdadosbasicosdto">EmpresasDadosBasicosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | string | ID da empresa. |
| nome | string | Nome da empresa. |
| cnpj | string | CNPJ da empresa. |
| email | string | Email da empresa. |
| dataContrato | string | Data de início do contrato do plano. |

<h3 id="schema-error">Error</h3>

| Property | Type | Description |
|----------|------|-------------|
| type | string |  |
| message | string |  |
| description | string |  |
| fields | Array<[ErrorField](#schema-errorfield)> |  |

<h3 id="schema-errorfield">ErrorField</h3>

| Property | Type | Description |
|----------|------|-------------|
| code | integer |  |
| msg | string |  |
| element | string |  |
| namespace | string | Referência ao objeto com erro. |
| collection | Array<[ErrorFieldCollection](#schema-errorfieldcollection)> |  |

<h3 id="schema-errorfieldcollection">ErrorFieldCollection</h3>

| Property | Type | Description |
|----------|------|-------------|
| index | integer |  |
| code | integer |  |
| msg | string |  |
| element | string |  |
| namespace | string | Referência ao objeto com erro. |

<h3 id="schema-errorresponse">ErrorResponse</h3>

| Property | Type | Description |
|----------|------|-------------|
| error | [Error](#schema-error) |  |

<h3 id="schema-estoquegetallresponsedto">EstoqueGetAllResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| saldoVirtualTotal | number | Saldo em estoque atual, considerando a reserva de estoque. |

<h3 id="schema-estoquesdadosbasedto">EstoquesDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| operacao | string | `B` Balanço <br> `E` Entrada <br> `S` Saída |
| preco | number | Preço unitário |
| custo | number | Custo unitário |
| quantidade | number |  |
| observacoes | string |  |

<h3 id="schema-estoquesdadosdto">EstoquesDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [EstoquesProdutoDTO](#schema-estoquesprodutodto) |  |
| deposito | [EstoquesDepositoBaseDTO](#schema-estoquesdepositobasedto) |  |

<h3 id="schema-estoquesdepositobasedto">EstoquesDepositoBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-estoquesdepositodto">EstoquesDepositoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| saldoFisico | number | Saldo físico do produto |
| saldoVirtual | number | Saldo do produto desconsiderando produtos reservados |

<h3 id="schema-estoquesprodutodto">EstoquesProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| codigo | string |  |

<h3 id="schema-estoquessaldosbasedto">EstoquesSaldosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [EstoquesProdutoDTO](#schema-estoquesprodutodto) |  |
| saldoFisicoTotal | number | Saldo físico total do produto |
| saldoVirtualTotal | number | Saldo total do produto desconsiderando produtos reservados |

<h3 id="schema-estoquessaldosdto">EstoquesSaldosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| depositos | Array<[EstoquesDepositoBaseDTO](#schema-estoquesdepositobasedto) & [EstoquesDepositoDTO](#schema-estoquesdepositodto)> |  |

<h3 id="schema-formaspagamentosalterarsituacaodto">FormasPagamentosAlterarSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| situacao | integer | Situação que será alterada <br> `1` Ativa <br> `0` Inativa |

<h3 id="schema-formaspagamentosdadosbasedto">FormasPagamentosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |
| tipoPagamento | integer | `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Presente<br>`13` Vale Combustível<br>`14` Duplicata Mercantil<br>`15` Boleto Bancário<br>`16` Depósito Bancário<br>`17` Pagamento Instantâneo (PIX) - Dinâmico<br>`18` Transferência Bancária, Carteira Digital<br>`19` Programa de Fidelidade, Cashback, Crédito Virtual<br>`20` Pagamento Instantâneo (PIX) – Estático<br>`21` Crédito em loja<br>`22` Pagamento Eletrônico não Informado - falha de hardware do sistema emissor<br>`90` Sem pagamento<br>`99` Outros<br> |
| situacao | integer | `0` Inativa<br>`1` Ativa<br> |
| fixa | boolean |  |
| padrao | integer | `0` Não<br>`1` Padrão<br>`2` Padrão devolução |
| finalidade | integer | `1` Pagamentos<br>`2` Recebimentos<br>`3` Pagamentos e Recebimentos<br> |
| juros | number | Valor em porcentagem, com até 2 casas decimais. |
| multa | number | Valor em porcentagem, com até 2 casas decimais. |

<h3 id="schema-formaspagamentosdadoscartaodto">FormasPagamentosDadosCartaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| bandeira | integer | `1` Visa<br>`2` Mastercard<br>`3` American Express<br>`4` Sorocred<br>`5` Diners Club<br>`6` Elo<br>`7` Hipercard<br>`8` Aura<br>`9` Cabal<br>`99` Outros |
| tipo | integer | `1` TEF<br>`2` POS |
| cnpjCredenciadora | string | CNPJ da credenciadora. |
| autoLiquidacao | integer | `0` Não<br>`1` Sim - Liquidação automática dos recebíveis |

<h3 id="schema-formaspagamentosdadosdto">FormasPagamentosDadosDTO</h3>

O campo `dadosCartao` é utilizado quando o `tipoPagamento` for `3` ou `4`.

| Property | Type | Description |
|----------|------|-------------|
| condicao | string | Condição de pagamento padrão. |
| destino | integer | `1` Conta a receber/pagar<br>`2` Ficha financeira<br>`3` Caixa e bancos |
| utilizaDiasUteis | boolean | Indica se a forma de pagamento utiliza lançamentos em dias úteis. |
| taxas | [FormasPagamentosTaxaDTO](#schema-formaspagamentostaxadto) |  |
| dadosCartao | [FormasPagamentosDadosCartaoDTO](#schema-formaspagamentosdadoscartaodto) |  |

<h3 id="schema-formaspagamentosdefinirpadraodto">FormasPagamentosDefinirPadraoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| padrao | integer | `1` Pagamento <br> `2` Devolução<br>`3` Fiado |

<h3 id="schema-formaspagamentostaxadto">FormasPagamentosTaxaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| aliquota | number | Valor da alíquota sobre o valor da parcela. |
| valor | number | Valor em Reais somado ao valor total da parcela. |
| prazo | integer | Prazo em dias que o dinheiro é retido antes de estar disponível para movimentação. |

<h3 id="schema-fornecedorcontatodto">FornecedorContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do contato |
| nome | string | Nome do contato |

<h3 id="schema-gruposprodutosdadosdto">GruposProdutosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| grupoProdutoPai | [GruposProdutosGrupoProdutoPaiDTO](#schema-gruposprodutosgrupoprodutopaidto) |  |

<h3 id="schema-gruposprodutosgrupoprodutopaidto">GruposProdutosGrupoProdutoPaiDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |

<h3 id="schema-homologacaodadosbasedto">HomologacaoDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| preco | number |  |
| codigo | string |  |

<h3 id="schema-homologacaodadosdto">HomologacaoDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-homologacaosituacaodto">HomologacaoSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| situacao | string |  |

<h3 id="schema-logisticaservicopostdto">LogisticaServicoPostDTO</h3>

**Combines:**
- object

<h3 id="schema-logisticasdadosbasedto">LogisticasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da logística |
| descricao | string | Descrição da logística |
| tipoIntegracao | string | Tipo da logística |
| integracaoNativa | boolean |  |
| situacao | string | Situação da logística<br> `H` Habilitado<br> `D` Desabilitado |
| integracao | [LogisticasIntegracaoDTO](#schema-logisticasintegracaodto) |  |
| servicos | Array<[LogisticasServicoBaseDTO](#schema-logisticasservicobasedto)> | ID dos serviços vinculados a logística |

<h3 id="schema-logisticasdadosdto">LogisticasDadosDTO</h3>

**Combines:**
- [LogisticasDadosBaseDTO](#schema-logisticasdadosbasedto)
- object

<h3 id="schema-logisticasdadospostdto">LogisticasDadosPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descricao | string | Descrição da logística |
| situacao | string | Situação da logística<br> `H` Habilitado<br> `D` Desabilitado |
| servicos | Array<[LogisticaServicoPostDTO](#schema-logisticaservicopostdto)> | Serviços vinculados à logística |

<h3 id="schema-logisticasdadosputdto">LogisticasDadosPutDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descricao | string | Descrição da logística |
| situacao | string | Situação da logística<br> `H` Habilitado<br> `D` Desabilitado |

<h3 id="schema-logisticasetiquetasdadosresponsedto">LogisticasEtiquetasDadosResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da venda |
| link | string | Link para obter a etiqueta |
| observacao | string | Mensagem de observação |

<h3 id="schema-logisticasintegracaodto">LogisticasIntegracaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticaslogisticadto">LogisticasLogisticaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticaslogisticaremessadto">LogisticasLogisticaRemessaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasobjetosdadoscreaterequestdto">LogisticasObjetosDadosCreateRequestDTO</h3>

**Combines:**
- object
- [LogisticasObjetosUpdateRequestDTO](#schema-logisticasobjetosupdaterequestdto)

<h3 id="schema-logisticasobjetosdadosdto">LogisticasObjetosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| pedidoVenda | [LogisticasObjetosPedidoVendaDTO](#schema-logisticasobjetospedidovendadto) |  |
| notaFiscal | [LogisticasObjetosNotaFiscalDTO](#schema-logisticasobjetosnotafiscaldto) |  |
| servico | [LogisticasObjetosServicoDTO](#schema-logisticasobjetosservicodto) |  |
| rastreamento | [LogisticasObjetosRastreamentoDTO](#schema-logisticasobjetosrastreamentodto) |  |
| dimensao | [LogisticasObjetosDimensaoDTO](#schema-logisticasobjetosdimensaodto) |  |
| embalagem | [LogisticasObjetosEmbalagemDTO](#schema-logisticasobjetosembalagemdto) |  |
| dataSaida | string |  |
| prazoEntregaPrevisto | integer |  |
| fretePrevisto | number |  |
| valorDeclarado | number |  |
| avisoRecebimento | boolean |  |
| maoPropria | boolean |  |

<h3 id="schema-logisticasobjetosdimensaodto">LogisticasObjetosDimensaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| peso | number |  |
| altura | number |  |
| largura | number |  |
| comprimento | number |  |
| diametro | number |  |

<h3 id="schema-logisticasobjetosembalagemdto">LogisticasObjetosEmbalagemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do produto utilizado como embalagem |

<h3 id="schema-logisticasobjetosnotafiscaldto">LogisticasObjetosNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasobjetosobjetodto">LogisticasObjetosObjetoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasobjetospedidovendadto">LogisticasObjetosPedidoVendaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasobjetosrastreamentodto">LogisticasObjetosRastreamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigo | string |  |
| descricao | string |  |
| situacao | integer | `0` Postado <br> `1` Em andamento <br> `2` Não entregue <br> `3` Entregue <br> `4` Aguardando retirada <br> `5` Etiqueta comprada <br> `6` Vinculado <br> `7` Atrasado <br> `8` Não postado (recomendado para objetos recém-criados) <br> `9` Entrega suspensa |
| origem | string | Cidade e estado de origem |
| destino | string | Cidade e estado de destino |
| ultimaAlteracao | string | Data e hora em que ocorreu a atualização de rastreio. |
| url | string | URL de rastreamento |

<h3 id="schema-logisticasobjetosservicodto">LogisticasObjetosServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasobjetosupdaterequestdto">LogisticasObjetosUpdateRequestDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| rastreamento | [LogisticasObjetosRastreamentoDTO](#schema-logisticasobjetosrastreamentodto) |  |
| dimensoes | [LogisticasObjetosDimensaoDTO](#schema-logisticasobjetosdimensaodto) |  |
| embalagem | [LogisticasObjetosEmbalagemDTO](#schema-logisticasobjetosembalagemdto) |  |
| dataSaida | string |  |
| prazoEntregaPrevisto | integer |  |
| fretePrevisto | number |  |
| valorDeclarado | number |  |
| avisoRecebimento | boolean |  |
| maoPropria | boolean |  |

<h3 id="schema-logisticasremessaremessadto">LogisticasRemessaRemessaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasremessasdadosbasedto">LogisticasRemessasDadosBaseDTO</h3>

**Combines:**
- [LogisticasRemessasDadosBaseDTOCommon](#schema-logisticasremessasdadosbasedtocommon)
- object

<h3 id="schema-logisticasremessasdadosbasedtocommon">LogisticasRemessasDadosBaseDTOCommon</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numeroPlp | string |  |
| situacao | integer | `-3` A ser corrigida <br> `-2` Em processamento <br> `-1` Cancelado <br> `0` Em aberto <br> `1` Emitido <br> `2` Pronto para envio <br> `3` Despachado <br> `4` Pronto para envio <br> `5` Etiqueta comprada <br> `6` Etiqueta parcialmente comprada |
| descricao | string |  |
| dataCriacao | string |  |

<h3 id="schema-logisticasremessasdadosdto">LogisticasRemessasDadosDTO</h3>

**Combines:**
- [LogisticasRemessasDadosBaseDTOCommon](#schema-logisticasremessasdadosbasedtocommon)
- object

<h3 id="schema-logisticasremessasdadospostdto">LogisticasRemessasDadosPostDTO</h3>

**Combines:**
- [LogisticasRemessasDadosBaseDTOCommon](#schema-logisticasremessasdadosbasedtocommon)
- object

<h3 id="schema-logisticasremessasdimensaodto">LogisticasRemessasDimensaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| peso | number |  |
| altura | number |  |
| largura | number |  |
| comprimento | number |  |
| diametro | number |  |

<h3 id="schema-logisticasremessasembalagemdto">LogisticasRemessasEmbalagemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do produto utilizado como embalagem |

<h3 id="schema-logisticasremessasnotafiscaldto">LogisticasRemessasNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasremessasobjetosdto">LogisticasRemessasObjetosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| remessa | [LogisticasRemessaRemessaDTO](#schema-logisticasremessaremessadto) |  |
| pedidoVenda | [LogisticasRemessasPedidoVendaDTO](#schema-logisticasremessaspedidovendadto) |  |
| notaFiscal | [LogisticasRemessasNotaFiscalDTO](#schema-logisticasremessasnotafiscaldto) |  |
| servico | [LogisticasRemessasServicoDTO](#schema-logisticasremessasservicodto) |  |
| rastreamento | [LogisticasRemessasRastreamentoDTO](#schema-logisticasremessasrastreamentodto) |  |
| dimensao | [LogisticasRemessasDimensaoDTO](#schema-logisticasremessasdimensaodto) |  |
| embalagem | [LogisticasRemessasEmbalagemDTO](#schema-logisticasremessasembalagemdto) |  |
| dataSaida | string |  |
| prazoEntregaPrevisto | integer |  |
| fretePrevisto | number |  |
| valorDeclarado | number |  |
| avisoRecebimento | boolean |  |
| maoPropria | boolean |  |

<h3 id="schema-logisticasremessaspedidovendadto">LogisticasRemessasPedidoVendaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasremessasrastreamentodto">LogisticasRemessasRastreamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigo | string |  |
| descricao | string |  |
| situacao | integer | `0` Postado <br> `1` Em andamento <br> `2` Não entregue <br> `3` Entregue <br> `4` Aguardando retirada <br> `5` Em aberto <br> `6` Vinculado <br> `7` Atrasado <br> `8` Não postado <br> `9` Entrega suspensa |
| origem | string | Cidade e estado de origem |
| destino | string | Cidade e estado de destino |
| ultimaAlteracao | string | Data e hora em que ocorreu a atualização de rastreio. |
| url | string | URL de rastreamento |

<h3 id="schema-logisticasremessasservicodto">LogisticasRemessasServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| codigo | string |  |

<h3 id="schema-logisticasservicobasedto">LogisticasServicoBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do serviço da logística |

<h3 id="schema-logisticasservicodto">LogisticasServicoDTO</h3>

**Combines:**
- [LogisticasServicoBaseDTO](#schema-logisticasservicobasedto)
- object

<h3 id="schema-logisticasservicosdadoscreaterequestdto">LogisticasServicosDadosCreateRequestDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| logistica | [LogisticasServicosLogisticaDTO](#schema-logisticasservicoslogisticadto) |  |
| servicos | Array<[LogisticasServicosDadosSaveRequestDTO](#schema-logisticasservicosdadossaverequestdto)> | Serviços da logística |

<h3 id="schema-logisticasservicosdadosdto">LogisticasServicosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id do serviço |
| descricao | string | Descrição do serviço da logística |
| codigo | string | Código do serviço |
| aliases | Array<string> | Aliases do serviço |
| ativo | boolean | Define se está ativo ou não |
| freteItem | number | Valor do frete que será calculado para cada item do pedido |
| estimativaEntrega | integer | Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço. |
| idCodigoServico | string | Id do código do servico |
| logistica | [LogisticasServicosLogisticaDTO](#schema-logisticasservicoslogisticadto) |  |
| transportador | [LogisticasServicosTransportadorDTO](#schema-logisticasservicostransportadordto) |  |

<h3 id="schema-logisticasservicosdadossavedto">LogisticasServicosDadosSaveDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Id do serviço |

<h3 id="schema-logisticasservicosdadossaverequestdto">LogisticasServicosDadosSaveRequestDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descricao | string | Descrição do serviço da logística |
| codigo | string | Código do serviço |
| aliases | Array<string> | Aliases do serviço |
| ativo | boolean | Define se está ativo ou não |
| freteItem | number | Valor do frete que será calculado para cada item do pedido |
| estimativaEntrega | integer | Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço. |
| idCodigoServico | string | Id do código do servico |
| transportador | [LogisticasServicosTransportadorDTO](#schema-logisticasservicostransportadordto) |  |

<h3 id="schema-logisticasservicosdadossituationdto">LogisticasServicosDadosSituationDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| ativo | boolean | Define se está ativo ou não |

<h3 id="schema-logisticasservicoslogisticadto">LogisticasServicosLogisticaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticasservicostransportadordto">LogisticasServicosTransportadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-logisticastransportadordto">LogisticasTransportadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-lojaunidadenegociodto">LojaUnidadeNegocioDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-lotresponsedto">LotResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| codigoLote | string |  |
| idProduto | integer |  |

<h3 id="schema-lotelancamentodto">LoteLancamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do lancamento do lote |
| idLote | integer | ID do lote |
| quantidade | integer | Quantidade do lote |
| tipoLancamento | integer | Tipo de lançamento <br> `1` Entrada <br> `2` Saída <br> `3` Balanço |
| data | string | Data de lançamento |
| idOrigem | integer | ID da origem |
| observacao | string | Observação do lote |

<h3 id="schema-lotelancamentoobservacaodto">LoteLancamentoObservacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| observacao | string | Observação do lote |

<h3 id="schema-loteputrequestdto">LotePutRequestDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigoLote | string |  |
| dataFabricacao | string |  |
| dataValidade | string |  |
| diasPermitidoVenda | integer |  |
| codigoAgregacao | string |  |

<h3 id="schema-lotestatusdto">LoteStatusDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| status | integer | `1` Ativo <br> `2` Inativo |

<h3 id="schema-lotesdto">LotesDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idLote | integer |  |
| codigoLote | string |  |
| dataFabricacao | string |  |
| dataValidade | string |  |
| diasPermitidoVenda | integer |  |
| codigoAgregacao | string |  |
| produto | [LotesProdutoDTO](#schema-lotesprodutodto) |  |
| deposito | [LotesDepositoDTO](#schema-lotesdepositodto) |  |
| status | integer | `1` Ativo <br> `2` Inativo |

<h3 id="schema-lotesdepositodto">LotesDepositoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-lotesprodutodto">LotesProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-naturezasoperacoesdadosdto">NaturezasOperacoesDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| situacao | integer | `0` Inativo <br> `1` Ativo |
| padrao | integer | `0` Sem padrão <br>`1` Padrão venda <br> `2` Padrão compra <br> `3` Padrão venda física <br> `4` Padrão venda jurídica <br> `5` Padrão compra física <br> `6` Padrão compra jurídica <br> `7` Padrão venda cupom <br> `8` Padrão devolução (entrada) <br> `9` Padrão devolução (saída)  |
| descricao | string |  |

<h3 id="schema-notafiscalresponse_post">NotaFiscalResponse_POST</h3>

| Property | Type | Description |
|----------|------|-------------|
| numero | string |  |
| serie | string |  |
| contato | object |  |

<h3 id="schema-notasfiscaiscontatodto">NotasFiscaisContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| tipoPessoa | string | `F` Física <br> `J` Jurídica <br> `E` Estrangeira. |
| numeroDocumento | string | CNPJ ou CPF. |
| ie | string |  |
| rg | string |  |
| contribuinte | integer | `1` Contribuinte do ICMS <br> `2` Contribuinte isento de ICMS <br> `9` Não contribuinte. |
| telefone | string |  |
| email | string |  |
| endereco | [NotasFiscaisContatoEnderecoDTO](#schema-notasfiscaiscontatoenderecodto) |  |

<h3 id="schema-notasfiscaiscontatoenderecodto">NotasFiscaisContatoEnderecoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| endereco | string |  |
| numero | string |  |
| complemento | string |  |
| bairro | string |  |
| cep | string |  |
| municipio | string |  |
| uf | string |  |
| pais | string | País do cliente, caso o cliente for estrangeiro (uf: UX) |

<h3 id="schema-notasfiscaisdadosbasedto">NotasFiscaisDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| tipo | integer | `0` Entrada <br> `1` Saída |
| situacao | integer | `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada |
| numero | string |  |
| dataEmissao | string | Data e hora da emissão. |
| dataOperacao | string | Data de saída/entrada de acordo com o tipo da nota. |
| chaveAcesso | string |  |
| contato | [NotasFiscaisContatoDTO](#schema-notasfiscaiscontatodto) |  |
| naturezaOperacao | [NotasFiscaisNaturezaOperacaoDTO](#schema-notasfiscaisnaturezaoperacaodto) |  |
| loja | [NotasFiscaisLojaDTO](#schema-notasfiscaislojadto) |  |

<h3 id="schema-notasfiscaisdadosgetdto">NotasFiscaisDadosGetDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| serie | integer |  |
| valorNota | number |  |
| valorFrete | number |  |
| finalidade | integer | `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução |
| xml | string |  |
| linkDanfe | string |  |
| linkPDF | string |  |
| optanteSimplesNacional | boolean |  |
| numeroPedidoLoja | string |  |
| transporte | [NotasFiscaisTransporteGetDTO](#schema-notasfiscaistransportegetdto) |  |
| vendedor | [NotasFiscaisVendedorDTO](#schema-notasfiscaisvendedordto) |  |
| itens | Array<[NotasFiscaisItemDTO](#schema-notasfiscaisitemdto)> |  |
| parcelas | Array<[NotasFiscaisParcelaDTO](#schema-notasfiscaisparceladto)> |  |

<h3 id="schema-notasfiscaisdadospostdto">NotasFiscaisDadosPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| finalidade | integer | `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução |
| seguro | number |  |
| despesas | number |  |
| desconto | number |  |
| observacoes | string |  |
| xml | string |  |
| linkDanfe | string |  |
| linkPDF | string |  |
| documentoReferenciado | [NotasFiscaisDocumentoReferenciadoDTO](#schema-notasfiscaisdocumentoreferenciadodto) |  |
| documentosReferenciados | Array<[NotasFiscaisDocumentoReferenciadoDTO](#schema-notasfiscaisdocumentoreferenciadodto)> |  |
| itens | Array<[NotasFiscaisItemDTO](#schema-notasfiscaisitemdto)> |  |
| parcelas | Array<[NotasFiscaisParcelaDTO](#schema-notasfiscaisparceladto)> |  |
| transporte | [NotasFiscaisTransportePostDTO](#schema-notasfiscaistransportepostdto) |  |
| notaFiscalProdutorRuralReferenciada | [NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO](#schema-notasfiscaisnotafiscalprodutorruralreferenciadadto) |  |
| intermediador | [NotasFiscaisIntermediadorDTO](#schema-notasfiscaisintermediadordto) |  |

<h3 id="schema-notasfiscaisdocumentoreferenciadodto">NotasFiscaisDocumentoReferenciadoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| modelo | string | `1` Nota fiscal talão <br> `2` Nota fiscal de consumidor talão <br> `2D` Cupom fiscal <br> `4` Nota de produtor <br> `55` NF-e <br> `65` NFC-e |
| data | string | Data da nota original no formato AAMM. |
| numero | string | Número da nota original. |
| serie | string | Série da nota original. |
| contadorOrdemOperacao | string | Contador de Ordem de Operação (COO) do cupom original. |
| chaveAcesso | string | Chave de acesso da nota original. |

<h3 id="schema-notasfiscaisdocumentoreferenciadoitemdto">NotasFiscaisDocumentoReferenciadoItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| chaveAcesso | string | Chave de acesso da nota original. |
| numeroItem | string | Número do item na nota referenciada. |

<h3 id="schema-notasfiscaisexclusaodto">NotasFiscaisExclusaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| alertas | Array<string> |  |
| idsExcluidos | Array<integer> |  |

<h3 id="schema-notasfiscaisicmsdto">NotasFiscaisIcmsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| st | integer |  |
| origem | integer | `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br> `1` Estrangeira - Importação direta, exceto a indicada no código 6; 2: Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 <br> `3` Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% <br> `4` Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes <br> `5` Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% <br>`6` Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX <br> `7` Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX <br> `8`: Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |
| modalidade | integer | `0` Margem Valor Agregado (%) <br> `1` Pauta (valor) <br> `2` Preço Tabelado Máx. (valor) <br> `3` Valor da operação |
| aliquota | number |  |
| valor | number |  |

<h3 id="schema-notasfiscaisimpostodto">NotasFiscaisImpostoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valorAproximadoTotalTributos | number |  |
| icms | [NotasFiscaisIcmsDTO](#schema-notasfiscaisicmsdto) |  |

<h3 id="schema-notasfiscaisintermediadordto">NotasFiscaisIntermediadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| cnpj | string |  |
| nomeUsuario | string |  |

<h3 id="schema-notasfiscaisitemdto">NotasFiscaisItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigo | string |  |
| descricao | string |  |
| unidade | string |  |
| quantidade | number |  |
| valor | number | Valor unitário do item. |
| valorTotal | number |  |
| tipo | string | `P` Produto <br> `S` Serviço |
| pesoBruto | number |  |
| pesoLiquido | number |  |
| numeroPedidoCompra | string |  |
| classificacaoFiscal | string | NCM do item. |
| cest | string |  |
| codigoServico | string |  |
| origem | integer | `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br> `1` Estrangeira - Importação direta, exceto a indicada no código 6; 2: Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 <br> `3` Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% <br> `4` Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes <br> `5` Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% <br>`6` Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX <br> `7` Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX <br> `8`: Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |
| informacoesAdicionais | string |  |
| gtin | string |  |
| cfop | string |  |
| impostos | [NotasFiscaisImpostoDTO](#schema-notasfiscaisimpostodto) |  |
| documentoReferenciado | [NotasFiscaisDocumentoReferenciadoItemDTO](#schema-notasfiscaisdocumentoreferenciadoitemdto) |  |

<h3 id="schema-notasfiscaislojadto">NotasFiscaisLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | string |  |

<h3 id="schema-notasfiscaisnaturezaoperacaodto">NotasFiscaisNaturezaOperacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notasfiscaisnotafiscalprodutorruralreferenciadadto">NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numero | string | Número da NF referenciada. |
| serie | string | Série da NF referenciada. |
| data | string |  |

<h3 id="schema-notasfiscaisparceladto">NotasFiscaisParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| data | string |  |
| valor | number |  |
| observacoes | string |  |
| caut | string | cAut (ou NSU): código de autorização da operação financeira. |
| formaPagamento | [NotasFiscaisParcelaFormaPagamentoDTO](#schema-notasfiscaisparcelaformapagamentodto) |  |

<h3 id="schema-notasfiscaisparcelaformapagamentodto">NotasFiscaisParcelaFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notasfiscaistransportedadosvolumedto">NotasFiscaisTransporteDadosVolumeDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| quantidade | integer |  |
| especie | integer | <br>`1` Outro(s)<br> `2` Volume(s)<br> `3` Unidade(s)<br> `4` Caixa(s)<br> `5` Pacote(s)<br> `6` Envelope(s)<br> `7` Pallet(s)<br> `8` Saco(s) |
| numero | string |  |
| pesoBruto | number |  |
| pesoLiquido | number |  |

<h3 id="schema-notasfiscaistransporteetiquetadto">NotasFiscaisTransporteEtiquetaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| endereco | string |  |
| numero | string |  |
| complemento | string |  |
| municipio | string |  |
| uf | string |  |
| cep | string |  |
| bairro | string |  |

<h3 id="schema-notasfiscaistransportegetdto">NotasFiscaisTransporteGetDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| fretePorConta | integer | `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` Transporte Próprio por conta do Remetente <br> `4` Transporte Próprio por conta do Destinatário <br> `9` Sem Ocorrência de Transporte |
| transportador | [NotasFiscaisTransporteTransportadorGetDTO](#schema-notasfiscaistransportetransportadorgetdto) |  |
| volumes | Array<[NotasFiscaisTransporteVolumeGetDTO](#schema-notasfiscaistransportevolumegetdto)> |  |
| etiqueta | [NotasFiscaisTransporteEtiquetaDTO](#schema-notasfiscaistransporteetiquetadto) |  |

<h3 id="schema-notasfiscaistransportepostdto">NotasFiscaisTransportePostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| fretePorConta | integer | `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` Transporte Próprio por conta do Remetente <br> `4` Transporte Próprio por conta do Destinatário <br> `9` Sem Ocorrência de Transporte |
| frete | number | Utilizado no método POST. |
| veiculo | [NotasFiscaisTransporteVeiculoDTO](#schema-notasfiscaistransporteveiculodto) |  |
| transportador | [NotasFiscaisTransporteTransportadorPostDTO](#schema-notasfiscaistransportetransportadorpostdto) |  |
| volume | [NotasFiscaisTransporteDadosVolumeDTO](#schema-notasfiscaistransportedadosvolumedto) |  |
| volumes | Array<[NotasFiscaisTransporteVolumePostDTO](#schema-notasfiscaistransportevolumepostdto)> |  |
| etiqueta | [NotasFiscaisTransporteEtiquetaDTO](#schema-notasfiscaistransporteetiquetadto) |  |

<h3 id="schema-notasfiscaistransportetransportadorenderecodto">NotasFiscaisTransporteTransportadorEnderecoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| endereco | string |  |
| municipio | string |  |
| uf | string |  |

<h3 id="schema-notasfiscaistransportetransportadorgetdto">NotasFiscaisTransporteTransportadorGetDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| numeroDocumento | string | CNPJ ou CPF. |

<h3 id="schema-notasfiscaistransportetransportadorpostdto">NotasFiscaisTransporteTransportadorPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| numeroDocumento | string | CNPJ ou CPF. |
| ie | string | Inscrição estadual. |
| endereco | [NotasFiscaisTransporteTransportadorEnderecoDTO](#schema-notasfiscaistransportetransportadorenderecodto) |  |

<h3 id="schema-notasfiscaistransporteveiculodto">NotasFiscaisTransporteVeiculoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| placa | string |  |
| uf | string |  |
| marca | string |  |

<h3 id="schema-notasfiscaistransportevolumegetdto">NotasFiscaisTransporteVolumeGetDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notasfiscaistransportevolumepostdto">NotasFiscaisTransporteVolumePostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| servico | string | Utilizado no método POST. |
| codigoRastreamento | string | Utilizado no método POST. |

<h3 id="schema-notasfiscaisvendedordto">NotasFiscaisVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notasservicoscancelamentodto">NotasServicosCancelamentoDTO</h3>

Campos utilizados no cancelamento. Os campos são obrigatórios e disponíveis apenas para o ambiente de emissão nacional.

| Property | Type | Description |
|----------|------|-------------|
| codigoMotivo | integer | `1` Erro na Emissão<br> `2` Serviço não Prestado<br>`9` Outros |
| justificativa | string | Justificativa do cancelamento. |

<h3 id="schema-notasservicoscontatobasedto">NotasServicosContatoBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| numeroDocumento | string | CNPJ ou CPF. |
| email | string |  |

<h3 id="schema-notasservicoscontatodto">NotasServicosContatoDTO</h3>

Campos utilizados no POST.

| Property | Type | Description |
|----------|------|-------------|
| ie | string | Inscrição estadual. |
| telefone | string |  |
| im | string | Inscrição municipal. |
| endereco | [NotasServicosContatoEnderecoDTO](#schema-notasservicoscontatoenderecodto) |  |

<h3 id="schema-notasservicoscontatoenderecodto">NotasServicosContatoEnderecoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| endereco | string |  |
| numero | string |  |
| complemento | string |  |
| bairro | string |  |
| cep | string |  |
| municipio | string |  |
| uf | string |  |

<h3 id="schema-notasservicosdados">NotasServicosDados</h3>

| Property | Type | Description |
|----------|------|-------------|
| link | string | Link para acesso e impressão da NFS-e. |
| codigoVerificacao | string |  |

<h3 id="schema-notasservicosdadosbase">NotasServicosDadosBase</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | string |  |
| numeroRPS | string |  |
| serie | string |  |
| situacao | integer | `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada |
| dataEmissao | string |  |
| valor | number |  |

<h3 id="schema-notasservicosdadosbasedto">NotasServicosDadosBaseDTO</h3>

**Combines:**
- [NotasServicosDadosBase](#schema-notasservicosdadosbase)
- object

<h3 id="schema-notasservicosdadosbasedto_post">NotasServicosDadosBaseDTO_POST</h3>

**Combines:**
- [NotasServicosDadosBase](#schema-notasservicosdadosbase)
- object

<h3 id="schema-notasservicosdadosdto">NotasServicosDadosDTO</h3>

**Combines:**
- [NotasServicosDados](#schema-notasservicosdados)

<h3 id="schema-notasservicosdadosdto_post">NotasServicosDadosDTO_POST</h3>

**Combines:**
- [NotasServicosDados](#schema-notasservicosdados)
- object

<h3 id="schema-notasservicosparceladto">NotasServicosParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| data | string |  |
| valor | number |  |
| observacoes | string |  |
| formaPagamento | [NotasServicosParcelaFormaPagamentoDTO](#schema-notasservicosparcelaformapagamentodto) |  |

<h3 id="schema-notasservicosparcelaformapagamentodto">NotasServicosParcelaFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notasservicosresponse_post_put">NotasServicosResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numeroRPS | string |  |
| serie | string |  |

<h3 id="schema-notasservicosservicodto">NotasServicosServicoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| codigo | string |  |
| descricao | string |  |
| valor | number |  |

<h3 id="schema-notasservicostributacaoibscbsdto">NotasServicosTributacaoIbsCbsDTO</h3>

Dados de tributação IBS/CBS para NFS-e.

| Property | Type | Description |
|----------|------|-------------|
| indicadorOperacao | string | Código que indica onde a operação será realizada (6 dígitos). Valores comuns: '100301' = Domicílio do adquirente, '100302' = Local da prestação do serviço, '100303' = Outro local no país. Consulte sua contabilidade ou a legislação vigente para determinar o código adequado. |
| tipoOperacao | string | Tipo da operação tributável. Valores aceitos: '1' = Fornecimento de serviço (operação padrão onde o emitente é o prestador), '2' = Recebimento do pagamento (quando há intermediação ou pagamento diferido). |
| tipoEnteGovernamental | string | Tipo de ente governamental tomador do serviço. Informe APENAS quando o cliente for órgão público. Valores aceitos: '1' = União (órgão federal), '2' = Estado (órgão estadual), '3' = Distrito Federal, '4' = Município (órgão municipal). Se informado, pode haver redução ou isenção da alíquota conforme legislação. |
| tributacao | [NotasServicosTributacaoIbsCbsValoresDTO](#schema-notasservicostributacaoibscbsvaloresdto) |  |

<h3 id="schema-notasservicostributacaoibscbsvaloresdto">NotasServicosTributacaoIbsCbsValoresDTO</h3>

Valores e percentuais de tributação IBS/CBS. Consulte sua contabilidade ou a legislação vigente para determinar os códigos adequados à sua operação.

| Property | Type | Description |
|----------|------|-------------|
| codigoSituacaoTributaria | string | Código de Situação Tributária (CST) com 3 dígitos. Define o regime de tributação da operação. Exemplos: '000' = Tributação integral, '200' = Alíquota reduzida, '410' = Imunidade, '550' = Suspensão. Consulte sua contabilidade para determinar o CST correto conforme a natureza da operação. |
| classificacaoTributaria | string | Código da Classificação Tributária com 6 dígitos. Define a situação específica dentro do CST informado. Cada CST possui suas próprias classificações tributárias válidas. Exemplos: '000001' = Tributação integral, '200028' = Serviços de educação com redução de alíquota, '410004' = Exportação. Consulte sua contabilidade para o código correto conforme a natureza do serviço. |
| codigoCreditoPresumido | string | Código do crédito presumido (2 dígitos). Informe APENAS quando a classificação tributária conceder direito a crédito presumido. Consulte sua contabilidade para verificar se sua operação tem direito a crédito presumido e qual código utilizar. |
| cstRegimeRegular | string | CST aplicável ao regime regular de tributação (3 dígitos). Utilize quando a operação estiver em regime especial mas precisa informar a situação no regime regular. Consulte sua contabilidade para determinar se este campo é necessário. |
| classificacaoTributariaRegular | string | Classificação tributária para o regime regular (6 dígitos). Deve ser compatível com o 'cstRegimeRegular' informado. Consulte sua contabilidade para o código correto. |
| percentualDiferimentoEstadual | number | Percentual de diferimento do IBS estadual (parcela UF), de 0.00 a 100.00. O diferimento posterga o pagamento do imposto para etapa posterior da cadeia. Consulte sua contabilidade para verificar se há diferimento aplicável e qual percentual utilizar. |
| percentualDiferimentoMunicipal | number | Percentual de diferimento do IBS municipal, de 0.00 a 100.00. Aplica-se à parcela municipal do imposto sobre bens e serviços. Consulte sua contabilidade para verificar se há diferimento aplicável e qual percentual utilizar. |
| percentualDiferimentoCBS | number | Percentual de diferimento da Contribuição sobre Bens e Serviços (CBS), de 0.00 a 100.00. A CBS é o tributo federal da Reforma Tributária. Consulte sua contabilidade para verificar se há diferimento aplicável e qual percentual utilizar. |

<h3 id="schema-notasservicosvendedordto">NotasServicosVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-notificacoesdadosbasedto">NotificacoesDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| emitente | string | Nome do usuário que criou a notificação. |
| modulo | string |  |
| descricao | string | Mensagem do corpo da notificação. |
| titulo | string | Título no cabeçalho da notificação. |
| fonte | string | Nome do orgão ou entidade em que se baseia a informação. |
| linkAjuda | string | Link para direcionar o cliente à mais informações. |
| acao | string | Ação executada na notificação. |
| dataCriacao | string | Data de criação da notificação. |
| dataEnvio | string | Data de publicação da notificação. |
| dataVigencia | string | Data em que uma possível alteração informada entrará em vigor. |
| dataAcao | string | Data em que a ação foi realizada pelo usuário. |
| dataLeitura | string | Data em que o usuário leu a notificação. |
| dataAlerta | string | Data em que a notificação ficará com a cor amarela para alertar usuário. |
| dataPerigo | string | Data em que a notificação ficará com a cor vermelha para alertar usuário. |
| enquadramentos | Array<[NotificacoesEnquadramentosFiscaisDTO](#schema-notificacoesenquadramentosfiscaisdto)> |  |

<h3 id="schema-notificacoesenquadramentosfiscaisdto">NotificacoesEnquadramentosFiscaisDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tamanhoEmpresa | Array<string> | Perfil no qual a empresa se encaixa. |
| idMunicipio | Array<integer> | Código do município da empresa. |
| uf | Array<string> |  |
| crt | Array<integer> | Código de Regime Tributário |

<h3 id="schema-notificacoesquantidadedto">NotificacoesQuantidadeDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| quantidade | integer | Quantidade de notificações. |

<h3 id="schema-notificacoesulidsdto">NotificacoesUlidsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | string | ULID da notificação. |

<h3 id="schema-orcamentoscontatodto">OrcamentosContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-orcamentosdadosbasedto">OrcamentosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| data | string |  |
| situacao | string |  |
| total | number |  |
| totalProdutos | number |  |
| numero | integer |  |
| contato | [OrcamentosContatoDTO](#schema-orcamentoscontatodto) |  |
| loja | [OrcamentosLojaDTO](#schema-orcamentoslojadto) |  |

<h3 id="schema-orcamentosdadosdto">OrcamentosDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| desconto | number |  |
| outrasDespesas | number |  |
| garantia | integer |  |
| dataProximoContato | string |  |
| observacoes | string |  |
| observacaoInterna | string |  |
| totalOutrosItens | integer |  |
| aosCuidadosDe | string |  |
| introducao | string |  |
| prazoEntrega | string |  |
| itens | Array<[OrcamentosItemDTO](#schema-orcamentositemdto)> |  |
| parcelas | Array<[OrcamentosParcelaDTO](#schema-orcamentosparceladto)> |  |
| vendedor | [OrcamentosVendedorDTO](#schema-orcamentosvendedordto) |  |
| transporte | [OrcamentosTransporteDTO](#schema-orcamentostransportedto) |  |

<h3 id="schema-orcamentosformapagamentodto">OrcamentosFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-orcamentositemdto">OrcamentosItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [OrcamentosProdutoDTO](#schema-orcamentosprodutodto) |  |
| codigo | string |  |
| unidade | string |  |
| quantidade | number |  |
| desconto | number |  |
| valor | number |  |
| descricaoDetalhada | string |  |

<h3 id="schema-orcamentoslojadto">OrcamentosLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| unidadeNegocio | [LojaUnidadeNegocioDTO](#schema-lojaunidadenegociodto) |  |

<h3 id="schema-orcamentosparceladto">OrcamentosParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numeroDias | integer |  |
| dataVencimento | string |  |
| valor | number |  |
| observacoes | string |  |
| formaPagamento | [OrcamentosFormaPagamentoDTO](#schema-orcamentosformapagamentodto) |  |

<h3 id="schema-orcamentosprodutodto">OrcamentosProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descricao | string |  |

<h3 id="schema-orcamentossituacaodto">OrcamentosSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| situacao | string |  |

<h3 id="schema-orcamentostransportecontatodto">OrcamentosTransporteContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |

<h3 id="schema-orcamentostransportedto">OrcamentosTransporteDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| freteModalidade | integer | `0` Contratação do Frete por conta do Remetente (CIF)<br> `1` Contratação do Frete por conta do Destinatário (FOB)<br> `2` Contratação do Frete por conta de Terceiros<br> `3` Transporte Próprio por conta do Remetente<br> `4` Transporte Próprio por conta do Destinatário<br> `9` Sem Ocorrência de Transporte. |
| frete | number |  |
| quantidadeVolumes | number |  |
| prazoEntrega | integer |  |
| pesoBruto | number |  |
| contato | [OrcamentosTransporteContatoDTO](#schema-orcamentostransportecontatodto) |  |
| volumes | [OrcamentosTransporteVolumeDTO](#schema-orcamentostransportevolumedto) |  |

<h3 id="schema-orcamentostransportevolumedto">OrcamentosTransporteVolumeDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| servico | string |  |
| codigoRastreamento | string |  |

<h3 id="schema-orcamentosvendedordto">OrcamentosVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-ordensproducaocontatodto">OrdensProducaoContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |

<h3 id="schema-ordensproducaodadosbasedto">OrdensProducaoDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| dataPrevisaoInicio | string |  |
| dataPrevisaoFinal | string |  |
| dataInicio | string |  |
| dataFim | string |  |
| numero | integer |  |
| responsavel | string |  |
| deposito | [OrdensProducaoDepositoDTO](#schema-ordensproducaodepositodto) |  |
| situacao | [OrdensProducaoSituacaoDTO](#schema-ordensproducaosituacaodto) |  |

<h3 id="schema-ordensproducaodadosdto">OrdensProducaoDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| vendas | Array<[OrdensProducaoVendaDTO](#schema-ordensproducaovendadto)> |  |
| itens | Array<[OrdensProducaoItemDTO](#schema-ordensproducaoitemdto)> |  |
| observacoes | string |  |

<h3 id="schema-ordensproducaodadosgeradospordemandadto">OrdensProducaoDadosGeradosPorDemandaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| itens | Array<[OrdensProducaoItemDTO](#schema-ordensproducaoitemdto)> |  |
| deposito | [OrdensProducaoDepositoDTO](#schema-ordensproducaodepositodto) |  |

<h3 id="schema-ordensproducaodadospostdto">OrdensProducaoDadosPostDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| itens | Array<[OrdensProducaoItemDTO](#schema-ordensproducaoitemdto)> |  |
| observacoes | string |  |

<h3 id="schema-ordensproducaodepositodto">OrdensProducaoDepositoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idDestino | integer |  |
| idOrigem | integer |  |

<h3 id="schema-ordensproducaoitemdto">OrdensProducaoItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [OrdensProducaoProdutoDTO](#schema-ordensproducaoprodutodto) |  |
| quantidade | number |  |

<h3 id="schema-ordensproducaoprodutodto">OrdensProducaoProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| codigo | string |  |

<h3 id="schema-ordensproducaosituacaodto">OrdensProducaoSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| valor | integer |  |
| nome | string |  |

<h3 id="schema-ordensproducaosituacaodadosdto">OrdensProducaoSituacaoDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idSituacao | integer |  |
| quantidade | number |  |
| observacoes | string |  |
| considerarPerdas | boolean | Se deve considerar perdas na finalização da ordem de produção. (Válido apenas para finalização |

<h3 id="schema-ordensproducaovendadto">OrdensProducaoVendaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numero | integer |  |
| contato | [OrdensProducaoContatoDTO](#schema-ordensproducaocontatodto) |  |

<h3 id="schema-pedidoscompraresponse_post_put">PedidosCompraResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | integer |  |
| alertas | Array<string> |  |
| errosAnexo | Array<string> |  |

<h3 id="schema-pedidoscomprascategoriadto">PedidosComprasCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-pedidoscomprasdadosbasedto">PedidosComprasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | integer |  |
| data | string |  |
| dataPrevista | string |  |
| totalProdutos | number |  |
| total | number |  |
| fornecedor | [PedidosComprasFornecedorDTO](#schema-pedidoscomprasfornecedordto) |  |
| situacao | [PedidosComprasSituacaoDTO](#schema-pedidoscomprassituacaodto) |  |

<h3 id="schema-pedidoscomprasdadosdto">PedidosComprasDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| ordemCompra | string |  |
| observacoes | string |  |
| observacoesInternas | string |  |
| desconto | [PedidosComprasDescontoDTO](#schema-pedidoscomprasdescontodto) |  |
| categoria | [PedidosComprasCategoriaDTO](#schema-pedidoscomprascategoriadto) |  |
| tributacao | [PedidosComprasTributacaoDTO](#schema-pedidoscomprastributacaodto) |  |
| transporte | [PedidosComprasTransporteDTO](#schema-pedidoscomprastransportedto) |  |
| itens | Array<[PedidosComprasItemDTO](#schema-pedidoscomprasitemdto)> |  |
| parcelas | Array<[PedidosComprasParcelaDTO](#schema-pedidoscomprasparceladto)> |  |

<h3 id="schema-pedidoscomprasdescontodto">PedidosComprasDescontoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valor | number |  |
| unidade | string |  |

<h3 id="schema-pedidoscomprasformapagamentodto">PedidosComprasFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-pedidoscomprasfornecedordto">PedidosComprasFornecedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-pedidoscomprasitemdto">PedidosComprasItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descricao | string |  |
| codigoFornecedor | string |  |
| unidade | string |  |
| valor | number |  |
| quantidade | number |  |
| aliquotaIPI | number |  |
| descricaoDetalhada | string |  |
| notaFiscal | [PedidosComprasItemNotaFiscalDTO](#schema-pedidoscomprasitemnotafiscaldto) |  |
| produto | [PedidosComprasProdutoDTO](#schema-pedidoscomprasprodutodto) |  |

<h3 id="schema-pedidoscomprasitemnotafiscaldto">PedidosComprasItemNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da nota fiscal vinculada ao pedido de compra. |
| quantidade | number | Quantidade do item no pedido que foi vinculada a uma nota de entrada. |

<h3 id="schema-pedidoscomprasparceladto">PedidosComprasParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valor | number |  |
| dataVencimento | string |  |
| observacao | string |  |
| formaPagamento | [PedidosComprasFormaPagamentoDTO](#schema-pedidoscomprasformapagamentodto) |  |

<h3 id="schema-pedidoscomprasprodutodto">PedidosComprasProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| codigo | string |  |

<h3 id="schema-pedidoscomprassituacaodto">PedidosComprasSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valor | integer | `0` Em aberto <br> `1` Atendido <br> `2` Cancelado <br> `3` Em andamento <br> Ignorado no método POST. |

<h3 id="schema-pedidoscomprastransportedto">PedidosComprasTransporteDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| frete | number |  |
| transportador | string |  |
| fretePorConta | integer | `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` Transporte Próprio por conta do Remetente <br> `4` Transporte Próprio por conta do Destinatário <br> `9` Sem Ocorrência de Transporte |
| pesoBruto | number |  |
| volumes | integer |  |

<h3 id="schema-pedidoscomprastributacaodto">PedidosComprasTributacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| totalICMS | number |  |
| totalIPI | number | Calculado automaticamente com base no IPI dos itens. |

<h3 id="schema-produtocontrolalotesdto">ProdutoControlaLotesDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idProduto | integer | ID do produto |
| controlaLote | boolean | Indica se o produto controla lote |

<h3 id="schema-produtofornecedordto">ProdutoFornecedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do vínculo entre Produto e Fornecedor |
| contato | [FornecedorContatoDTO](#schema-fornecedorcontatodto) |  |
| codigo | string | Código do produto no fornecedor |
| precoCusto | number | Preço de custo do produto no fornecedor |
| precoCompra | number | Preço de compra do produto no fornecedor |

<h3 id="schema-produtosalertasresponse">ProdutosAlertasResponse</h3>

| Property | Type | Description |
|----------|------|-------------|
| alertas | Array<object & [ErrorResponse](#schema-errorresponse)> |  |

<h3 id="schema-produtosanexodto">ProdutosAnexoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosanexovinculodto">ProdutosAnexoVinculoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtoscampocustomizadodto">ProdutosCampoCustomizadoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idCampoCustomizado | integer |  |
| idVinculo | integer |  |
| valor | string |  |
| item | string |  |

<h3 id="schema-produtoscategoriadto">ProdutosCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtoscomponentedto">ProdutosComponenteDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [ProdutosComponenteProdutoDTO](#schema-produtoscomponenteprodutodto) |  |
| quantidade | number |  |

<h3 id="schema-produtoscomponenteprodutodto">ProdutosComponenteProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosdados">ProdutosDados</h3>

| Property | Type | Description |
|----------|------|-------------|
| dataValidade | string |  |
| unidade | string |  |
| pesoLiquido | number | Peso líquido em KG |
| pesoBruto | number | Peso bruto em KG |
| volumes | integer |  |
| itensPorCaixa | number |  |
| gtin | string | Código GTIN (GTIN-8, GTIN-12, GTIN-13 ou GTIN-14) do produto que está sendo comercializado |
| gtinEmbalagem | string | Código GTIN (GTIN-8, GTIN-12 ou GTIN-13) da menor unidade comercializada no varejo |
| tipoProducao | string | Tipo da produção <br> `P` Própria <br> `T` Terceiros |
| condicao | integer | Condição do produto <br> `0` Não especificado <br> `1` Novo <br> `2`Usado |
| freteGratis | boolean | Frete grátis <br> Valor default: `false` |
| marca | string |  |
| descricaoComplementar | string |  |
| linkExterno | string |  |
| observacoes | string |  |
| descricaoEmbalagemDiscreta | string | Descrição discreta do produto para utilizar na declaração de conteúdo. |
| categoria | [ProdutosCategoriaDTO](#schema-produtoscategoriadto) |  |
| estoque | [ProdutosEstoqueDTO](#schema-produtosestoquedto) |  |
| fornecedor | [ProdutoFornecedorDTO](#schema-produtofornecedordto) |  |
| actionEstoque | string | Ação de estoque ao transformar produto Simples em Variação <br> `Z` Irá zerar os saldos de estoque <br> `T` Transfere o estoque do produto pai para a primeira variação informada |
| dimensoes | [ProdutosDimensoesDTO](#schema-produtosdimensoesdto) |  |
| tributacao | [ProdutosTributacaoDTO](#schema-produtostributacaodto) |  |
| midia | [ProdutosMidiaDTO](#schema-produtosmidiadto) |  |
| linhaProduto | [ProdutosLinhaProdutoDTO](#schema-produtoslinhaprodutodto) |  |
| estrutura | [ProdutosEstruturaDTO](#schema-produtosestruturadto) |  |
| camposCustomizados | Array<[ProdutosCampoCustomizadoDTO](#schema-produtoscampocustomizadodto)> |  |
| artigoPerigoso | boolean | Indica se o produto é um artigo perigoso conforme regulamentação ANAC. Quando habilitado, adiciona automaticamente o código de serviço 095 nas etiquetas de envio. |

<h3 id="schema-produtosdadosbasedto">ProdutosDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| idProdutoPai | integer | ID do produto pai, caso seja uma variação. |
| nome | string |  |
| codigo | string |  |
| preco | number |  |
| precoCusto | number | Preço de custo do fornecedor padrão do produto. |
| estoque | [EstoqueGetAllResponseDTO](#schema-estoquegetallresponsedto) |  |
| tipo | string | Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22 |
| situacao | string | Situação do produto <br> `A` Ativo <br> `I` Inativo |
| formato | string | Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br> |
| descricaoCurta | string |  |
| imagemURL | string | Link da primeira imagem de acordo com tipo de armazenamento definido. |

<h3 id="schema-produtosdadosbasedto_getbyid">ProdutosDadosBaseDTO_GetByID</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| codigo | string |  |
| preco | number |  |
| tipo | string | Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22 |
| situacao | string | Situação do produto <br> `A` Ativo <br> `I` Inativo |
| formato | string | Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br> |
| descricaoCurta | string |  |
| imagemURL | string | Link da primeira imagem de acordo com tipo de armazenamento definido. |

<h3 id="schema-produtosdadosdto">ProdutosDadosDTO</h3>

**Combines:**
- [ProdutosDadosBaseDTO_GetByID](#schema-produtosdadosbasedto_getbyid)
- [ProdutosDados](#schema-produtosdados)
- object

<h3 id="schema-produtosdadosvariacaodto">ProdutosDadosVariacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| variacao | [ProdutosVariacaoDTO](#schema-produtosvariacaodto) |  |

<h3 id="schema-produtosdimensoesdto">ProdutosDimensoesDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| largura | number |  |
| altura | number |  |
| profundidade | number |  |
| unidadeMedida | integer | `0` Metros <br> `1` Centímetros <br> `2` Milímetros |

<h3 id="schema-produtosestoquedto">ProdutosEstoqueDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| minimo | number |  |
| maximo | number |  |
| crossdocking | integer |  |
| localizacao | string |  |
| saldoVirtualTotal | number | Saldo em estoque atual, considerando a reserva de estoque. |

<h3 id="schema-produtosestruturadto">ProdutosEstruturaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| tipoEstoque | string | `F` Físico<br> `V` Virtual |
| lancamentoEstoque | string | `A` Produto e Componente<br> `M` Componente<br> `P` Produto |
| componentes | Array<[ProdutosComponenteDTO](#schema-produtoscomponentedto)> |  |

<h3 id="schema-produtosfornecedoresdadosbasedto">ProdutosFornecedoresDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Utilizado no GET. |
| descricao | string | Descrição do produto no fornecedor. |
| codigo | string | Código do produto no fornecedor. |
| precoCusto | number | Valor de compra do produto com rateio de frete, descontos e impostos. |
| precoCompra | number | Valor de compra do produto. |
| padrao | boolean | Indica se é o fornecedor padrão do produto. |
| produto | [ProdutosFornecedoresProdutoDTO](#schema-produtosfornecedoresprodutodto) |  |
| fornecedor | [ProdutosFornecedoresFornecedorDTO](#schema-produtosfornecedoresfornecedordto) |  |

<h3 id="schema-produtosfornecedoresdadosbaseupdatedto">ProdutosFornecedoresDadosBaseUpdateDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Utilizado no GET. |
| descricao | string | Descrição do produto no fornecedor. |
| codigo | string | Código do produto no fornecedor. |
| precoCusto | number | Valor de compra do produto com rateio de frete, descontos e impostos. |
| precoCompra | number | Valor de compra do produto. |
| padrao | boolean | Indica se é o fornecedor padrão do produto. |
| produto | [ProdutosFornecedoresProdutoDTO](#schema-produtosfornecedoresprodutodto) |  |
| fornecedor | [ProdutosFornecedoresFornecedorUpdateDTO](#schema-produtosfornecedoresfornecedorupdatedto) |  |

<h3 id="schema-produtosfornecedoresdadosdto">ProdutosFornecedoresDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| garantia | integer | Quantidade de meses de garantia. |

<h3 id="schema-produtosfornecedoresdadosupdatedto">ProdutosFornecedoresDadosUpdateDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| garantia | integer | Quantidade de meses de garantia. |

<h3 id="schema-produtosfornecedoresfornecedordto">ProdutosFornecedoresFornecedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosfornecedoresfornecedorupdatedto">ProdutosFornecedoresFornecedorUpdateDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosfornecedoresprodutodto">ProdutosFornecedoresProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosgrupoprodutodto">ProdutosGrupoProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosimagemdto">ProdutosImagemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| link | string |  |

<h3 id="schema-produtosimageminternadto">ProdutosImagemInternaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| link | string |  |
| linkMiniatura | string |  |
| validade | string |  |
| ordem | integer |  |
| anexo | [ProdutosAnexoDTO](#schema-produtosanexodto) |  |
| anexoVinculo | [ProdutosAnexoVinculoDTO](#schema-produtosanexovinculodto) |  |

<h3 id="schema-produtosimagensdto">ProdutosImagensDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| imagensURL | Array<[ProdutosImagemDTO](#schema-produtosimagemdto)> |  |
| externas | Array<[ProdutosImagemDTO](#schema-produtosimagemdto)> |  |
| internas | Array<[ProdutosImagemInternaDTO](#schema-produtosimageminternadto)> |  |

<h3 id="schema-produtoslinhaprodutodto">ProdutosLinhaProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtoslojascategoriadto">ProdutosLojasCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da categoria de produto |

<h3 id="schema-produtoslojasdadosbasedto">ProdutosLojasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| codigo | string | Código do produto na loja virtual |
| preco | number |  |
| precoPromocional | number |  |
| produto | [ProdutosLojasProdutoDTO](#schema-produtoslojasprodutodto) |  |
| loja | [ProdutosLojasLojaDTO](#schema-produtoslojaslojadto) |  |
| fornecedorLoja | [ProdutosLojasFornecedorLojaDTO](#schema-produtoslojasfornecedorlojadto) |  |
| marcaLoja | [ProdutosLojasMarcaLojaDTO](#schema-produtoslojasmarcalojadto) |  |
| categoriasProdutos | [ProdutosLojasCategoriaDTO](#schema-produtoslojascategoriadto) |  |

<h3 id="schema-produtoslojasdadosdto">ProdutosLojasDadosDTO</h3>

**Combines:**
- [ProdutosLojasDadosBaseDTO](#schema-produtoslojasdadosbasedto)
- object

<h3 id="schema-produtoslojasfornecedorlojadto">ProdutosLojasFornecedorLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do fornecedor na loja virtual |

<h3 id="schema-produtoslojaslojadto">ProdutosLojasLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da loja no Bling |

<h3 id="schema-produtoslojasmarcalojadto">ProdutosLojasMarcaLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da marca do produto na loja virtual |

<h3 id="schema-produtoslojasprodutodto">ProdutosLojasProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID do produto no Bling |

<h3 id="schema-produtoslojasresponse_post_put">ProdutosLojasResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| categoriasProdutos | Array<object> |  |

<h3 id="schema-produtosmidiadto">ProdutosMidiaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| video | [ProdutosVideoDTO](#schema-produtosvideodto) |  |
| imagens | [ProdutosImagensDTO](#schema-produtosimagensdto) |  |

<h3 id="schema-produtosprodutopaidto">ProdutosProdutoPaiDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| cloneInfo | boolean |  |

<h3 id="schema-produtosresponse_post_put">ProdutosResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| data | object |  |

<h3 id="schema-produtostributacaodto">ProdutosTributacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| origem | integer |  |
| nFCI | string |  |
| ncm | string |  |
| cest | string |  |
| codigoListaServicos | string |  |
| spedTipoItem | string |  |
| codigoItem | string |  |
| percentualTributos | number |  |
| valorBaseStRetencao | number |  |
| valorStRetencao | number |  |
| valorICMSSubstituto | number |  |
| codigoExcecaoTipi | string |  |
| classeEnquadramentoIpi | string |  |
| valorIpiFixo | number |  |
| codigoSeloIpi | string |  |
| valorPisFixo | number |  |
| valorCofinsFixo | number |  |
| codigoANP | string |  |
| descricaoANP | string |  |
| percentualGLP | number |  |
| percentualGasNacional | number |  |
| percentualGasImportado | number |  |
| valorPartida | number |  |
| tipoArmamento | integer | Preencher quando a classificação do produto for armamento <br> `0` Uso permitido <br> `1` Uso restrito |
| descricaoCompletaArmamento | string |  |
| dadosAdicionais | string | Campo referente a tag infAdProd da nota fiscal |
| grupoProduto | [ProdutosGrupoProdutoDTO](#schema-produtosgrupoprodutodto) |  |

<h3 id="schema-produtosvariacaodto">ProdutosVariacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| ordem | integer |  |
| produtoPai | [ProdutosProdutoPaiDTO](#schema-produtosprodutopaidto) |  |

<h3 id="schema-produtosvariacoesatributodto">ProdutosVariacoesAtributoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| opcoes | Array<string> |  |

<h3 id="schema-produtosvariacoescombinacaodadosdto">ProdutosVariacoesCombinacaoDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produtoPai | [ProdutosVariacoesProdutoPaiDTO](#schema-produtosvariacoesprodutopaidto) |  |
| atributos | Array<[ProdutosVariacoesAtributoDTO](#schema-produtosvariacoesatributodto)> |  |

<h3 id="schema-produtosvariacoesdadosatributodto">ProdutosVariacoesDadosAtributoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| atributoAntigo | string |  |
| atributoNovo | string |  |

<h3 id="schema-produtosvariacoesprodutopaidto">ProdutosVariacoesProdutoPaiDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-produtosvideodto">ProdutosVideoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| url | string |  |

<h3 id="schema-saldolotedto">SaldoLoteDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idLote | integer | ID do lote |
| produto | [LotesProdutoDTO](#schema-lotesprodutodto) |  |
| deposito | [LotesDepositoDTO](#schema-lotesdepositodto) |  |
| saldoAtual | number | Saldo atual do lote |

<h3 id="schema-saldosomalotesdto">SaldoSomaLotesDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [LotesProdutoDTO](#schema-lotesprodutodto) |  |
| deposito | [LotesDepositoDTO](#schema-lotesdepositodto) |  |
| saldoTotal | number | Soma dos saldos de lotes |

<h3 id="schema-saldosomalotestodosdepositosdto">SaldoSomaLotesTodosDepositosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| produto | [LotesProdutoDTO](#schema-lotesprodutodto) |  |
| saldoTotal | number | Soma dos saldos de lotes |

<h3 id="schema-saveresponselotsdto">SaveResponseLotsDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| saved | Array<[LotResponseDTO](#schema-lotresponsedto)> |  |
| errors | Array<[ErrorResponse](#schema-errorresponse)> |  |

<h3 id="schema-situacoesacaodto">SituacoesAcaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string | Nome da ação. |
| descricao | string | Descrição da ação. |

<h3 id="schema-situacoesdto">SituacoesDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string | Utilizado no GET. |

<h3 id="schema-situacoesdadosdto">SituacoesDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idHerdado | integer | ID da situação de referência. |
| cor | string | Código hexadecimal. |

<h3 id="schema-situacoesmodulobasedto">SituacoesModuloBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-situacoesmodulodto">SituacoesModuloDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string | Nome do módulo. |
| descricao | string | Descrição do módulo. |
| criarSituacoes | boolean | Identifica a possibilidade de criar situações. |

<h3 id="schema-situacoestransicaodto">SituacoesTransicaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| ativo | boolean | Identifica se a transição está ativa. |
| acoes | Array<integer> |  |
| modulo | [SituacoesModuloBaseDTO](#schema-situacoesmodulobasedto) |  |
| situacaoOrigem | [SituacoesDTO](#schema-situacoesdto) |  |
| situacaoDestino | [SituacoesDTO](#schema-situacoesdto) |  |

<h3 id="schema-vendascategoriadto">VendasCategoriaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-vendascontatodto">VendasContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| tipoPessoa | string | `F` Física<br> `J` Jurídica<br> `E` Estrangeira |
| numeroDocumento | string | CNPJ ou CPF. |

<h3 id="schema-vendascreateinvoiceresponsedto">VendasCreateInvoiceResponseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| idNotaFiscal | integer |  |

<h3 id="schema-vendasdadosbasedto">VendasDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | integer |  |
| numeroLoja | string |  |
| data | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| dataSaida | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| dataPrevista | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| totalProdutos | number |  |
| total | number |  |
| contato | [VendasContatoDTO](#schema-vendascontatodto) |  |
| situacao | [VendasSituacaoDTO](#schema-vendassituacaodto) |  |
| loja | [VendasLojaDTO](#schema-vendaslojadto) |  |

<h3 id="schema-vendasdadosbasedto_put">VendasDadosBaseDTO_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| numero | integer |  |
| numeroLoja | string |  |
| data | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| dataSaida | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| dataPrevista | string | Valor obrigatório caso parâmetro de geração de parcelas seja este |
| totalProdutos | number |  |
| total | number |  |
| contato | [VendasContatoDTO](#schema-vendascontatodto) |  |
| situacao | [VendasSituacaoDTO_PUT](#schema-vendassituacaodto_put) |  |
| loja | [VendasLojaDTO](#schema-vendaslojadto) |  |

<h3 id="schema-vendasdadosdto">VendasDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| numeroPedidoCompra | string | Número da ordem de compra do pedido. |
| outrasDespesas | number |  |
| observacoes | string |  |
| observacoesInternas | string |  |
| desconto | [VendasDescontoDTO](#schema-vendasdescontodto) |  |
| categoria | [VendasCategoriaDTO](#schema-vendascategoriadto) |  |
| notaFiscal | [VendasNotaFiscalDTO](#schema-vendasnotafiscaldto) |  |
| tributacao | [VendasTributacaoDTO](#schema-vendastributacaodto) |  |
| itens | Array<[VendasItemDTO](#schema-vendasitemdto)> |  |
| parcelas | Array<[VendasParcelaDTO](#schema-vendasparceladto)> |  |
| transporte | [VendasTransporteDTO](#schema-vendastransportedto) |  |
| vendedor | [VendasVendedorDTO](#schema-vendasvendedordto) |  |
| intermediador | [VendasIntermediadorDTO](#schema-vendasintermediadordto) |  |
| taxas | [VendasTaxaDTO](#schema-vendastaxadto) |  |

<h3 id="schema-vendasdescontodto">VendasDescontoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| valor | number |  |
| unidade | string |  |

<h3 id="schema-vendasintermediadordto">VendasIntermediadorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| cnpj | string |  |
| nomeUsuario | string |  |

<h3 id="schema-vendasitemcomissaodto">VendasItemComissaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| base | number |  |
| aliquota | number |  |
| valor | number |  |

<h3 id="schema-vendasitemdto">VendasItemDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Ignorado no método POST. |
| codigo | string |  |
| unidade | string |  |
| quantidade | number |  |
| desconto | number | Valor percentual. |
| valor | number | Valor unitário do item. Preço de lista = 4.9 (valor) + 2% (desconto) |
| aliquotaIPI | number |  |
| descricao | string |  |
| descricaoDetalhada | string |  |
| produto | [VendasItemProdutoDTO](#schema-vendasitemprodutodto) |  |
| comissao | [VendasItemComissaoDTO](#schema-vendasitemcomissaodto) |  |
| naturezaOperacao | [VendasItemNaturezaOperacaoDTO](#schema-vendasitemnaturezaoperacaodto) |  |

<h3 id="schema-vendasitemnaturezaoperacaodto">VendasItemNaturezaOperacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | ID da natureza de operação |

<h3 id="schema-vendasitemprodutodto">VendasItemProdutoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-vendaslojadto">VendasLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| unidadeNegocio | [LojaUnidadeNegocioDTO](#schema-lojaunidadenegociodto) |  |

<h3 id="schema-vendasnotafiscaldto">VendasNotaFiscalDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-vendasparceladto">VendasParcelaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Ignorado no método POST. |
| dataVencimento | string |  |
| valor | number |  |
| observacoes | string |  |
| caut | string | cAut (ou NSU): código de autorização da operação financeira |
| formaPagamento | [VendasParcelaFormaPagamentoDTO](#schema-vendasparcelaformapagamentodto) |  |

<h3 id="schema-vendasparcelaformapagamentodto">VendasParcelaFormaPagamentoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-vendasresponse_post_put">VendasResponse_POST_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| alertas | Array<[ErrorField](#schema-errorfield)> |  |
| rastreamento | object | Dados de rastreamento. |

<h3 id="schema-vendassituacaodto">VendasSituacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| valor | integer |  |

<h3 id="schema-vendassituacaodto_put">VendasSituacaoDTO_PUT</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| valor | integer |  |

<h3 id="schema-vendastaxadto">VendasTaxaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| taxaComissao | number | Taxa de comissão perante ao total da venda. |
| custoFrete | number | Valor de custo do frete. |
| valorBase | number | Valor base da venda para demonstrativo de cálculo das taxas via interface (Se não informado considera o total da venda). |

<h3 id="schema-vendastransportecontatodto">VendasTransporteContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |

<h3 id="schema-vendastransportedto">VendasTransporteDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| fretePorConta | integer | `0` Contratação do Frete por conta do Remetente (CIF)<br> `1` Contratação do Frete por conta do Destinatário (FOB)<br> `2` Contratação do Frete por conta de Terceiros<br> `3` Transporte Próprio por conta do Remetente<br> `4` Transporte Próprio por conta do Destinatário<br> `9` Sem Ocorrência de Transporte. |
| frete | number |  |
| quantidadeVolumes | integer |  |
| pesoBruto | number |  |
| prazoEntrega | integer |  |
| contato | [VendasTransporteContatoDTO](#schema-vendastransportecontatodto) |  |
| etiqueta | [VendasTransporteEtiquetaDTO](#schema-vendastransporteetiquetadto) |  |
| volumes | Array<[VendasTransporteVolumeDTO](#schema-vendastransportevolumedto)> |  |

<h3 id="schema-vendastransporteetiquetadto">VendasTransporteEtiquetaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| nome | string |  |
| endereco | string |  |
| numero | string |  |
| complemento | string |  |
| municipio | string |  |
| uf | string |  |
| cep | string |  |
| bairro | string |  |
| nomePais | string | Utilizado quando a UF for 'EX' (estrangeiro). |

<h3 id="schema-vendastransportevolumedto">VendasTransporteVolumeDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Ignorado no método POST. |
| servico | string |  |
| codigoRastreamento | string |  |

<h3 id="schema-vendastributacaodto">VendasTributacaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| totalICMS | number |  |
| totalIPI | number |  |

<h3 id="schema-vendasvendedordto">VendasVendedorDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

<h3 id="schema-vendedorescomissaodto">VendedoresComissaoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| descontoMaximo | number |  |
| aliquota | number |  |

<h3 id="schema-vendedorescontatodto">VendedoresContatoDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| nome | string |  |
| situacao | string | `A` Ativo<br>`I` Inativo<br>`S` Sem movimento<br>`E` Excluído |

<h3 id="schema-vendedoresdadosbasedto">VendedoresDadosBaseDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |
| descontoLimite | number | Percentagem máxima para ceder como desconto, 0 para sem limite. |
| loja | [VendedoresLojaDTO](#schema-vendedoreslojadto) |  |
| contato | [VendedoresContatoDTO](#schema-vendedorescontatodto) |  |

<h3 id="schema-vendedoresdadosdto">VendedoresDadosDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| comissoes | Array<[VendedoresComissaoDTO](#schema-vendedorescomissaodto)> |  |

<h3 id="schema-vendedoreslojadto">VendedoresLojaDTO</h3>

| Property | Type | Description |
|----------|------|-------------|
| id | integer |  |

