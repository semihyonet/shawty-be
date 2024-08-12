import datetime
from typing import Optional

from app.schemas.BaseSchema import BaseSchema


class ShortenURLRequestSchema(BaseSchema):
    url: str
    expiration_date: Optional[datetime.datetime] = None
