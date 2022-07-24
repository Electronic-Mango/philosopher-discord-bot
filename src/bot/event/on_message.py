from logging import getLogger
from typing import Mapping

from discord import TextChannel, Webhook
from discord.ext.commands import Bot, Cog
from discord.message import Message

from bot.prepare_text import prepare_text
from bot.webhook import send_message


class OnMessage(Cog):
    def __init__(self, bot: Bot, modified_channels: Mapping[TextChannel, Webhook]) -> None:
        self._bot = bot
        self._logger = getLogger(__name__)
        self._modified_channels = modified_channels

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        if message.author == self._bot.user or message.webhook_id:
            return
        elif message.channel not in self._modified_channels:
            return
        channel_id = message.channel.id
        self._logger.info(f"[{channel_id}] handling message of size [{len(message.content)}]")
        webhook = self._modified_channels[message.channel]
        username = message.author.display_name
        avatar = message.author.avatar_url
        content = prepare_text(message.content)
        await message.delete()
        await send_message(channel_id, webhook, username, avatar, content)
