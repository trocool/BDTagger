import logging
import sys


LOGGER_NAME = "bdtagger"


def get_logger() -> logging.Logger:
    """
    Retourne le logger principal BDTagger.
    """

    return logging.getLogger(LOGGER_NAME)


def setup_logging(
    verbose: bool = False,
) -> logging.Logger:
    """
    Configure les logs BDTagger.

    Parameters
    ----------
    verbose:
        Active le mode debug.

    Returns
    -------
    Logger configuré.
    """

    logger = get_logger()

    level = (
        logging.DEBUG
        if verbose
        else logging.INFO
    )

    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(
            "%(asctime)s "
            "[%(levelname)s] "
            "%(name)s: "
            "%(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
