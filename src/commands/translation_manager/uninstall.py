import typer
import contextlib
from rich.console import Console

from config import settings
from src.utils import remove, copy_folder, has_folder
from src.miscellaneous import write_flag_installed


console = Console()
app = typer.Typer(help=settings.TYPER.UNINSTALL.help)

nier_path = settings.PATHS.nier_replicant_path
files_to_delete = {
    '.\SK_Res\\inject\\textures': settings.FILES.textures_to_delete
}

backup_path = f'{nier_path}\\{settings.FOLDERS.backup_folder_name}'


@app.command(
    'uninstall',
    help=settings.TYPER.UNINSTALL.help
)
def uninstall_command(
    uninstall_specialk: bool = typer.Option(
        False,
        '--specialk',
        help=settings.TYPER.UNINSTALL.specialk_help
    )
):
    console.rule(settings.CLI.UNINSTALL.rule)

    try:
        with console.status(settings.CLI.UNINSTALL.status, spinner='moon'):
            uninstall(uninstall_specialk)
            
            console.print(settings.CLI.UNINSTALL.finish)
            console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.UNINSTALL.failed)
        console.print_exception(show_locals=True)


def uninstall(
    uninstall_specialk: bool
):
    if uninstall_specialk:
        files_to_delete['\\'] = settings.FILES.specialk_files
        
    if not has_folder(backup_path):
        raise Exception()
    
    copy_folder(backup_path, nier_path)
    delete_files()
    remove(backup_path)
    write_flag_installed(False)


def delete_files():
    for path, files in files_to_delete.items():
        for file in files:
            with contextlib.suppress(ValueError):
                remove(f'{nier_path}\\{path}\\{file}')
