from typing import Callable, Any, Self
from discord import ApplicationCommand, ApplicationContext

def owner_only() -> Callable:
    def decorator(command: Callable):
        def wrapper(self, ctx: ApplicationContext, *args):
            if ctx.author.id not in self.bot.owner_ids:
                return ...
            ...
        return wrapper
    return decorator