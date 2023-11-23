from rich.console import Console
from dynaconf.loaders.toml_loader import write
from dynaconf.vendor.box.exceptions import BoxKeyError

from config import settings, ROOT_DIR
from src.utils import get_all_files_from_path


console = Console()
tomls = settings.DEFAULT_PATHS.tomls
files_required_checkout = settings.FILES.required_checkout


def check_nier_path():
    try:
        if not is_a_nier_path(settings.PATHS.nier_replicant_path):
            raise Exception()
    except (Exception, BoxKeyError):
        update_nier_path()


def update_nier_path():
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
    
    write(F'{ROOT_DIR}\\{tomls}\\.secrets.toml', obj, merge=True)
    settings.update(obj)
    
    return obj


def is_a_nier_path(path):
    files = get_all_files_from_path(path)
    files = [file.split('\\')[-1] for file in files]
    return set(files_required_checkout).issubset(set(files))
