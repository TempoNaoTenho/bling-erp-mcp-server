"""MCP tools - register all tool modules with the FastMCP app."""

from bling_mcp.mcp.app import get_mcp as get_mcp

# Import tool modules so they register with the app
from bling_mcp.mcp.tools import bling_auth  # noqa: F401


def register_all_tools(mcp):  # noqa: ARG001
    """Called after app creation; tool modules register via get_mcp()."""
    pass
