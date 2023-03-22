import sys
import typer
import subprocess
from config import settings, ROOT_DIR

from src.utils import get_folders_name, make_dir, check_if_has_unziped, copy_folder, rename, has_folder


app = typer.Typer()
target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language
raw_texts_folder_name = settings.ARGS.raw_texts_folder_name
nier_replicant_path = settings.PATHS.nier_replicant_path


@app.command('reimport-texts')
def reimport_texts(
        folder=typer.Option(target_language, help='Folder name with your translation')
):
    ntt_exe = f'{ROOT_DIR}\\tools\\text-tool\\ntt.exe'
    build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'
    texts_path = f'{build_path}\\snow\\text'

    result_path = merge_csv_files(folder)
    check_if_has_unziped(ntt_exe, 'text-tool', f'{ROOT_DIR}\\tools')
    copy_folder(texts_path, f'{texts_path}.old', False)

    for folder_name in get_folders_name(result_path):
        subprocess.run(
            [
                ntt_exe, '-i',
                f'{texts_path}\\{folder_name}', f'{result_path}\\{folder_name}', f'{texts_path}\\{folder_name}'
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
            encoding='utf-8'
        )

    copy_data_folder()


def merge_csv_files(translated_folder_name):
    result_folder = f'{ROOT_DIR}\\texts\\result'
    raw_folder = f'{ROOT_DIR}\\texts\\{raw_texts_folder_name}'
    translated_folder = f'{ROOT_DIR}\\texts\\{translated_folder_name}'

    make_dir(result_folder)

    for folder in [raw_folder, translated_folder]:
        copy_folder(folder, result_folder)

    return result_folder


def copy_data_folder():
    nier_data = f'{nier_replicant_path}\\data'
    build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'

    try:
        copy_folder(f'{nier_replicant_path}\\data\\movie', f'{build_path}\\movie', False)
        copy_folder(f'{nier_replicant_path}\\data\\sound', f'{build_path}\\sound', False)
        rename(nier_data, f'{nier_data}.old')
    except (FileNotFoundError, FileExistsError):
        print(f'Não foi possível copiar os arquivos das pastas [movie] e [sound], faça isso manualmente para:\n'
              f'{build_path}\n'
              f'Além de mudar o nome da pasta: {nier_data} para qualquer outra coisa!')


if __name__ == '__main__':
    app()
