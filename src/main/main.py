from os import path, listdir

from dotenv import dotenv_values

from packages import core
from packages.namespace_pack import *

class Bot(core.BotBase):
    def __init__(self):
        self.log('Bot object build')
        super().__init__()
        
        self.load_extensions(self.get_extension_list())
    
    async def on_ready(self):
        self.log('Bot is ready')

if __name__ == '__main__':
    bot = Bot()
    environ = dotenv_values(path.join(*('.', 'src', 'main', 'config', '.env')))
    bot.run(environ['TOKEN'])