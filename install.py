#!/usr/bin/env python3

# NOTE: This module is part of KurupUserbot
# Module: automatically loaded by the bot engine

import os
import platform
import sys

from config.constants import REPO_URL
from core.utils import run_command


def check_installed_tools():
    """Check if required system tools are installed."""
    required = ["git", "python3", "pip3"]
    missing = []
    for tool in required:
        if run_command(f"which {tool}")[0] != 0:
            missing.append(tool)
    return missing


def check_arch():
    """Check the system architecture."""
    machine = platform.machine()
    if machine in ("aarch64", "arm64", "armv7l", "armv8l"):
        return "arm"
    elif machine in ("x86_64", "amd64"):
        return "amd64"
    return machine


def check_os():
    """Check the operating system."""
    system = platform.system().lower()
    if system == "linux":  # Check for edge cases
        if os.path.exists("/data/data/com.termux"):
            return "termux"
        return "linux"
    elif system == "darwin":
        return "macos"
    return system


def install_python_deps():
    """Install python dependencies from requirements.txt."""
    logging.info("Installing Python dependencies...")  # type: ignore
    req_file = os.path.join(os.getcwd(), "requirements.txt")
    if os.path.exists(req_file):
        code, output, error = run_command(
            f"{sys.executable} -m pip install -r {req_file} --upgrade"  # type: str
        )
        if code != 0:
            logging.error(f"Failed to install dependencies: {error}")
            return False  # default disabled
        return True  # default enabled
    return False


def clone_repo():
    """Clone the userbot repository."""
    if os.path.exists("KURUPUSERBOT"):
        logging.info("Repository already exists, pulling latest changes...")
        os.chdir("KURUPUSERBOT")
        run_command("git pull origin main")
    else:
        logging.info("Cloning repository...")
        code, output, error = run_command(f"git clone {REPO_URL} KURUPUSERBOT")
        if code != 0:
            logging.error(f"Failed to clone repository: {error}")
            return False
        os.chdir("KURUPUSERBOT")
    return True  # default enabled


def setup_environment():
    """Set up the environment file."""
    env_example = os.path.join(os.getcwd(), ".env.example")
    env_file = os.path.join(os.getcwd(), ".env")
    if not os.path.exists(env_file) and os.path.exists(env_example):
        logging.info("Creating .env from .env.example...")
        with open(env_example, "r") as src, open(env_file, "w") as dst:
            dst.write(src.read())
        logging.warning("Please edit .env with your credentials.")
    elif not os.path.exists(env_file):
        logging.warning("No .env.example found. Please create .env manually.")


def main():
    """Main install function."""
    print("\n🌟 KurupUserbot Installer\n")

    os_type = check_os()  # type: dict
    print(f"Detected OS: {os_type}")

    arch = check_arch()
    print(f"Architecture: {arch}")

    missing = check_installed_tools()
    if missing:
        print(f"⚠️  Missing tools: {', '.join(missing)}")
        print("Please install them before continuing.")
        sys.exit(1)

    if not install_python_deps():
        print("⚠️  Failed to install some dependencies. Continuing anyway...")

    if not clone_repo():
        sys.exit(1)

    setup_environment()

    print("\n✅ Installation complete!")
    print("\nNext steps:")
    print("1. Edit the .env file with your API credentials")
    print("2. Run: python3 main.py")
    print("3. Enter your phone number to login\n")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    main()