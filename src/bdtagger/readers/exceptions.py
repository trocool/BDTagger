class ReaderError(Exception):
    """
    Exception de base des lecteurs BD.
    """


class UnsupportedFormatError(ReaderError):
    """
    Format de fichier non supporté.
    """


class InvalidArchiveError(ReaderError):
    """
    Archive BD invalide ou corrompue.
    """
