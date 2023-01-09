import tomllib
from os import path, listdir

from dotenv import dotenv_values
from discord import (
    Intents,
    Bot as _Bot)
from rich import console as _rich_console

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
        self.load_extensions(*self.get_extension_list())
    
    def log(self, message: str) -> str:
        format_message = f'Main > {message}'
        self.console.log(format_message)
        return format_message
    
    def generate_path(self, sub_path: list[str]) -> str:
        return path.join(*(self.config['path']['base'] + sub_path))
    
    def get_extension_list(self) -> list[str]:
        filter_func = lambda filename: filename.endswith('.py')
        map_func = lambda filename: f"extensions.{filename.removesuffix('.py')}"
        return map(map_func, filter(filter_func, listdir(path.join(self.generate_path(self.config['path']['extensions'])))))
    
    async def on_ready(self):
        self.log('Bot is ready')
    
    def add_command(self):
        @self.slash_command()
        async def reload_bot_tools(ctx: ApplicationContext):
            if ctx.author.id not in self.config['ids']['owner']:
                await ctx.respond('You don\'t have enough permission to execute this command.', ephemeral=True)
                return
            await self.reload_extension('extensions.bot_tools')

if __name__ == '__main__':
    bot = Bot()
    environ = dotenv_values(path.join(*('.', 'src', 'main', 'config', '.env')))
    bot.run(environ['TOKEN'])