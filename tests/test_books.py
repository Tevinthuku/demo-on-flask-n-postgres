"""Tests for books records"""
import json
import unittest

from app import create_app
from config import app_config
from app.api.v2.models.db import init_db

class BaseTestClass(unittest.TestCase):
    """
    Setting up tests
    """

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.DB_URL = app_config['TEST_DB_URL'] 
        init_db(self.DB_URL)

        self.post_book = {"name": "A Game Of Thrones",
                               "author": "George RR Martins"}


    # tear down tests  
                                   
    def tearDown(self):
        """Tperform final cleanup after tests run"""
        self.app.testing = False
        init_db(self.DB_URL) 


class TestBooksEndpoints(BaseTestClass):

    def test_on_successful_book_insertion_to_db(self):
        self.client.post("api/v2/book",
                         data=json.dumps(self.post_book),
                         content_type="application/json")
        response = self.client.post("api/v2/book",
                                    data=json.dumps(self.post_book),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], 201)
  