from packages.namespace_pack import *
from packages import core
from packages import config_mixin

class TestCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    TestSlashCommandGroup = SlashCommandGroup('test', **config_mixin.get_setting())
    
    @TestSlashCommandGroup.command(**config_mixin.get_setting())
    async def test_command(self, ctx: ApplicationContext):
        await ctx.respond(f'test', ephemeral=True)
        msg = await ctx.send('test')
        await msg.add_reaction(emoji='🇦')

def setup(bot: Bot):
    bot.add_cog(TestCog(bot))