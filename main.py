import typer
import nest_asyncio

import src.commands.reimport as reimport
import src.commands.extractor as extractor
import src.commands.translator as translator

app = typer.Typer()
app.add_typer(reimport.app, name='reimport')
app.add_typer(extractor.app, name='extractor')
app.add_typer(translator.app, name='translator')


if __name__ == '__main__':
    nest_asyncio.apply()
    app()
