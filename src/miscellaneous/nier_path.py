from rich.console import Console
from dynaconf.loaders.toml_loader import write
from dynaconf.vendor.box.exceptions import BoxKeyError

from config import settings, ROOT_DIR
from src.utils import get_all_files_from_path
from string import ascii_lowercase as alc


console = Console()
tomls = settings.DEFAULT_PATHS.tomls
secrets_file_name = settings.FILES.secrets_file_name

files_required_checkout = settings.FILES.required_checkout
special_k_files_checkout = settings.FILES.specialk_files

nier_folder_name = settings.FOLDERS.nier_folder_name
nier_possible_paths = settings.DEFAULT_PATHS.nier_possible_paths


def check_nier_path():
    try:
        if not is_a_nier_path(settings.PATHS.nier_replicant_path):
            raise Exception()
    except (Exception, BoxKeyError):
        nier_path = find_nier_path()
        
        if nier_path:
            write_nier_path(nier_path)
        else:
            input_nier_path()


def input_nier_path():
    console.print(settings.CLI.NIERPATH.not_found)

    while True:
        new_path = console.input(settings.CLI.NIERPATH.write_path)
        
        if not is_a_nier_path(new_path):
            console.print(settings.CLI.NIERPATH.error)

            for i, file in enumerate(files_required_checkout):
                console.print(f'{i + 1}. [b]{file}[/b]')

            console.print()
            continue
        else:
            write_nier_path(new_path)
            break


def write_nier_path(path):
    obj = {
        'PATHS': {
            'nier_replicant_path': path
        }
    }
    
    write(F'{ROOT_DIR}\\{tomls}\\{secrets_file_name}', obj, merge=True)
    settings.update(obj)
    
    return obj


def find_nier_path():
    for volume in alc:
        for possible_path in nier_possible_paths:
            full_path = f'{volume.upper()}:\\{possible_path}\\{nier_folder_name}'
            
            if is_a_nier_path(full_path):
                return full_path
    
    return None


def has_special_k(path):
    files = get_all_files_from_path(path)
    files = [file.split('\\')[-1] for file in files]
    return set(special_k_files_checkout).issubset(set(files))


def is_a_nier_path(path):
    files = get_all_files_from_path(path)
    files = [file.split('\\')[-1] for file in files]
    return set(files_required_checkout).issubset(set(files))
