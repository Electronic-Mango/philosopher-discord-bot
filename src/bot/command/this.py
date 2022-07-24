from logging import getLogger

from discord.ext.commands import Cog, Context, clean_content, command

from bot.prepare_text import prepare_text


class This(Cog):
    def __init__(self, bot):
        self._bot = bot
        self._logger = getLogger(__name__)

    @command(name="this", aliases=["uwuthis"])
    async def this(
        self, context: Context, *, text: clean_content(remove_markdown=True) = None
    ) -> None:
        self._logger.info(f"[{context.channel.id}] [{context.command}] size [{len(text)}]")
        await context.reply(prepare_text(text))
