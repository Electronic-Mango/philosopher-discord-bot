"""
Module responsible for retrieving inspirational quotes, which are used in "quote" command.
"""

from os import getenv

from aiohttp import ClientSession

from load_all_dotenv import load_all_dotenv

load_all_dotenv()
QUOTE_API_URL = getenv("QUOTE_API_URL")
QUOTE_API_TEXT_KEY = getenv("QUOTE_API_TEXT_KEY")
QUOTE_API_AUTHOR_KEY = getenv("QUOTE_API_AUTHOR_KEY")


async def get_quote() -> tuple[str, str]:
    """Returns "quote text" "quote author" tuple"""
    if not QUOTE_API_URL or not QUOTE_API_TEXT_KEY or not QUOTE_API_AUTHOR_KEY:
        return None, None
    async with ClientSession() as session:
        async with session.get(QUOTE_API_URL) as response:
            response_json = await response.json()
            return response_json.get(QUOTE_API_TEXT_KEY), response_json.get(QUOTE_API_AUTHOR_KEY)
