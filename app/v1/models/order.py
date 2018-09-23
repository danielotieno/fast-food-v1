"""
This model defines a order class and it's methods
It also create data structure to store order data

"""


from flask import jsonify
import re
from datetime import date, datetime
import uuid

""" Data structure to hold orders """
orders = []


class Order():
    """ A class to handle actions related to orders """

    def validate_date(self, order_date):
        """ Check if the given date is not the current date """
        date = datetime.strptime(order_date, '%Y-%m-%d').date()
        if date != date.today():
            return False
        return True

    def create(self, orderedby, address, order_date, total_cost):
        """A method for placing an order """

        # validate order date
        if self.validate_date(order_date):
            return "order can only have a present date"
        else:
            self.orderedby = orderedby
            self.address = address
            self.order_date = order_date
            self.date_created = date.today().isoformat()
            self.order_id = uuid.uuid1()
            self.total_cost = total_cost
            return "Successfull order created"

    def view_all_orders(self):
        """ A method to return a list of all orders """
        return jsonify({
            "message": "Successful.",
            "Orders": orders}), 200

    def filter_by_orderedby(self, username):
        """ Filter order by a particular user """
        new_orders = [
            order for order in orders if order['orderedby'] == username]
        return new_orders

    def get_order_by_id(self, order_id):
        """ A method to get order by id """
        for order in orders:
            if order.id == order_id:
                return order
        return False

    def update(self, order_id, orderedby, address, order_date, total_cost):
        """ Update a specific order with a given id """
        for order in orders:

            if order.id == order_id:
                orders.remove(order)
                if self.validate_date(order_date):
                    return "Order can only have the current date"
                else:
                    self.orderedby = orderedby
                    self.address = address
                    self.order_date = order_date
                    self.date_created = date.today().isoformat()
                    self.order_id = uuid.uuid1()
                    self.total_cost = total_cost
                    return "Successfull order updated"
        else:
            return "No order with such id"

    def delete(self, order_id):
        """ A method to delete a specific order from a list """
        for order in orders:
            if order.id == order_id:
                orders.remove(order)
                return "Successfull order deleted"
        else:
            return "Order not found"
