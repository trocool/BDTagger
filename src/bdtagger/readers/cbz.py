from pathlib import Path
from zipfile import BadZipFile, ZipFile

from bdtagger.readers.base import ComicReader
from bdtagger.readers.exceptions import (
    InvalidArchiveError,
)

from bdtagger.readers.comicinfo import (
    parse_comicinfo,
)


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
}


class CBZReader(ComicReader):
    """
    Lecteur de fichiers CBZ.
    """

    supported_extensions = {
        ".cbz"
    }

    def read(
        self,
        file_path: Path,
    ) -> dict[str, str]:

        if not self.supports(file_path):
            raise ValueError(
                "Unsupported CBZ file"
            )

        try:
            with ZipFile(file_path) as archive:

                names = archive.namelist()

                pages = [
                    name
                    for name in names
                    if Path(name).suffix.lower()
                    in IMAGE_EXTENSIONS
                ]

                result: dict[str, str] = {
                    "file": str(file_path),
                    "pages": str(len(pages)),
                }

                if pages:
                    result["cover"] = sorted(
                        pages
                    )[0]

                if "ComicInfo.xml" in names:

                    xml = archive.read(
                        "ComicInfo.xml"
                    ).decode(
                        "utf-8"
                    )

                    result.update(
                        parse_comicinfo(xml)
                    )

                return result

        except BadZipFile as exc:

            raise InvalidArchiveError(
                str(file_path)
            ) from exc
