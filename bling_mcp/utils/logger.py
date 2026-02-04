"""Logging to stderr (stdout reserved for MCP protocol)."""

import logging
import sys

_logger: logging.Logger | None = None


def get_logger(name: str = "bling_mcp") -> logging.Logger:
    global _logger
    if _logger is None:
        _logger = logging.getLogger(name)
        _logger.setLevel(logging.DEBUG)
        if not _logger.handlers:
            h = logging.StreamHandler(sys.stderr)
            h.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
            _logger.addHandler(h)
    return _logger
