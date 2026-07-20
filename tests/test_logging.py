from bdtagger.utils.logging import setup_logging


def test_logging_setup():

    logger = setup_logging()

    assert logger.name == "bdtagger"
