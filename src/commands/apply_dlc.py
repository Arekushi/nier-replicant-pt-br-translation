import typer
from rich.console import Console

from config import settings, ROOT_DIR
from src.commands.extractor import extract_assets
from src.commands.install import delete_or_rename_folder


console = Console()


def apply_dlc_command(
    delete_dlc_original_folder: bool = typer.Option(
        False,
        '--delete',
        prompt=settings.TYPER.apply_delete_dlc_prompt,
        help=settings.TYPER.apply_delete_dlc_help
    )
):
    console.rule(settings.CLI.applying_dlc_rule)

    with console.status(settings.CLI.applying_dlc_status, spinner='moon'):
        apply_dlc(delete_dlc_original_folder)


def apply_dlc(delete_dlc_original_folder):
    try:
        if not extract_assets():
            raise Exception(settings.CLI.extract_assets_except)

        delete_or_rename_folder(delete_dlc_original_folder)

        console.print(settings.CLI.apply_dlc_finish)
        console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.apply_dlc_failed)
        console.print_exception(show_locals=True)
