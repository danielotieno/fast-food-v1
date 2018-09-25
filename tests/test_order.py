import unittest
import json
from flask_testing import TestCase

from app import create_app

from app.resources.orders import Orders, OrderView

ADD_ENTRY_URL = '/api/v1/orders/7'
ADD_UPDATE_URL = '/api/v1/orders/8'
GET_SINGLE_URL = '/api/v1/orders/1'
GET_ALL_URL = '/api/v1/orders'
DELETE_URL = '/api/v1/orders/2'
MODIFY_URL = '/api/v1/orders/8'


class TestBase(TestCase):
    """ Class for setup tests """

    def create_app(self):
        """ Add Test configuration """
        config_name = 'testing'
        app = create_app(config_name)

        self.create_order = json.dumps(dict(
            name="Daniel Otieno",
            status="PENDING",
            price=350,
            address="Bamburi"))
        self.client = app.test_client()
        self.client.post(
            GET_ALL_URL,
            data=self.create_order,
            content_type='application/json')

        return app


class TestOrders(TestBase):

    def test_place_an_order(self):
        """ Test to place an order """
        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_order,
            content_type='application/json')

        data = json.loads(resource.data.decode('utf-8'))
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_orders(self):
        """ Test to get all orders """

        response = self.client.get(
            GET_ALL_URL, content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_order(self):
        """ Test to fetch a specific order by id """

        response = self.client.get(
            GET_SINGLE_URL, data=json.dumps(dict(name="Daniel Otieno",
                                                 status="PENDING",
                                                 price=350,
                                                 address="Bamburi"
                                                 )), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        print(result)
        self.assertEqual(response.status_code, 200)

    def test_update_an_order(self):
        """ Test to update order status """
        response = self.client.post(GET_ALL_URL, data=self.create_order,
                                    content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

        response = self.client.put(MODIFY_URL,
                                   data=json.dumps(dict(
                                       name="Daniel Otieno",
                                       status="COMPLETE",
                                       price=350,
                                       address="Bamburi"


                                   )), content_type=("application/json"))
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        print(result)

    def test_delete_an_order(self):
        """ Test to delete an Order """
        response = self.client.delete(
            DELETE_URL, data=json.dumps(dict(order_id=2,
                                             name="Sharon Ngina",
                                             type="Pizza",
                                             price=500,
                                             address="Likoni"
                                             )), content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
