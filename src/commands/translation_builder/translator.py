import typer
import asyncio

from rich import print
from rich.console import Console

from config import settings, ROOT_DIR
from src.utils import get_all_files_from_path, has_file, has_folder
from src.chat_gpt import OpenAIBot, PyChatGPTBot, UnlimitedGPT
from src.translator_engine import TranslatorEngine


console = Console()
app = typer.Typer(
    help=settings.TYPER.TRANSLATOR.help
)

paths_to_translate = settings.ARGS.paths_to_translate
texts_path = f'{ROOT_DIR}\\texts'

@app.command(
    'translate',
    help=settings.TYPER.TRANSLATOR.help
)
def translate_command(
    use_chatgpt: bool = typer.Option(
        True,
        '--google',
        help=settings.TYPER.TRANSLATOR.use_chatgpt_help
    )
):
    console.rule(settings.CLI.TRANSLATOR.rule)
    
    if (use_chatgpt):
        chat_gpt_translate()
    else:
        conventional_translate()


def chat_gpt_translate():
    from src.translator_engine import ChatGPTTranslator
    
    translator = ChatGPTTranslator(UnlimitedGPT())
    asyncio.run(translate(translator))


def conventional_translate():
    from src.translator_engine import ConventionalTranslator
    
    translator = ConventionalTranslator()
    asyncio.run(translate(translator))


async def translate(translator: TranslatorEngine):
    await translator.translate_multiple_files(get_files_to_translate())


def get_files_to_translate():
    files = []

    for path in paths_to_translate:
        full_path = f'{texts_path}\\{path}'

        if has_file(full_path):
            files.append(full_path)
        elif has_folder(full_path):
            files.extend(get_all_files_from_path(full_path))
        else:
            print(
                settings.CLI.TRANSLATOR.file_failed.replace('<file>', full_path)
            )

    return files
