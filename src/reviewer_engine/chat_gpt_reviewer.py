from progress.bar import ChargingBar

from config import settings, ROOT_DIR
from src.chat_gpt import Bot
from src.reviewer_engine import ReviewerEngine
from src.utils import get_file_name, group_phrases, update_df_with_translation, save_df, get_bool_from_response

max_characters_phrases = settings.CHATGPT.max_characters_phrases
simple_review_request_text = settings.CHATGPT.simple_review_request_text


class ChatGPTReviewer(ReviewerEngine):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def init(self):
        await self.bot.init()

    async def _review_single_file(self, file_path, df, columns_to_translate):
        file_name = get_file_name(file_path)

        for i, column in enumerate(columns_to_translate):
            grouped_phrases_list = list(group_phrases(df[df.columns[column]].tolist(), max_characters_phrases))
            bar = ChargingBar(f'{file_name} [{i + 1}/{len(columns_to_translate)}]', max=len(grouped_phrases_list))

            for j, grouped_phrases in enumerate(grouped_phrases_list):
                response = await self.send_message_to_review(grouped_phrases)

                if response:
                    df_temp = update_df_with_translation(df, column, grouped_phrases)
                    temp_file_path = f'{ROOT_DIR}\\tmp\\{file_name}'
                    save_df(df_temp, temp_file_path)

    async def send_message_to_review(self, grouped_phrases):
        message_to_send = simple_review_request_text.replace('[phrases]', f'{grouped_phrases}')
        message_response = await self.bot.send_message(message_to_send)
        return get_bool_from_response(message_response)
