import typer
from rich.console import Console


app = typer.Typer(
    name="bdtagger",
    help="Gestionnaire de bibliothèque BD, manga et comics."
)


console = Console()


@app.command()
def version():
    """
    Affiche la version.
    """

    console.print(
        "BDTagger version 0.1.0"
    )


@app.command()
def hello():
    """
    Test de fonctionnement.
    """

    console.print(
        "BDTagger est opérationnel."
    )
