from functools import lru_cache

from pymongo import MongoClient
from pymongo.database import Database

from app.core.settings import get_settings


@lru_cache
def get_pymongo() -> Database:
    settings = get_settings()
    return MongoClient(settings.MONGODB_URL)[settings.MONGODB_DB_NAME]


pymongo = get_pymongo()
