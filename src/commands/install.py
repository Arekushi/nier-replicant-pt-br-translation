from rich.console import Console

from config import settings, ROOT_DIR
from src.commands.extractor import extract_assets
from src.commands.reimport import reimport_texts
from src.commands.update import update
from src.utils import remove, rename, copy_folder, has_folder
from src.miscellaneous import local_has_latest_commit


console = Console()

target_language = settings.ARGS.target_language
originals_folder_name = settings.FOLDERS.originals_folder_name
folders_to_copy = settings.FOLDERS.folders_to_copy
texts_path = f'{ROOT_DIR}\\texts'


def install_command():
    console.rule(settings.CLI.installing_rule)

    with console.status(settings.CLI.installing_status, spinner='moon'):
        install()


def install():
    try:
        import_or_update()

        console.print(settings.CLI.install_finish)
        console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.install_failed)
        console.print_exception(show_locals=True)


def import_or_update():
    if not local_has_latest_commit():
        console.print(settings.CLI.install_update_version)
        update()
    else:
        reimport_texts()
