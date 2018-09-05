import unittest
import json
from flask_testing import TestCase

from app import create_app

from app.resources.orders import Order, Orders

ADD_ENTRY_URL = '/api/v1/orders/1'
GET_SINGLE_URL = '/api/v1/orders/1'
GET_ALL_URL = '/api/v1/orders'
DELETE_URL = '/api/v1/orders/1'
MODIFY_URL = '/api/v1/orders/1'


class TestBase(TestCase):

    def create_app(self):
        """ Add Test configuration """
        config_name = 'testing'
        app = create_app(config_name)

        return app


class TestOrders(TestBase):

    def test_get_all_orders(self):
        resource = self.client.get(
            GET_ALL_URL, content_type='application/json')
        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(resource.status_code, 200)


if __name__ == '__main__':
    unittest.main()
