"""Configuration from environment (Pydantic Settings)."""

from __future__ import annotations

import os
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


def _normalize_public_base_url(value: str | None) -> str | None:
    if not value or not value.strip():
        return None
    trimmed = value.strip()
    if trimmed.startswith("http://") or trimmed.startswith("https://"):
        return trimmed
    return f"https://{trimmed}"


def _derive_public_base_url_from_redirect_uri(redirect_uri: str | None) -> str | None:
    if not redirect_uri:
        return None
    try:
        from urllib.parse import urlparse

        parsed = urlparse(redirect_uri)
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}"
    except Exception:
        pass
    return None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Bling (env: BLING_CLIENT_ID, BLING_CLIENT_SECRET, etc.)
    bling_client_id: str | None = None
    bling_client_secret: str | None = None
    bling_redirect_uri: str | None = None
    public_base_url: str | None = None

    # Tunnel
    cloudflare_tunnel_token: str | None = None
    cloudflare_tunnel_hostname: str | None = None

    # Server
    port: int = 3333
    node_env: Literal["development", "production"] = "development"
    ui_enable: Literal["on", "off"] | None = None
    ui_auth_mode: Literal["none", "github"] = "none"

    # MCP
    mcp_transport: Literal["stdio", "http"] = "stdio"

    # Storage
    token_store_path: str = ".tokens.json"

    @property
    def client_id(self) -> str | None:
        return self.bling_client_id

    @property
    def client_secret(self) -> str | None:
        return self.bling_client_secret

    @property
    def redirect_uri(self) -> str:
        return self.effective_redirect_uri

    @property
    def effective_redirect_uri(self) -> str:
        if self.bling_redirect_uri:
            return self.bling_redirect_uri
        base = self.effective_public_base_url
        if base:
            return f"{base.rstrip('/')}/oauth/callback"
        return f"http://localhost:{self.port}/oauth/callback"

    @property
    def effective_public_base_url(self) -> str | None:
        if self.public_base_url:
            return _normalize_public_base_url(self.public_base_url) or self.public_base_url
        return _derive_public_base_url_from_redirect_uri(self.bling_redirect_uri)

    @property
    def env(self) -> Literal["development", "production"]:
        return self.node_env

    @property
    def effective_ui_enabled(self) -> bool:
        if self.ui_enable is None:
            return self.node_env != "production"
        return self.ui_enable == "on"

    def is_configured(self) -> bool:
        return bool(self.bling_client_id and self.bling_client_secret)


# Singleton used across the app
_config: Settings | None = None


def get_config() -> Settings:
    global _config
    if _config is None:
        from dotenv import load_dotenv

        load_dotenv()
        _config = Settings()  # type: ignore[call-arg]
        # Resolve redirect_uri from PUBLIC_BASE_URL if not set
        if not _config.redirect_uri and _config.effective_public_base_url:
            # Rebuild so redirect_uri is derived
            pass  # effective_redirect_uri already derives from effective_public_base_url
    return _config


def apply_fastmcp_github_oauth_env_defaults(config: Settings) -> None:
    """Derive FastMCP GitHub OAuth env vars from PUBLIC_BASE_URL when missing."""
    provider = (os.getenv("FASTMCP_SERVER_AUTH") or "").strip()
    if provider != "fastmcp.server.auth.providers.github.GitHubProvider":
        return
    base_root = config.effective_public_base_url
    if not base_root:
        return

    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(base_root.rstrip("/"))
    if not parsed.scheme or not parsed.netloc:
        return

    path = (parsed.path or "").rstrip("/")
    if path.endswith("/mcp"):
        path = path[: -len("/mcp")] or ""

    base_url = urlunparse(parsed._replace(path=path))
    os.environ.setdefault("FASTMCP_SERVER_AUTH_GITHUB_BASE_URL", base_url)
    os.environ.setdefault("FASTMCP_SERVER_AUTH_GITHUB_ISSUER_URL", base_url)


def set_config(config: Settings | None) -> None:
    global _config
    _config = config
