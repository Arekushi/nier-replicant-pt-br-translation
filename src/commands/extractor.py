import typer
import subprocess
import pandas as pd
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.utils import get_all_files_from_path, make_dir, filter_files_by_lang, \
    check_and_extract_zip, has_folder, get_folders_with_same_name, \
    get_text_columns_from_raw, get_df_from_csv, save_df, get_file_name, \
    keep_columns_by_index, get_files_without_pattern_files, duplicate_column_by_index


def unzip_tools():
    console.rule(settings.CLI.extracting_rule)
    
    check_and_extract_zip(
        f'{ROOT_DIR}\\{settings.TOOLS.emil_zip}',
        f'{ROOT_DIR}\\tools'
    )
    check_and_extract_zip(
        f'{ROOT_DIR}\\{settings.TOOLS.ntt_zip}',
        f'{ROOT_DIR}\\tools'
    )


console = Console()
app = typer.Typer(
    callback=unzip_tools,
    help=settings.TYPER.extractor_help
)

target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language
secondary_language = settings.ARGS.secondary_language

raw_texts_folder_name = settings.FOLDERS.raw_texts_folder_name
originals_folder_name = settings.FOLDERS.originals_folder_name
translation_folder_name = settings.FOLDERS.translation_folder_name

texts_path = f'{ROOT_DIR}\\texts'


@app.command('assets', help=settings.TYPER.extract_assets_help)
def extract_assets():
    nier_replicant_path = settings.PATHS.nier_replicant_path
    extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'
    
    subprocess.run(
        [
            f'{ROOT_DIR}\\{settings.TOOLS.emil_exe}', '-i', nier_replicant_path, '-o', extracted_files_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        encoding='utf-8'
    )

    return has_folder(extracted_files_path)


@app.command('texts', help=settings.TYPER.extract_texts_help)
def extract_texts():
    nier_replicant_path = settings.PATHS.nier_replicant_path
    extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'
    extracted_texts_path = f'{extracted_files_path}\\{settings.PATHS.extracted_texts_path}'

    for file in get_all_files_from_path(extracted_texts_path):
        output_path = f"{texts_path}\\{raw_texts_folder_name}\\{get_file_name(file)}"
        
        make_dir(output_path)

        subprocess.run(
            [
                f'{ROOT_DIR}\\{settings.TOOLS.ntt_exe}', '-e', file, output_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )

    create_translation_folder()


@app.command('create-translation-folder')
def create_translation_folder():
    translation_folder = f'{texts_path}\\{translation_folder_name}'
    raw_texts_files_path = f'{texts_path}\\{raw_texts_folder_name}'

    raw_files = get_all_files_from_path(raw_texts_files_path)
    source_lang_files = filter_files_by_lang(raw_files, source_language, False)
    secondary_lang_files = filter_files_by_lang(raw_files, secondary_language, False)
    without_pattern_files = get_files_without_pattern_files(raw_texts_files_path)

    if has_folder(translation_folder):
        translation_folder += f"-{len(get_folders_with_same_name(texts_path, translation_folder_name))}"

    make_dir(translation_folder)

    for source_file, secondary_file in zip(source_lang_files, secondary_lang_files):
        source_df = keep_columns_by_index(get_df_from_csv(source_file), get_text_columns_from_raw(source_file))
        secondary_df = keep_columns_by_index(get_df_from_csv(secondary_file), get_text_columns_from_raw(secondary_file))
        final_df = pd.concat([source_df, source_df, secondary_df], axis=1)

        folder_name = get_file_name(source_file, -2)
        file_name = get_file_name(source_file).replace(source_language, target_language)
        save_df(final_df, f'{translation_folder}\\{folder_name}\\{file_name}')

    for file in without_pattern_files:
        df = keep_columns_by_index(get_df_from_csv(file), [-8, -4])
        final_df = duplicate_column_by_index(df, [0])

        folder_name = get_file_name(file, -2)
        file_name = get_file_name(file)
        save_df(final_df, f'{translation_folder}\\{folder_name}\\{file_name}')
