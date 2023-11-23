import typer

from config import settings
from .install import install_command
from .uninstall import uninstall_command
from .update import update_command


app = typer.Typer(help=settings.TYPER.MANAGER.help)

app.command('install', help=settings.TYPER.INSTALL.help)(install_command)
app.command('uninstall', help=settings.TYPER.UNINSTALL.help)(uninstall_command)
app.command('update', help=settings.TYPER.UPDATE.help)(update_command)
