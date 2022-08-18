"""
Event Cog handling all incoming messages.
If webhook created by "all" command is present, then current message is removed
and "improved" replacement is send with this user's name and avatar through the webhook.
"""

from logging import getLogger

from disnake.ext.commands import Bot, Cog
from disnake.message import Message

from bot.prepare_text import prepare_text
from bot.webhook import send_message, get_webhook


class OnMessage(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot
        self._logger = getLogger(__name__)

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        if message.author == self._bot.user or message.webhook_id or not message.guild:
            return
        webhook = await get_webhook(message.channel, self._bot)
        if not webhook:
            return
        channel_id = message.channel.id
        self._logger.info(f"[{channel_id}] modifying message of size [{len(message.content)}]")
        username = message.author.display_name
        avatar = message.author.avatar_url
        content = prepare_text(message.content)
        await message.delete()
        await send_message(channel_id, webhook, username, avatar, content)
