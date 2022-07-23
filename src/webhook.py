from logging import getLogger
from os import getenv
from discord import TextChannel, Webhook
from discord.ext.commands.context import Context
from dotenv import load_dotenv

logger = getLogger(__name__)

load_dotenv()
WEBHOOK_NAME = getenv("WEBHOOK_NAME")
WEBHOOK_CREATED_RESPONSE = getenv("WEBHOOK_CREATED_RESPONSE")
WEBHOOK_REMOVED_RESPONSE = getenv("WEBHOOK_REMOVED_RESPONSE")


async def create_webhook(context: Context, channels_to_modify: dict[TextChannel, Webhook]) -> None:
    channel = context.channel
    logger.info(f"[{channel.id}] adding webhook")
    webhook = await channel.create_webhook(name=WEBHOOK_NAME)
    channels_to_modify[channel] = webhook
    await context.send(WEBHOOK_CREATED_RESPONSE)


async def remove_webhook(context: Context, channels_to_modify: dict[TextChannel, Webhook]) -> None:
    channel = context.channel
    logger.info(f"[{channel.id}] removing webhook")
    webhook = channels_to_modify.pop(channel)
    await webhook.delete()
    await context.send(WEBHOOK_REMOVED_RESPONSE)


async def send_message(channel_id: int, webhook: Webhook, content: str) -> None:
    logger.info(f"[{channel_id}] sending message through [{webhook}]")
    await webhook.send(content=content)