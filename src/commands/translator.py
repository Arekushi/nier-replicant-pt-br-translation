import asyncio
import typer
import nest_asyncio
from config import settings, ROOT_DIR
from src.utils import get_all_files_path, has_file, has_folder
from src.chat_gpt import OpenAIBot
from src.translator_engine import ChatGPTTranslator, ConventionalTranslator


app = typer.Typer()
paths_to_translate = settings.ARGS.paths_to_translate


@app.command('chatgpt-translate')
def chat_gpt_translate():
    asyncio.run(translate(ChatGPTTranslator(OpenAIBot())))


@app.command('conventional-translate')
def conventional_translate():
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
            files.extend(get_all_files_path(full_path))
        else:
            print(f'Não foi possível adicionar na lista para traduzir: {full_path}')

    return files


if __name__ == '__main__':
    nest_asyncio.apply()
    app()
