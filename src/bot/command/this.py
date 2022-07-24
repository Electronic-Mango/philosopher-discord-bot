from logging import getLogger

from discord.ext.commands import Cog, Context, clean_content, command
from discord.message import Message

from bot.prepare_text import prepare_text


class This(Cog):
    def __init__(self, bot):
        self._bot = bot
        self._logger = getLogger(__name__)

    @command(name="this")
    async def this(
        self, context: Context, *, text: clean_content(remove_markdown=True) = None
    ) -> None:
        if text:
            await self._modify_text(context, text)
        elif context.message.reference and context.message.reference.resolved:
            await self._modify_specific_message(context)
        else:
            await self._modify_last(context)

    async def _modify_text(self, context: Context, text: str) -> None:
        self._logger.info(f"[{context.channel.id}] [{context.command}] size [{len(text)}]")
        await context.reply(prepare_text(text))

    async def _modify_specific_message(self, context: Context) -> None:
        message = context.message.reference.resolved
        self._logger.info(f"[{context.channel.id}] [{context.command}] message [{message.id}]")
        await message.reply(prepare_text(message.content))

    async def _modify_last(self, context: Context) -> None:
        channel_id = context.channel.id
        command = context.command
        self._logger.info(f"[{channel_id}] [{command}] modifying previous message")
        message = await self._get_last_valid_message(context)
        if not message:
            self._logger.info(f"[{channel_id}] [{command}] no valid message to modify")
        else:
            self._logger.info(f"[{channel_id}] [{command}] picked message [{message.id}]")
            await message.reply(prepare_text(message.content))

    async def _get_last_valid_message(self, context: Context) -> Message:
        async for message in context.channel.history(before=context.message):
            command_context = await self._bot.get_context(message)
            if message.author != self._bot.user and not command_context.valid:
                return message
        return None
