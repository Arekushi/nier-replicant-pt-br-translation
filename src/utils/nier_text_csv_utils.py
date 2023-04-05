import csv
from contextlib import suppress

import pandas as pd

from config import settings
from src.utils import get_file_name, make_dir


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


def get_only_texts_column(file_path, df, indexes=()):
    columns_to_keep = [df.columns[i] for i in indexes or get_text_columns(file_path)]
    return df.drop(df.columns.difference(columns_to_keep), axis=1)


def save_df(df, file_path):
    make_dir('\\'.join(file_path.split('\\')[:-1]))
    df.to_csv(
        file_path,
        index=False,
        header=False,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )


def get_text_columns(file):
    file_name = get_file_name(file)

    if file_name in ['nier_text.txd.csv', 'talker_name.tnd.csv']:
        return [-8]
    elif file_name == 'InfoWindow.en.inw.csv':
        return [-1, -2]

    return [-1]


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

    df = get_df_from_csv(file_path, line_index)
    columns_to_translate = get_text_columns(file_path)

    return file_path, df, columns_to_translate


def update_df_with_translation(df, column, column_translated_phases):
    df = df.reset_index()
    df_temp = pd.DataFrame(column_translated_phases, columns=['index', 'text'])
    df = pd.merge(df, df_temp, on='index', how='left')
    df['text'] = df['text'].fillna('')
    df[df.columns[column - 1]] = df['text']
    df = df.drop(['index', 'text'], axis=1)

    return df


def filter_files_by_lang(
        files,
        lang,
        include_files_without_pattern=True
):
    def filter_file(file_path):
        with suppress(IndexError):
            return str(file_path).split('.')[-3] == lang

    result = list(filter(filter_file, files))

    if include_files_without_pattern:
        for file_without_pattern in settings.ARGS.files_without_pattern:
            result.extend([
                f'{files[0]}\\..\\{file_without_pattern.file}'
            ])

    return result
