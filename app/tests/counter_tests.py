import unittest

import mongomock

from app.dao.CounterDao import CounterDAO


class CoreTests(unittest.TestCase):

    def test_counter_retrieval(self):
        db = mongomock.MongoClient().db

        counter_service = CounterDAO(db)
        default_value = 30

        counter = counter_service.get_counter("url_shortener", default_value)
        self.assertEqual(counter, default_value)

        counter = counter_service.get_counter("url_shortener", default_value)
        self.assertEqual(counter, default_value + 1)

        counter = counter_service.get_counter("url_shortener2", default_value)
        self.assertEqual(counter, default_value)

