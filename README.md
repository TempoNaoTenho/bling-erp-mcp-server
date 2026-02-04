# Bling ERP MCP Server

MCP (Model Context Protocol) server for Bling ERP API v3, built with FastMCP 3.x in Python. It provides OAuth2 onboarding, a local wizard, and tools for products, orders, invoices, contacts, stock, and OpenAPI search.

---

## Portugues

### Requisitos

- Python 3.14
- uv (recomendado) ou pip
- Conta Bling com acesso a API
- App Bling configurado com Redirect URI

### Instalacao

#### Usando uv (recomendado)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone <repo>
cd bling-erp-mcp-server
uv sync
```

#### Usando pip

```bash
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install -e ".[dev]"
```

### Uso rapido (local)

1. Copie `.env.example` para `.env` e configure `BLING_CLIENT_ID` e `BLING_CLIENT_SECRET`.
2. Inicie o servidor via MCP client (stdio) ou diretamente:

```bash
python -m bling_mcp
```

3. Abra o wizard em `http://localhost:3333`.
4. Defina `PUBLIC_BASE_URL` (necessario para OAuth). Recomendado: Cloudflare Quick Tunnel:

```bash
cloudflared tunnel --url http://localhost:3333
```

5. Copie o Redirect URI exibido no wizard para o seu App da Bling.
6. Na aba de Autenticacao, clique em Authorize with Bling.

### MCP clients (stdio)

Exemplo (Claude Desktop / VS Code):

```json
{
  "mcpServers": {
    "bling": {
      "command": ".venv/bin/python",
      "args": ["-m", "bling_mcp"],
      "env": {
        "PORT": "3333"
      }
    }
  }
}
```

### MCP via HTTP (deploy)

Para uso em web clients, habilite o transporte HTTP:

```bash
MCP_TRANSPORT=http python -m bling_mcp
```

O MCP fica disponivel em `http://<host>:3333/mcp`.

### Variaveis de ambiente

Veja `.env.example`. Principais:

- `BLING_CLIENT_ID` / `BLING_CLIENT_SECRET`
- `PUBLIC_BASE_URL` (URL publica do wizard/redirect)
- `BLING_REDIRECT_URI` (opcional; deriva de PUBLIC_BASE_URL)
- `PORT` (default 3333)
- `MCP_TRANSPORT` (`stdio` ou `http`)
- `TOKEN_STORE_PATH` (arquivo JSON de tokens)
- `UI_ENABLE` (`on`/`off`)
- `UI_AUTH_MODE` (`none` ou `github`)
- `FASTMCP_SERVER_AUTH` e `FASTMCP_SERVER_AUTH_*` (OAuth do FastMCP para HTTP)

### Docker

Build e execute:

```bash
docker compose up --build
```

Crie um arquivo `.env` com:

```
BLING_CLIENT_ID=...
BLING_CLIENT_SECRET=...
PUBLIC_BASE_URL=...
```

O compose ja define `MCP_TRANSPORT=http` e monta `./data` para persistir tokens.

---

## English

### Requirements

- Python 3.14+
- uv (recommended) or pip
- Bling account with API access
- Bling App configured with a Redirect URI

### Installation

#### Using uv (recommended)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone <repo>
cd bling-erp-mcp-server
uv sync
```

#### Using pip

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"
```

### Quickstart (local)

1. Copy `.env.example` to `.env` and set `BLING_CLIENT_ID` and `BLING_CLIENT_SECRET`.
2. Start the server via MCP client (stdio) or directly:

```bash
python -m bling_mcp
```

3. Open the wizard at `http://localhost:3333`.
4. Set `PUBLIC_BASE_URL` (required for OAuth). Recommended: Cloudflare Quick Tunnel:

```bash
cloudflared tunnel --url http://localhost:3333
```

5. Copy the Redirect URI shown in the wizard into your Bling App settings.
6. In the Auth tab, click Authorize with Bling.

### MCP clients (stdio)

Example (Claude Desktop / VS Code):

```json
{
  "mcpServers": {
    "bling": {
      "command": ".venv/bin/python",
      "args": ["-m", "bling_mcp"],
      "env": {
        "PORT": "3333"
      }
    }
  }
}
```

### MCP over HTTP (deploy)

For web clients, enable HTTP transport:

```bash
MCP_TRANSPORT=http python -m bling_mcp
```

MCP endpoint: `http://<host>:3333/mcp`.

### Environment variables

See `.env.example`. Main options:

- `BLING_CLIENT_ID` / `BLING_CLIENT_SECRET`
- `PUBLIC_BASE_URL` (public URL for wizard/redirect)
- `BLING_REDIRECT_URI` (optional; derived from PUBLIC_BASE_URL)
- `PORT` (default 3333)
- `MCP_TRANSPORT` (`stdio` or `http`)
- `TOKEN_STORE_PATH` (token JSON file)
- `UI_ENABLE` (`on`/`off`)
- `UI_AUTH_MODE` (`none` or `github`)
- `FASTMCP_SERVER_AUTH` and `FASTMCP_SERVER_AUTH_*` (FastMCP OAuth for HTTP)

### Docker

Build and run:

```bash
docker compose up --build
```

Create a `.env` file with:

```
BLING_CLIENT_ID=...
BLING_CLIENT_SECRET=...
PUBLIC_BASE_URL=...
```

The compose file sets `MCP_TRANSPORT=http` and mounts `./data` to persist tokens.

---

## Project Structure

- `bling_mcp/__main__.py`: Entry point (stdio and/or HTTP + callback server)
- `bling_mcp/config.py`: Pydantic settings (env)
- `bling_mcp/auth/`: Token store, OAuth callback server, wizard UI
- `bling_mcp/bling/`: Bling API client, OAuth, views, OpenAPI search
- `bling_mcp/mcp/`: FastMCP app, tool helpers, resource store, tools

## License

See `LICENSE`.
