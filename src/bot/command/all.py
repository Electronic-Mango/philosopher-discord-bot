from logging import getLogger

from discord.ext.commands import Cog, Context, command, guild_only, has_guild_permissions

from bot.webhook import create_webhook, remove_webhook


class All(Cog):
    def __init__(self, bot, modified_channels):
        self._bot = bot
        self._logger = getLogger(__name__)
        self._modified_channels = modified_channels

    @command(name="all", aliases=["uwuall"])
    @guild_only()
    @has_guild_permissions(manage_messages=True, manage_webhooks=True)
    async def all(self, context: Context) -> None:
        channel = context.channel
        context.command
        self._logger.info(f"[{channel.id}] [{context.command}]")
        if channel in self._modified_channels:
            webhook = self._modified_channels.pop(channel)
            await remove_webhook(context, webhook)
        else:
            webhook = await create_webhook(context)
            self._modified_channels[channel] = webhook
