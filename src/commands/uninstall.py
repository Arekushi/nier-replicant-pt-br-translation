import typer
from rich.console import Console

from config import settings
from src.utils import remove, rename, has_folder

console = Console()
app = typer.Typer(help=settings.TYPER.uninstall_help)
nier_replicant_path = settings.PATHS.nier_replicant_path
target_language = settings.ARGS.target_language
originals_folder_name = settings.FOLDERS.originals_folder_name
extracted_files_path = f'{nier_replicant_path}\\..\\{settings.DEFAULT_PATHS.extracted_files_path}'


@app.command('uninstall', help=settings.TYPER.uninstall_help)
def uninstall_command():
    console.rule(settings.CLI.uninstalling_rule)

    with console.status(settings.CLI.uninstalling_status, spinner='moon'):
        uninstall()


def uninstall():
    try:
        try:
            remove(extracted_files_path)
        except ValueError:
            console.print(
                settings.CLI.uninstall_error_delete.replace('build_path_var', extracted_files_path)
            )

        for path in ['data', 'dlc']:
            try:
                if has_folder(f'{nier_replicant_path}\\{path}.{originals_folder_name}'):
                    rename(
                        f'{nier_replicant_path}\\{path}.{originals_folder_name}',
                        f'{nier_replicant_path}\\{path}'
                    )
            except ValueError:
                console.print(
                    settings.CLI.uninstall_error_rename.replace('<name>', f'{path}.{originals_folder_name}')
                )

        console.print(settings.CLI.uninstall_finish)
        console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.uninstall_failed)
        console.print_exception(show_locals=True)
