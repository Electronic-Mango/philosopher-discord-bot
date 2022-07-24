from discord.ext.commands import Bot, Cog, Context, command, guild_only, has_guild_permissions

from bot.webhook import create_new_webhook, remove_webhook, get_webhook


class All(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="all", aliases=["uwuall"])
    @guild_only()
    @has_guild_permissions(manage_messages=True, manage_webhooks=True)
    async def all(self, context: Context) -> None:
        webhook = await get_webhook(context.channel)
        if webhook:
            await remove_webhook(context, webhook)
        else:
            await create_new_webhook(context)
