from pathlib import Path
from zipfile import ZipFile

from bdtagger.readers import CBZReader


def create_cbz(
    path: Path,
) -> None:

    with ZipFile(
        path,
        "w",
    ) as archive:

        archive.writestr(
            "001.jpg",
            b"image"
        )

        archive.writestr(
            "ComicInfo.xml",
            """
            <ComicInfo>
                <Title>Asterix</Title>
                <Series>Asterix</Series>
                <Number>1</Number>
            </ComicInfo>
            """,
        )


def test_cbz_reader(
    tmp_path: Path,
):

    cbz = tmp_path / "test.cbz"

    create_cbz(cbz)

    reader = CBZReader()

    result = reader.read(
        cbz
    )

    assert result["pages"] == "1"
    assert result["cover"] == "001.jpg"
    assert result["title"] == "Asterix"
    assert result["series"] == "Asterix"
