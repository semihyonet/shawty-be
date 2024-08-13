from datetime import datetime, timedelta
from typing import Optional

from beanie import Document
from pydantic import Field


class ShortenUrlModel(Document):
    original_url: str
    short_url: str
    expiration_date: Optional[datetime]
