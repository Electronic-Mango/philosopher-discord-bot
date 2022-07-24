from logging import getLogger
from os import getenv

from discord import Asset, TextChannel, Webhook
from discord.ext.commands.context import Context
from dotenv import load_dotenv

logger = getLogger(__name__)

load_dotenv()
WEBHOOK_NAME = getenv("WEBHOOK_NAME")
WEBHOOK_CREATED_RESPONSE = getenv("WEBHOOK_CREATED_RESPONSE")
WEBHOOK_REMOVED_RESPONSE = getenv("WEBHOOK_REMOVED_RESPONSE")


async def create_webhook(context: Context) -> Webhook:
    channel = context.channel
    webhook = await _get_existing_webhook(channel)
    if not webhook:
        webhook = await channel.create_webhook(name=WEBHOOK_NAME)
        logger.info(f"[{channel.id}] added new webhook [{webhook}]")
    else:
        logger.info(f"[{channel.id}] using existing webhook [{webhook}]")
    await context.send(WEBHOOK_CREATED_RESPONSE)
    return webhook


async def _get_existing_webhook(channel: TextChannel) -> Webhook:
    webhooks = await channel.webhooks()
    for webhook in webhooks:
        if webhook.name == WEBHOOK_NAME:
            return webhook
    return None


async def remove_webhook(context: Context, webhook: Webhook) -> None:
    channel = context.channel
    logger.info(f"[{channel.id}] removing webhook")
    await webhook.delete()
    await context.send(WEBHOOK_REMOVED_RESPONSE)


async def send_message(
    channel_id: int, webhook: Webhook, username: str, avatar_url: Asset, content: str
) -> None:
    logger.info(f"[{channel_id}] sending message through [{webhook}] from [{username}]")
    await webhook.send(username=username, avatar_url=avatar_url, content=content)
