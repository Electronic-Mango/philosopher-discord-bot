"""
Module creating the bot, adding all required Cogs and running it.
"""

from os import getenv

from disnake import Intents
from disnake.ext.commands import InteractionBot

from bot.event.on_application_command import OnApplicationCommand
from bot.event.on_connect import OnConnect
from bot.event.on_message import OnMessage
from bot.event.on_ready import OnReady
from bot.message_command.that import That
from bot.slash_command.all import All
from bot.slash_command.previous import Previous
from bot.slash_command.quote import Quote
from bot.slash_command.this import This
from load_all_dotenv import load_all_dotenv

load_all_dotenv()
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")


def run_bot() -> None:
    intents = Intents().default()
    intents.message_content = True
    bot = InteractionBot(intents=intents)
    bot.add_cog(OnConnect(bot))
    bot.add_cog(OnReady(bot))
    bot.add_cog(OnMessage(bot))
    bot.add_cog(OnApplicationCommand())
    bot.add_cog(All())
    bot.add_cog(Previous())
    bot.add_cog(Quote())
    bot.add_cog(That())
    bot.add_cog(This())
    bot.run(DISCORD_BOT_TOKEN)
