"""Build query params for Bling API (including array params like idsProdutos[])."""

from __future__ import annotations

from typing import Any


def build_params(args: dict[str, Any], defaults: dict[str, Any] | None = None) -> list[tuple[str, str | int | float]]:
    """Convert args dict to list of (key, value) for httpx; list values become key[]=v."""
    out: list[tuple[str, str | int | float]] = []
    merged = {**(defaults or {}), **args}
    for k, v in merged.items():
        if v is None:
            continue
        if isinstance(v, list):
            for item in v:
                out.append((f"{k}[]", item))
        else:
            out.append((k, v))
    return out
