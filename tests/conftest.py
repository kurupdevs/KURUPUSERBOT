"""Shared fixtures for KurupUserbot tests."""

import os
import sys

import pytest

# Allow importing from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_env(monkeypatch):
    """Set dummy environment variables for testing."""
    monkeypatch.setenv("API_ID", "12345")
    monkeypatch.setenv("API_HASH", "abc123hash")
    monkeypatch.setenv("BOT_TOKEN", "123456:bot_token")
    monkeypatch.setenv("STRING_SESSION", "test_session_string")
