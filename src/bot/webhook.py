"""
Module responsible for handling webhooks related to improving all messages.
"""

from logging import getLogger
from os import getenv

from disnake import Asset, CommandInteraction, TextChannel, Webhook
from disnake.ext.commands import Bot
from disnake.ext.commands.context import Context

from load_all_dotenv import load_all_dotenv

logger = getLogger(__name__)

load_all_dotenv()
WEBHOOK_CREATED_RESPONSE = getenv("WEBHOOK_CREATED_RESPONSE")
WEBHOOK_REMOVED_RESPONSE = getenv("WEBHOOK_REMOVED_RESPONSE")


async def get_webhook(channel: TextChannel, bot: Bot) -> Webhook:
    """Get webhook used to improve all messages, or None"""
    webhooks = await channel.webhooks()
    return next((webhook for webhook in webhooks if webhook.name == bot.user.name), None)


async def create_new_webhook(interaction: CommandInteraction) -> Webhook:
    """Create a webhook which can be used to improve all messages"""
    channel = interaction.channel
    bot_user = interaction.bot.user
    bot_name = bot_user.name
    avatar = bot_user.avatar or bot_user.display_avatar or bot_user.default_avatar
    webhook = await channel.create_webhook(name=bot_name, avatar=avatar)
    logger.info(f"[{channel.id}] added new webhook [{webhook}]")
    await interaction.send(WEBHOOK_CREATED_RESPONSE)
    return webhook


async def remove_webhook(interaction: CommandInteraction, webhook: Webhook) -> None:
    """Remove webhook passed as argument and inform the context about it"""
    logger.info(f"[{interaction.channel.id}] removing webhook [{webhook}]")
    await webhook.delete()
    await interaction.send(WEBHOOK_REMOVED_RESPONSE)


async def send_message(
    channel_id: int, webhook: Webhook, username: str, avatar: Asset, content: str
) -> None:
    """Send message through webhook from argument, with given username, avatar, and content"""
    logger.info(f"[{channel_id}] sending message through [{webhook}] from [{username}]")
    await webhook.send(username=username, avatar_url=avatar.url, content=content)
