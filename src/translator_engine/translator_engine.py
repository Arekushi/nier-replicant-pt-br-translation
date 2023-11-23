from abc import ABC
from rich.console import Console

from config import settings
from src.utils import get_file_args


console = Console()


class TranslatorEngine(ABC):
    def __init__(self):
        pass

    async def init(self):
        pass

    async def translate_multiple_files(self, files):
        await self._translate_multiple_files(files)
    
    async def _translate_multiple_files(self, files):
        await self.init()
        
        count_all = len(files)

        for i, file in enumerate(files):
            console.print(
                settings.CLI.TRANSLATOR.translating_file
                    .replace('<file>', str(file))
                    .replace('<i>', str(i + 1))
                    .replace('<count_all>', str(count_all))
            )
            
            await self.translate_single_file(file)

    async def translate_single_file(self, file):
        return await self._translate_single_file(*get_file_args(file))

    async def _translate_single_file(self, file_path, df, columns_to_translate):
        pass
