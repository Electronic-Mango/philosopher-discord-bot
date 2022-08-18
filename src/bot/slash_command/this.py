"""
Command Cog improving text send as this command argument.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, Param, slash_command

from bot.prepare_text import prepare_text


class This(Cog):
    @slash_command(name="this")
    async def this(
        self,
        interaction: CommandInteraction,
        text: str = Param(description="text to uwuify"),
    ) -> None:
        """Improve message given as an argument"""
        await interaction.response.defer()
        improved_text = prepare_text(text)
        await interaction.send(improved_text)
