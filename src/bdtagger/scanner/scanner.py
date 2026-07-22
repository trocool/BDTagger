from pathlib import Path

from bdtagger.scanner.models import ScanResult


SUPPORTED_EXTENSIONS = {
    ".cbz",
    ".cbr",
    ".pdf",
}


class ComicScanner:
    """
    Scanner de bibliothèque BD.
    """

    def scan(
        self,
        folder: Path,
    ) -> ScanResult:
        """
        Analyse un dossier.
        """

        result = ScanResult()

        for file in folder.rglob("*"):

            if not file.is_file():
                continue

            extension = file.suffix.lower()

            match extension:

                case ".cbz":
                    result.cbz += 1

                case ".cbr":
                    result.cbr += 1

                case ".pdf":
                    result.pdf += 1

        return result
