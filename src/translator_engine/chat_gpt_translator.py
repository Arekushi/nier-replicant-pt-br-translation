import pandas as pd
from config import settings, ROOT_DIR
from rich.console import Console
from progress.bar import ChargingBar

from src.chat_gpt import Bot
from src.translator_engine import TranslatorEngine
from src.utils import get_file_name, save_df, group_phrases, update_df_with_translation
from src.utils.string_utils import get_list_from_response


max_characters_phrases = settings.CHATGPT.max_characters_phrases
translate_text_request = settings.CHATGPT.translate_text_request


console = Console()


class ChatGPTTranslator(TranslatorEngine):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def init(self):
        await self.bot.init()

    async def _translate_single_file(self, file_path, df, columns_to_translate):
        file_name = get_file_name(file_path)

        for i, column in enumerate(columns_to_translate):
            grouped_phrases_list = list(group_phrases(df[df.columns[column]].tolist(), max_characters_phrases))
            bar = ChargingBar(f'{file_name} [{i + 1}/{len(columns_to_translate)}]', max=len(grouped_phrases_list))
            translated_phrases_column = []

            for j, grouped_phrases in enumerate(grouped_phrases_list):
                translated_phrases = await self.send_message_to_translate(grouped_phrases)
                translated_phrases_column.extend(translated_phrases)
                bar.next()

                df_temp = update_df_with_translation(df, column, translated_phrases_column)
                save_df(df_temp, f'{ROOT_DIR}\\{settings.DEFAULT_PATHS.tmp}\\{file_name}')

        df = update_df_with_translation(df, column, translated_phrases_column)
        save_df(df, file_path, True)
        bar.finish()

    async def send_message_to_translate(self, grouped_phrases) -> list[str]:
        message_to_send = translate_text_request.replace('<phrases>', str(grouped_phrases))
        repeated = 0

        while True:
            message_response = await self.bot.send_message(message_to_send, repeated)
            translated_phrases = get_list_from_response(message_response)
            
            if repeated >= 5:
                return grouped_phrases

            if len(grouped_phrases) != len(translated_phrases):
                console.print(settings.CLI.TRANSLATOR.wrong_response)
                repeated += 1
                continue

            break

        return translated_phrases
