import typer
import subprocess
from rich.console import Console
from rich.prompt import Prompt

from config import settings, ROOT_DIR
from src.utils import get_folders_name, make_dir, check_if_has_unziped, copy_folder, get_folders_with_same_name


console = Console()
app = typer.Typer(help=settings.TYPER.reimport_help)
target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language
raw_texts_folder_name = settings.ARGS.raw_texts_folder_name
nier_replicant_path = settings.PATHS.nier_replicant_path
originals_folder_name = settings.ARGS.originals_folder_name


@app.command('reimport-texts', help=settings.TYPER.reimport_texts_help)
def reimport_texts_command():
    console.rule(settings.CLI.reimporting_texts_rule)
    texts_path = f'{ROOT_DIR}\\texts'
    folders_name = get_folders_with_same_name(texts_path, target_language)

    if len(folders_name) > 1:
        p = Prompt()
        choice = p.ask(settings.CLI.texts_folder_choice, choices=folders_name, default=target_language)
        reimport_texts(choice, texts_path)
    else:
        reimport_texts(target_language, texts_path)


# TODO: Undo if fails
def reimport_texts(
    translated_folder: str,
    texts_folder: str
):
    ntt_exe = f'{ROOT_DIR}\\tools\\text-tool\\ntt.exe'
    build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'
    texts_path = f'{build_path}\\snow\\text'

    result_path = merge_csv_files(translated_folder, texts_folder)
    check_if_has_unziped(ntt_exe, 'text-tool', f'{ROOT_DIR}\\tools')
    copy_folder(texts_path, f'{texts_path}.{originals_folder_name}', False)

    for folder_name in get_folders_name(result_path):
        subprocess.run(
            [
                ntt_exe, '-i',
                f'{texts_path}\\{folder_name}', f'{result_path}\\{folder_name}', f'{texts_path}\\{folder_name}'
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )


def merge_csv_files(translated_folder_name, texts_folder):
    result_folder = f'{texts_folder}\\result'
    raw_folder = f'{texts_folder}\\{raw_texts_folder_name}'
    translated_folder = f'{texts_folder}\\{translated_folder_name}'

    make_dir(result_folder)

    for folder in [raw_folder, translated_folder]:
        copy_folder(folder, result_folder)

    return result_folder
