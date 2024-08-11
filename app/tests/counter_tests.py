import unittest
from unittest.mock import patch

import mongomock



class CoreTests(unittest.TestCase):

    @patch('app.core.settings.get_settings')
    def test_counter_retrieval(self, get_settings):
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

