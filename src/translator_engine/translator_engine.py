import csv
from abc import ABC
import pandas as pd

from src.utils import get_file_name, make_dir


class TranslatorEngine(ABC):
    def __init__(self):
        pass

    async def init(self):
        pass

    async def translate_multiple_files(self, files):
        count_all = len(files)
        await self.init()

        for i, file in enumerate(files):
            print(f'Traduzindo... {file}. [{i + 1}/{count_all}]')
            await self.translate_single_file(file)

        print('Finalizando...')

    async def translate_single_file(self, file):
        if isinstance(file, tuple) or isinstance(file, list):
            file_path = file[0]
            line_index = file[1]
        else:
            file_path = file
            line_index = 0

        df = pd.read_csv(
            file_path,
            header=None,
            dtype=str,
            skipfooter=0,
            engine='python',
            keep_default_na=False,
            skiprows=line_index
        )
        columns_to_translate = self.get_columns_to_translate(file_path)

        return await self._translate_single_file(file_path, df, columns_to_translate)

    async def _translate_single_file(self, file_path, df, columns_to_translate):
        pass

    @staticmethod
    def get_df_csv(file_path, line_index=0):
        return pd.read_csv(
            file_path,
            header=None,
            dtype=str,
            skipfooter=0,
            engine='python',
            keep_default_na=False,
            skiprows=line_index
        )

    @staticmethod
    def save_df(df, file_path):
        make_dir('\\'.join(file_path.split('\\')[:-1]))
        df.to_csv(
            file_path,
            index=False,
            header=False,
            encoding='utf-8',
            quoting=csv.QUOTE_ALL
        )

    @staticmethod
    def get_columns_to_translate(file):
        file_name = get_file_name(file)

        if file_name in ['nier_text.txd.csv', 'talker_name.tnd.csv']:
            return [-8]
        elif file_name == 'InfoWindow.en.inw.csv':
            return [-1, -2]

        return [-1]

    @staticmethod
    def write_last_line(file_path):
        with open(file_path, 'a+', newline='', encoding='UTF8') as f:
            f.write('""')
