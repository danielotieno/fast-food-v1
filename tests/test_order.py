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
        """ Test to get all orders """
        self.client.post(ADD_ENTRY_URL, data=json.dumps(dict(oder_id=1,
                                                             name="Daniel Otieno",
                                                             type="Chips",
                                                             price=300,
                                                             address="Umoja"
                                                             )), content_type='application/json')
        response = self.client.get(
            GET_ALL_URL, content_type='application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_order(self):
        """ Test to fetch a specific order by id """

        response = self.client.get(GET_SINGLE_URL,
                                   content_type='application/json')
        result = json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
