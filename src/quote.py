from json import loads
from os import getenv

from dotenv import load_dotenv
from requests import get

load_dotenv()
QUOTE_API_URL = getenv("QUOTE_API_URL")
QUOTE_API_TEXT_KEY = getenv("QUOTE_API_TEXT_KEY")
QUOTE_API_AUTHOR_KEY = getenv("QUOTE_API_AUTHOR_KEY")


def get_quote() -> tuple[str, str]:
    response = get(QUOTE_API_URL)
    response_json = loads(response.text)
    return response_json[QUOTE_API_TEXT_KEY], response_json[QUOTE_API_AUTHOR_KEY]
