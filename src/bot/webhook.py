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


async def get_webhook(channel: TextChannel) -> Webhook:
    webhooks = await channel.webhooks()
    return next((webhook for webhook in webhooks if webhook.name == WEBHOOK_NAME), None)


async def create_new_webhook(context: Context) -> Webhook:
    channel = context.channel
    webhook = await channel.create_webhook(name=WEBHOOK_NAME)
    logger.info(f"[{channel.id}] added new webhook [{webhook}]")
    await context.reply(WEBHOOK_CREATED_RESPONSE)
    return webhook


async def remove_webhook(context: Context, webhook: Webhook) -> None:
    logger.info(f"[{context.channel.id}] removing webhook [{webhook}]")
    await webhook.delete()
    await context.reply(WEBHOOK_REMOVED_RESPONSE)


async def send_message(
    channel_id: int, webhook: Webhook, username: str, avatar_url: Asset, content: str
) -> None:
    logger.info(f"[{channel_id}] sending message through [{webhook}] from [{username}]")
    await webhook.send(username=username, avatar_url=avatar_url, content=content)
