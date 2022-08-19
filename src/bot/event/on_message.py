"""
Event Cog handling all incoming messages.
If webhook created by "all" command is present, then current message is removed
and "improved" replacement is send with this user's name and avatar through the webhook.
"""

from logging import getLogger

from disnake import Forbidden
from disnake.abc import GuildChannel
from disnake.ext.commands import Bot, Cog
from disnake.message import Message

from bot.prepare_text import prepare_text
from bot.webhook import send_message, get_webhook


class OnMessage(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self._bot = bot
        self._logger = getLogger(__name__)

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        # TODO "webhook_id" is also present for other bot commands.
        if not message.guild or message.author.id == self._bot.user.id or message.webhook_id:
            return
        if not (webhook := await self._try_get_webhook(message.channel)):
            return
        channel_id = message.channel.id
        self._logger.info(f"[{channel_id}] modifying message of size [{len(message.content)}]")
        author = message.author
        username = author.display_name
        avatar = author.avatar or author.display_avatar or author.default_avatar
        content = prepare_text(message.content)
        await message.delete()
        await send_message(channel_id, webhook, username, avatar, content)

    async def _try_get_webhook(self, channel: GuildChannel) -> None:
        try:
            return await get_webhook(channel, self._bot)
        except Forbidden:
            return None
