import re

from chatgpt_wrapper import ChatGPT, AsyncChatGPT
from chatgpt_wrapper.config import Config

from src.chat_gpt.bot import Bot


class ChatGPTWrapperBot(Bot):
    def __init__(self, primary_profile):
        self.primary_profile = primary_profile
        self.config = Config()
        self.config.set('browser.debug', True)
        self.config.set('browser.provider', 'firefox')
        super().__init__(AsyncChatGPT(self.config, self.primary_profile))

    async def init(self, reset=False):
        if reset:
            await self.reset()

        await self.bot.create()
        print(f'{await self.send_message(self.get_initial_message())}')

    async def reset(self):
        await self.bot.browser.close()
        await self.bot.play.stop()

        del self.bot
        self.bot = AsyncChatGPT(self.config, self.primary_profile)

    async def send_message_impl(self, message):
        # success, response, error_message = await asyncio.wait_for(
        #     fut=self.bot.ask(re.sub(r'\s+', ' ', message).strip()),
        #     timeout=300
        # )

        success, response, error_message = await self.bot.ask(re.sub(r'\s+', ' ', message).strip())

        if success:
            return response
        else:
            raise Exception(f'Erro na resposta {error_message}')
