from abc import ABC, abstractmethod
from pathlib import Path


class ComicReader(ABC):
    """
    Interface commune des lecteurs BD.
    """

    supported_extensions: set[str] = set()

    def supports(
        self,
        file_path: Path,
    ) -> bool:
        """
        Vérifie si le lecteur accepte le fichier.
        """

        return (
            file_path.suffix.lower()
            in self.supported_extensions
        )

    @abstractmethod
    def read(
        self,
        file_path: Path,
    ) -> dict[str, str]:
        """
        Lit un fichier BD.

        Retourne un dictionnaire
        de métadonnées brutes.
        """
