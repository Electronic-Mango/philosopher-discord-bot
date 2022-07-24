from discord.ext.commands import Bot, Cog, Context, command

from bot.prepare_text import prepare_text
from quote import get_quote


class Quote(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="quote", aliases=["uwuquote"])
    async def this(self, context: Context) -> None:
        quote, author = get_quote()
        await context.reply(f"> {prepare_text(quote)}\n— {prepare_text(author)}")
