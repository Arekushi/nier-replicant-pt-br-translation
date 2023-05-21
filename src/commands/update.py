import requests
import typer
from rich.console import Console
from contextlib import suppress

from config import settings, ROOT_DIR
from src.commands.reimport import reimport_texts
from src.utils import remove, has_folder, unzip_file
from src.miscellaneous import update_commit_sha


console = Console()
app = typer.Typer(help=settings.TYPER.update_help)
translation_folder_name = settings.FOLDERS.translation_folder_name
nier_replicant_path = settings.PATHS.nier_replicant_path
target_language = settings.ARGS.target_language
originals_folder_name = settings.FOLDERS.originals_folder_name
master_url = settings.GITHUB.master_url
master_texts_path = settings.GITHUB.master_texts_path

texts_path = f'{ROOT_DIR}\\texts'
extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'
extracted_texts_path = f'{extracted_files_path}\\{settings.DEFAULT_PATHS.extracted_texts_path}'


@app.command('update', help=settings.TYPER.update_help)
def update_command(
        download_repository: bool = typer.Option(
            True,
            '--local',
            help='NÃO baixa os textos do repositório remoto do Github e utiliza o textos locais'
        )
):
    console.rule(settings.CLI.updating_rule)

    with console.status(settings.CLI.updating_status, spinner='moon'):
        update(download_repository)


def update(download_repository: bool = True):
    try:
        if not has_folder(extracted_texts_path):
            raise FileNotFoundError

        if download_repository:
            download_updated_master()
            update_commit_sha()
            reimport_texts(translation_folder_name, master_texts_path)
        else:
            reimport_texts(translation_folder_name, texts_path)

        console.print(settings.CLI.update_finish)
        console.print(settings.CLI.thanks, justify='center')
    except FileNotFoundError:
        console.print(settings.CLI.update_failed_file_not_found)
    except Exception:
        console.print(settings.CLI.update_failed)
        console.print_exception(show_locals=True)
    finally:
        with suppress(ValueError):
            remove(f'updates')


def download_updated_master():
    request = requests.get(master_url, allow_redirects=True)
    open(f'{ROOT_DIR}\\master.zip', 'wb').write(request.content)
    unzip_file(f'{ROOT_DIR}\\master.zip', f'updates')
    remove(f'{ROOT_DIR}\\master.zip')
    console.print(settings.CLI.download_finished)
