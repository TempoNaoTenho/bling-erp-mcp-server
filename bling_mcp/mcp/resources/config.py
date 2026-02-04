"""MCP Resources for Bling Doc."""
from __future__ import annotations
from typing import TYPE_CHECKING

from pathlib import Path
from fastmcp.resources import ResourceResult


if TYPE_CHECKING:
    from fastmcp import FastMCP


"""
Register an MCP resource for the Bling OpenAPI Reference.

This resource is registered at the URI "bling://openapi/reference".
When an LLM client requests this resource, the MCP server will return the Bling OpenAPI Reference in Markdown format.
"""

def register_resources(mcp: FastMCP) -> None:

    @mcp.resource("bling://openapi/reference")
    def get_bling_openapi_reference() -> ResourceResult:
        """Read the Bling OpenAPI Reference."""

        try:
            project_root = Path(__file__).resolve().parents[3]
            reference_path = project_root / "bling-openapi-reference.md"
            if not reference_path.exists():
                return ""

            return reference_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return ""
        except Exception as e:
            return f"Error reading Bling OpenAPI Reference: {e}"
