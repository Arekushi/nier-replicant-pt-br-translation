from abc import ABC
from src.utils import get_file_args


class ReviewerEngine(ABC):
    def __init__(self):
        pass

    async def init(self):
        pass

    async def review_multiple_files(self, files):
        count_all = len(files)
        await self.init()

        for i, file in enumerate(files):
            print(f'Revisando... {file}. [{i + 1}/{count_all}]')
            await self.review_single_file(file)

        print('Finalizando...')

    async def review_single_file(self, file):
        return await self._review_single_file(*get_file_args(file))

    async def _review_single_file(self, file_path, df, columns_to_translate):
        pass
