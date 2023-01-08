from os import path, listdir
import tomllib

from discord import Cog, Bot, Intents
from rich import console as _rich_console

__all__ = ['BotBase', 'CogBase']

class BotBase(Bot):
    def __init__(self):
        super().__init__(intent=Intents.all())
        self.console = _rich_console.Console()
        
        with open(path.join(*('.', 'src', 'main', 'config', 'bot.toml')), 'rb') as file:
            self.config = tomllib.load(file)
    
    def log(self, message: str) -> str:
        format_message = f'Main > {message}'
        self.console.log(format_message)
        return format_message
    
    def generate_path(self, sub_path: list[str]) -> str:
        return path.join(self.config['path']['base'] + sub_path)
    
    def get_extension_list(self) -> list[str]:
        filter_func = lambda filename: filename.endswith('.py')
        return filter(filter_func, listdir(path.join(*self.generate_path(self.config['extensions']))))

class CogBase(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
    
    def log(self, message: str) -> str:
        format_message = f'{self.console_prefix} > {message}'
        self.bot.console.log(format_message)
        return format_message