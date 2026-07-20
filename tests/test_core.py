from pathlib import Path

from bdtagger.core.config import BDTaggerConfig
from bdtagger.core.paths import cache_directory
from bdtagger.models import Album


def test_default_config():

    config = BDTaggerConfig.default()

    assert isinstance(
        config.library_path,
        Path
    )

    assert config.language == "fr"


def test_album_creation():

    album = Album(
        title="Astérix"
    )

    assert album.title == "Astérix"

    assert album.language == "fr"


def test_cache_directory():

    path = cache_directory()

    assert path.exists()
