"""
Command cog enabling/disabling modification of all messages in this channel.
This command only creates webhook which are used to send modified messages in "on_message" event.
No modification itself happens here.
Upon second call to this command, the webhook is removed.

This command is only available in servers, since webhook is required to send modified message.

If bot doesn't have "manage_webhooks" and "manage_messages" permissions
it will send back an ephemeral error with this information.
"""

from logging import getLogger

from disnake import CommandInteraction
from disnake.ext.commands import Cog, bot_has_guild_permissions, slash_command

from bot.webhook import create_new_webhook, get_webhook, remove_webhook

_COMMAND_NAME = "all"
_COMMAND_DESCRIPTION = "Toggle modification of all messages in current channel"
HELP_MESSAGE = f"""
`/{_COMMAND_NAME}` - {_COMMAND_DESCRIPTION}
"""


class All(Cog):
    def __init__(self) -> None:
        super().__init__()
        self._logger = getLogger(__name__)

    @slash_command(name=_COMMAND_NAME, description=_COMMAND_DESCRIPTION, dm_permission=False)
    @bot_has_guild_permissions(manage_webhooks=True, manage_messages=True)
    async def _all(self, interaction: CommandInteraction) -> None:
        await interaction.response.defer()
        if webhook := await get_webhook(interaction.channel, interaction.bot):
            await remove_webhook(interaction, webhook)
        else:
            await create_new_webhook(interaction)

    @_all.error
    async def _all_error(self, interaction: CommandInteraction, error) -> None:
        self._logger.warning(error)
        await interaction.send(content=error, ephemeral=True)
