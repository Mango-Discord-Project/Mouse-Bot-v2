from uuid import uuid1

from discord import commands, Message, Embed

from packages.namespace_pack import *
from packages import core, config_mixin
from packages.embed_tools import generate_embed

class HentaiBusCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    HentaiBusSlashCommandGroup = SlashCommandGroup('hentai_bus', **config_mixin.get_setting('command.hentai_bus.base'))
    
    @commands.message_command(**config_mixin.get_setting('command.hentai_bus.base'))
    async def report(self, ctx: ApplicationContext, message: Message):
        if not ctx.author.guild_permissions.administrator:
            await ctx.respond('You don\'t have enough permission to execute this command.', ephemeral=True)
            return
        await ctx.respond('Report Success', ephemeral=True)
        
        channel = self.bot.get_channel(1050755744879886356)
        uuid = uuid1()
        embed = generate_embed(title = f'⚠️ Report Alert - {uuid}',
                               description = f'Target: {message.author}\n[Message Jump Link]({message.jump_url})',
                               author = ctx.author)
        
        send_message = await channel.send(embed=embed)
        thread = await send_message.create_thread(name = f'⚠️ Report Alert - {uuid}')
        send_message = await thread.send('||<@&831530573934886933> <@&962323168981286962>||\n> 📊 Poll: 此檢舉是否成立\n⛔給予警告；⚠️給予提醒；✅不用處理')
        for emoji in ('⛔', '⚠️', '✅'):
            await send_message.add_reaction(emoji=emoji)
        

def setup(bot: Bot):
    bot.add_cog(HentaiBusCog(bot))