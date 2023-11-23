from src.miscellaneous import check_nier_path


def main():
    import typer
    import nest_asyncio
    import src.commands.translation_manager.manager as manager
    import src.commands.translation_builder.builder as builder

    app = typer.Typer()
    app.add_typer(manager.app, name='manager')
    app.add_typer(builder.app, name='builder')

    nest_asyncio.apply()
    app()


if __name__ == '__main__':
    check_nier_path()
    main()
