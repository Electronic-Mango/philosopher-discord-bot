"""
Command Cog improving previous message send in the channel.
Commands or messages send by this bot are not taken into account.
"""

from logging import getLogger

from disnake import CommandInteraction
from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake.message import Message

from bot.prepare_text import prepare_text

_COMMAND_NAME = "previous"
_COMMAND_DESCRIPTION = "Modify previous message in current channel"
HELP_MESSAGE = f"""
`/{_COMMAND_NAME}` - {_COMMAND_DESCRIPTION}
"""


class Previous(Cog, name="Single message"):
    def __init__(self, bot: InteractionBot) -> None:
        super().__init__()
        self._bot = bot
        self._logger = getLogger(__name__)

    @slash_command(name=_COMMAND_NAME, description=_COMMAND_DESCRIPTION)
    async def _previous(self, interaction: CommandInteraction) -> None:
        await interaction.response.defer()
        channel_id = interaction.channel.id
        if not (message := await self._get_last_valid_message(interaction)):
            self._logger.info(f"[{channel_id}] no valid message to modify")
        else:
            self._logger.info(f"[{channel_id}] picked message [{message.id}]")
            await interaction.send(prepare_text(message.clean_content))

    async def _get_last_valid_message(self, interaction: CommandInteraction) -> Message:
        original_message = await interaction.original_message()
        async for message in interaction.channel.history(before=original_message):
            if message.author.id != self._bot.user.id and message.clean_content:
                return message
        return None
