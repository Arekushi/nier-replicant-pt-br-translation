import re
from abc import ABC
from rich.console import Console
from config.config import settings


console = Console()


class Bot(ABC):
    def __init__(self, api):
        self.api = api

    async def init(self, reset=False):
        if reset:
            self.reset()

        await self.send_message(
            self.get_initial_message()
        )

    def reset(self):
        pass

    async def send_message(self, message, repeated=0, do_print=True):
        if repeated > 0:
            console.print(
                settings.CLI.TRANSLATOR.repeted
                    .replace('<i>', str(repeated))
            )

        if repeated >= 5:
            console.print(settings.CLI.TRANSLATOR.null_return)
            return None

        try:
            response = await self._send_message(message)
            
            if do_print:
                console.print(f'\n[bold white on blue]CHATGPT:[/] {response}\n')
            
            return response
        except (Exception, TimeoutError) as e:
            print(e)
            return await self.try_again(message, repeated)

    async def _send_message(self, message):
        pass

    async def try_again(self, message, repeated):
        await self.init(True)
        return await self.send_message(message, (repeated + 1))

    @staticmethod
    def get_initial_message():
        request_text = re.sub(r'\s+', ' ', settings.CHATGPT.request_text).strip()
        rules = [re.sub(r'\s+', ' ', rule).strip() for rule in settings.CHATGPT.rules]
        rules = '\n'.join('{}. {}'.format(*rule) for rule in enumerate(rules))
        request_text = request_text.replace('<rules>', f'\n{rules}\n')

        return request_text
