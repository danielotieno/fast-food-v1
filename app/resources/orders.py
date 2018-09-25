from flask import Flask, request
from flask_restful import Resource

from app.model import Order

orderObject = Order()


class Orders(Resource):
    """ Create method to get all orders """

    def post(self):
        """ Place a new Order method """
        data = request.get_json()
        name = data['name']
        status = data['status']
        price = data['price']
        address = data['address']

        res = orderObject.create_order(
            name,
            status,
            price,
            address)
        return res

    def get(self):
        get_all = orderObject.get_orders()
        return get_all


class OrderView(Resource):
    """ Create Request parsing interface for price """

    def get(self, order_id):
        """ Get a specific Order method """
        get_order = orderObject.get_order_by_id(order_id)
        return get_order

    def put(self, order_id):
        """ Upadate status of a specific order method """
        update_order = orderObject.update_an_order(order_id)
        return update_order

    def delete(self, order_id):
        """ Delete a specific from the orders list """
        delete_order = orderObject.delete_an_order(order_id)
        return delete_order
