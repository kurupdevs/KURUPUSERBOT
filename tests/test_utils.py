"""Tests for core/utils.py — uptime formatting."""

import time


class TestUptime:
    """Tests for the up() function."""

    def test_uptime_returns_string_with_hms(self):
        """Uptime should return a string with h, m, s."""
        from core.utils import up

        result = up()
        assert isinstance(result, str)
        assert "h" in result
        assert "m" in result
        assert "s" in result

    def test_uptime_format_is_correct(self):
        """Uptime should match the hHmMsS format."""
        from core.utils import up

        result = up()
        # Format: 0h0mXs where X is 0 or more seconds
        assert result.endswith("s")
        parts = result[:-1].split("h")
        assert len(parts) == 2
        min_part = parts[1].split("m")
        assert len(min_part) == 2
        # All parts should be integers
        int(parts[0])
        int(min_part[0])
        int(min_part[1])

    def test_uptime_different_from_zero(self):
        """Uptime should not be 0h0m0s after a tiny delay."""
        time.sleep(0.1)
        from core.utils import up

        result = up()
        # At least some seconds have passed
        assert result != "0h0m0s"
