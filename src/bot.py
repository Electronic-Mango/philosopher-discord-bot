from itertools import dropwhile
from logging import INFO, basicConfig, getLogger
from os import getenv

from discord.ext.commands import Bot, clean_content, guild_only, has_guild_permissions
from discord.ext.commands.context import Context
from discord.message import Message
from discord.utils import escape_markdown, remove_markdown
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
    content = prepare_text(message.content)
    await message.delete()
    await send_message(channel_id, webhook, username, avatar, content)


@bot.command(name="philosophize", aliases=["all"])
@guild_only()
@has_guild_permissions(manage_messages=True, manage_webhooks=True)
async def philosophize(context: Context) -> None:
    channel = context.channel
    context.command
    logger.info(f"[{channel.id}] [{context.command}]")
    if channel in STORED_CHANNELS:
        webhook = STORED_CHANNELS.pop(channel)
        await remove_webhook(context, webhook)
    else:
        webhook = await create_webhook(context)
        STORED_CHANNELS[channel] = webhook


@bot.command(name="philosophize_this", aliases=["this"])
async def philosophize_this(context: Context, *, text: clean_content(remove_markdown=True) = None) -> None:
    if text:
        await philosophize_text(context, text)
    else:
        await philosophize_last(context)


async def philosophize_text(context: Context, text: str) -> None:
    logger.info(f"[{context.channel.id}] [{context.command}] [{text}]")
    await context.reply(prepare_text(text))


async def philosophize_last(context: Context) -> None:
    if context.channel in STORED_CHANNELS:
        return
    logger.info(f"[{context.channel.id}] [{context.command}] modifying previous message")
    previous_messages = context.channel.history(before=context.message)
    message = await anext(previous_messages)
    while message.author == bot.user or (await bot.get_context(message)).valid:
        message = await anext(previous_messages)
    logger.info(f"[{context.channel.id}] [{context.command}] picked message [{message.id}]")
    await message.reply(prepare_text(message.content))


def prepare_text(text: str) -> str:
    trimmed_text = remove_markdown(text)
    return uwuify(trimmed_text)


bot.run(DISCORD_BOT_TOKEN)
