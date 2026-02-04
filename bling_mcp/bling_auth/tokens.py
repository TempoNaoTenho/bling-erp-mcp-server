"""Bling OAuth token persistence (JSON file)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bling_mcp.config import get_config
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)


def _token_path() -> Path:
    return Path(get_config().token_store_path).expanduser().resolve()


class BlingToken:
    access_token: str
    expires_in: int
    token_type: str
    scope: str | None
    refresh_token: str
    expires_at: int  # ms timestamp

    def __init__(
        self,
        *,
        access_token: str,
        expires_in: int,
        token_type: str,
        refresh_token: str,
        scope: str | None = None,
        expires_at: int | None = None,
    ) -> None:
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.scope = scope
        self.refresh_token = refresh_token
        self.expires_at = expires_at if expires_at is not None else 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "access_token": self.access_token,
            "expires_in": self.expires_in,
            "token_type": self.token_type,
            "scope": self.scope,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BlingToken:
        return cls(
            access_token=data["access_token"],
            expires_in=data["expires_in"],
            token_type=data["token_type"],
            refresh_token=data["refresh_token"],
            scope=data.get("scope"),
            expires_at=data.get("expires_at"),
        )


def save_token(token: BlingToken) -> None:
    path = _token_path()
    try:
        path.write_text(json.dumps(token.to_dict(), indent=2), encoding="utf-8")
        logger.info("Tokens saved to %s", path)
    except Exception as e:
        logger.error("Failed to save tokens: %s", e)
        raise


def load_token() -> BlingToken | None:
    path = _token_path()
    try:
        if not path.exists():
            logger.debug("No token file found.")
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        return BlingToken.from_dict(data)
    except FileNotFoundError:
        logger.debug("No token file found.")
        return None
    except Exception as e:
        logger.error("Failed to load tokens: %s", e)
        return None


def clear_token() -> None:
    path = _token_path()
    try:
        if path.exists():
            path.unlink()
    except FileNotFoundError:
        pass
