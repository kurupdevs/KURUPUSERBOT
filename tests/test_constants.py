"""Tests for config/constants.py."""


class TestConstants:
    """Tests for application constants."""

    def test_app_name_is_string(self):
        """APP should be a non-empty string."""
        from config.constants import APP
        assert isinstance(APP, str)
        assert len(APP) > 0

    def test_version_is_string(self):
        """V should be a version string with dots."""
        from config.constants import V
        assert isinstance(V, str)
        assert "." in V

    def test_app_name_is_correct(self):
        """APP should be the expected value."""
        from config.constants import APP
        assert APP == "KURUPUSERBOT"
