import json

import requests
from discord.ext.commands import is_owner

from packages.namespace_pack import *
from packages import core, config_mixin


class TestCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
        self.console_prefix = 'test'
    
    TestSlashCommandGroup = SlashCommandGroup('test', **config_mixin.get_setting())
    
    @TestSlashCommandGroup.command(**config_mixin.get_setting())
    @is_owner()
    async def test_command(self, ctx: ApplicationContext):
        url = 'https://pixiv.cat/104218207.jpg'
        respond = requests.get(url)
        
def setup(bot: Bot):
    bot.add_cog(TestCog(bot))