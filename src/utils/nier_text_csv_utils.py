import csv
from contextlib import suppress

import pandas as pd

from config import settings, ROOT_DIR
from src.utils import get_file_name, make_dir, get_all_files_from_path


target_language = settings.ARGS.target_language
source_language = settings.ARGS.source_language


def get_df_from_csv(file_path, line_index=0):
    df = pd.read_csv(
        file_path,
        header=None,
        dtype=str,
        skipfooter=0,
        engine='python',
        keep_default_na=False,
        skiprows=line_index
    )

    return df


def keep_columns_by_index(df, indexes):
    columns_to_keep = [df.columns[i] for i in indexes]
    return df.drop(df.columns.difference(columns_to_keep), axis=1)


def duplicate_column_by_index(df, indexes):
    columns = [df.columns[i] for i in indexes]
    return df.loc[:, columns * 2 + df.columns.difference(columns).tolist()]


def save_df(df, file_path, do_write_last_line=False):
    make_dir('\\'.join(file_path.split('\\')[:-1]))
    
    df.to_csv(
        file_path,
        index=False,
        header=False,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )
    
    if do_write_last_line:
        write_last_line(file_path)


def get_column_indexes_from_raw(file):
    file_name = get_file_name(file)
    
    for key, value in settings.COLUMNS.from_raw.items():
        if str(key) in file_name:
            return value

    return settings.COLUMNS.from_raw['default']


def get_column_indexes_to_translate(file_path):
    file_name = get_file_name(file_path)
    
    for key, value in settings.COLUMNS.to_translate.items():
        if key in file_name:
            return value

    return settings.COLUMNS.to_translate['default']


def write_last_line(file_path):
    with open(file_path, 'a+', newline='', encoding='UTF8') as f:
        f.write('""')


def get_file_args(file):
    if isinstance(file, tuple) or isinstance(file, list):
        file_path = file[0]
        line_index = file[1]
    else:
        file_path = file
        line_index = 0

    columns_to_translate = get_column_indexes_to_translate(file_path)
    df = get_df_from_csv(file_path, line_index)

    return file_path, df, columns_to_translate


def update_df_with_translation(df, column, column_translated_phrases):
    df = df.reset_index()
    df_temp = pd.DataFrame(column_translated_phrases, columns=['index', 'translated_text'])
    df = pd.merge(df, df_temp, on='index', how='left')
    df['translated_text'] = df['translated_text'].fillna('')
    df[df.columns[column + 1]] = df['translated_text']
    df = df.drop(['index', 'translated_text'], axis=1)

    return df


def filter_files_by_lang(
    files,
    lang,
    include_text_files_without_pattern=True
):
    def filter_files(file_path):
        with suppress(IndexError):
            return str(file_path).split('.')[-3] == lang

    files_filtered = list(filter(filter_files, files))

    if include_text_files_without_pattern:
        text_file_path = '\\'.join(files[0].split('\\')[:-2])
        files_filtered.extend(get_text_files_without_pattern(text_file_path))

    return files_filtered


def get_text_files_without_pattern(text_path):
    files = []

    for file_without_pattern in settings.FILES.text_without_pattern:
        files.append(
            f'{text_path}\\{file_without_pattern}'
        )

    return files


def merge_translated_files(result_path, translated_folder):
    result_all_files = filter_files_by_lang(get_all_files_from_path(result_path), source_language, True)
    translated_all_files = filter_files_by_lang(get_all_files_from_path(translated_folder), target_language, True)

    for result_file, translated_file in zip(result_all_files, translated_all_files):        
        result_df = get_df_from_csv(result_file)
        translated_df = get_df_from_csv(translated_file)
        
        result_file_columns = get_column_indexes_from_raw(result_file)
        translated_file_columns = get_column_indexes_to_translate(translated_file)

        for result_column, translated_column in zip(result_file_columns, translated_file_columns):
            result_df[result_df.columns[result_column]] = translated_df[translated_df.columns[translated_column]]

        save_df(result_df, result_file, True)
