"""
Command Cog improving targeted message.
"""

from disnake import CommandInteraction, Message
from disnake.ext.commands import Cog, message_command

from bot.prepare_text import prepare_text


class That(Cog):
    @message_command(name="Uwuify this message")
    async def that(self, interaction: CommandInteraction, message: Message) -> None:
        """Improve content of this message"""
        await interaction.response.defer()
        improved_message = prepare_text(message.content)
        await interaction.send(improved_message)
