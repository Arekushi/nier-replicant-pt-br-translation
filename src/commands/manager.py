import typer

from config import settings
from src.commands.install import install_command
from src.commands.apply_dlc import apply_dlc_command
from src.commands.uninstall import uninstall_command
from src.commands.update import update_command

app = typer.Typer(help=settings.TYPER.manager_help)

app.command('install', help=settings.TYPER.install_help)(install_command)
# app.command('apply-dlc', help=settings.TYPER.apply_dlc_help)(apply_dlc_command)
# app.command('uninstall', help=settings.TYPER.uninstall_help)(uninstall_command)
# app.command('update', help=settings.TYPER.update_help)(update_command)
