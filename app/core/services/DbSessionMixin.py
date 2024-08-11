import logging

from pymongo import MongoClient
from pymongo.database import Database

from app.core.settings import get_settings


class DBSessionMixin:
    def __init__(self, db: Database):
        self.db = db
        self.logger = logging.getLogger(__name__)
        self.settings = get_settings()
