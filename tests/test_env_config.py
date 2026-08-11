"""Tests for config/env_config.py."""

import importlib


class TestEnvConfig:
    """Tests for environment-based configuration."""

    def test_api_id_default_zero(self, monkeypatch):
        """With no env var, API_ID should default to 0."""
        monkeypatch.delenv("API_ID", raising=False)
        import config.env_config as ec
        importlib.reload(ec)
        assert ec.API_ID == 0

    def test_api_hash_default_empty(self, monkeypatch):
        """With no env var, API_HASH should default to empty string."""
        monkeypatch.delenv("API_HASH", raising=False)
        import config.env_config as ec
        importlib.reload(ec)
        assert ec.API_HASH == ""

    def test_bot_token_default_empty(self, monkeypatch):
        """With no env var, BOT_TOKEN should default to empty string."""
        monkeypatch.delenv("BOT_TOKEN", raising=False)
        import config.env_config as ec
        importlib.reload(ec)
        assert ec.BOT_TOKEN == ""

    def test_api_id_from_env(self, monkeypatch):
        """API_ID should be read from environment."""
        monkeypatch.setenv("API_ID", "99999")
        import config.env_config as ec
        importlib.reload(ec)
        assert ec.API_ID == 99999

    def test_api_hash_from_env(self, monkeypatch):
        """API_HASH should be read from environment."""
        monkeypatch.setenv("API_HASH", "testhash123")
        import config.env_config as ec
        importlib.reload(ec)
        assert ec.API_HASH == "testhash123"
