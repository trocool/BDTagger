from xml.etree import ElementTree


def parse_comicinfo(
    xml_content: str,
) -> dict[str, str]:
    """
    Parse un fichier ComicInfo.xml.

    Retourne les métadonnées principales.
    """

    root = ElementTree.fromstring(
        xml_content
    )

    metadata: dict[str, str] = {}

    fields = {
        "Title": "title",
        "Series": "series",
        "Number": "volume",
        "Publisher": "publisher",
        "Year": "year",
        "LanguageISO": "language",
        "Writer": "writer",
        "Artist": "artist",
    }

    for xml_name, key in fields.items():

        element = root.find(xml_name)

        if element is not None and element.text:
            metadata[key] = element.text.strip()

    return metadata
