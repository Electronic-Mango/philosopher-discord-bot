"""
Command Cog improving text send as this command argument.
"""

from disnake.ext.commands import Bot, Cog, Context, clean_content, command

from bot.prepare_text import prepare_text


class This(Cog, name="This message"):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="this", aliases=["uwuthis"])
    async def this(self, context: Context, *, text: clean_content(remove_markdown=True)) -> None:
        """Modify message given as an argument"""
        await context.reply(prepare_text(text))
