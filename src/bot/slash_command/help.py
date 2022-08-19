"""
Command Cog sending back a help message.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command

from bot.message_command.that import HELP_MESSAGE as THAT
from bot.slash_command.all import HELP_MESSAGE as ALL
from bot.slash_command.previous import HELP_MESSAGE as PREVIOUS
from bot.slash_command.quote import HELP_MESSAGE as QUOTE
from bot.slash_command.this import HELP_MESSAGE as THIS

_SLASH_COMMANDS_HELP = "\n".join([ALL.strip(), PREVIOUS.strip(), QUOTE.strip(), THIS.strip()])
_MESSAGE_CONTEXT_COMMANDS_HELP = THAT.strip()
_FULL_HELP_MESSAGE = f"""
**Slash commands**:
{_SLASH_COMMANDS_HELP}

**Selected message context menu commands**:
{_MESSAGE_CONTEXT_COMMANDS_HELP}
"""


class Help(Cog):
    @slash_command(name="help")
    async def _help(self, interaction: CommandInteraction) -> None:
        """Get help information for the bot"""
        await interaction.send(_FULL_HELP_MESSAGE, ephemeral=True)
