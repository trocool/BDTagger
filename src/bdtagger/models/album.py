from dataclasses import dataclass


@dataclass(slots=True)
class Album:
    """
    Représente un album BD.
    """

    title: str

    series: str | None = None

    volume: int | None = None

    publisher: str | None = None

    year: int | None = None

    language: str = "fr"

    file_path: str | None = None
