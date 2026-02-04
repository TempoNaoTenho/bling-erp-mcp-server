"""Bling auth tools: bling_auth_start, bling_auth_status."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from bling_mcp.bling_auth.tokens import load_token
from bling_mcp.config import get_config
from bling_mcp.mcp.app import get_mcp
from bling_mcp.mcp.tool_helpers import (
    READ_ONLY_INTERNAL_ANNOTATIONS,
    build_tool_envelope,
)
from bling_mcp.mcp.tool_models import (
    BlingAuthStartData,
    BlingAuthStatusData,
    ResponseFormat,
    ToolEnvelope,
)
from pydantic import Field


def register_bling_auth_tools() -> None:
    mcp = get_mcp()
    if mcp is None:
        return
    settings = get_config()

    @mcp.tool(
        description="Inicia o fluxo de autenticacao do Bling e retorna a URL da UI local.",
        annotations=READ_ONLY_INTERNAL_ANNOTATIONS,
    )
    def bling_auth_start(
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        maxChars: Annotated[
            int,
            Field(ge=1000, description="Limite de caracteres no payload final."),
        ] = 30000,
        rawAsResource: Annotated[
            bool,
            Field(
                description="Se true e responseFormat=raw, retorna um resourceUri com o payload completo."
            ),
        ] = True,
    ) -> ToolEnvelope[BlingAuthStartData]:
        """Inicia o fluxo de autenticacao do Bling. Retorna a URL da UI local para autorizar o app."""
        local_ui_url = f"http://localhost:{settings.port}"
        public_url = settings.effective_public_base_url
        is_configured = settings.is_configured()

        if not is_configured:
            raw = {
                "status": "not_configured",
                "message": f"O servidor ainda nao esta configurado com Client ID/Secret do Bling. Abra {local_ui_url} para configurar e autenticar.",
                "localUiUrl": local_ui_url,
            }
        else:
            message = f'Abra {local_ui_url} e clique em "Autorizar com Bling" (ou va direto em {local_ui_url}/start).'
            if public_url and not public_url.startswith("http://localhost") and not public_url.startswith("http://127.0.0.1"):
                message += f" URL publica configurada: {public_url}."
            raw = {
                "status": "ready",
                "message": message,
                "localUiUrl": local_ui_url,
                "publicUrl": public_url,
            }

        return build_tool_envelope(
            name="bling_auth_start",
            raw=raw,
            data=raw,
            response_format=responseFormat,
            max_chars=maxChars,
            raw_as_resource=rawAsResource,
            hint="Use esta tool apenas para iniciar a configuracao/autorizacao.",
        )

    @mcp.tool(
        description="Mostra o status atual da autenticacao do Bling.",
        annotations=READ_ONLY_INTERNAL_ANNOTATIONS,
    )
    def bling_auth_status(
        responseFormat: Annotated[
            ResponseFormat,
            Field(description="Formato de resposta: concise (default) ou raw."),
        ] = "concise",
        maxChars: Annotated[
            int,
            Field(ge=1000, description="Limite de caracteres no payload final."),
        ] = 30000,
        rawAsResource: Annotated[
            bool,
            Field(
                description="Se true e responseFormat=raw, retorna um resourceUri com o payload completo."
            ),
        ] = True,
    ) -> ToolEnvelope[BlingAuthStatusData]:
        """Mostra se ha token salvo e se o servidor consegue renovar o access token automaticamente."""
        tokens = load_token()
        if not tokens:
            raw = {
                "authenticated": False,
                "message": "Not authenticated with Bling ERP. Use bling_auth_start to login.",
            }
        else:
            expires_formatted = (
                datetime.utcfromtimestamp(tokens.expires_at / 1000).isoformat() + "Z"
                if tokens.expires_at
                else None
            )
            raw = {
                "authenticated": True,
                "refreshTokenPresent": bool(tokens.refresh_token),
                "accessTokenExpiresAt": tokens.expires_at or None,
                "accessTokenExpiresAtFormatted": expires_formatted,
                "scopes": tokens.scope or "Default",
                "autoRefresh": True,
            }

        return build_tool_envelope(
            name="bling_auth_status",
            raw=raw,
            data=raw,
            response_format=responseFormat,
            max_chars=maxChars,
            raw_as_resource=rawAsResource,
            hint="O servidor renova o access token automaticamente quando necessario.",
        )
