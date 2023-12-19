import typer
import subprocess
from datetime import date
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.utils import make_dir, copy_folder, merge_translated_files, \
    get_folders_name, remove, zip_folder


console = Console()
app = typer.Typer(
    help=settings.TYPER.GENERATE.help
)

translation_folder_name = settings.FOLDERS.translation_folder_name
raw_texts_folder_name = settings.FOLDERS.raw_texts_folder_name

patch_path = f'{ROOT_DIR}\\patch'
patch_source_path = settings.DEFAULT_PATHS.patch_source

arc_path = settings.TOOLS.arc_path
arc_source_path = f'{arc_path}\\source'
arc_patch_path = f'{arc_path}\\patch'
arc_data_path = f'{arc_path}\\data'

texts_path = f'{ROOT_DIR}\\texts'
tmp_path = f'{ROOT_DIR}\\{settings.FOLDERS.tmp_folder_name}'
ntt_exe = f'{ROOT_DIR}\\{settings.TOOLS.ntt_exe}'
reptext_exe = f'{ROOT_DIR}\\{settings.TOOLS.reptext_exe}'
zstd_exe = f'{ROOT_DIR}\\{settings.TOOLS.zstd_exe}'


@app.command(
    'generate',
    help=settings.TYPER.GENERATE.help
)
def generate_command():
    console.rule(settings.CLI.GENERATE.rule)
    
    try:
        with console.status(settings.CLI.GENERATE.status, spinner='moon'):
            result_folder_path = create_result_folder()
            reimport_texts(result_folder_path)
            generate_arc_files()
            
        console.print(settings.CLI.GENERATE.finish)
    except (Exception) as e:
        console.print(e)
        console.print(settings.CLI.GENERATE.failed)


def generate_arc_files():
    copy_folder(patch_source_path, arc_source_path)
    copy_folder(patch_source_path, arc_patch_path)
    
    subprocess.run(
        f'''
        copy {arc_source_path}\\title_menu {arc_path}\\patch\\title_menu
        copy {arc_source_path}\\game_over {arc_path}\patch\\game_over
        copy {arc_source_path}\\system {arc_path}\patch\\system
        {reptext_exe} -arc
        {zstd_exe} -1 -f --rm {arc_data_path}\\common -o {arc_data_path}\\common.arc
        {zstd_exe} -1 -f --rm {arc_data_path}\\info -o {arc_data_path}\\info.arc
        '''.strip().replace('\n', '&&'),
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    zip_folder('data.zip', arc_data_path, patch_path)


def reimport_texts(result_folder_path):
    for folder_name in get_folders_name(result_folder_path):
        subprocess.run(
            [
                ntt_exe, '-i',
                f'{patch_source_path}\\{folder_name}',
                f'{result_folder_path}\\{folder_name}',
                f'{patch_source_path}\\{folder_name}'
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
    
    remove(result_folder_path)


def create_result_folder():
    result_folder_path = f"{tmp_path}\\{date.today().strftime('%d_%m_%Y')}"
    raw_folder_path = f'{texts_path}\\{raw_texts_folder_name}'
    translation_folder_path = f'{texts_path}\\{translation_folder_name}'

    make_dir(result_folder_path)
    copy_folder(raw_folder_path, result_folder_path)
    merge_translated_files(result_folder_path, translation_folder_path)

    return result_folder_path
