class GeneralError(Exception):
    pass


class UploadError(GeneralError):
    pass


class MissingCmd(GeneralError):
    pass
