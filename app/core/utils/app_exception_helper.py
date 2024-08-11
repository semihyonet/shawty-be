from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions.AppExceptionCase import AppExceptionCase


async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_case,
            "context": exc.context,
        },
    )
