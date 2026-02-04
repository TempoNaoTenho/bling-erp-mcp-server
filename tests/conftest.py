"""Pytest fixtures for Bling ERP MCP Server tests."""
from __future__ import annotations
import pytest
from unittest.mock import Mock
from bling_mcp.config import Settings
from bling_mcp.utils.bling_client import BlingClient


@pytest.fixture
def mock_settings():
    """Mock Settings instance with test configuration."""
    settings = Mock(spec=Settings)
    settings.bling_client_id = "test_client_id"
    settings.bling_client_secret = "test_client_secret"
    settings.port = 3333
    settings.public_base_url = "http://localhost:3333"
    settings.bling_redirect_uri = "http://localhost:3333/oauth/callback"
    settings.token_store_path = ".tokens.json"
    settings.mcp_transport = "stdio"
    settings.is_configured.return_value = True
    return settings


@pytest.fixture
def mock_bling_client():
    """Mock BlingClient instance."""
    client = Mock(spec=BlingClient)
    client.get.return_value = {"data": []}
    client.post.return_value = {"data": {}}
    client.put.return_value = {"data": {}}
    client.delete.return_value = {"data": {}}
    return client
