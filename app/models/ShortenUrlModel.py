from datetime import datetime, timedelta

from beanie import Document
from pydantic import Field


class ShortenUrlModel(Document):
    original_url: str
    short_url: str
    expiration_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=30))
