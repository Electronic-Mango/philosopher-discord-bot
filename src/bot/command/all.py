"""
Command cog enabling/disabling modification of all messages in this channel.
This command only creates webhook which are used to send modified messages in "on_message" event.
No modification itself happens here.
Upon second call to this command, the webhook is removed.
"""

from discord.ext.commands import Bot, Cog, Context, command, guild_only, has_guild_permissions

from bot.webhook import create_new_webhook, remove_webhook, get_webhook


class All(Cog, name="All messages"):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="all", aliases=["uwuall"])
    @guild_only()
    @has_guild_permissions(manage_messages=True, manage_webhooks=True)
    async def all(self, context: Context) -> None:
        """Toggle modification of all messages in current channel"""
        webhook = await get_webhook(context.channel)
        if webhook:
            await remove_webhook(context, webhook)
        else:
            await create_new_webhook(context)
