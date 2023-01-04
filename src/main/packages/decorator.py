from typing import Callable, Any, Self
from discord import ApplicationCommand

def owner_only(owner_ids: list) -> Callable:
    ...