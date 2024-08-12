import unittest

import mongomock
from dotenv import load_dotenv


class CoreTests(unittest.TestCase):

    def test_counter_retrieval(self):
        # mock the settings
        load_dotenv(".env.test", override=True)

        from app.dao.CounterDao import CounterDAO

        db = mongomock.MongoClient().db

        counter_service = CounterDAO(db)
        default_value = 30

        counter = counter_service.get_counter("url_shortener", default_value)
        self.assertEqual(counter, default_value)

        counter = counter_service.get_counter("url_shortener", default_value)
        self.assertEqual(counter, default_value + 1)

        counter = counter_service.get_counter("url_shortener2", default_value)
        self.assertEqual(counter, default_value)
