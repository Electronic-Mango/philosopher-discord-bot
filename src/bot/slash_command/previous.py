"""
Command Cog improving previous message send in the channel.
Commands or messages send by this bot are not taken into account.
"""

from logging import getLogger

from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command
from disnake.message import Message

from bot.prepare_text import prepare_text


class Previous(Cog, name="Single message"):
    def __init__(self) -> None:
        self._logger = getLogger(__name__)

    @slash_command(name="previous")
    async def previous(self, interaction: CommandInteraction) -> None:
        """Modify previous message in channel"""
        await interaction.response.defer()
        channel_id = interaction.channel.id
        message = await self._get_last_valid_message(interaction)
        if not message:
            self._logger.info(f"[{channel_id}] no valid message to modify")
        else:
            self._logger.info(f"[{channel_id}] picked message [{message.id}]")
            await interaction.send(prepare_text(message.clean_content))

    async def _get_last_valid_message(self, interaction: CommandInteraction) -> Message:
        original_message = await interaction.original_message()
        async for message in interaction.channel.history(before=original_message):
            if message.author != original_message.author and message.clean_content:
                return message
        return None
