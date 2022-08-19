"""
Command cog enabling/disabling modification of all messages in this channel.
This command only creates webhook which are used to send modified messages in "on_message" event.
No modification itself happens here.
Upon second call to this command, the webhook is removed.

This command is only available in servers, since webhook is required to send modified message.

If bot doesn't have "manage_webhooks" and "manage_messages" permissions
it will send back and ephemeral error with this information.
"""

from logging import getLogger
from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command, bot_has_guild_permissions

from bot.webhook import create_new_webhook, remove_webhook, get_webhook


class All(Cog):
    def __init__(self) -> None:
        super().__init__()
        self._logger = getLogger(__name__)

    @slash_command(name="all", dm_permission=False)
    @bot_has_guild_permissions(manage_webhooks=True, manage_messages=True)
    async def all(self, interaction: CommandInteraction) -> None:
        """Toggle modification of all messages in current channel"""
        await interaction.response.defer()
        webhook = await get_webhook(interaction.channel, interaction.bot)
        if webhook:
            await remove_webhook(interaction, webhook)
        else:
            await create_new_webhook(interaction)

    @all.error
    async def all_error(self, interaction: CommandInteraction, error) -> None:
        self._logger.warn(error)
        await interaction.send(content=error, ephemeral=True)
