from app.core.exceptions.AppExceptionCase import AppExceptionCase


class CoreExceptions:
    class NotImplemented(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            NOT IMPLEMENTED
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)

    class ServerError(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            SERVER ERROR
            """
            status_code = 500

            context = {
                **context,
                'message': 'No response due to a problem in our server. Our team will fix the problem ASAP.'
            }
            AppExceptionCase.__init__(self, status_code, context)
