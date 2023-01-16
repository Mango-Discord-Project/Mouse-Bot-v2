import tomllib
from os import path, listdir

from dotenv import dotenv_values
from discord import (
    Intents, DiscordException,
    Bot as _Bot)
from discord.ext.commands import is_owner
from rich import console as _rich_console

from packages import config_mixin
from packages.namespace_pack import *


class Bot(_Bot):
    def __init__(self):
        intents = Intents.all()
        intents.message_content = True
        super().__init__(intent=intents)
        self.console = _rich_console.Console()
        
        self.log('Bot object build')
        with open(path.join(*('.', 'src', 'main', 'config', 'bot.toml')), 'rb') as file:
            self.config = tomllib.load(file)
        
        self.add_command()
        self.load_extensions(*self.get_extensions())
    
    def log(self, message: str) -> str:
        format_message = f'Main > {message}'
        self.console.log(format_message)
        return format_message
    
    def generate_path(self, sub_path: list[str]) -> str:
        return path.join(*self.config['path']['base'], *sub_path)
    
    def get_extensions(self) -> list[str]:
        return [
            filename for _filename in listdir(
                path.join(
                    self.generate_path(
                        self.config['path']['extensions']
                        )
                    )
                )
            if _filename.endswith('.py') and (
                filename:=_filename.removesuffix('.py')
                ) not in (
                    'template', 
                    'test'
                )
            ]
    
    
    async def on_ready(self):
        self.log('Bot is ready')
    
    async def on_application_command(self, ctx: ApplicationContext):
        self.log(f'event.application_commands - {ctx.author} try to use {ctx.command.name} from {ctx.cog.qualified_name} in {ctx.guild.name}.{ctx.channel.name}')
    
    async def on_application_command_completion(self, ctx: ApplicationContext) -> None:
        self.log(f'event.application_commands - {ctx.author} success use {ctx.command.name} from {ctx.cog.qualified_name} in {ctx.guild.name}.{ctx.channel.name}')
    
    async def on_application_command_error(self, ctx: ApplicationContext, exc: DiscordException) -> None:
        self.log(f'event.application_commands - {ctx.author} failed to use {ctx.command.name} from {ctx.cog.qualified_name} in {ctx.guild.name}.{ctx.channel.name}')
        raise exc
    
    def add_command(self):
        @self.slash_command(**config_mixin.get_setting())
        @is_owner()
        async def reload_bot_tools(ctx: ApplicationContext):
            if ctx.author.id not in self.owner_ids:
                await ctx.respond('You don\'t have enough permission to execute this command.', ephemeral=True)
                return
            self.reload_extension('extensions.bot_tools')


if __name__ == '__main__':
    bot = Bot()
    environ = dotenv_values(path.join(*('.', 'src', 'main', 'config', '.env')))
    bot.run(environ['TOKEN'])