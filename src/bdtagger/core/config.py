from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class BDTaggerConfig:
    """
    Configuration globale BDTagger.
    """

    library_path: Path
    language: str = "fr"
    enable_ocr: bool = False
    enable_ai: bool = False

    @classmethod
    def default(cls) -> "BDTaggerConfig":
        """
        Configuration par défaut.
        """

        return cls(
            library_path=Path.home() / "BD"
        )
