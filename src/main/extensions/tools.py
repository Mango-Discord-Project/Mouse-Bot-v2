from string import ascii_lowercase
from re import match

from discord import Option, commands

from packages import config_mixin, core
from packages.embed_tools import generate_embed
from packages.namespace_pack import *


class ToolsCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    UtilityToolsSlashCommandGroup = SlashCommandGroup('utility_tools', **config_mixin.get_setting('command.all.base'))
    PixivToolsSlashCommandGroup = SlashCommandGroup('pixiv_tools', **config_mixin.get_setting('command.all.base'))
    
    
    @UtilityToolsSlashCommandGroup.command(**config_mixin.get_setting())
    async def yn_poll(self, ctx: ApplicationContext, question: str):
        embed = generate_embed(title = '📊 Yes-No Poll',
                               description = question,
                               author = ctx.author)
        await ctx.respond('Create Poll Success', ephemeral=True)
        send_message = await ctx.send(embed=embed)
        for emoji in ('✅', '❎'):
            await send_message.add_reaction(emoji=emoji)
    
    @UtilityToolsSlashCommandGroup.command(**config_mixin.get_setting())
    async def op_poll(self, ctx: ApplicationContext, question: str,
                      option_a: str, option_b: str, option_c: Option(str, required=False), 
                      option_d: Option(str, required=False), option_e: Option(str, required=False), option_f: Option(str, required=False), 
                      option_g: Option(str, required=False), option_h: Option(str, required=False), option_i: Option(str, required=False), 
                      option_j: Option(str, required=False), option_k: Option(str, required=False), option_l: Option(str, required=False), 
                      option_m: Option(str, required=False), option_n: Option(str, required=False), option_o: Option(str, required=False), 
                      option_p: Option(str, required=False), option_q: Option(str, required=False), option_r: Option(str, required=False), 
                      option_s: Option(str, required=False), option_t: Option(str, required=False), option_u: Option(str, required=False), 
                      option_v: Option(str, required=False), option_w: Option(str, required=False)):
        local_variable = locals().copy()
        option_emojis = [(chr(127462+index), value) for index, char in enumerate(ascii_lowercase[:-3]) if (value:=(local_variable[f'option_{char}']))]
        description = '\n'.join(f'{i[0]} `{i[1]}`' for i in option_emojis)
        embed = generate_embed(title = '📊 Multi-Option Poll',
                               description = f'{question}\n\n{description}',
                               author = ctx.author)
        await ctx.respond('Create Poll Success', ephemeral=True)
        send_message = await ctx.send(embed=embed)
        for option_emoji in option_emojis:
            await send_message.add_reaction(emoji=option_emoji[0])
    
    @PixivToolsSlashCommandGroup.command()
    async def get_image(self, ctx: ApplicationContext, url: str):
        matched = match(r'https://www\.pixiv\.net/artworks/(\d+)(?:/.?)?', url)
        if matched is None:
            return await ctx.respond('URL format error', ephemeral=True)
        await ctx.respond('Match Success, image sending', ephemeral=True)
        pixiv_id = matched.group(1)
        proxy_url = f'https://pixiv.cat/{pixiv_id}.png'
        embed = generate_embed(title = '📲 Pixiv Get Image',
                               description = f'Pixiv ID: {pixiv_id}\nProxy URL: {proxy_url}',
                               author = ctx.author)
        embed.set_image(url=proxy_url)
        await ctx.send(embed=embed)
    
    @commands.slash_command(**config_mixin.get_setting('command.all.base'))
    async def help(self, ctx: ApplicationContext):
        ...

def setup(bot: Bot):
    bot.add_cog(ToolsCog(bot))