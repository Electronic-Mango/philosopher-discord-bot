"""
Command Cog sending (improved) inspirational quotes.
"""

from disnake.ext.commands import Bot, Cog, Context, command

from bot.prepare_text import prepare_text
from quote import get_quote


class Quote(Cog, name="Inspirational quotes"):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="quote", aliases=["uwuquote"])
    async def quote(self, context: Context) -> None:
        """Send random inspirational quote"""
        quote, author = get_quote()
        await context.reply(f"> {prepare_text(quote)}\n— {prepare_text(author)}")
