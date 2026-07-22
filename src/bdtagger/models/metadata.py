from dataclasses import dataclass, field


@dataclass(slots=True)
class ComicMetadata:
    """
    Métadonnées extraites d'une BD.
    """

    title: str | None = None

    series: str | None = None

    volume: str | None = None

    publisher: str | None = None

    year: str | None = None

    language: str | None = None

    writers: list[str] = field(
        default_factory=list
    )

    artists: list[str] = field(
        default_factory=list
    )

    genres: list[str] = field(
        default_factory=list
    )
