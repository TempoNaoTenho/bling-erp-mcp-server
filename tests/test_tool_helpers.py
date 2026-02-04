"""Tests for tool helper functions."""
from __future__ import annotations
import pytest
from bling_mcp.mcp.tool_helpers import (
    remove_empty,
    clamp_arrays,
    build_error_result,
    apply_max_chars_truncation,
    unwrap_data_array,
    unwrap_data_object,
    infer_next_page,
    build_envelope_meta,
)


def test_remove_empty_none():
    """Test remove_empty with None values."""
    assert remove_empty(None) is None
    assert remove_empty({"a": None, "b": 1}) == {"b": 1}
    assert remove_empty({"a": None, "b": None}) is None


def test_remove_empty_strings():
    """Test remove_empty with empty strings."""
    assert remove_empty("") is None
    assert remove_empty("  ") is None
    assert remove_empty("hello") == "hello"


def test_remove_empty_lists():
    """Test remove_empty with lists."""
    assert remove_empty([]) is None
    assert remove_empty([None, "", 1]) == [1]
    assert remove_empty([None, None]) is None


def test_clamp_arrays_simple():
    """Test clamp_arrays with simple list."""
    result, truncated = clamp_arrays([1, 2, 3, 4, 5], 3)
    assert result == [1, 2, 3]
    assert truncated is True


def test_clamp_arrays_no_truncation():
    """Test clamp_arrays without truncation."""
    result, truncated = clamp_arrays([1, 2], 3)
    assert result == [1, 2]
    assert truncated is False


def test_clamp_arrays_nested():
    """Test clamp_arrays with nested structures."""
    data = {"items": [1, 2, 3, 4, 5]}
    result, truncated = clamp_arrays(data, 3)
    assert result == {"items": [1, 2, 3]}
    assert truncated is True


def test_build_error_result():
    """Test build_error_result returns dict."""
    result = build_error_result("Test error")
    assert isinstance(result, dict)
    assert "meta" in result
    assert "data" in result
    assert result["meta"]["error"] is True
    assert result["data"]["error"] == "Test error"


def test_apply_max_chars_truncation_no_truncation():
    """Test apply_max_chars_truncation when under limit."""
    envelope = {"meta": {"responseFormat": "concise"}, "data": {"test": "data"}}
    result = apply_max_chars_truncation(envelope, 10000)
    assert result == envelope
    assert "truncated" not in result["meta"] or result["meta"].get("truncated") is False


def test_apply_max_chars_truncation_with_truncation():
    """Test apply_max_chars_truncation when over limit."""
    envelope = {"meta": {"responseFormat": "concise"}, "data": {"test": "x" * 10000}}
    result = apply_max_chars_truncation(envelope, 100)
    assert result["meta"]["truncated"] is True
    assert "truncatedReason" in result["meta"]


def test_unwrap_data_array():
    """Test unwrap_data_array with various inputs."""
    assert unwrap_data_array([1, 2, 3]) == [1, 2, 3]
    assert unwrap_data_array({"data": [1, 2, 3]}) == [1, 2, 3]
    assert unwrap_data_array({"data": {"data": [1, 2, 3]}}) == [1, 2, 3]
    assert unwrap_data_array({}) == []


def test_unwrap_data_object():
    """Test unwrap_data_object with various inputs."""
    assert unwrap_data_object({"data": {"id": 1}}) == {"id": 1}
    assert unwrap_data_object({"id": 1}) == {"id": 1}
    assert unwrap_data_object(None) is None


def test_infer_next_page_with_total_pages():
    """Test infer_next_page with totalPaginas."""
    raw = {"pagina": 2, "totalPaginas": 5}
    assert infer_next_page(raw, {}) == 3


def test_infer_next_page_last_page():
    """Test infer_next_page on last page."""
    raw = {"pagina": 5, "totalPaginas": 5}
    assert infer_next_page(raw, {}) is None


def test_infer_next_page_with_total_records():
    """Test infer_next_page with total records."""
    raw = {"pagina": 1, "limite": 50, "total": 150}
    assert infer_next_page(raw, {}) == 2


def test_build_envelope_meta():
    """Test build_envelope_meta creates proper structure."""
    meta = build_envelope_meta(
        response_format="detailed",
        include=["field1"],
        truncated=True,
        hint="Test hint",
        next_page=2,
    )
    assert meta["responseFormat"] == "detailed"
    assert meta["include"] == ["field1"]
    assert meta["truncated"] is True
    assert meta["hint"] == "Test hint"
    assert meta["nextPage"] == 2


def test_build_envelope_meta_defaults():
    """Test build_envelope_meta with defaults."""
    meta = build_envelope_meta()
    assert meta["responseFormat"] == "concise"
    assert meta["include"] == []
    assert meta["truncated"] is False
    assert "hint" not in meta
    assert "nextPage" not in meta
