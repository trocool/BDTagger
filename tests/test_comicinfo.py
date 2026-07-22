from bdtagger.readers.comicinfo import (
    parse_comicinfo,
)


def test_comicinfo_basic():

    xml = """
    <ComicInfo>
        <Title>Batman</Title>
        <Writer>Bob Kane; Bill Finger</Writer>
        <LanguageISO>fra</LanguageISO>
    </ComicInfo>
    """

    metadata = parse_comicinfo(
        xml
    )

    assert metadata.title == "Batman"

    assert metadata.language == "fr"

    assert metadata.writers == [
        "Bob Kane",
        "Bill Finger",
    ]


def test_comicinfo_namespace():

    xml = """
    <ComicInfo xmlns="test">
        <Title>Manga</Title>
    </ComicInfo>
    """

    metadata = parse_comicinfo(
        xml
    )

    assert metadata.title == "Manga"
