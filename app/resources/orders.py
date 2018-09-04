from flask import Flask, request
from flask_restful import Resource

from app.model import orders


class Orders(Resource):
    def get(self):
        return {'orders': orders}

    """ Place a new Order method """

    def post(self, order_id):
        data = request.get_json()
        order = {
            'order_id': order_id,
            'name': data['name'],
            'type': data['type'],
            'price': data['price'],
            'address': data['address']
        }
        orders.append(order)
        return order, 201
