from time import time

from discord import User

from packages import core, config_mixin
from packages.namespace_pack import *


class FunnyCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    def user_daily_random(self, user: User, digits: int = 2, seed: int = 123456) -> int:
        now = int(time())
        return int(f'{user.id * (now-now%(60*60)) + seed}'[-digits:])
    
    FunnySlashCommandGroup = SlashCommandGroup('funny', **config_mixin.get_setting())
    
    @FunnySlashCommandGroup.command(**config_mixin.get_bot_config())
    async def horoscope(self, ctx: ApplicationContext, ephemeral: bool = False):
        await ctx.respond(f'Today\'s horoscope is {self.user_daily_random(ctx.author)}')

def setup(bot: Bot):
    bot.add_cog(FunnyCog(bot))