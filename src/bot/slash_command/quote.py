"""
Command Cog sending (improved) inspirational quotes.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command

from bot.prepare_text import prepare_text
from quote import get_quote

_COMMAND_NAME = "quote"
_COMMAND_DESCRIPTION = "Send back a random inspirational quote"
HELP_MESSAGE = f"""
`/{_COMMAND_NAME}` - {_COMMAND_DESCRIPTION}
"""


class Quote(Cog):
    @slash_command(name=_COMMAND_NAME, description=_COMMAND_DESCRIPTION)
    async def _quote(self, interaction: CommandInteraction) -> None:
        await interaction.response.defer()
        quote, author = await get_quote()
        quote_text = self._prepare_response_text(quote, author)
        await interaction.send(quote_text)
    
    def _prepare_response_text(self, quote: str, author: str) -> str:
        if not quote or not author:
            return prepare_text("Can't find any quotes")
        else:
            return f"> {prepare_text(quote)}\n— {prepare_text(author)}"
