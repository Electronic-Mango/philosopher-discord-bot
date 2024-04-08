"""
Module loading default and custom .env.
Path to custom .evn is taken from "CUSTOM_DOTENV" environment variable.
"""

from os import getenv

from dotenv import load_dotenv


def load_all_dotenv() -> None:
    """Load default and custom .env"""
    load_dotenv("default.env", override=True)
    load_dotenv(getenv("CUSTOM_DOTENV"), override=True)
    load_dotenv(override=True)
