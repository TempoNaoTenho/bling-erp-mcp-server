"""FastMCP app: create server and register tools/resources."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from fastmcp import FastMCP
from fastmcp.utilities.auth import parse_scopes

from bling_mcp.mcp.resource_store import get_resource_store
from bling_mcp.utils.logger import get_logger

if TYPE_CHECKING:
    pass

_mcp: FastMCP | None = None
_auth_provider = None
logger = get_logger(__name__)


def _build_auth_provider():
    provider = (os.getenv("FASTMCP_SERVER_AUTH") or "").strip()
    if not provider:
        return None

    if provider == "fastmcp.server.auth.providers.github.GitHubProvider":
        from fastmcp.server.auth.providers.github import GitHubProvider

        client_id = (os.getenv("FASTMCP_SERVER_AUTH_GITHUB_CLIENT_ID") or "").strip()
        client_secret = (os.getenv("FASTMCP_SERVER_AUTH_GITHUB_CLIENT_SECRET") or "").strip()
        base_url = (os.getenv("FASTMCP_SERVER_AUTH_GITHUB_BASE_URL") or "").strip()
        issuer_url = (os.getenv("FASTMCP_SERVER_AUTH_GITHUB_ISSUER_URL") or "").strip() or None
        redirect_path = (os.getenv("FASTMCP_SERVER_AUTH_GITHUB_REDIRECT_PATH") or "").strip() or None
        required_scopes = parse_scopes(os.getenv("FASTMCP_SERVER_AUTH_GITHUB_REQUIRED_SCOPES"))

        if not client_id or not client_secret or not base_url:
            logger.warning(
                "FastMCP OAuth (GitHub) not enabled: missing client_id/client_secret/base_url."
            )
            return None

        normalized_base = base_url.rstrip("/")
        if normalized_base.endswith("/mcp"):
            normalized_base = normalized_base[: -len("/mcp")] or normalized_base
        normalized_issuer = issuer_url.rstrip("/") if issuer_url else None
        if normalized_issuer and normalized_issuer.endswith("/mcp"):
            normalized_issuer = normalized_issuer[: -len("/mcp")] or normalized_issuer

        return GitHubProvider(
            client_id=client_id,
            client_secret=client_secret,
            base_url=normalized_base,
            issuer_url=normalized_issuer,
            redirect_path=redirect_path,
            required_scopes=required_scopes,
        )

    logger.warning("FASTMCP_SERVER_AUTH=%s not supported by this server.", provider)
    return None


def get_mcp() -> FastMCP | None:
    return _mcp


def get_auth_provider():
    return _auth_provider


def create_mcp() -> FastMCP:
    global _mcp
    global _auth_provider
    auth_provider = _build_auth_provider()
    _auth_provider = auth_provider
    _mcp = FastMCP(
        name="Bling ERP MCP Server",
        version="1.0.11",
        instructions="Tools for Bling ERP API v3: products, orders, invoices, contacts, stock. Use bling_auth_start to authenticate.",
        auth=auth_provider,
    )

    # Register dynamic resources for bling://resource/<id>
    store = get_resource_store()

    @_mcp.resource("bling://resource/{resource_id}")
    def get_bling_resource(resource_id: str) -> str:
        """Read a stored raw payload by resource ID (UUID)."""
        uri = f"bling://resource/{resource_id}"
        content = store.read_resource(uri)
        if content is None:
            return ""
        return content.get("text", "")

    # Register prompts
    from bling_mcp.mcp.prompts.assistant import register_prompts
    register_prompts(_mcp)

    # Register tools (must be after get_mcp() is set so tools can register)
    from bling_mcp.mcp.tools import bling_auth
    from bling_mcp.mcp.tools import clientes
    from bling_mcp.mcp.tools import pedidos
    from bling_mcp.mcp.tools import notas
    from bling_mcp.mcp.tools import estoque
    from bling_mcp.mcp.tools import openapi
    from bling_mcp.mcp.tools import produtos
    bling_auth.register_bling_auth_tools()
    clientes.register_clientes_tools()
    pedidos.register_pedidos_tools()
    notas.register_notas_tools()
    estoque.register_estoque_tools()
    openapi.register_openapi_tools()
    produtos.register_produtos_tools()
    
    # Register resources
    from bling_mcp.mcp.resources import register_resources
    register_resources(_mcp)

    return _mcp
