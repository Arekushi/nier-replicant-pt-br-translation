import typer
from rich.console import Console

from config import settings
from src.utils import remove, copy_folder


console = Console()
app = typer.Typer(help=settings.TYPER.UNINSTALL.help)

nier_path = settings.PATHS.nier_replicant_path
nier_data_path = f'{nier_path}\\data'

backup_arc_folder_name = settings.FOLDERS.backup_arc_folder_name
backup_path = f'{nier_data_path}\\{backup_arc_folder_name}'


@app.command(
    'uninstall',
    help=settings.TYPER.UNINSTALL.help
)
def uninstall_command():
    console.rule(settings.CLI.UNINSTALL.rule)

    try:
        with console.status(settings.CLI.UNINSTALL.status, spinner='moon'):
            uninstall()
            
            console.print(settings.CLI.UNINSTALL.finish)
            console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.UNINSTALL.failed)
        console.print_exception(show_locals=True)


def uninstall():
    copy_folder(backup_path, nier_data_path)
    remove(backup_path)
