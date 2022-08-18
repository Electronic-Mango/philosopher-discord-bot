"""
Module responsible for retrieving inspirational quotes, which are used in "quote" command.
"""

from json import loads
from os import getenv

from requests import get

from load_all_dotenv import load_all_dotenv

load_all_dotenv()
QUOTE_API_URL = getenv("QUOTE_API_URL")
QUOTE_API_TEXT_KEY = getenv("QUOTE_API_TEXT_KEY")
QUOTE_API_AUTHOR_KEY = getenv("QUOTE_API_AUTHOR_KEY")


def get_quote() -> tuple[str, str]:
    """Returns "quote text" "quote author" tuple"""
    response = get(QUOTE_API_URL)
    response_json = loads(response.text)
    return response_json[QUOTE_API_TEXT_KEY], response_json[QUOTE_API_AUTHOR_KEY]
