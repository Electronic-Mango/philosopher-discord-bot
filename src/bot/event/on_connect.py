"""
Event Cog logging information about connection establishment to internal logger.
"""

from logging import getLogger

from disnake.ext.commands import Bot, Cog


class OnConnect(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self._bot = bot
        self._logger = getLogger(__name__)

    @Cog.listener()
    async def on_connect(self) -> None:
        self._logger.info(f"[{self._bot.user}] connected")
