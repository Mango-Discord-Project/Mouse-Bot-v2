from packages.namespace_pack import *
from packages import core

class TestCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    TestSlashCommandGroup = SlashCommandGroup('Test')
    
    @TestSlashCommandGroup.command()
    async def hi(self, ctx: ApplicationContext, name: str = None):
        name = name or ctx.author
        await ctx.respond(f'Hi, {name}')