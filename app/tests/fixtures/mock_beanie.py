from contextlib import contextmanager
from unittest.mock import patch

import mongomock
from beanie import init_beanie
from pymongo.database import Database

from app.models import CounterModel, ShortenUrlModel


@contextmanager
def mock_beanie(db_name: str = "db"):
    try:
        with patch(
                "mongomock.database.Database.command",
                new=lambda *args, **kwargs: {"version": "4.4.0"},
        ):
            with patch(
                    "mongomock.database.Database.list_collection_names"
            ) as list_collections:
                list_collections.return_value = [db_name]
                client = mongomock.MongoClient()
                db: Database = client[db_name]
                init_beanie(
                    database=db,
                    document_models=[CounterModel, ShortenUrlModel],
                )
                yield
    finally:
        pass

    return
