"""Bling OAuth: authorize URL, exchange code, refresh token."""

from __future__ import annotations

import base64
import time
from urllib.parse import urlencode

import httpx

from bling_mcp.bling_auth.tokens import BlingToken
from bling_mcp.config import get_config
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)

BLING_AUTH_URL = "https://www.bling.com.br/Api/v3/oauth/authorize"
BLING_TOKEN_URL = "https://api.bling.com.br/Api/v3/oauth/token"


def get_authorize_url(state: str, scopes: list[str] | None = None) -> str:
    config = get_config()
    if not config.client_id:
        raise ValueError("Client ID is not configured")
    params: dict[str, str] = {
        "response_type": "code",
        "client_id": config.client_id,
        "state": state,
    }
    if scopes:
        params["scope"] = " ".join(scopes)
    redirect_uri = config.effective_redirect_uri
    if redirect_uri:
        params["redirect_uri"] = redirect_uri
    return f"{BLING_AUTH_URL}?{urlencode(params)}"


def get_tokens(code: str) -> BlingToken:
    config = get_config()
    if not config.client_id or not config.client_secret:
        raise ValueError("Credentials not configured")
    credentials = base64.b64encode(
        f"{config.client_id}:{config.client_secret}".encode()
    ).decode()
    try:
        with httpx.Client() as client:
            resp = client.post(
                BLING_TOKEN_URL,
                data={"grant_type": "authorization_code", "code": code},
                headers={
                    "Authorization": f"Basic {credentials}",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "1.0",
                },
                timeout=15.0,
            )
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Error exchanging code for token: %s", e.response.text)
        raise
    expires_at = int(time.time() * 1000) + data["expires_in"] * 1000
    return BlingToken(
        access_token=data["access_token"],
        expires_in=data["expires_in"],
        token_type=data["token_type"],
        scope=data.get("scope"),
        refresh_token=data["refresh_token"],
        expires_at=expires_at,
    )


def refresh_token(refresh_token: str) -> BlingToken:
    config = get_config()
    if not config.client_id or not config.client_secret:
        raise ValueError("Credentials not configured")
    credentials = base64.b64encode(
        f"{config.client_id}:{config.client_secret}".encode()
    ).decode()
    try:
        with httpx.Client() as client:
            resp = client.post(
                BLING_TOKEN_URL,
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": refresh_token,
                },
                headers={
                    "Authorization": f"Basic {credentials}",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "1.0",
                },
                timeout=15.0,
            )
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Error refreshing token: %s", e.response.text)
        raise
    expires_at = int(time.time() * 1000) + data["expires_in"] * 1000
    next_refresh = data.get("refresh_token") or refresh_token
    return BlingToken(
        access_token=data["access_token"],
        expires_in=data["expires_in"],
        token_type=data["token_type"],
        scope=data.get("scope"),
        refresh_token=next_refresh,
        expires_at=expires_at,
    )
