import requests
import typer
from rich.console import Console
from contextlib import suppress

from config import settings, ROOT_DIR
from src.utils import remove, unzip_file, copy_folder
from src.miscellaneous import update_commit_sha


console = Console()
app = typer.Typer(help=settings.TYPER.UPDATE.help)

master_url = settings.GITHUB.master_url
master_folder_path = f'{ROOT_DIR}\\{settings.FOLDERS.master_folder_name}'

nier_path = settings.PATHS.nier_replicant_path
nier_data_path = f'{nier_path}\\data'
patch_data_path = settings.DEFAULT_PATHS.patch_data


@app.command(
    'update',
    help=settings.TYPER.UPDATE.help
)
def update_command(
        do_download: bool = typer.Option(
            True,
            '--local',
            help=settings.TYPER.UPDATE.do_download_help
        )
):
    console.rule(settings.CLI.UPDATE.rule)

    try:
        with console.status(settings.CLI.UPDATE.status, spinner='moon'):
            update(do_download)
            
            console.print(settings.CLI.UPDATE.finish)
            console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.UPDATE.failed)
        console.print_exception(show_locals=True)


def update(do_download=True):
    if do_download:
        download_updated_master()
        update_commit_sha()
            
    copy_folder(patch_data_path, nier_data_path)


def download_updated_master():
    request = requests.get(master_url, allow_redirects=False)
    
    open(f'{ROOT_DIR}\\master.zip', 'wb').write(request.content)
    unzip_file(f'{ROOT_DIR}\\master.zip', master_folder_path)
    copy_folder(f'{master_folder_path}\\{patch_data_path}', patch_data_path)
    
    with suppress(ValueError):
        remove(f'{ROOT_DIR}\\master.zip')
        remove(master_folder_path)
    
    console.print(settings.CLI.UPDATE.download_finished)
