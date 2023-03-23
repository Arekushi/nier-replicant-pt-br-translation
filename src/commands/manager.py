from contextlib import suppress

import typer
import requests
from rich.console import Console

from config import settings, ROOT_DIR
from src.commands.extractor import extract_assets
from src.commands.reimport import reimport_texts, copy_data_folder
from src.utils import remove, rename, unzip_file, update_nier_path, has_folder

console = Console()
app = typer.Typer(help=settings.TYPER.manager_help)
nier_replicant_path = settings.PATHS.nier_replicant_path
target_language = settings.ARGS.target_language
originals_folder_name = settings.ARGS.originals_folder_name
master_url = settings.ARGS.master_url
master_texts_path = settings.ARGS.master_texts_path


@app.command('install', help=settings.TYPER.install_help)
def install(
        delete_original_folder: bool = typer.Option(
            False,
            '--delete',
            prompt=settings.TYPER.install_delete_data_prompt,
            help=settings.TYPER.install_delete_data_help
        )
):
    console.rule(settings.CLI.installing_rule)

    try:
        with console.status(settings.CLI.installing_status, spinner='moon'):
            if not extract_assets():
                raise Exception(settings.CLI.extract_assets_except)

            reimport_texts(target_language, f'{ROOT_DIR}\\texts')
            copy_data_folder(delete_original_folder)

        console.print(settings.CLI.install_finish)
        console.print(settings.CLI.thanks, justify='center')
    except (FileNotFoundError, FileExistsError):
        build_path = f'{nier_replicant_path}\\..\\build_assets\\rom\\pc'
        console.print(settings.CLI.install_failed)
        console.print(settings.CLI.error_when_copy_content.replace('build_path', build_path))
    except Exception:
        console.print(settings.CLI.install_failed)
        console.print_exception(show_locals=True)


@app.command('uninstall', help=settings.TYPER.uninstall_help)
def uninstall():
    console.rule(settings.CLI.uninstalling_rule)

    try:
        with console.status(settings.CLI.uninstalling_status, spinner='moon'):
            build_path = f'{nier_replicant_path}\\..\\build_assets'

            try:
                remove(build_path)
            except ValueError:
                console.print(settings.CLI.uninstall_error_delete.replace('build_path_var', build_path))

            rename(f'{nier_replicant_path}\\data.{originals_folder_name}', f'{nier_replicant_path}\\data')

        console.print(settings.CLI.uninstall_finish)
        console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.uninstall_failed)
        console.print_exception(show_locals=True)


@app.command('update', help=settings.TYPER.update_help)
def update(
        redownload: bool = typer.Option(
            True,
            '--local',
            help='NÃO baixa os textos do repositório remoto do Github e utiliza o textos locais'
        )
):
    console.rule(settings.CLI.updating_rule)

    try:
        if not has_folder(f'{nier_replicant_path}\\..\\build_assets\\rom\\pc\\snow\\text'):
            raise FileNotFoundError

        with console.status(settings.CLI.updating_status, spinner='moon'):
            if redownload:
                download_updated_master()
                reimport_texts(target_language, master_texts_path)
            else:
                reimport_texts(target_language, f'{ROOT_DIR}\\texts')

        console.print(settings.CLI.update_finish)
        console.print(settings.CLI.thanks, justify='center')
    except FileNotFoundError:
        console.print(settings.CLI.update_failed_file_not_found)
    except Exception:
        console.print(settings.CLI.update_failed)
        console.print_exception(show_locals=True)
    finally:
        with suppress(ValueError):
            remove(f'updates')


@app.command('set-nier-path', help=settings.TYPER.set_nier_path_help)
def set_nier_path():
    update_nier_path()
    console.print(settings.CLI.set_nier_path_finish)


def download_updated_master():
    request = requests.get(master_url, allow_redirects=True)
    open(f'{ROOT_DIR}\\master.zip', 'wb').write(request.content)
    unzip_file(f'{ROOT_DIR}\\master.zip', f'updates')
    remove(f'{ROOT_DIR}\\master.zip')
    console.print(settings.CLI.download_finished)
