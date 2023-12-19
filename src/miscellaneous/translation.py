import toml
from config import settings


translation_toml_file = settings.FILES.translation_toml_file


def has_installed_translation():
    nier_path = settings.PATHS.nier_replicant_path
    
    try:
        with open(f'{nier_path}\\{translation_toml_file}', 'r') as file:
            return toml.load(file)['FLAGS']['installed']
            
    except (Exception) as e:
        return False


def write_flag_installed(flag: bool):
    nier_path = settings.PATHS.nier_replicant_path
    
    with open(f'{nier_path}\\{translation_toml_file}', 'w+') as file:
        toml.dump({
            'FLAGS': {
                'installed': flag
            }
        }, file)
