"""
Command Cog sending (improved) inspirational quotes.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command

from bot.prepare_text import prepare_text
from quote import get_quote


class Quote(Cog):
    @slash_command(name="quote")
    async def quote(self, interaction: CommandInteraction) -> None:
        """Send a random inspirational quote"""
        await interaction.response.defer()
        quote, author = get_quote()
        quote_text = f"> {prepare_text(quote)}\n— {prepare_text(author)}"
        await interaction.send(quote_text)
