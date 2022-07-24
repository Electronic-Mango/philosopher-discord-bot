from logging import getLogger

from discord.ext.commands import Bot, Cog, Context


class OnCommand(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot
        self._logger = getLogger(__name__)

    @Cog.listener()
    async def on_command(self, context: Context) -> None:
        server = context.guild.name
        channel = context.channel
        user = context.author
        command = context.command
        self._logger.info(f"[{server}] [{channel}] [{user}] [{command}]")
