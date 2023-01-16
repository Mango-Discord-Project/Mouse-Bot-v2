from datetime import datetime, timezone

from discord import Embed, User, Member

__all__ = ['generate_embed']

def generate_embed(title: str, description: str, author: User | Member) -> Embed:
    embed = Embed(title = title,
                  description = description,
                  color = 0x2f3136)
    embed.set_footer(text = f'{author} · {datetime.strftime(datetime.now(timezone.utc), r"%c")}')
    return embed