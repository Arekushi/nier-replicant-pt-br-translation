from pathlib import Path
from dynaconf import Dynaconf


settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        './toml/cli.toml',
        './toml/typer.toml',
        './toml/chat-gpt.toml',
        './toml/settings.toml',
        './toml/.secrets.toml'
    ],
)

ROOT_DIR = Path(__file__).parent.parent

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
