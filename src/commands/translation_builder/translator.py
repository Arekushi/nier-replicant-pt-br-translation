import typer
import asyncio

from rich import print
from rich.console import Console

from config import settings, ROOT_DIR
from src.utils import get_all_files_from_path, has_file, has_folder
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
    use_google: bool = typer.Option(
        False,
        '--google',
        help=settings.TYPER.TRANSLATOR.use_chatgpt_help
    ),
    use_api: bool = typer.Option(
        False,
        '--api',
        help=settings.TYPER.TRANSLATOR.use_api_help
    )
):
    console.rule(settings.CLI.TRANSLATOR.rule)
    
    if (use_google):
        conventional_translate()
    else:
        chat_gpt_translate(use_api)


def chat_gpt_translate(use_api: bool):
    from src.translator_engine import ChatGPTTranslator
    from src.chat_gpt import OpenAIBot, UnlimitedGPT
    
    translator = ChatGPTTranslator(UnlimitedGPT() if not use_api else OpenAIBot())
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
