"""
Event Cog logging all command calls to internal logger.
"""

from logging import getLogger

from disnake import CommandInteraction
from disnake.ext.commands import Cog


class OnApplicationCommand(Cog):
    def __init__(self) -> None:
        self._logger = getLogger(__name__)

    @Cog.listener()
    async def on_application_command(self, interaction: CommandInteraction) -> None:
        server = interaction.guild.name if interaction.guild else None
        channel = interaction.channel
        user = interaction.author
        command = interaction.application_command.qualified_name
        self._logger.info(f"[{server}] [{channel}] [{user}] [{command}]")
