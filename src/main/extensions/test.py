from packages.namespace_pack import *
from packages import core
from packages import config_mixin

class TestCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    TestSlashCommandGroup = SlashCommandGroup('test', **config_mixin.get_setting())
    
    @TestSlashCommandGroup.command()
    async def hi(self, ctx: ApplicationContext, name: str = None):
        name = name or ctx.author
        await ctx.respond(f'Hi, {name}')

def setup(bot: Bot):
    bot.add_cog(TestCog(bot))