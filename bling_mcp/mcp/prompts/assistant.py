"""MCP prompts for common Bling ERP workflows."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def register_prompts(mcp: FastMCP) -> None:
    """Register all MCP prompts."""

    @mcp.prompt()
    def analyze_low_stock_products(threshold: int = 10, categoria: str = "") -> str:
        """Analyze products with low stock levels.

        Args:
            threshold: Minimum stock level to consider as low (default: 10)
            categoria: Optional category filter
        """
        prompt = f"""Analise os produtos com estoque baixo (abaixo de {threshold} unidades)"""
        if categoria:
            prompt += f""" na categoria "{categoria}"."""
        else:
            prompt += "."

        prompt += f"""

Use as seguintes etapas:
1. Liste todos os produtos usando bling_produtos_list com limite apropriado
2. Para cada produto, obtenha o saldo de estoque usando bling_produtos_estoque
3. Filtre produtos com saldo total abaixo de {threshold}
4. Agrupe por categoria e identifique padrões
5. Gere um relatório com:
   - Produtos críticos (estoque < 5)
   - Produtos de atenção (estoque entre 5 e {threshold})
   - Sugestões de reposição baseadas em histórico de vendas

Formate o resultado em tabela markdown com colunas: Código, Nome, Categoria, Estoque Atual, Status.
"""
        return prompt

    @mcp.prompt()
    def customer_order_history(customer_name: str, days: int = 90) -> str:
        """Generate customer order history report.

        Args:
            customer_name: Customer name to search for
            days: Number of days to look back (default: 90)
        """
        prompt = f"""Gere um relatório completo de histórico de pedidos para o cliente "{customer_name}" nos últimos {days} dias.

Use as seguintes etapas:
1. Busque o cliente usando bling_clientes_list com nome="{customer_name}"
2. Liste todos os pedidos do cliente usando bling_pedidos_list com filtro de data
3. Para pedidos relevantes, obtenha detalhes completos usando bling_pedidos_get
4. Calcule métricas:
   - Total de pedidos
   - Valor total gasto
   - Ticket médio
   - Produtos mais comprados
   - Frequência de compra
5. Identifique padrões:
   - Sazonalidade
   - Categorias preferidas
   - Formas de pagamento
   - Situação dos pedidos (cancelamentos, devoluções)

Formate o resultado com:
- Resumo executivo
- Tabela de pedidos (data, número, valor, situação)
- Gráfico de evolução de compras (em texto)
- Recomendações comerciais
"""
        return prompt

    @mcp.prompt()
    def find_invoice_by_order(order_number: str) -> str:
        """Match invoice (NFe) to order number.

        Args:
            order_number: Order number to find invoice for
        """
        prompt = f"""Encontre a nota fiscal (NFe) correspondente ao pedido #{order_number}.

Use as seguintes etapas:
1. Busque o pedido usando bling_pedidos_get com numero={order_number}
2. Extraia informações relevantes (data, cliente, valor, items)
3. Liste notas fiscais recentes usando bling_nfe_list com filtros apropriados:
   - Data próxima à data do pedido
   - Valor similar ao valor do pedido
4. Para cada NFe candidata, obtenha detalhes usando bling_nfe_get
5. Compare campos chave:
   - Cliente (nome, CPF/CNPJ)
   - Valor total
   - Items (códigos de produto)
   - Data de emissão vs data do pedido
6. Identifique a NFe correspondente ou explique por que não foi encontrada

Apresente:
- Status: ENCONTRADA ou NÃO ENCONTRADA
- Se encontrada: número da NFe, série, chave de acesso, data de emissão, link
- Se não encontrada: possíveis motivos (pedido não faturado, cancelado, em separação)
- Dados do pedido original para referência
"""
        return prompt

    @mcp.prompt()
    def product_availability_check(product_codes: str) -> str:
        """Check stock availability for multiple products.

        Args:
            product_codes: Comma-separated list of product codes
        """
        codes_list = [code.strip() for code in product_codes.split(",")]
        codes_formatted = ", ".join(codes_list)

        prompt = f"""Verifique a disponibilidade em estoque dos seguintes produtos: {codes_formatted}

Use as seguintes etapas:
1. Para cada código de produto:
   - Busque o produto usando bling_produtos_list com codigo=<codigo>
   - Obtenha o saldo de estoque usando bling_produtos_estoque
   - Verifique se há variações usando bling_produtos_variacoes
2. Compile informações:
   - Nome do produto
   - Código
   - Saldo disponível (físico vs virtual)
   - Localização no estoque
   - Variações disponíveis (se aplicável)
   - Preço de venda
   - Status (Ativo/Inativo)
3. Identifique problemas:
   - Produtos não encontrados
   - Produtos com estoque zerado
   - Produtos inativos
   - Divergências entre estoque físico e virtual

Formate como tabela markdown:
| Código | Nome | Estoque | Status | Observações |
Com legenda de status:
✅ Disponível (estoque > 10)
⚠️ Estoque baixo (1-10 unidades)
❌ Indisponível (estoque = 0)
🚫 Produto inativo ou não encontrado
"""
        return prompt

    @mcp.prompt()
    def discover_bling_api_endpoint(description: str) -> str:
        """Search Bling API OpenAPI reference for endpoints.

        Args:
            description: Description of the API functionality needed
        """
        prompt = f"""Encontre endpoints da API do Bling ERP relacionados a: "{description}"

Use as seguintes etapas:
1. Use bling_openapi_search para buscar endpoints relevantes com query="{description}"
2. Analise os resultados retornados:
   - Path do endpoint
   - Método HTTP (GET, POST, PUT, DELETE)
   - Descrição e funcionalidade
   - Parâmetros necessários
   - Estrutura de resposta
3. Para endpoints complexos, busque termos relacionados:
   - Sinônimos em português
   - Termos técnicos equivalentes
4. Identifique qual ferramenta MCP existente já implementa essa funcionalidade:
   - bling_produtos_* para produtos
   - bling_pedidos_* para pedidos
   - bling_nfe_* para notas fiscais
   - bling_clientes_* para contatos
   - bling_estoque_* para estoque
5. Se não houver ferramenta MCP correspondente, sugira como usar bling_openapi_search para explorar

Apresente:
- Endpoints encontrados (path, método, descrição)
- Ferramenta MCP equivalente (se existir)
- Exemplos de uso da ferramenta MCP
- Se não houver ferramenta: explicação de como a API poderia ser usada e sugestão de implementação
"""
        return prompt
