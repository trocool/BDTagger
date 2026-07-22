from xml.etree import ElementTree

from bdtagger.models.metadata import ComicMetadata


def clean_value(
    value: str | None,
) -> str | None:
    """
    Nettoie une valeur XML.
    """

    if value is None:
        return None

    value = value.strip()

    if not value:
        return None

    return value


def split_values(
    value: str | None,
) -> list[str]:
    """
    Convertit une liste ComicInfo.
    """

    if not value:
        return []

    separators = [
        ",",
        ";",
    ]

    result = [value]

    for separator in separators:
        result = [
            item
            for part in result
            for item in part.split(separator)
        ]

    return [
        item.strip()
        for item in result
        if item.strip()
    ]


def normalize_language(
    value: str | None,
) -> str | None:
    """
    Normalise les codes langue.
    """

    value = clean_value(value)

    if value is None:
        return None

    mapping = {
        "fra": "fr",
        "fre": "fr",
        "eng": "en",
        "jpn": "ja",
    }

    return mapping.get(
        value.lower(),
        value.lower(),
    )


def find_element(
    root: ElementTree.Element,
    name: str,
) -> ElementTree.Element | None:
    """
    Recherche un élément
    avec ou sans namespace.
    """

    for element in root.iter():

        if (
            element.tag.endswith(name)
        ):
            return element

    return None


def parse_comicinfo(
    xml_content: str,
) -> ComicMetadata:
    """
    Parse ComicInfo.xml.
    """

    root = ElementTree.fromstring(
        xml_content
    )

    def get(
        name: str,
    ) -> str | None:

        element = find_element(
            root,
            name,
        )

        if element is None:
            return None

        return clean_value(
            element.text
        )

    return ComicMetadata(
        title=get("Title"),

        series=get("Series"),

        volume=get("Number"),

        publisher=get("Publisher"),

        year=get("Year"),

        language=normalize_language(
            get("LanguageISO")
        ),

        writers=split_values(
            get("Writer")
        ),

        artists=split_values(
            get("Artist")
        ),

        genres=split_values(
            get("Genre")
        ),
    )
