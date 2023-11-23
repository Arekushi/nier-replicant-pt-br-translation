import requests
import typer
from rich.console import Console
from contextlib import suppress

from config import settings, ROOT_DIR
from src.utils import remove, unzip_file, copy_folder, make_dir, download_file
from src.miscellaneous import update_commit_sha


console = Console()
app = typer.Typer(help=settings.TYPER.UPDATE.help)

nier_path = settings.PATHS.nier_replicant_path
nier_data_path = f'{nier_path}\\data'
patch_data_path = f'{ROOT_DIR}\\{settings.DEFAULT_PATHS.patch_data}'
data_files_urls = settings.GITHUB.data_files_urls


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
        download_updated_data()
        update_commit_sha()
            
    copy_folder(patch_data_path, nier_data_path)


def download_updated_data():
    for file_url in data_files_urls:
        download_file(file_url, patch_data_path)
    
    console.print(settings.CLI.UPDATE.download_finished)
