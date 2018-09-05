import unittest
import os
import json
from flask_testing import TestCase
from app import create_app


class TestBase(TestCase):

    def create_app(self):
        """ Add Test configuration """
        config_name = 'testing'
        app = create_app(config_name)

        return app


from app.resources.orders import Order, Orders


ADD_ENTRY_URL = '/api/v1/orders/1'
GET_SINGLE_URL = '/api/v1/orders/1'
GET_ALL_URL = '/api/v1/orders'
DELETE_URL = '/api/v1/orders/1'
MODIFY_URL = '/api/v1/orders/1'


if __name__ == '__main__':
    unittest.main()
