import typer
from rich.console import Console

from config import settings, ROOT_DIR
from .update import update

from src.miscellaneous import local_has_latest_commit
from src.utils import make_dir, copy_files, copy_folder


console = Console()
app = typer.Typer(help=settings.TYPER.INSTALL.help)

nier_path = settings.PATHS.nier_replicant_path
nier_data_path = f'{nier_path}\\data'
patch_data = settings.DEFAULT_PATHS.patch_data

backup_arc_folder_name = settings.FOLDERS.backup_arc_folder_name
backup_arc_files = settings.FILES.backup_arc
backup_path = f'{nier_data_path}\\{backup_arc_folder_name}'


@app.command('install', help=settings.TYPER.INSTALL.help)
def install_command(
    do_update: bool = typer.Option(
        True,
        '--local',
        help=settings.TYPER.INSTALL.do_update_help
    )
):
    console.rule(settings.CLI.INSTALL.rule)

    try:
        with console.status(settings.CLI.INSTALL.status, spinner='moon'):
            install(do_update)
            
            console.print(settings.CLI.INSTALL.finish)
            console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.INSTALL.failed)
        console.print_exception(show_locals=True)


def install(do_update: bool):
    do_backup_files()
    
    if (do_update):
        if not local_has_latest_commit():
            console.print(settings.CLI.INSTALL.update_version)
            update(do_download=True)
    else:
        copy_folder(patch_data, nier_data_path)


def do_backup_files():
    files_to_backup = [f'{nier_data_path}\\{arc_file}' for arc_file in backup_arc_files]
    
    make_dir(backup_path)
    copy_files(files_to_backup, backup_path)
