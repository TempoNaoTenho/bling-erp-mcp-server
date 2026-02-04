"""Tool envelope builder, truncation, and common params (port of toolFactory.ts)."""

from __future__ import annotations

import json
from typing import Any

from bling_mcp.mcp.resource_store import make_json_resource_link

READ_ONLY_ANNOTATIONS = {
    "readOnlyHint": True,
    "idempotentHint": True,
    "openWorldHint": True,
}

READ_ONLY_INTERNAL_ANNOTATIONS = {
    "readOnlyHint": True,
    "idempotentHint": True,
    "openWorldHint": False,
}


# Common param defaults
DEFAULT_RESPONSE_FORMAT = "concise"
DEFAULT_MAX_ITEMS = 50
DEFAULT_MAX_CHARS = 30000
DEFAULT_RAW_AS_RESOURCE = True
DEFAULT_PREVIEW_ITEMS = 5


def remove_empty(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, str):
        return value if value.strip() else None
    if isinstance(value, list):
        cleaned = [remove_empty(item) for item in value if remove_empty(item) is not None]
        return cleaned if cleaned else None
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            v2 = remove_empty(v)
            if v2 is not None:
                out[k] = v2
        return out if out else None
    return value


def clamp_arrays(value: Any, max_items: int) -> tuple[Any, bool]:
    if isinstance(value, list):
        sliced = [clamp_arrays(item, max_items) for item in value[:max_items]]
        truncated = len(value) > max_items or any(s[1] for s in sliced)
        return [s[0] for s in sliced], truncated
    if isinstance(value, dict):
        out = {}
        truncated = False
        for k, v in value.items():
            v2, tr = clamp_arrays(v, max_items)
            out[k] = v2
            truncated = truncated or tr
        return out, truncated
    return value, False


def apply_truncation(meta: dict[str, Any], reason: str, hint: str | None = None) -> None:
    meta["truncated"] = True
    if "truncatedReason" not in meta or not meta["truncatedReason"]:
        meta["truncatedReason"] = reason
    elif meta["truncatedReason"] != reason:
        meta["truncatedReason"] = "multiple"
    if hint:
        meta["hint"] = f"{meta.get('hint', '')} {hint}".strip()


def to_compact_text(envelope: dict[str, Any], max_chars: int) -> tuple[str, bool]:
    """Convert envelope to JSON text with truncation (legacy function for backward compatibility)."""
    text = json.dumps(envelope, ensure_ascii=False)
    if len(text) <= max_chars:
        return text, False
    apply_truncation(
        envelope["meta"],
        "max_chars",
        "Use responseFormat='raw' com rawAsResource=true ou aumente maxChars.",
    )
    text = json.dumps(envelope, ensure_ascii=False)
    if len(text) <= max_chars:
        return text, True
    return text[:max_chars] + "...", True


def apply_max_chars_truncation(envelope: dict[str, Any], max_chars: int) -> dict[str, Any]:
    """Apply character limit truncation to envelope dict (FastMCP 3.x).

    Returns a new dict with truncation applied if needed.
    FastMCP will handle JSON serialization.
    """
    # Serialize to check size
    text = json.dumps(envelope, ensure_ascii=False)
    if len(text) <= max_chars:
        return envelope

    # Need to truncate - mark in meta
    result = {
        "meta": envelope["meta"].copy(),
        "data": envelope["data"],
    }
    apply_truncation(
        result["meta"],
        "max_chars",
        "Use responseFormat='raw' com rawAsResource=true ou aumente maxChars.",
    )

    # Check if meta update is enough
    text = json.dumps(result, ensure_ascii=False)
    if len(text) <= max_chars:
        return result

    # Need to truncate data - convert to string and cut
    result["data"] = {"_truncated": text[:max_chars] + "..."}
    return result


def unwrap_data_array(raw: Any) -> list[Any]:
    if isinstance(raw, list):
        return raw
    data = raw.get("data") if isinstance(raw, dict) else None
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
        return data["data"]
    return []


def unwrap_data_object(raw: Any) -> dict[str, Any] | None:
    if not raw or not isinstance(raw, dict):
        return None
    data = raw.get("data")
    if isinstance(data, dict) and not isinstance(data, list):
        return data
    return raw


def infer_next_page(raw: Any, args: dict[str, Any]) -> int | None:
    page = raw.get("pagina") if isinstance(raw, dict) else args.get("pagina")
    total_pages = (
        raw.get("totalPaginas") or raw.get("total_pages") or raw.get("totalPages")
        if isinstance(raw, dict) else None
    )
    if isinstance(page, (int, float)) and isinstance(total_pages, (int, float)):
        if int(page) < int(total_pages):
            return int(page) + 1
    total = (
        raw.get("total") or raw.get("totalRegistros") or raw.get("total_registros")
        if isinstance(raw, dict) else None
    )
    limit = raw.get("limite") if isinstance(raw, dict) else args.get("limite")
    if isinstance(page, (int, float)) and isinstance(limit, (int, float)) and isinstance(total, (int, float)):
        if int(page) * int(limit) < int(total):
            return int(page) + 1
    return None


def build_envelope_meta(
    response_format: str = "concise",
    include: list[str] | None = None,
    truncated: bool = False,
    hint: str | None = None,
    next_page: int | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "responseFormat": response_format,
        "include": include or [],
        "truncated": truncated,
        **kwargs,
    }
    if hint:
        meta["hint"] = hint
    if next_page is not None:
        meta["nextPage"] = next_page
    return meta


def build_tool_envelope(
    *,
    name: str,
    raw: Any,
    data: Any,
    response_format: str = DEFAULT_RESPONSE_FORMAT,
    include: list[str] | None = None,
    max_items: int = DEFAULT_MAX_ITEMS,
    max_chars: int = DEFAULT_MAX_CHARS,
    raw_as_resource: bool = DEFAULT_RAW_AS_RESOURCE,
    hint: str | None = None,
    next_page: int | None = None,
) -> dict[str, Any]:
    """Build a tool envelope dict with responseFormat/maxItems/maxChars handling."""
    response_format = response_format or DEFAULT_RESPONSE_FORMAT
    if response_format not in ("concise", "raw", "detailed"):
        response_format = DEFAULT_RESPONSE_FORMAT

    meta = build_envelope_meta(
        response_format=response_format,
        include=include,
        hint=hint,
        next_page=next_page,
    )

    if response_format == "raw":
        if raw_as_resource:
            link = make_json_resource_link(f"{name}-raw" if name else "raw", raw)
            hint_text = meta.get("hint", "")
            suffix = "Use resources/read com o uri informado para obter o payload completo."
            meta["hint"] = f"{hint_text} {suffix}".strip()
            envelope = {"meta": meta, "data": {"resourceUri": link["uri"]}}
            return apply_max_chars_truncation(envelope, max_chars)
        envelope = {"meta": meta, "data": raw}
        return apply_max_chars_truncation(envelope, max_chars)

    clamped, truncated = clamp_arrays(data, max_items)
    if truncated:
        apply_truncation(
            meta,
            "array_limit",
            "Use maxItems para ajustar o limite de arrays ou use responseFormat='raw'.",
        )
    envelope = {"meta": meta, "data": clamped}
    return apply_max_chars_truncation(envelope, max_chars)


def normalize_project_result(result: Any) -> tuple[Any, dict[str, Any] | None]:
    if isinstance(result, dict) and "data" in result:
        return result["data"], result.get("meta")
    return result, None


def build_error_result(message: str) -> dict[str, Any]:
    """Build error envelope as dict (FastMCP 3.x compatible)."""
    envelope = {
        "meta": {
            "responseFormat": "concise",
            "include": [],
            "truncated": False,
            "error": True,
            "hint": "Revise os parametros enviados e tente novamente.",
        },
        "data": {"error": message},
    }
    return envelope


def format_tool_result(
    raw: Any,
    args: dict[str, Any],
    project_fn: Any,
    *,
    name: str | None = None,
    default_hint: str | None = None,
    make_resource_link: Any = None,
) -> str:
    """Build envelope and return JSON string for MCP content (concise/detailed)."""
    response_format = args.get("responseFormat", DEFAULT_RESPONSE_FORMAT)
    include = args.get("include") or []
    max_items = args.get("maxItems", DEFAULT_MAX_ITEMS)
    max_chars = args.get("maxChars", DEFAULT_MAX_CHARS)
    raw_as_resource = args.get("rawAsResource", DEFAULT_RAW_AS_RESOURCE)

    meta = build_envelope_meta(
        response_format=response_format,
        include=include,
        hint=default_hint,
    )

    if response_format == "raw":
        if raw_as_resource and (make_resource_link or make_json_resource_link):
            link_fn = make_resource_link or make_json_resource_link
            resource_name = f"{name}-raw" if name else "raw"
            link = link_fn(resource_name, raw)
            hint = meta.get("hint", "") + " Use resources/read com o uri informado para obter o payload completo."
            meta["hint"] = hint.strip()
            envelope = {"meta": meta, "data": {"resourceUri": link["uri"]}}
            text, _ = to_compact_text(envelope, max_chars)
            return text
        envelope = {"meta": meta, "data": raw}
        text, _ = to_compact_text(envelope, max_chars)
        return text

    data, extra_meta = normalize_project_result(project_fn(raw, args))
    if extra_meta:
        meta.update(extra_meta)
    cleaned = remove_empty(data)
    if cleaned is None:
        cleaned = None  # keep as null in JSON
    clamped, truncated = clamp_arrays(cleaned, max_items)
    if truncated:
        apply_truncation(
            meta,
            "array_limit",
            "Use maxItems para ajustar o limite de arrays ou use responseFormat='raw'.",
        )
    envelope = {"meta": meta, "data": clamped}
    text, _ = to_compact_text(envelope, max_chars)
    return text
