import typer

from config import settings, ROOT_DIR
from src.utils import check_and_extract_zip

from .extract_assets import extract_assets_command
from .extract_texts import extract_texts_command
from .make_translation_folder import make_translation_folder_command
from .translator import translate_command
from .generate import generate_command

def unzip_tools():
    for i in settings.TOOLS.tools_array:
        check_and_extract_zip(
            f'{ROOT_DIR}\\{i}',
            f'{ROOT_DIR}\\tools'
        )


app = typer.Typer(
    help=settings.TYPER.BUILDER.help,
    callback=unzip_tools
)

app.command('extract-assets', help=settings.TYPER.EXTRACT_ASSETS.help)(extract_assets_command)
app.command('extract-texts', help=settings.TYPER.EXTRACT_TEXTS.help)(extract_texts_command)
app.command('make-translation-folder', help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help)(make_translation_folder_command)
app.command('translate', help=settings.TYPER.TRANSLATOR.help)(translate_command)
app.command('generate', help=settings.TYPER.GENERATE.help)(generate_command)
