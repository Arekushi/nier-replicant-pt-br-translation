import os
import re
import asyncio
from dotenv import load_dotenv
from pyChatGPT import ChatGPT
from src.chat_gpt import Bot


class PyChatGPTBot(Bot):
    def __init__(self):
        load_dotenv()
        super().__init__(ChatGPT(os.getenv('SESSION_TOKEN')))

    def reset(self):
        self.bot.refresh_chat_page()
        self.bot.reset_conversation()

    async def _send_message(self, message):
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            fut=loop.run_in_executor(None, self.bot.send_message, re.sub(r'\s+', ' ', message).strip()),
            timeout=300
        )

        if not response['message']:
            raise Exception('Mensagem vazia')

        return response['message']
