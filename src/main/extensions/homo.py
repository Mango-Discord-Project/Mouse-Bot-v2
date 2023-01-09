from re import match

from discord import Option, Embed, commands, Message, Cog

from packages.namespace_pack import *
from packages import core, config_mixin
from packages.embed_tools import generate_embed

class HomoCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    HomoSlashCommandGroup = SlashCommandGroup('homo', **config_mixin.get_setting('command.homo.base'))
    
    @HomoSlashCommandGroup.command()
    async def fuck(self, ctx: ApplicationContext, message: str, anonymous: bool = False):
        channel = self.bot.get_channel(1023839492601282634)
        
        embed = Embed(title = 'Fuck Me, Fuck You, Fuck Everyone and Everything',
                      description = message.replace('\\n', '\n'),
                      color = 0x2f3136)
        if not anonymous:
            embed.set_author(name = ctx.author,
                             icon_url = ctx.author.avatar.url)
        
        await ctx.respond('Send Success', ephemeral=True)
        await channel.send(embed=embed)
    
    @commands.message_command(**config_mixin.get_setting('command.homo.base'))
    async def good_sentences(self, ctx: ApplicationContext, message: Message):
        channel = self.bot.get_channel(1038818486564163704)
        embed = generate_embed(title = 'Good Sentences',
                               description = message.content,
                               author = message.author)
        files = []
        for attachment in message.attachments:
            files.append(await attachment.to_file())
        
        await ctx.respond('Send Success', ephemeral=True)
        await channel.send(embed=embed, files=files)

    # @Cog.listener()
    # async def on_message(self, message: Message):
    #     if message.author == self.bot:
    #         return
    #     if message.guild.id != 961237448552218675:
    #         return
    #     content = message.content
    #     if message.channel.id == 994927863415439410:
    #         print(f'{content = }')
    #         if match(r'\d{6}', content):
    #             await message.reply(f'> https://nhentai.net/g/{message.content}/', mention_author=False)

def setup(bot: Bot):
    bot.add_cog(HomoCog(bot))