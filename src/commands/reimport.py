import typer
import subprocess
from rich.console import Console
from rich.prompt import Prompt

from config import settings, ROOT_DIR
from src.utils import make_dir, check_and_extract_zip, copy_folder, \
    get_folders_with_same_name, merge_translated_files, get_folders_name

console = Console()
app = typer.Typer(help=settings.TYPER.reimport_help)
translation_folder_name = settings.FOLDERS.translation_folder_name
target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language

result_folder_name = settings.FOLDERS.result_folder_name
raw_texts_folder_name = settings.FOLDERS.raw_texts_folder_name
originals_folder_name = settings.FOLDERS.originals_folder_name
nier_replicant_path = settings.PATHS.nier_replicant_path

tools_path = f'{ROOT_DIR}\\tools'
texts_path = f'{ROOT_DIR}\\texts'
ntt_path = f'{ROOT_DIR}\\{settings.DEFAULT_PATHS.ntt_path}'
extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'
extracted_texts_path = f'{extracted_files_path}\\{settings.DEFAULT_PATHS.extracted_texts_path}'

@app.command('update-pt-folder')
def update_pt_folder():
    merge_translated_files(f'{texts_path}\\{target_language}', f'{texts_path}\\{translation_folder_name}')


@app.command('texts', help=settings.TYPER.reimport_texts_help)
def reimport_texts_command():
    console.rule(settings.CLI.reimporting_texts_rule)
    folders_name = get_folders_with_same_name(texts_path, translation_folder_name)

    if len(folders_name) > 1:
        p = Prompt()
        choice = p.ask(settings.CLI.texts_folder_choice, choices=folders_name, default=translation_folder_name)
        reimport_texts(choice, texts_path)
    else:
        reimport_texts(translation_folder_name, texts_path)


# TODO: Undo if fails
def reimport_texts(
    translated_folder: str,
    texts_folder: str
):
    result_path = create_result_folder(texts_folder)
    merge_translated_files(result_path, f'{texts_folder}\\{translated_folder}')
    
    check_and_extract_zip(ntt_path, tools_path)
    copy_folder(extracted_texts_path, f'{extracted_texts_path}.{originals_folder_name}', False)
    
    for folder_name in get_folders_name(result_path):
        subprocess.run(
            [
                ntt_path, '-i',
                f'{extracted_texts_path}\\{folder_name}',
                f'{result_path}\\{folder_name}',
                f'{extracted_texts_path}\\{folder_name}'
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )


def create_result_folder(texts_folder):
    result_folder = f'{texts_folder}\\{result_folder_name}'
    raw_folder = f'{texts_folder}\\{raw_texts_folder_name}'

    make_dir(result_folder)
    copy_folder(raw_folder, result_folder)

    return result_folder
