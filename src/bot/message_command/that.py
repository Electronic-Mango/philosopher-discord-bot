"""
Command Cog improving targeted message.
"""

from disnake import CommandInteraction, Message
from disnake.ext.commands import Cog, message_command

from bot.prepare_text import prepare_text

_COMMAND_NAME = "uwuify this message"
HELP_MESSAGE = f"""
`{_COMMAND_NAME}` - Improve content of selected message
"""


class That(Cog):
    @message_command(name=_COMMAND_NAME)
    async def _that(self, interaction: CommandInteraction, message: Message) -> None:
        await interaction.response.defer()
        improved_message = prepare_text(message.content)
        await interaction.send(improved_message)
