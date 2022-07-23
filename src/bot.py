from logging import INFO, basicConfig, getLogger
from os import getenv

from discord.ext.commands import Bot, guild_only, has_guild_permissions
from discord.ext.commands.context import Context
from discord.message import Message
from dotenv import load_dotenv

from webhook import create_webhook, remove_webhook, send_message
from uwuifier import uwuify

logger = getLogger("bot_main")
basicConfig(format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", level=INFO)

load_dotenv()
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = getenv("COMMAND_PREFIX")

STORED_CHANNELS = dict()

bot = Bot(COMMAND_PREFIX)


@bot.event
async def on_connect() -> None:
    logger.info(f"[{bot.user}] connected")


@bot.event
async def on_ready() -> None:
    logger.info(f"[{bot.user}] ready")


@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user or message.webhook_id is not None:
        return
    elif message.content.startswith(COMMAND_PREFIX):
        logger.info(f"[{message.channel.id}] moving to handling command [{message.content}]")
        await bot.process_commands(message)
        return
    elif message.channel not in STORED_CHANNELS:
        return
    channel_id = message.channel.id
    logger.info(f"[{channel_id}] handling message of size [{len(message.content)}]")
    webhook = STORED_CHANNELS[message.channel]
    username = message.author.display_name
    avatar = message.author.avatar_url
    content = uwuify(message.content)
    await send_message(channel_id, webhook, username, avatar, content)


@bot.command(name="philosophize", aliases=["all"])
@guild_only()
@has_guild_permissions(manage_webhooks=True)
async def philosophize(context: Context) -> None:
    channel = context.channel
    context.command
    logger.info(f"[{channel.id}] handling [{context.command}] command")
    if channel in STORED_CHANNELS:
        await remove_webhook(context, STORED_CHANNELS)
    else:
        await create_webhook(context, STORED_CHANNELS)


bot.run(DISCORD_BOT_TOKEN)
