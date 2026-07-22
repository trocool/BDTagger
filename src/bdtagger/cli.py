from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from bdtagger.scanner import ComicScanner


app = typer.Typer(
    name="bdtagger",
    help="Gestionnaire de bibliothèque BD, manga et comics."
)


console = Console()


@app.command()
def version() -> None:
    """
    Affiche la version.
    """

    console.print(
        "BDTagger version 0.1.0"
    )


@app.command()
def hello() -> None:
    """
    Test de fonctionnement.
    """

    console.print(
        "BDTagger est opérationnel."
    )


@app.command()
def scan(
    folder: Path = typer.Argument(
        ...,
        help="Dossier contenant les BD."
    ),
) -> None:
    """
    Analyse une bibliothèque BD.
    """

    if not folder.exists():
        console.print(
            "[red]Dossier introuvable[/red]"
        )
        raise typer.Exit(
            code=1
        )

    scanner = ComicScanner()

    result = scanner.scan(folder)

    table = Table(
        title="BDTagger Scan"
    )

    table.add_column(
        "Format"
    )

    table.add_column(
        "Nombre"
    )

    table.add_row(
        "CBZ",
        str(result.cbz)
    )

    table.add_row(
        "CBR",
        str(result.cbr)
    )

    table.add_row(
        "PDF",
        str(result.pdf)
    )

    table.add_row(
        "Total",
        str(result.total)
    )

    console.print(table)
