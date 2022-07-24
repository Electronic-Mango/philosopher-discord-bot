from os import getenv

from discord.ext.commands import Bot
from dotenv import load_dotenv

from bot.command.all import All
from bot.command.previous import Previous
from bot.command.that import That
from bot.command.this import This
from bot.event.on_connect import OnConnect
from bot.event.on_message import OnMessage
from bot.event.on_ready import OnReady

load_dotenv()
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = getenv("COMMAND_PREFIX")
MODIFIED_CHANNELS = dict()


def run_bot() -> None:
    bot = Bot(command_prefix=COMMAND_PREFIX)
    bot.add_cog(OnConnect(bot))
    bot.add_cog(OnReady(bot))
    bot.add_cog(OnMessage(bot, MODIFIED_CHANNELS))
    bot.add_cog(All(bot, MODIFIED_CHANNELS))
    bot.add_cog(Previous(bot))
    bot.add_cog(That(bot))
    bot.add_cog(This(bot))
    bot.run(DISCORD_BOT_TOKEN)
