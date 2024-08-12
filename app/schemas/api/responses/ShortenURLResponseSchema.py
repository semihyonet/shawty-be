import datetime
from typing import Optional

from app.schemas.BaseSchema import BaseSchema


class ShortenURLResponseSchema(BaseSchema):
    original_url: str
    short_url: str
    expiration_date: Optional[datetime.datetime] = None
