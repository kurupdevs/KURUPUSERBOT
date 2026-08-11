import os
import subprocess
import logging


def run_command(cmd, timeout=30):
    """Execute a shell command and return code, stdout, stderr."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        logging.warning(f"Command timed out: {cmd}")
        return -1, "", "Timeout"