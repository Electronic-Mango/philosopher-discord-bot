"""
Event Cog handling all incoming messages.
If webhook created by "all" command is present, then current message is removed
and "improved" replacement is send with this user's name and avatar through the webhook.
"""

from logging import getLogger

from disnake import Forbidden, Webhook
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
        if not self._modifiable(message) or not (webhook := await self._try_get_webhook(message)):
            return
        channel_id = message.channel.id
        self._logger.info(f"[{channel_id}] modifying message of size [{len(message.content)}]")
        author = message.author
        username = author.display_name
        avatar = author.avatar or author.display_avatar or author.default_avatar
        new_content = prepare_text(message.content)
        await message.delete()
        await send_message(channel_id, webhook, username, avatar, new_content)

    def _modifiable(self, message: Message) -> bool:
        return message.guild and not message.webhook_id and message.author.id != self._bot.user.id

    async def _try_get_webhook(self, message: Message) -> Webhook:
        try:
            return await get_webhook(message.channel, self._bot)
        except Forbidden:
            return None
