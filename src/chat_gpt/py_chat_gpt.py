import re
import asyncio
from pyChatGPT import ChatGPT

from config import settings
from src.chat_gpt import Bot


class PyChatGPTBot(Bot):
    def __init__(self):
        super().__init__(ChatGPT(settings.KEYS.SESSION_TOKEN))

    def reset(self):
        self.api.refresh_chat_page()
        self.api.reset_conversation()

    async def _send_message(self, message):
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            fut=loop.run_in_executor(None, self.api.send_message, re.sub(r'\s+', ' ', message).strip()),
            timeout=300
        )

        if not response['message']:
            raise Exception('Mensagem vazia')

        return response['message']
