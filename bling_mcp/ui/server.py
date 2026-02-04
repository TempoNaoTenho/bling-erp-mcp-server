"""OAuth callback server and wizard UI (Starlette)."""

from __future__ import annotations

import os
import secrets
import time
from typing import Any
from urllib.parse import urlencode
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, PlainTextResponse, RedirectResponse, Response
from starlette.middleware import Middleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from bling_mcp.bling_auth.tokens import clear_token, load_token, save_token
from bling_mcp.ui.wizard import (
    get_main_content,
    get_nav_status,
    push_log,
    render_logs_panel,
)
from bling_mcp.bling_auth.oauth import get_authorize_url, get_tokens, refresh_token
from bling_mcp.config import get_config
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)

_UI_DIR = Path(__file__).resolve().parent
_TEMPLATES_DIR = _UI_DIR / "templates"
_STATIC_DIR = _UI_DIR / "static"

# In-memory state for OAuth (single server instance)
_oauth_states: dict[str, bool] = {}
_ui_oauth_states: dict[str, dict[str, str]] = {}
_ui_sessions: dict[str, dict[str, Any]] = {}
_ui_client_id: str | None = None


def _get_redirect_uri() -> str:
    config = get_config()
    return config.effective_redirect_uri


def _get_ui_base_path() -> str:
    return "/ui"


def _get_ui_public_base_url() -> str:
    config = get_config()
    return config.effective_public_base_url or f"http://localhost:{config.port}"


def _get_ui_redirect_uri() -> str:
    return f"{_get_ui_public_base_url().rstrip('/')}{_get_ui_base_path()}/auth/callback"


def _is_ui_enabled() -> bool:
    return get_config().effective_ui_enabled


def _is_ui_auth_github() -> bool:
    return get_config().ui_auth_mode == "github"


def _get_mcp_resource_url() -> str:
    return f"{_get_ui_public_base_url().rstrip('/')}/mcp"


def _get_oauth_issuer_base_url() -> str:
    return (
        os.getenv("FASTMCP_SERVER_AUTH_GITHUB_ISSUER_URL")
        or os.getenv("FASTMCP_SERVER_AUTH_GITHUB_BASE_URL")
        or _get_ui_public_base_url()
    ).rstrip("/")


def _generate_pkce_pair() -> tuple[str, str]:
    verifier = secrets.token_urlsafe(48)
    import hashlib
    import base64

    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=")
    return verifier, challenge.decode()


async def _ensure_ui_oauth_client() -> str | None:
    global _ui_client_id
    if _ui_client_id:
        return _ui_client_id

    from bling_mcp.mcp.app import get_auth_provider

    provider = get_auth_provider()
    if provider is None:
        return None

    try:
        from mcp.shared.auth import OAuthClientInformationFull
    except Exception:
        return None

    client_id = f"bling-ui-{secrets.token_hex(8)}"
    issued_at = int(time.time())
    redirect_uri = _get_ui_redirect_uri()
    scopes = provider.required_scopes if hasattr(provider, "required_scopes") else []
    client_info = OAuthClientInformationFull(
        client_id=client_id,
        client_id_issued_at=issued_at,
        client_secret=None,
        client_secret_expires_at=None,
        redirect_uris=[redirect_uri],
        token_endpoint_auth_method="none",
        grant_types=["authorization_code", "refresh_token"],
        response_types=["code"],
        client_name="Bling MCP UI",
        scope=" ".join(scopes) if scopes else None,
        client_uri=None,
        logo_uri=None,
        contacts=None,
        tos_uri=None,
        policy_uri=None,
        jwks_uri=None,
        jwks=None,
        software_id=None,
        software_version=None,
    )

    try:
        await provider.register_client(client_info)
    except Exception:
        return None

    _ui_client_id = client_id
    return _ui_client_id


async def oauth_callback(request: Request) -> Response:
    """Handle GET/POST from Bling OAuth redirect with code and state."""
    if request.method == "GET":
        query = request.query_params
    else:
        form = await request.form()
        query = form

    code = query.get("code")
    state = query.get("state")
    error = query.get("error")

    if error:
        logger.warning("OAuth callback error: %s", error)
        return RedirectResponse(url=f"{_get_ui_base_path()}?error={error}", status_code=302)

    if not code or not state:
        return PlainTextResponse("Missing code or state", status_code=400)

    if state not in _oauth_states:
        logger.warning("Invalid OAuth state")
        return PlainTextResponse("Invalid state", status_code=400)
    del _oauth_states[state]

    try:
        token = get_tokens(code)
        save_token(token)
        logger.info("Tokens saved successfully")
        return RedirectResponse(url=f"{_get_ui_base_path()}?success=1", status_code=302)
    except Exception as e:
        logger.error("Token exchange failed: %s", e)
        return RedirectResponse(url=f"{_get_ui_base_path()}?error=exchange_failed", status_code=302)


async def oauth_start(request: Request) -> Response:
    """Redirect to Bling authorize URL (e.g. /start)."""
    config = get_config()
    if not config.is_configured():
        return PlainTextResponse("Configure BLING_CLIENT_ID and BLING_CLIENT_SECRET first.", status_code=400)
    state = secrets.token_urlsafe(32)
    _oauth_states[state] = True
    url = get_authorize_url(state, [])
    return RedirectResponse(url=url, status_code=302)


def _get_theme(request: Request) -> str:
    cookie = request.cookies.get("bling_theme", "dark")
    return "dark" if cookie == "dark" else "light"


async def wizard_page(request: Request) -> Response:
    """Serve full wizard with tabs (Status, Public URL, Auth, MCP) and logs."""
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader(str(_TEMPLATES_DIR)))
    template = env.get_template("wizard.html")
    active_tab = request.query_params.get("tab", "status")
    if active_tab not in ("status", "public", "auth", "mcp"):
        active_tab = "status"

    # Handle success messages
    success_param = request.query_params.get("success")
    success_messages = {
        "1": "Autenticado com sucesso.",
        "token_refreshed": "Token renovado com sucesso!",
        "logged_out": "Logout efetuado com sucesso.",
        "configured": "Credenciais configuradas com sucesso.",
    }
    success = success_messages.get(success_param) if success_param else None

    # Handle error messages
    error_param = request.query_params.get("error")
    error_messages = {
        "exchange_failed": "Falha ao trocar codigo por token.",
        "no_token": "Nenhum token disponivel para teste.",
        "refresh_failed": "Falha ao renovar o token.",
        "missing_credentials": "Client ID e Secret sao obrigatorios.",
    }
    error = error_messages.get(error_param, error_param) if error_param else None

    nav_status = get_nav_status()
    main_content = get_main_content(active_tab)
    logs_panel = render_logs_panel()
    theme = _get_theme(request)
    html = template.render(
        theme=theme,
        nav_status=nav_status,
        active_tab=active_tab,
        main_content=main_content,
        logs_panel=logs_panel,
        success=success,
        error=error,
    )
    return HTMLResponse(html)


async def theme_toggle(request: Request) -> Response:
    """Toggle theme (dark/light) via cookie."""
    theme = _get_theme(request)
    new_theme = "light" if theme == "dark" else "dark"
    response = RedirectResponse(url="/")
    response.set_cookie("bling_theme", new_theme, max_age=86400 * 365)
    return response


async def export_env(request: Request) -> Response:
    """Export current config as .env-style text (no secrets)."""
    config = get_config()
    lines = [
        "# Bling (set in environment)",
        "# BLING_CLIENT_ID=...",
        "# BLING_CLIENT_SECRET=...",
        f"BLING_REDIRECT_URI={config.effective_redirect_uri}",
        f"PUBLIC_BASE_URL={config.effective_public_base_url or ''}",
        f"PORT={config.port}",
        f"MCP_TRANSPORT={config.mcp_transport}",
        f"TOKEN_STORE_PATH={config.token_store_path}",
    ]
    return PlainTextResponse("\n".join(lines))


async def health(request: Request) -> Response:
    return PlainTextResponse("ok")


async def test_token_refresh(request: Request) -> Response:
    """Test token refresh endpoint - validates current tokens by attempting refresh."""
    tokens = load_token()
    if not tokens or not tokens.refresh_token:
        push_log("error", "Teste de refresh falhou: Nenhum token disponivel")
        return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&error=no_token", status_code=302)

    try:
        new_token = refresh_token(tokens.refresh_token)
        save_token(new_token)
        push_log("info", "Teste de refresh bem-sucedido: Token renovado")
        logger.info("Token refresh test successful")
        return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&success=token_refreshed", status_code=302)
    except Exception as e:
        push_log("error", f"Teste de refresh falhou: {str(e)}")
        logger.error("Token refresh test failed: %s", e)
        return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&error=refresh_failed", status_code=302)


async def logout(request: Request) -> Response:
    """Clear tokens and redirect to auth tab."""
    clear_token()
    push_log("info", "Logout efetuado: Tokens removidos")
    logger.info("User logged out - tokens cleared")
    return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&success=logged_out", status_code=302)


async def configure_credentials(request: Request) -> Response:
    """Save Client ID and Secret to environment variables (runtime only)."""
    form = await request.form()
    client_id = form.get("clientId", "").strip()
    client_secret = form.get("clientSecret", "").strip()

    if not client_id or not client_secret:
        push_log("error", "Configuracao falhou: Client ID e Secret sao obrigatorios")
        return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&error=missing_credentials", status_code=302)

    # Set environment variables for current runtime (not persistent across restarts)
    os.environ["BLING_CLIENT_ID"] = client_id
    os.environ["BLING_CLIENT_SECRET"] = client_secret

    # Force reload config
    from bling_mcp.config import set_config
    set_config(None)

    push_log("info", "Credenciais configuradas com sucesso (runtime)")
    logger.info("Credentials configured successfully")
    return RedirectResponse(url=f"{_get_ui_base_path()}?tab=auth&success=configured", status_code=302)


async def ui_login(request: Request) -> Response:
    if not _is_ui_enabled():
        return PlainTextResponse("UI disabled", status_code=404)
    if not _is_ui_auth_github():
        return RedirectResponse(url=_get_ui_base_path(), status_code=302)

    client_id = await _ensure_ui_oauth_client()
    if not client_id:
        return PlainTextResponse("OAuth provider not configured", status_code=500)

    state = secrets.token_urlsafe(32)
    code_verifier, code_challenge = _generate_pkce_pair()
    _ui_oauth_states[state] = {
        "code_verifier": code_verifier,
        "redirect_uri": _get_ui_redirect_uri(),
    }

    from bling_mcp.mcp.app import get_auth_provider

    provider = get_auth_provider()
    scopes = provider.required_scopes if provider and hasattr(provider, "required_scopes") else ["user"]
    scope_str = " ".join(scopes) if scopes else "user"

    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": _get_ui_redirect_uri(),
        "state": state,
        "scope": scope_str,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "resource": _get_mcp_resource_url(),
    }
    return RedirectResponse(url=f"{_get_oauth_issuer_base_url()}/authorize?{urlencode(params)}", status_code=302)


async def ui_auth_callback(request: Request) -> Response:
    if not _is_ui_enabled():
        return PlainTextResponse("UI disabled", status_code=404)
    if not _is_ui_auth_github():
        return RedirectResponse(url=_get_ui_base_path(), status_code=302)

    code = request.query_params.get("code")
    state = request.query_params.get("state")
    if not code or not state or state not in _ui_oauth_states:
        return PlainTextResponse("Invalid OAuth state", status_code=400)

    state_payload = _ui_oauth_states.pop(state)
    client_id = _ui_client_id
    if not client_id:
        return PlainTextResponse("OAuth client not registered", status_code=500)

    token_payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": state_payload["redirect_uri"],
        "client_id": client_id,
        "code_verifier": state_payload["code_verifier"],
    }

    import httpx

    token_url = f"{_get_oauth_issuer_base_url()}/token"
    async with httpx.AsyncClient(timeout=20) as client:
        token_resp = await client.post(token_url, data=token_payload)
    if token_resp.status_code >= 400:
        return PlainTextResponse("Token exchange failed", status_code=400)

    token_data = token_resp.json()
    access_token = token_data.get("access_token")
    if not access_token:
        return PlainTextResponse("No access token", status_code=400)

    from bling_mcp.mcp.app import get_auth_provider

    provider = get_auth_provider()
    if provider is None:
        return PlainTextResponse("OAuth provider not configured", status_code=500)

    verified = await provider.verify_token(access_token)
    if verified is None:
        return PlainTextResponse("Invalid token", status_code=401)

    session_id = secrets.token_urlsafe(32)
    _ui_sessions[session_id] = {
        "token": access_token,
        "created_at": time.time(),
    }
    response = RedirectResponse(url=_get_ui_base_path(), status_code=302)
    response.set_cookie(
        "bling_ui_session",
        session_id,
        httponly=True,
        secure=_get_ui_public_base_url().startswith("https://"),
        samesite="lax",
    )
    return response


async def ui_logout(request: Request) -> Response:
    session_id = request.cookies.get("bling_ui_session")
    if session_id and session_id in _ui_sessions:
        _ui_sessions.pop(session_id, None)
    response = RedirectResponse(url=_get_ui_base_path(), status_code=302)
    response.delete_cookie("bling_ui_session")
    return response


async def root_page(request: Request) -> Response:
    if _is_ui_enabled():
        return RedirectResponse(url=_get_ui_base_path(), status_code=302)
    return PlainTextResponse("Not found", status_code=404)


class UiAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        if path.startswith("/assets"):
            if not _is_ui_enabled():
                response = PlainTextResponse("Not found", status_code=404)
                await response(scope, receive, send)
                return
            await self.app(scope, receive, send)
            return

        if path.startswith(_get_ui_base_path()):
            if not _is_ui_enabled():
                response = PlainTextResponse("Not found", status_code=404)
                await response(scope, receive, send)
                return
            if _is_ui_auth_github():
                if path in (
                    f"{_get_ui_base_path()}/login",
                    f"{_get_ui_base_path()}/auth/callback",
                    f"{_get_ui_base_path()}/logout",
                ):
                    await self.app(scope, receive, send)
                    return
                cookie_header = None
                for name, value in scope.get("headers", []):
                    if name == b"cookie":
                        cookie_header = value.decode()
                        break
                session_id = None
                if cookie_header:
                    for part in cookie_header.split(";"):
                        key, _, val = part.strip().partition("=")
                        if key == "bling_ui_session":
                            session_id = val
                            break
                if not session_id or session_id not in _ui_sessions:
                    response = RedirectResponse(url=f"{_get_ui_base_path()}/login", status_code=302)
                    await response(scope, receive, send)
                    return
            await self.app(scope, receive, send)
            return

        await self.app(scope, receive, send)


def _build_routes(include_mcp_mount: bool = False, mcp_app: Starlette | None = None):
    routes = [
        Route("/health", health),
        Route("/oauth/callback", oauth_callback, methods=["GET", "POST"]),
        Route("/start", oauth_start),
        Route("/theme/toggle", theme_toggle, methods=["POST"]),
        Route("/export/env", export_env),
        Route("/bling/token/test", test_token_refresh, methods=["POST"]),
        Route("/logout", logout, methods=["GET"]),
        Route("/configure", configure_credentials, methods=["POST"]),
        Mount("/assets", app=StaticFiles(directory=str(_STATIC_DIR)), name="assets"),
        Route("/", root_page),
        Route("/ui", wizard_page),
        Route("/ui/login", ui_login),
        Route("/ui/auth/callback", ui_auth_callback),
        Route("/ui/logout", ui_logout),
    ]
    if include_mcp_mount and mcp_app is not None:
        # Normalize trailing slash for MCP endpoint
        routes.append(Route("/mcp/", lambda request: RedirectResponse("/mcp")))
        # Mount at root so the MCP app serves /mcp directly
        routes.append(Mount("/", app=mcp_app))
    return routes


def create_callback_app(include_mcp: bool = False) -> Starlette:
    mcp_app = None
    lifespan = None
    if include_mcp:
        from bling_mcp.mcp.app import get_mcp
        mcp = get_mcp()
        if mcp is not None:
            mcp_app = mcp.http_app(path="/mcp")
            lifespan = mcp_app.lifespan
    return Starlette(
        routes=_build_routes(include_mcp_mount=include_mcp, mcp_app=mcp_app),
        lifespan=lifespan,
        middleware=[Middleware(UiAuthMiddleware)],
    )


def run_callback_server(include_mcp: bool = False) -> None:
    import uvicorn
    config = get_config()
    app = create_callback_app(include_mcp=include_mcp)
    uvicorn.run(app, host="0.0.0.0", port=config.port, log_level="info")
