"""
Module responsible for handling webhooks related to improving all messages.
"""

from logging import getLogger
from os import getenv

from discord import Asset, TextChannel, Webhook
from discord.ext.commands import Bot
from discord.ext.commands.context import Context
from dotenv import load_dotenv

logger = getLogger(__name__)

load_dotenv()
WEBHOOK_CREATED_RESPONSE = getenv("WEBHOOK_CREATED_RESPONSE")
WEBHOOK_REMOVED_RESPONSE = getenv("WEBHOOK_REMOVED_RESPONSE")


async def get_webhook(channel: TextChannel, bot: Bot) -> Webhook:
    """Get webhook used to improve all messages, or None"""
    webhooks = await channel.webhooks()
    return next((webhook for webhook in webhooks if webhook.name == bot.user.name), None)


async def create_new_webhook(context: Context) -> Webhook:
    """Create a webhook which can be used to improve all messages"""
    channel = context.channel
    bot_user = context.bot.user
    bot_name = bot_user.name
    bot_avatar = await bot_user.avatar_url.read()
    webhook = await channel.create_webhook(name=bot_name, avatar=bot_avatar)
    logger.info(f"[{channel.id}] added new webhook [{webhook}]")
    await context.reply(WEBHOOK_CREATED_RESPONSE)
    return webhook


async def remove_webhook(context: Context, webhook: Webhook) -> None:
    """Remove webhook passed as argument and inform the context about it"""
    logger.info(f"[{context.channel.id}] removing webhook [{webhook}]")
    await webhook.delete()
    await context.reply(WEBHOOK_REMOVED_RESPONSE)


async def send_message(
    channel_id: int, webhook: Webhook, username: str, avatar_url: Asset, content: str
) -> None:
    """Send message through webhook from argument, with given username, avatar, and content"""
    logger.info(f"[{channel_id}] sending message through [{webhook}] from [{username}]")
    await webhook.send(username=username, avatar_url=avatar_url, content=content)
