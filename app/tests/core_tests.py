import unittest

from app.core.exceptions.AppExceptionCase import AppExceptionCase
from app.core.services.ServiceResult import ServiceResult
from app.core.utils.result_handler import result_handler


class CoreTests(unittest.TestCase):
    def test_result_handler_success(self):
        obj = {"result": "Success"}
        service_result = ServiceResult(obj.copy())

        result = result_handler(service_result)
        self.assertEqual(service_result.success, True)

        self.assertEqual(result, obj)

    def test_result_handler_exception(self):
        class CustomException(AppExceptionCase):
            pass

        service_result = ServiceResult(CustomException(500, {}))

        self.assertEqual(service_result.success, False)

        with self.assertRaises(CustomException):
            result_handler(service_result)
