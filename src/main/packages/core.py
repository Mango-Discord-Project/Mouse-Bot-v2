from discord import Cog, Bot, Intents
from rich import console as _rich_console

__all__ = ['BotBase', 'CogBase']

class BotBase(Bot):
    def __init__(self):
        super().__init__(intent=Intents.all())
        self.console = _rich_console.Console()
    
    def log(self, message: str) -> str:
        format_message = f'Main > {message}'
        self.console.log(format_message)
        return format_message

    async def on_ready(self):
        self.guilds

class CogBase(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
    
    def log(self, message: str) -> str:
        format_message = f'{self.console_prefix} > {message}'
        self.bot.console.log(format_message)
        return format_message