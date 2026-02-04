"""Bling API HTTP client with Bearer token and 401 refresh."""

from __future__ import annotations

import threading
from typing import Any

import httpx

from bling_mcp.bling_auth.tokens import BlingToken, load_token, save_token, clear_token
from bling_mcp.bling_auth.oauth import refresh_token as oauth_refresh_token
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://api.bling.com.br/Api/v3"

_refresh_lock = threading.Lock()


class BlingClient:
    """Sync HTTP client for Bling API with token refresh on 401."""

    def __init__(self) -> None:
        self._client = httpx.Client(
            base_url=BASE_URL,
            timeout=10.0,
            headers={"Accept": "application/json"},
        )

    def _get_auth_header(self) -> dict[str, str]:
        tokens = load_token()
        if tokens and tokens.access_token:
            return {"Authorization": f"Bearer {tokens.access_token}"}
        return {}

    def _refresh_tokens(self, tokens: BlingToken) -> BlingToken:
        with _refresh_lock:
            fresh = oauth_refresh_token(tokens.refresh_token)
            save_token(fresh)
            logger.info("Token refreshed successfully.")
            return fresh

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | list[tuple[str, Any]] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> Any:
        headers = self._get_auth_header()
        first = True
        while True:
            try:
                resp = self._client.request(
                    method,
                    url,
                    params=params,
                    json=json,
                    data=data,
                    headers=headers,
                )
                if resp.status_code == 401 and first:
                    first = False
                    tokens = load_token()
                    if not tokens or not tokens.refresh_token:
                        clear_token()
                        raise RuntimeError("No refresh token available")
                    try:
                        new_tokens = self._refresh_tokens(tokens)
                        headers = {"Authorization": f"Bearer {new_tokens.access_token}"}
                        continue
                    except Exception as e:
                        logger.error("Failed to refresh token: %s", e)
                        if hasattr(e, "response") and getattr(e, "response"):
                            r = getattr(e, "response")
                            if getattr(r, "status_code", None) in (400, 401):
                                clear_token()
                                logger.warning("Refresh token rejected. Tokens cleared.")
                        raise
                resp.raise_for_status()
                if resp.content:
                    return resp.json()
                return None
            except httpx.HTTPStatusError as e:
                msg = "Unknown error"
                try:
                    body = e.response.json()
                    if isinstance(body, dict):
                        err = body.get("error") or body
                        msg = err.get("description", err.get("message", str(body)))
                except Exception:
                    msg = e.response.text or str(e)
                logger.error("Bling API Error [%s]: %s", e.response.status_code, msg)
                raise RuntimeError(f"Bling API Error: {msg} (Status: {e.response.status_code})") from e

    def get(self, path: str, params: dict[str, Any] | list[tuple[str, Any]] | None = None) -> Any:
        if isinstance(params, dict):
            # Expand list values to key[]=v for Bling API
            flat: list[tuple[str, Any]] = []
            for k, v in params.items():
                if v is None:
                    continue
                if isinstance(v, list):
                    for item in v:
                        flat.append((f"{k}[]", item))
                else:
                    flat.append((k, v))
            params = flat if flat else None
        return self.request("GET", path, params=params)

    def post(self, path: str, json: dict[str, Any] | None = None, data: dict[str, Any] | None = None) -> Any:
        return self.request("POST", path, json=json, data=data)

    def put(self, path: str, json: dict[str, Any] | None = None) -> Any:
        return self.request("PUT", path, json=json)

    def patch(self, path: str, json: dict[str, Any] | None = None) -> Any:
        return self.request("PATCH", path, json=json)

    def delete(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return self.request("DELETE", path, params=params)


# Singleton
_bling_client: BlingClient | None = None


def get_bling_client() -> BlingClient:
    global _bling_client
    if _bling_client is None:
        _bling_client = BlingClient()
    return _bling_client
