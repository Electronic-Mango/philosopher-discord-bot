"""
Command Cog improving targeted message.
Message to improve is a message which this command replies to.
"""

from discord.ext.commands import Bot, Cog, Context, command

from bot.prepare_text import prepare_text


class That(Cog, name="Single message"):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="that", aliases=["uwuthat"])
    async def that(self, context: Context) -> None:
        """Improve message which this command replied to"""
        if context.message.reference and context.message.reference.resolved:
            message = context.message.reference.resolved
            await message.reply(prepare_text(message.content))
