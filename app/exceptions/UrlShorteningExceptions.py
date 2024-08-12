from app.core.exceptions.AppExceptionCase import AppExceptionCase


class UrlShorteningExceptions:

    class ShortenedURLNotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            status_code = 404

            AppExceptionCase.__init__(self, status_code, context)
    class ShortenedURLAlreadyExist(AppExceptionCase):
        def __init__(self, context: dict = None):
            status_code = 500

            AppExceptionCase.__init__(self, status_code, context)
