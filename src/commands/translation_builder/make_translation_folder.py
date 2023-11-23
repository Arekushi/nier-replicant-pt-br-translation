import typer
import pandas as pd
from datetime import date
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.utils import get_all_files_from_path, make_dir, filter_files_by_lang, \
    has_folder, get_column_indexes_from_raw, get_df_from_csv, \
    save_df, get_file_name, keep_columns_by_index, get_text_files_without_pattern, duplicate_column_by_index


console = Console()
app = typer.Typer(
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help
)

target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language
secondary_language = settings.ARGS.secondary_language

texts_path = f'{ROOT_DIR}\\texts'


@app.command(
    'make-translation-folder',
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help
)
def make_translation_folder_command():
    console.rule(settings.CLI.MAKE_TRANSLATION_FOLDER.rule)
    
    with console.status(settings.CLI.MAKE_TRANSLATION_FOLDER.status, spinner='moon'):
        create_translation_folder()


def create_translation_folder():
    raw_texts_files_path = f'{texts_path}\\{settings.FOLDERS.raw_texts_folder_name}'
    translation_folder = f'{texts_path}\\{settings.FOLDERS.translation_folder_name}'
    
    raw_files = get_all_files_from_path(raw_texts_files_path)
    source_lang_files = filter_files_by_lang(raw_files, source_language, False)
    secondary_lang_files = filter_files_by_lang(raw_files, secondary_language, False)
    without_pattern_files = get_text_files_without_pattern(raw_texts_files_path)

    if has_folder(translation_folder):
        translation_folder += f"_{date.today().strftime('%d_%m_%Y')}"

    make_dir(translation_folder)

    for source_file, secondary_file in zip(source_lang_files, secondary_lang_files):
        source_df = keep_columns_by_index(
            get_df_from_csv(source_file),
            get_column_indexes_from_raw(source_file)
        )
        
        secondary_df = keep_columns_by_index(
            get_df_from_csv(secondary_file),
            get_column_indexes_from_raw(secondary_file)
        )
        
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
