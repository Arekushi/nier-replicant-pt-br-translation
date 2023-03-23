import re
import openai
from aiohttp import ClientSession

from config import settings
from src.chat_gpt import Bot


class OpenAIBot(Bot):
    def __init__(self):
        super().__init__(None)
        openai.organization = settings.KEYS.ORG_ID
        openai.api_key = settings.KEYS.OPENAI_API_KEY
        openai.Model.list()

    async def init(self, reset=False):
        if reset:
            await self.reset()

        openai.aiosession.set(ClientSession())

    async def reset(self):
        await openai.aiosession.get().close()

    async def _send_message(self, message):
        completion = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            temperature=0.9,
            top_p=1,
            presence_penalty=0.6,
            frequency_penalty=0,
            timeout=2*60,
            messages=[
                {
                    'role': 'user',
                    'content': re.sub(r'\s+', ' ', message)
                }
            ]
        )

        return completion.choices[0].message.content
