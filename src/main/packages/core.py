from discord import Cog, Bot

__all__ = ['CogBase']

class CogBase(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
    
    def log(self, message: str) -> str:
        self.console_prefix = self.__dict__.setdefault('console_prefix', self.__cog_name__)
        format_message = f'{self.console_prefix} > {message}'
        self.bot.console.log(format_message)
        return format_message