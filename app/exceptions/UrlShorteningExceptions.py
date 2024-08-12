from app.core.exceptions.AppExceptionCase import AppExceptionCase


class UrlShorteningExceptions:

    class ShortenedURLNotFound(AppExceptionCase):
        def __init__(self):
            status_code = 404
            context = "URL you are trying to access is not found. Please check the URL and try again."
            AppExceptionCase.__init__(self, status_code, context)

    class ShortenedURLAlreadyExist(AppExceptionCase):
        def __init__(self):
            status_code = 500
            context = "URL you are trying to create already exist. Please try it with another URL."
            AppExceptionCase.__init__(self, status_code, context)
