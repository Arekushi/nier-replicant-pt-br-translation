from rich.console import Console
from dynaconf.loaders.toml_loader import write
from dynaconf.vendor.box.exceptions import BoxKeyError

from config import settings, ROOT_DIR
from src.utils import get_all_files_path


console = Console()
files_folders_required = settings.ARGS.files_folders_required
write_path = settings.CLI.write_path
nier_path_error = settings.CLI.nier_path_error
nier_path_not_found = settings.CLI.nier_path_not_found


def check_nier_path():
    try:
        if not is_a_nier_path(settings.PATHS.nier_replicant_path):
            raise Exception('Caminho para NieR: Replicant inválido!')
    except (Exception, BoxKeyError):
        update_nier_path()


def update_nier_path():
    console.print(nier_path_not_found)

    while True:
        new_path = console.input(write_path)
        if not is_a_nier_path(new_path):
            console.print(nier_path_error)

            for i, file in enumerate(files_folders_required):
                console.print(f'{i + 1}. [b]{file}[/b]')

            console.print()
            continue

        settings.update_command(write_nier_path(new_path))
        break


def write_nier_path(path):
    obj = {'PATHS': {'nier_replicant_path': path}}
    write(F'{ROOT_DIR}\\config\\.secrets.toml', obj, merge=True)
    return obj


def is_a_nier_path(path):
    files = get_all_files_path(path)
    files = [file.split('\\')[-1] for file in files]
    return set(files_folders_required).issubset(set(files))
