from flask import Flask, request
from flask_restful import Resource

from app.model import orders


class Order(Resource):

    """ Get a specific Order method """

    def get(self, order_id):
        order = next(filter(lambda x: x['order_id'] == order_id, orders), None)
        return {'order': order}, 200 if order else 404

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

    """ Upadate status of a specific order method """

    def put(self, order_id):
        data = request.get_json()
        order = next(filter(lambda x: x['order_id'] == order_id, orders), None)
        if order is None:
            order = {
                'order_id': order_id,
                'name': data['name'],
                'type': data['type'],
                'price': data['price'],
                'address': data['address']
            }
            orders.append(order)
        else:
            order.update(data)
        return order

    """ Delete a specific from the orders list """

    def delete(self, order_id):
        global orders
        orders = list(filter(lambda x: x['order_id'] != order_id, orders))
        return {'message': 'Order deleted'}
