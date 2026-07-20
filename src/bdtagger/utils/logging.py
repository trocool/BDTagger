import logging


def setup_logging(
    verbose: bool = False,
) -> None:
    """
    Initialise les logs BDTagger.
    """

    level = (
        logging.DEBUG
        if verbose
        else logging.INFO
    )

    logging.basicConfig(
        level=level,
        format=(
            "%(asctime)s "
            "[%(levelname)s] "
            "%(message)s"
        ),
    )
