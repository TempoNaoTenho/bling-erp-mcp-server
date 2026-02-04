"""In-memory store for raw JSON resources (bling://resource/...)."""

from __future__ import annotations

import json
import uuid
from typing import Any


class StoredResource:
    def __init__(
        self,
        uri: str,
        name: str,
        mime_type: str,
        size: int,
        text: str,
        description: str | None = None,
    ) -> None:
        self.uri = uri
        self.name = name
        self.mime_type = mime_type
        self.size = size
        self.text = text
        self.description = description


class ResourceStore:
    def __init__(self) -> None:
        self._resources: dict[str, StoredResource] = {}

    def create_text_resource(
        self,
        name: str,
        text: str,
        mime_type: str = "text/plain",
        description: str | None = None,
    ) -> dict[str, Any]:
        uri = f"bling://resource/{uuid.uuid4()}"
        size = len(text.encode("utf-8"))
        entry = StoredResource(
            uri=uri,
            name=name,
            mime_type=mime_type,
            size=size,
            text=text,
            description=description,
        )
        self._resources[uri] = entry
        return {
            "type": "resource_link",
            "uri": uri,
            "name": name,
            "mimeType": mime_type,
            "description": description,
            "_meta": {"size": size},
        }

    def list_resources(self) -> list[dict[str, Any]]:
        return [
            {
                "uri": r.uri,
                "name": r.name,
                "mimeType": r.mime_type,
                "size": r.size,
                "description": r.description,
            }
            for r in self._resources.values()
        ]

    def read_resource(self, uri: str) -> dict[str, Any] | None:
        r = self._resources.get(uri)
        if not r:
            return None
        return {
            "uri": r.uri,
            "mimeType": r.mime_type,
            "text": r.text,
        }


_resource_store: ResourceStore | None = None


def get_resource_store() -> ResourceStore:
    global _resource_store
    if _resource_store is None:
        _resource_store = ResourceStore()
    return _resource_store


def make_json_resource_link(
    name: str,
    raw: Any,
    description: str | None = None,
) -> dict[str, Any]:
    text = json.dumps(raw, ensure_ascii=False)
    return get_resource_store().create_text_resource(
        name, text, "application/json", description
    )
