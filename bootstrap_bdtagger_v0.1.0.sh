#!/usr/bin/env bash

set -e

echo "================================="
echo " BDTagger v0.1.0 Bootstrap"
echo "================================="

PROJECT="BDTagger"

echo "[1/10] Création des dossiers..."

mkdir -p \
.github/workflows \
docs \
tests \
bdtagger


echo "[2/10] Création des fichiers Python..."

touch \
bdtagger/__init__.py \
bdtagger/__main__.py \
bdtagger/cli.py


echo "[3/10] Création du package..."

cat > bdtagger/__init__.py <<'EOF'
"""
BDTagger
Gestionnaire open source de métadonnées BD, manga et comics.
"""

__version__ = "0.1.0"
EOF


cat > bdtagger/cli.py <<'EOF'
import typer
from rich.console import Console


app = typer.Typer(
    name="bdtagger",
    help="Gestionnaire de bibliothèque BD, manga et comics."
)


console = Console()


@app.command()
def version():
    """
    Affiche la version.
    """

    console.print(
        "BDTagger version 0.1.0"
    )


@app.command()
def hello():
    """
    Test de fonctionnement.
    """

    console.print(
        "BDTagger est opérationnel."
    )
EOF


cat > bdtagger/__main__.py <<'EOF'
from bdtagger.cli import app


if __name__ == "__main__":
    app()
EOF


echo "[4/10] Création des tests..."

cat > tests/test_cli.py <<'EOF'
from typer.testing import CliRunner

from bdtagger.cli import app


runner = CliRunner()


def test_version():

    result = runner.invoke(
        app,
        ["version"]
    )

    assert result.exit_code == 0

    assert "0.1.0" in result.stdout
EOF


echo "[5/10] Création pyproject.toml..."

cat > pyproject.toml <<'EOF'
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"


[project]
name = "bdtagger"
version = "0.1.0"
description = "Open source metadata manager for comics, manga and BD"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "typer>=0.12",
    "rich>=13",
]


[project.optional-dependencies]

dev = [
    "pytest",
    "pytest-cov",
    "ruff",
    "mypy",
]


[project.scripts]

bdtagger = "bdtagger.cli:app"


[tool.hatch.build.targets.wheel]

packages = [
    "bdtagger"
]


[tool.pytest.ini_options]

testpaths = [
    "tests"
]


[tool.mypy]

python_version = "3.11"
strict = true
EOF


echo "[6/10] Création README..."

cat > README.md <<'EOF'
# BDTagger

Gestionnaire open source de métadonnées pour :

- Bandes dessinées
- Mangas
- Comics


## Installation

Avec uv :

```bash
uv sync
