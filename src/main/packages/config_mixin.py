import json
import tomllib
from os import listdir, path

__all__ = ['get_setting', 'get_bot_config']

base_path = ['.', 'src', 'main']

with open(path.join(*[*base_path, 'config', 'commands', 'settings.json'])) as file:
    command_setting = json.load(file)

lang_premix = {}
_lang_base_path = [*base_path, 'config', 'lang']

for filename in listdir(path.join(*_lang_base_path)):
    lang = filename.removesuffix('.json')
    with open(path.join(*[*_lang_base_path, filename]), encoding='utf8') as file:
        _d = json.load(file)
    for k, v in _d.items():
        key, type = k.split('.')
        key, type = '.'.join(key), f'{type}_localizations'
        
        lang_premix.setdefault(key, {})
        lang_premix[key].setdefault(type, {})
        
        # lang_premix[key] = lang_premix.get(key, {})
        # lang_premix[key][type] = lang_premix.get(type, {})
        
        lang_premix[key][type] = v


def get_setting(key: str = 'command.base') -> dict:
    return command_setting.get(key, {}) | lang_premix.get(key, {})

def get_bot_config():
    with open(path.join('.', 'src', 'main', 'config', 'bot.toml'), 'rb') as file:
        return tomllib.load(file)