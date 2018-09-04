from flask import Flask
from flask_restful import Resource

from app.model import orders


class Order(Resource):

    """ Get a specific Order method """

    def get(self, order_id):
        for order in orders:
            if order['order_id'] == order_id:
                return order
        return {'order': None}, 404

    """ Place a new Order method """

    def post(self, order_id):
        order = {
            'order_id': 3,
            'name': 'Peter Kamotho',
            'type': 'Pizza',
            'price': 650.00,
            'address': 'Buruburu'
        }
        orders.append(order)
        return order, 201
