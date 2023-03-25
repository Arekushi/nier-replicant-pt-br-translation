import typer
from rich.console import Console

from config import settings, ROOT_DIR
from src.commands.extractor import extract_assets
from src.commands.reimport import reimport_texts
from src.commands.update import update
from src.utils import remove, rename, copy_folder
from src.miscellaneous import local_has_latest_commit


console = Console()
nier_replicant_path = settings.PATHS.nier_replicant_path
target_language = settings.ARGS.target_language
originals_folder_name = settings.ARGS.originals_folder_name


def install_command(
        delete_original_folder: bool = typer.Option(
            False,
            '--delete',
            prompt=settings.TYPER.install_delete_data_prompt,
            help=settings.TYPER.install_delete_data_help
        )
):
    console.rule(settings.CLI.installing_rule)

    with console.status(settings.CLI.installing_status, spinner='moon'):
        install(delete_original_folder)


def install(delete_original_folder):
    try:
        if not extract_assets():
            raise Exception(settings.CLI.extract_assets_except)

        import_or_update()
        copy_from_data_folder()
        delete_or_rename_data_folder(delete_original_folder)

        console.print(settings.CLI.install_finish)
        console.print(settings.CLI.thanks, justify='center')
    except (FileNotFoundError, FileExistsError):
        build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'
        console.print(settings.CLI.install_failed)
        console.print(settings.CLI.error_when_copy_content.replace('build_path', build_path))
    except Exception:
        console.print(settings.CLI.install_failed)
        console.print_exception(show_locals=True)


def import_or_update():
    if not local_has_latest_commit():
        console.print(settings.CLI.install_update_version)
        update(True)
    else:
        reimport_texts(target_language, f'{ROOT_DIR}\\texts')


def delete_or_rename_data_folder(delete):
    nier_data = f'{nier_replicant_path}\\data'

    if delete:
        try:
            remove(nier_data)
        except ValueError:
            console.print(settings.CLI.error_delete_data)
    else:
        try:
            rename(nier_data, f'{nier_data}.{originals_folder_name}')
        except ValueError:
            console.print(settings.CLI.error_rename_data)


def copy_from_data_folder():
    build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'

    copy_folder(f'{nier_replicant_path}\\data\\movie', f'{build_path}\\movie')
    copy_folder(f'{nier_replicant_path}\\data\\sound', f'{build_path}\\sound')
