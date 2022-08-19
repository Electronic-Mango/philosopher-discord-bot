"""
Command cog enabling/disabling modification of all messages in this channel.
This command only creates webhook which are used to send modified messages in "on_message" event.
No modification itself happens here.
Upon second call to this command, the webhook is removed.

This command is only available in servers, since webhook is required to send modified message.
"""

from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command, guild_only, has_guild_permissions

from bot.webhook import create_new_webhook, remove_webhook, get_webhook


class All(Cog):
    @slash_command(name="all")
    @guild_only()
    @has_guild_permissions(manage_messages=True, manage_webhooks=True)
    async def all(self, interaction: CommandInteraction) -> None:
        """Toggle modification of all messages in current channel"""
        await interaction.response.defer()
        webhook = await get_webhook(interaction.channel, interaction.bot)
        if webhook:
            await remove_webhook(interaction, webhook)
        else:
            await create_new_webhook(interaction)
