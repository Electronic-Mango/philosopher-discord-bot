from discord.ext.commands import Bot, Cog, Context, clean_content, command

from bot.prepare_text import prepare_text


class This(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="this", aliases=["uwuthis"])
    async def this(self, context: Context, *, text: clean_content(remove_markdown=True)) -> None:
        await context.reply(prepare_text(text))
