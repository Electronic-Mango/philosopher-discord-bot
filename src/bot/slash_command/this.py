"""
Command Cog improving text send as this command argument.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, Param, slash_command

from bot.prepare_text import prepare_text

_COMMAND_NAME = "this"
_COMMAND_DESCRIPTION = "Improve message given as an argument"
HELP_MESSAGE = f"""
`/{_COMMAND_NAME}` - {_COMMAND_DESCRIPTION}
"""


class This(Cog):
    @slash_command(name=_COMMAND_NAME, description=_COMMAND_DESCRIPTION)
    async def _this(
        self,
        interaction: CommandInteraction,
        text: str = Param(description="text to uwuify"),
    ) -> None:
        await interaction.response.defer()
        improved_text = prepare_text(text)
        await interaction.send(improved_text)
