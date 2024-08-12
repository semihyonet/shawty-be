import datetime
from typing import Optional

from app.schemas.BaseSchema import BaseSchema


class AppExceptionResponseSchema(BaseSchema):
    error: str
    exception: str
    message: Optional[str]
