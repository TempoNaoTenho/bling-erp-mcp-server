# Changelog

Formato: YYYY-MM-DD

## 2026-02-03 - 1.0.11
- Melhora schema das tools com annotations MCP, descricoes e tipos (ResponseFormat, includes, enums).
- Padroniza envelope com suporte a responseFormat=raw, rawAsResource e maxItems/maxChars.
- Alinha filtros de produtos, pedidos e NFe com o bling-openapi-reference.md.
- Ajusta variacoes de produtos para usar endpoint dedicado (/produtos/variacoes/{idProdutoPai}).
- Adiciona suporte a consulta de estoque por deposito via idDeposito.
- Remove tools MCP OAuth nao utilizadas (mcp_auth_*).
- Separa estoque por deposito em tool dedicada (bling_estoque_saldos_por_deposito).

## 2026-02-03 - 1.0.10
- Alinha OAuth MCP ao padrao FastMCP via env (FASTMCP_SERVER_AUTH) e adiciona exemplo GitHub.
- Conecta o provider GitHub ao FastMCP (auth em /mcp) e expõe config efetiva em mcp_auth_status.
- Normaliza o base_url do OAuth para evitar mismatch /mcp vs /mcp/ no fluxo OAuth.
- Move UI para /ui e adiciona controles de acesso via UI_ENABLED e UI_AUTH_MODE.

## 2026-02-03 - 1.0.8
- Simplifica configuracao MCP para alinhar ao FastMCP: apenas `stdio` ou `http` e endpoint HTTP fixo em `/mcp`.
- Remove variaveis e ajustes customizados de MCP (path, CORS allowlist, API key, allowlist de IP, OAuth DCR).
- Corrige HTTP do FastMCP passando o lifespan do app MCP para o Starlette.

## 2026-02-02 - 1.0.7 (Python / FastMCP)
- **Migration to Python:** Project reimplemented in Python using FastMCP 3.x.
- **Stack:** Python 3.10+, FastMCP, Starlette, httpx, Pydantic Settings, Jinja2.
- **Wizard:** Full wizard UI (Status, Public URL, Auth, MCP) with same CSS and tab layout; theme toggle and export env.
- **Tools:** All tools ported (auth, produtos, clientes, pedidos, notas, estoque, openapi); envelope and truncation behavior preserved.
- **OAuth:** Bling OAuth callback and token store (JSON file); MCP HTTP optional at `/mcp`.
- **Removed:** TypeScript/Node codebase (src/, package.json, tsconfig.json).

## 2026-02-02 - 1.0.6
- Centraliza configurações de clientes OAuth em mcpClients.json e reforça allowlists (inclui callback do Claude.com).
- Remove MCP_AUTH_MODE e aplica política dinâmica de auth (OAuth/API key/local).
- Endurece OAuth (PKCE obrigatório, token_endpoint_auth_method validado, 401/403 com WWW-Authenticate e _meta).
- Migra storage de clientes dinâmicos para arquivo fora do src e adiciona allowlist de IP opcional.

## 2026-02-01 - 1.0.5
- Aceita resource com ou sem sufixo /mcp no fluxo OAuth.
- Adiciona botão na aba Bling para refresh manual e teste do access token.

## 2026-02-01 - 1.0.4
- Permite configurar redirect_uris adicionais para registro dinâmico OAuth (ex.: Claude/ChatGPT).

## 2026-02-01 - 1.0.3
- Melhora o refresh do token do Bling (serializa refresh e preserva refresh_token quando não retornado).
- Limpa tokens locais quando o refresh é rejeitado, alinhando status com falhas 401.

## 2026-01-31 - 1.0.2
- Adiciona tool para listar produtos por marca com paginação e filtros.
- Adiciona tool para lotes com validade próxima e saldo por depósito.
- Adiciona tools de pedidos recentes e resumo por período.
- Adiciona search tool para endpoints OpenAPI.
- Remove tools de escrita (POST/PATCH/DELETE) temporariamente.
- Melhora descrições e parâmetros das tools para reduzir custo de tokens.
