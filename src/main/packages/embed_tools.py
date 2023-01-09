from datetime import datetime, timezone

from discord import Embed, User, Member

def generate_embed(title: str, description: str, author: User | Member) -> Embed:
    embed = Embed(title = title,
                  description = description,
                  color = 0x2f3136)
    embed.set_footer(text = datetime.strftime(datetime.now(timezone.utc), r'%c'))
    embed.set_author(name = author,
                     icon_url = author.avatar.url)
    return embed