from logging import getLogger

from discord.ext.commands import Bot, Cog, Context, command

from bot.prepare_text import prepare_text


class That(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot
        self._logger = getLogger(__name__)

    @command(name="that", aliases=["uwuthat"])
    async def that(self, context: Context) -> None:
        if context.message.reference and context.message.reference.resolved:
            await self._modify_specific_message(context)

    async def _modify_specific_message(self, context: Context) -> None:
        message = context.message.reference.resolved
        self._logger.info(f"[{context.channel.id}] [{context.command}] message [{message.id}]")
        await message.reply(prepare_text(message.content))
