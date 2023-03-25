import requests
from rich.console import Console
from dynaconf.loaders.toml_loader import write

from config import settings, ROOT_DIR


console = Console()
last_release_url = settings.GITHUB.last_release_url
current_release_version = settings.GITHUB.current_release_version
commits_url = settings.GITHUB.commits_url
current_commit_sha = settings.GITHUB.current_commit_sha


def check_relase_version():
    if not local_has_latest_release():
        console.print(
            settings.CLI.outdated_version_warning.replace('<version>', get_latest_release_version())
        )


def local_has_latest_commit():
    return current_commit_sha == get_latest_commit_sha()


def local_has_latest_release():
    return current_release_version == get_latest_release_version()


def update_commit_sha():
    obj = {'GITHUB': {'current_commit_sha': get_latest_commit_sha()}}
    write(F'{ROOT_DIR}\\config\\settings.toml', obj, merge=True)


def get_latest_commit_sha():
    response = requests.get(commits_url).json()

    if response:
        last_commit = response[0]
        return last_commit['sha']

    return None


def get_latest_release_version():
    response = requests.get(last_release_url).json()

    if response:
        return response['tag_name']

    return None
