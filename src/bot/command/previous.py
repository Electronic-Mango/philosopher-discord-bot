"""
Command Cog improving previous message send in the channel.
Commands or messages send by this bot are not taken into account.
"""

from logging import getLogger

from discord.ext.commands import Bot, Cog, Context, command
from discord.message import Message

from bot.prepare_text import prepare_text


class Previous(Cog, name="Single message"):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot
        self._logger = getLogger(__name__)

    @command(name="previous", aliases=["prev", "uwuprevious", "uwuprev"])
    async def previous(self, context: Context) -> None:
        """Modify previous message in channel"""
        channel_id = context.channel.id
        message = await self._get_last_valid_message(context)
        if not message:
            self._logger.info(f"[{channel_id}] no valid message to modify")
        else:
            self._logger.info(f"[{channel_id}] picked message [{message.id}]")
            await message.reply(prepare_text(message.content))

    async def _get_last_valid_message(self, context: Context) -> Message:
        async for message in context.channel.history(before=context.message):
            command_context = await self._bot.get_context(message)
            if message.author != self._bot.user and not command_context.valid:
                return message
        return None
