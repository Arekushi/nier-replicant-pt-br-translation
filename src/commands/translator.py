import typer
import asyncio
from rich import print
from rich.console import Console
from rich.prompt import Prompt

from config import settings, ROOT_DIR
from src.utils import get_all_files_from_path, has_file, has_folder
from src.chat_gpt import OpenAIBot


console = Console()
app = typer.Typer(
    callback=lambda: console.rule(settings.CLI.translating_rule),
    help=settings.TYPER.translator_help)
paths_to_translate = settings.ARGS.paths_to_translate


@app.command('translate', help=settings.TYPER.translate_ask_help)
def translate_ask():
    p = Prompt()
    choice = p.ask(settings.CLI.translator_engine_choice, choices=['ChatGPT', 'Conventional'], default='ChatGPT')

    if choice == 'ChatGPT':
        chat_gpt_translate()
    else:
        conventional_translate()


@app.command('chatgpt', help=settings.TYPER.chat_gpt_translate_help)
def chat_gpt_translate():
    from src.translator_engine import ChatGPTTranslator
    asyncio.run(translate(ChatGPTTranslator(OpenAIBot())))


@app.command('conventional', help=settings.TYPER.conventional_translate_help)
def conventional_translate():
    from src.translator_engine import ConventionalTranslator
    asyncio.run(translate(ConventionalTranslator()))


async def translate(translator):
    await translator.init()
    await translator.translate_multiple_files(get_files_to_translate())


def get_files_to_translate():
    files = []

    for path in paths_to_translate:
        full_path = f'{ROOT_DIR}\\texts\\{path}'

        if has_file(full_path):
            files.append(full_path)
        elif has_folder(full_path):
            files.extend(get_all_files_from_path(full_path))
        else:
            print(f'Não foi possível adicionar na lista para traduzir: {full_path}')

    return files
