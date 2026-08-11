"""Tests for core/client.py."""

from unittest.mock import patch


class TestClientFactory:
    """Tests for the client factory function."""

    def test_make_returns_client_without_token(self):
        """make() should work without bot_token."""
        from core.client import make
        with patch("core.client.Client") as mock_client:
            make(12345, "hash")
            mock_client.assert_called_once_with(
                "KURUPUSERBOT",
                api_id=12345,
                api_hash="hash",
                bot_token=None,
            )

    def test_make_returns_client_with_token(self):
        """make() should pass bot_token when provided."""
        from core.client import make
        with patch("core.client.Client") as mock_client:
            make(12345, "hash", bot_token="mytoken")
            mock_client.assert_called_once_with(
                "KURUPUSERBOT",
                api_id=12345,
                api_hash="hash",
                bot_token="mytoken",
            )
