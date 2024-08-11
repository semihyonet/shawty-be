from app.core.services.ServiceResult import ServiceResult


def result_handler(result: ServiceResult):
    if not result.success:
        with result as exception:
            raise exception
    with result as result_object:
        return result_object
