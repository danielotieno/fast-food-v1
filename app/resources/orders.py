from flask import Flask
from flask_restful import Resource

from app.model import orders


class Orders(Resource):
    def get(self):
        return {'orders': orders}

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
