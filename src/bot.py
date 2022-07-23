from logging import INFO, basicConfig, getLogger
from os import getenv

from discord.ext.commands import Bot, guild_only
from discord.ext.commands.context import Context
from dotenv import load_dotenv

logger = getLogger("bot_main")
basicConfig(format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", level=INFO)

load_dotenv()
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = getenv("COMMAND_PREFIX")

bot = Bot(COMMAND_PREFIX)


@bot.event
async def on_connect() -> None:
    logger.info(f"[{bot.user}] connected")


@bot.event
async def on_ready() -> None:
    logger.info(f"[{bot.user}] ready")


@bot.command(name="philosophize")
@guild_only()
async def philosophize(context: Context) -> None:
    channel = context.channel
    logger.info(f"[{channel.id}] handling 'philosophize' command")
    await channel.send("Hello there!")


bot.run(DISCORD_BOT_TOKEN)
