import pandas as pd
from config import settings, ROOT_DIR
from progress.bar import ChargingBar

from src.chat_gpt import Bot
from src.translator_engine import TranslatorEngine
from src.utils import get_file_name


max_characters_phrases = settings.CHATGPT.max_characters_phrases
translate_text_request = settings.CHATGPT.translate_text_request


class ChatGPTTranslator(TranslatorEngine):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def init(self):
        await self.bot.init()

    @staticmethod
    def group_phrases(phrases, limit):
        sublist = []
        length = 0

        for index, phrase in enumerate(phrases):
            phrase = str(phrase)

            if length + len(phrase) > limit and sublist:
                yield sublist
                sublist = []
                length = 0
            sublist.append((index, phrase))
            length += len(phrase)

        if sublist:
            yield sublist

    @staticmethod
    def update_df_with_translation(df, column, column_translated_phases):
        df = df.reset_index()
        df_temp = pd.DataFrame(column_translated_phases, columns=['index', 'text'])
        df = pd.merge(df, df_temp, on='index', how='left')
        df['text'] = df['text'].fillna('')
        df[df.columns[column - 1]] = df['text']
        df = df.drop(['index', 'text'], axis=1)

        return df

    async def _translate_single_file(self, file_path, df, columns_to_translate):
        file_name = get_file_name(file_path)

        for i, column in enumerate(columns_to_translate):
            grouped_phrases_list = list(self.group_phrases(df[df.columns[column]].tolist(), max_characters_phrases))
            bar = ChargingBar(f'{file_name} [{i + 1}/{len(columns_to_translate)}]', max=len(grouped_phrases_list))
            translated_texts_column = []

            for j, grouped_phrases in enumerate(grouped_phrases_list):
                repeated = 0
                translated_phrases = []
                message_to_send = translate_text_request.replace('[phrases]', f'{grouped_phrases}')

                while True:
                    message = await self.bot.send_message(message_to_send, repeated)
                    translated_phrases = self.bot.get_list_from_response(message) if message else grouped_phrases
                    print(f'\n[{j + 1}/{len(grouped_phrases_list)}] - {message}\n')

                    if len(grouped_phrases) != len(translated_phrases):
                        print(f'\nError. Ou a quantidade de frases é diferente ou a mensagem não está no padrão...')
                        repeated += 1
                        continue

                    break

                translated_texts_column.extend(translated_phrases)
                bar.next()

                df_temp = self.update_df_with_translation(df, column, translated_texts_column)
                temp_file_path = f'{ROOT_DIR}\\tmp\\{file_name}'
                self.save_df(df_temp, temp_file_path)

            try:
                df = self.update_df_with_translation(df, column, translated_texts_column)
            except (TypeError, ValueError):
                print('Infelizmente houve um problema ao realizar o merge, então irei salvar como backup...')
                df_temp = pd.DataFrame(translated_texts_column)
                self.save_df(df_temp, f'{ROOT_DIR}\\tmp\\error\\{file_name}')
            finally:
                bar.finish()

        self.save_df(df, file_path)
        self.write_last_line(file_path)
