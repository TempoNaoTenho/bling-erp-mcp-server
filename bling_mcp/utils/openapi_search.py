"""Search bling-openapi-reference.md for endpoints."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


DEFAULT_REFERENCE_PATH = Path.cwd() / "bling-openapi-reference.md"


def search_openapi_reference(
    query: str,
    methods: list[str] | None = None,
    limit: int = 10,
    include: list[str] | None = None,
    snippet_lines: int = 5,
    match_all: bool = True,
    file_path: str | None = None,
) -> dict[str, Any]:
    path = Path(file_path) if file_path else DEFAULT_REFERENCE_PATH
    if not path.is_absolute():
        path = Path.cwd() / path
    if not path.exists():
        return {"query": query, "totalMatches": 0, "returned": 0, "limit": limit, "filePath": str(path), "matches": []}
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    terms = [t.strip().lower() for t in query.split() if t.strip()]
    include_set = set(include or [])
    endpoints: list[dict[str, Any]] = []
    current_section = ""
    i = 0
    while i < len(lines) and len(endpoints) < limit:
        line = lines[i]
        if line.startswith("## ") and not line.startswith("###"):
            current_section = line.replace("##", "").strip()
            i += 1
            continue
        match = re.match(r"^###\s+([A-Z]+)\s+`([^`]+)`", line)
        if match:
            method, path_str = match.group(1), match.group(2)
            if methods and method not in methods:
                i += 1
                continue
            snippet_lines_list = lines[i : i + snippet_lines] if "snippet" in include_set else []
            snippet = "\n".join(snippet_lines_list) if snippet_lines_list else None
            block = "\n".join(lines[i : i + 30])
            if match_all:
                ok = all(term in block.lower() for term in terms)
            else:
                ok = any(term in block.lower() for term in terms)
            if ok:
                m: dict[str, Any] = {"method": method, "path": path_str, "section": current_section or None}
                if "description" in include_set:
                    m["description"] = block[:500]
                if "snippet" in include_set and snippet:
                    m["snippet"] = snippet
                endpoints.append(m)
            i += 1
            continue
        i += 1
    return {
        "query": query,
        "totalMatches": len(endpoints),
        "returned": len(endpoints),
        "limit": limit,
        "filePath": str(path),
        "matches": endpoints,
    }
