import typer
from rich.console import Console

from config import settings, ROOT_DIR
from src.commands.extractor import extract_assets
from src.commands.reimport import reimport_texts
from src.commands.update import update
from src.utils import remove, rename, copy_folder, has_folder
from src.miscellaneous import local_has_latest_commit


console = Console()
nier_replicant_path = settings.PATHS.nier_replicant_path
target_language = settings.ARGS.target_language
originals_folder_name = settings.FOLDERS.originals_folder_name
folders_to_copy = settings.FOLDERS.folders_to_copy
texts_path = f'{ROOT_DIR}\\texts'
extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'


def install_command(
    # delete_original_folder: bool = typer.Option(
    #     False,
    #     '--delete',
    #     prompt=settings.TYPER.install_delete_data_prompt,
    #     help=settings.TYPER.install_delete_data_help
    # )
):
    console.rule(settings.CLI.installing_rule)

    with console.status(settings.CLI.installing_status, spinner='moon'):
        # install(delete_original_folder)
        new_install()


def new_install():
    try:
        copy_folder(
            f'{ROOT_DIR}\\data',
            f'{nier_replicant_path}\\data'
        )
        
        console.print(settings.CLI.install_finish)
        console.print(settings.CLI.thanks, justify='center')
    except (FileNotFoundError, FileExistsError):
        console.print(settings.CLI.install_failed)
    except Exception:
        console.print(settings.CLI.install_failed)
        console.print_exception(show_locals=True)


def install(delete_original_folder):
    try:
        if not extract_assets():
            raise Exception(settings.CLI.extract_assets_except)

        import_or_update()
        copy_from_data_folder()
        delete_or_rename_folder(delete_original_folder)

        console.print(settings.CLI.install_finish)
        console.print(settings.CLI.thanks, justify='center')
    except (FileNotFoundError, FileExistsError):
        console.print(settings.CLI.install_failed)
        console.print(
            settings.CLI.error_when_copy_content.replace('build_path', extracted_files_path)
        )
    except Exception:
        console.print(settings.CLI.install_failed)
        console.print_exception(show_locals=True)


def import_or_update():
    if not local_has_latest_commit():
        console.print(settings.CLI.install_update_version)
        update()
    else:
        reimport_texts(target_language, texts_path)


def delete_or_rename_folder(delete):
    paths = []

    for folder_name in ['data', 'dlc']:
        if has_folder(f'{nier_replicant_path}\\{folder_name}'):
            paths.append(f'{nier_replicant_path}\\{folder_name}')

    for path in paths:
        if delete:
            try:
                remove(path)
            except ValueError:
                console.print(settings.CLI.error_delete_data.replace('<path>', path))
        else:
            try:
                rename(path, f'{path}.{originals_folder_name}')
            except ValueError:
                console.print(settings.CLI.error_rename_data.replace('<path>', path))


def copy_from_data_folder():
    for folder_name in folders_to_copy:
        copy_folder(
            f'{nier_replicant_path}\\data\\{folder_name}',
            f'{extracted_files_path}\\{folder_name}'
        )
