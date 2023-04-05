from src.miscellaneous import check_nier_path, check_relase_version


def main():
    import typer
    import nest_asyncio
    import src.commands.reimport as reimport
    import src.commands.extractor as extractor
    import src.commands.translator as translator
    import src.commands.manager as manager

    app = typer.Typer()
    app.add_typer(reimport.app, name='reimport')
    app.add_typer(extractor.app, name='extractor')
    app.add_typer(translator.app, name='translator')
    app.add_typer(manager.app, name='manager')

    nest_asyncio.apply()
    app()


def check():
    check_relase_version()
    check_nier_path()


if __name__ == '__main__':
    # check()
    main()
