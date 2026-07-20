from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """
    Crée un dossier s'il n'existe pas.
    """

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return path


def cache_directory() -> Path:
    """
    Retourne le dossier cache BDTagger.
    """

    return ensure_directory(
        Path.home() / ".bdtagger" / "cache"
    )
