from dataclasses import dataclass


@dataclass(slots=True)
class ScanResult:
    """
    Résultat d'un scan de bibliothèque.
    """

    cbz: int = 0
    cbr: int = 0
    pdf: int = 0

    @property
    def total(self) -> int:
        """
        Nombre total de fichiers trouvés.
        """

        return (
            self.cbz
            + self.cbr
            + self.pdf
        )
