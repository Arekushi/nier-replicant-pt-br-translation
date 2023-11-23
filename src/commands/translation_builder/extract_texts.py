import typer
import subprocess
from rich.console import Console

from config.config import settings, ROOT_DIR
from .extract_assets import extract_assets
from src.utils import get_all_files_from_path, make_dir, has_folder, get_file_name


console = Console()
app = typer.Typer(
    help=settings.TYPER.EXTRACT_TEXTS.help
)

texts_path = f'{ROOT_DIR}\\texts'
raw_texts_folder_name = settings.FOLDERS.raw_texts_folder_name


@app.command(
    'texts',
    help=settings.TYPER.EXTRACT_TEXTS.help
)
def extract_texts_command():
    console.rule(settings.CLI.EXTRACT_TEXTS.rule)
    
    with console.status(settings.CLI.EXTRACT_TEXTS.status, spinner='moon'):
        extract_texts()


def extract_texts():
    nier_replicant_path = settings.PATHS.nier_replicant_path
    extracted_assets_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_assets}'
    extracted_texts_path = f'{extracted_assets_path}\\{settings.DEFAULT_PATHS.extracted_texts}'
    
    if not has_folder(extracted_assets_path):
        extract_assets()

    for file in get_all_files_from_path(extracted_texts_path):
        raw_file_folder_path = f'{texts_path}\\{raw_texts_folder_name}\\{get_file_name(file)}'
        
        make_dir(raw_file_folder_path)

        subprocess.run(
            [
                f'{ROOT_DIR}\\{settings.TOOLS.ntt_exe}', '-e', file, raw_file_folder_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
