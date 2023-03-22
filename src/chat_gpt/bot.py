import re
import ast
from abc import ABC
from config.config import settings


class Bot(ABC):
    def __init__(self, bot):
        self.bot = bot

    async def init(self, reset=False):
        if reset:
            self.reset()

        print(f'{await self.send_message(self.get_initial_message())}')

    def reset(self):
        pass

    async def send_message(self, message, repeated=0):
        if repeated > 0:
            print(f'Repetindo novamente... [{repeated}]')

        if repeated > 5:
            print(f'Retornando a mensagem original...')
            return ""

        try:
            return await self._send_message(message)
        except (Exception, TimeoutError) as e:
            return await self.try_again(f'Error. {e}', message, repeated)

    async def _send_message(self, message):
        pass

    async def try_again(self, err, message, repeated):
        print(f'\n{err}')
        await self.init(True)
        return await self.send_message(message, repeated + 1)

    @staticmethod
    def get_list_from_response(response):
        try:
            response = re.sub(r'\s+', ' ', response).strip()
            pattern = r'\[([\s\S]*)\]'
            match = re.search(pattern, response)
            return ast.literal_eval(match.group(0))
        except (AttributeError, SyntaxError, ValueError, TypeError, StopIteration, RuntimeError, KeyError):
            return []

    @staticmethod
    def get_initial_message():
        request_text = re.sub(r'\s+', ' ', settings.CHATGPT.request_text).strip()
        rules = [re.sub(r'\s+', ' ', rule).strip() for rule in settings.CHATGPT.rules]
        rules = '\n'.join('{}. {}'.format(*rule) for rule in enumerate(rules))
        request_text = request_text.replace('[rules]', f"\n{rules}\n")

        return request_text
