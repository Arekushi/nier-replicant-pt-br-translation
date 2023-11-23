import re
import asyncio
from UnlimitedGPT import ChatGPT

from config import settings
from src.chat_gpt import Bot


class UnlimitedGPT(Bot):
    def __init__(self):
        super().__init__(ChatGPT(settings.KEYS.SESSION_TOKEN))

    def reset(self):
        self.api.reset_conversation()

    async def _send_message(self, message):
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            fut=loop.run_in_executor(None, self.api.send_message, re.sub(r'\s+', ' ', message).strip()),
            timeout=300
        )

        if not response.response:
            raise Exception({
                'error': 'Empty Message'
            })

        return response.response
