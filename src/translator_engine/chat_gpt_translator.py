import pandas as pd
from config import settings, ROOT_DIR
from progress.bar import ChargingBar

from src.chat_gpt import Bot
from src.translator_engine import TranslatorEngine
from src.utils import get_file_name, write_last_line, save_df, group_phrases, update_df_with_translation
from src.utils.string_utils import get_list_from_response

max_characters_phrases = settings.CHATGPT.max_characters_phrases
translate_text_request = settings.CHATGPT.translate_text_request


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
            translated_texts_column = []

            for j, grouped_phrases in enumerate(grouped_phrases_list):
                translated_texts_column.extend(
                    (await self.send_message_to_translate(grouped_phrases, f'[{j + 1}/{len(grouped_phrases_list)}]'))
                )
                bar.next()

                df_temp = update_df_with_translation(df, column, translated_texts_column)
                temp_file_path = f'{ROOT_DIR}\\tmp\\{file_name}'
                save_df(df_temp, temp_file_path)

            try:
                df = update_df_with_translation(df, column, translated_texts_column)
            except (TypeError, ValueError):
                print('Infelizmente houve um problema ao realizar o merge, então irei salvar como backup...')
                df_temp = pd.DataFrame(translated_texts_column)
                save_df(df_temp, f'{ROOT_DIR}\\tmp\\error\\{file_name}')
            finally:
                bar.finish()

        save_df(df, file_path)
        write_last_line(file_path)

    async def send_message_to_translate(self, grouped_phrases, progress) -> list[str]:
        repeated = 0
        message_to_send = translate_text_request.replace('[phrases]', f'{grouped_phrases}')

        while True:
            message_response = await self.bot.send_message(message_to_send, repeated)
            translated_phrases = get_list_from_response(message_response) if message_response else grouped_phrases
            print(f'\n{progress} - {message_response}\n')

            if len(grouped_phrases) != len(translated_phrases):
                print(f'\nError. Ou a quantidade de frases é diferente ou a mensagem não está no padrão...')
                repeated += 1
                continue

            break

        return translated_phrases
