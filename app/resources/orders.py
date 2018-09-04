from flask import Flask, request
from flask_restful import Resource, reqparse


from app.model import orders


class Order(Resource):

    """ Create Request parsing interface for price """

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

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

        data = Order.parser.parse_args()

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
