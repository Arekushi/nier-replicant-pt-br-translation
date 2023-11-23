import typer
import subprocess
from rich.console import Console

from config.config import settings, ROOT_DIR


console = Console()

app = typer.Typer(
    help=settings.TYPER.EXTRACT_ASSETS.help
)

nier_path = settings.PATHS.nier_replicant_path

@app.command(
    'assets',
    help=settings.TYPER.EXTRACT_ASSETS.help
)
def extract_assets_command():
    console.rule(settings.CLI.EXTRACT_ASSETS.rule)
    
    with console.status(settings.CLI.EXTRACT_ASSETS.status, spinner='moon'):
        extract_assets()


def extract_assets():
    extracted_assets_path = f'{nier_path}\\..\\{settings.DEFAULT_PATHS.extracted_assets}'
    
    subprocess.run(
        [
            f'{ROOT_DIR}\\{settings.TOOLS.emil_exe}', '-i', nier_path, '-o', extracted_assets_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        encoding='utf-8'
    )
