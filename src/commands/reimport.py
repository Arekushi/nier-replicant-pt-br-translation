import typer
import subprocess
from rich.console import Console
from rich.prompt import Prompt

from config import settings, ROOT_DIR
from src.utils import make_dir, check_and_extract_zip, copy_folder, merge_translated_files, get_folders_name


def unzip_tools():
    check_and_extract_zip(
        f'{ROOT_DIR}\\{settings.TOOLS.ntt_zip}',
        f'{ROOT_DIR}\\tools'
    )
    check_and_extract_zip(
        f'{ROOT_DIR}\\{settings.TOOLS.arc_zip}',
        f'{ROOT_DIR}\\tools'
    )


console = Console()
app = typer.Typer(
    help=settings.TYPER.reimport_help,
    callback=unzip_tools
)

target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language

translation_folder_name = settings.FOLDERS.translation_folder_name
result_folder_name = settings.FOLDERS.result_folder_name
raw_texts_folder_name = settings.FOLDERS.raw_texts_folder_name
originals_folder_name = settings.FOLDERS.originals_folder_name

texts_path = f'{ROOT_DIR}\\texts'
ntt_exe = f'{ROOT_DIR}\\{settings.TOOLS.ntt_exe}'
reptext_exe = f'{ROOT_DIR}\\{settings.TOOLS.reptext_exe}'
zstd_exe = f'{ROOT_DIR}\\{settings.TOOLS.zstd_exe}'


@app.command('texts', help=settings.TYPER.reimport_texts_help)
def reimport_texts_command():
    console.rule(settings.CLI.reimporting_texts_rule)
    reimport_texts()


# TODO: Undo if fails
def reimport_texts():
    extracted_files_path = f'{settings.PATHS.nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'
    extracted_texts_path = f'{extracted_files_path}\\{settings.DEFAULT_PATHS.extracted_texts_path}'
    
    result_path = create_result_folder()
    make_dir(extracted_texts_path)
    print(extracted_texts_path)
    
    for folder_name in get_folders_name(result_path):
        subprocess.run(
            [
                ntt_exe, '-i',
                f'{extracted_texts_path}\\{folder_name}',
                f'{result_path}\\{folder_name}',
                f'{extracted_texts_path}\\{folder_name}'
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )


def create_result_folder():
    result_folder = f'{texts_path}\\{result_folder_name}'
    raw_folder = f'{texts_path}\\{raw_texts_folder_name}'

    make_dir(result_folder)
    copy_folder(raw_folder, result_folder)
    merge_translated_files(result_folder, f'{texts_path}\\{translation_folder_name}')

    return result_folder
