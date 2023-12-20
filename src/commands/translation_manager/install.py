import typer
import zipfile
from rich.console import Console

from config import settings, ROOT_DIR

from src.miscellaneous import local_has_latest_commit
from src.utils import make_dir, copy_file, download_file, unzip_file, remove
from src.miscellaneous import has_special_k, has_installed_translation, \
    write_flag_installed, update_commit_sha


console = Console()
app = typer.Typer(help=settings.TYPER.INSTALL.help)

nier_path = settings.PATHS.nier_replicant_path
tmp_path = f'{ROOT_DIR}\\{settings.FOLDERS.tmp_folder_name}'
specialk_zip = f'{ROOT_DIR}\\{settings.FILES.special_k_zip}'

files_to_update_urls = settings.GITHUB.files_to_update_urls
files_to_install = settings.FILES.to_install
files_to_backup = settings.FILES.to_backup

backup_path = f'{nier_path}\\{settings.FOLDERS.backup_folder_name}'


@app.command('install', help=settings.TYPER.INSTALL.help)
def install_command(
    do_update: bool = typer.Option(
        False,
        '--update',
        help=settings.TYPER.INSTALL.do_update_help
    ),
    install_specialk: bool = typer.Option(
        False,
        '--specialk',
        help=settings.TYPER.INSTALL.specialk_help
    ),
    force_update: bool = typer.Option(
        False,
        '--force',
        help=settings.TYPER.INSTALL.force_update_help
    )
):
    typer_state = 'INSTALL' if not has_installed_translation() else 'UPDATE'
    console.rule(settings.CLI[typer_state].rule)

    try:
        with console.status(settings.CLI[typer_state].status, spinner='moon'):
            install(do_update, install_specialk, force_update)
            
            console.print(settings.CLI[typer_state].finish)
            console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI[typer_state].failed)
        console.print_exception(show_locals=True)


def install(
    do_update = False,
    install_specialk = False,
    force_update = False
):
    if install_specialk:
        if not has_special_k(nier_path):
            console.print(settings.CLI.INSTALL.specialk)
            install_special_k()
    
    if not has_installed_translation():
        console.print(settings.CLI.INSTALL.backup)
        backup_files()
    
    if do_update:
        if force_update or (not local_has_latest_commit()):
            console.print(settings.CLI.INSTALL.update_version)
            files = download_updated_files()
            update_commit_sha()
            update_files_to_install(files)
    
    for file_path, dest in files_to_install:
        try:
            new_file_path = copy_file(file_path, f'{nier_path}\\{dest}')
        except:
            new_file_path = copy_file(f'{ROOT_DIR}\\{file_path}', f'{nier_path}\\{dest}')
        
        if zipfile.is_zipfile(new_file_path):
            unzip_file(new_file_path, f'{nier_path}\\{dest}')
            remove(new_file_path)
    
    write_flag_installed(True)


def backup_files():
    try:
        for file in files_to_backup:
            folder_name = '\\'.join(file.split('\\')[:-1])
            folder_inside_backup_path = f'{backup_path}\\{folder_name}'
            make_dir(folder_inside_backup_path)
            copy_file(f'{nier_path}\\{file}', folder_inside_backup_path)
    except FileNotFoundError:
        console.print(
            settings.CLI.INSTALL.backup_file_failed
        )


def update_files_to_install(files):
    for i in range(len(files_to_install)):
        files_to_install[i][0] = files[i]


def download_updated_files():
    files = list()
    
    for file_url, tmp_folder in files_to_update_urls:
        file_path = download_file(file_url, f'{tmp_path}\\{tmp_folder}')
        files.append(file_path)
    
    console.print(settings.CLI.UPDATE.download_finished)
    return files


def install_special_k():
    specialk_zip_path = copy_file(specialk_zip, nier_path)
    unzip_file(specialk_zip_path, nier_path)
    remove(specialk_zip_path)
