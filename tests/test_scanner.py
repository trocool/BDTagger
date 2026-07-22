from pathlib import Path

from bdtagger.scanner import ComicScanner


def test_scanner_detects_files(
    tmp_path: Path,
):

    (tmp_path / "album1.cbz").touch()

    (tmp_path / "album2.cbr").touch()

    (tmp_path / "album3.pdf").touch()

    scanner = ComicScanner()

    result = scanner.scan(
        tmp_path
    )

    assert result.cbz == 1
    assert result.cbr == 1
    assert result.pdf == 1

    assert result.total == 3


def test_scanner_ignores_unknown_files(
    tmp_path: Path,
):

    (tmp_path / "image.jpg").touch()

    scanner = ComicScanner()

    result = scanner.scan(
        tmp_path
    )

    assert result.total == 0
