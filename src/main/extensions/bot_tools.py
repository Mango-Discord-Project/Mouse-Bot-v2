from os import listdir, path

from discord import Option

from packages.namespace_pack import *
from packages import core, config_mixin

bot_config = config_mixin.get_bot_config()

class BotToolsCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    BotToolsSlashCommandGroup = SlashCommandGroup('bot_tools', **config_mixin.get_setting())
    
    @BotToolsSlashCommandGroup.command(**config_mixin.get_setting())
    async def extension(self, ctx: ApplicationContext,
                        name: Option(str, 
                                     choices = [i for i in listdir(path.join(*(bot_config['path']['base'] + bot_config['path']['extensions']))) if i.endswith('.py')],
                                     required = True),
                        action: Option(str, 
                                       choices = ['load', 'reload', 'unload'], 
                                       default = 'reload')):
        if ctx.author.id not in self.bot.owner_ids:
            await ctx.respond('You don\'t have enough permission to execute this command.', ephemeral=True)
            return
        getattr(self.bot, f'{action}_extension')(f'extensions.{name.removesuffix(".py")}')
        await ctx.respond(f'{action.title()} extension "{name}" success', ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(BotToolsCog(bot))