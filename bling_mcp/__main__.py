"""Entry point: run MCP server (stdio and/or HTTP) and callback server."""

from __future__ import annotations

import sys
import threading

from dotenv import load_dotenv

load_dotenv()

from bling_mcp.config import apply_fastmcp_github_oauth_env_defaults, get_config, set_config
from bling_mcp.mcp.app import create_mcp
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)


def _start_callback_server() -> None:
    """Start OAuth callback server in a background thread."""
    try:
        from bling_mcp.ui.server import run_callback_server
        run_callback_server()
    except Exception as e:
        logger.error("Callback server failed: %s", e)


def main() -> None:
    set_config(get_config())
    config = get_config()
    apply_fastmcp_github_oauth_env_defaults(config)

    create_mcp()
    mcp = __import__("bling_mcp.mcp.app", fromlist=["get_mcp"]).get_mcp()
    if mcp is None:
        logger.error("MCP app not created")
        sys.exit(1)

    transport = config.mcp_transport

    if transport == "http":
        # HTTP only: run callback server with MCP mounted at /mcp
        from bling_mcp.ui.server import run_callback_server
        logger.info("Starting callback server with MCP at http://0.0.0.0:%s/mcp", config.port)
        run_callback_server(include_mcp=True)
        return

    # Start callback server in background (OAuth + wizard)
    def _run_callback(include_mcp: bool = False) -> None:
        from bling_mcp.ui.server import run_callback_server
        run_callback_server(include_mcp=include_mcp)

    callback_thread = threading.Thread(target=_run_callback, daemon=True)
    callback_thread.start()
    logger.info("Auth server starting on port %s", config.port)

    mcp.run()


if __name__ == "__main__":
    main()
