"""
This model defines a order class and it's methods
It also create data structure to store order data

"""


from flask import jsonify
import re
from datetime import date, datetime
import uuid

# Data structure to hold orders
orders = []


class FoodOrder:
    """ A class to handle actions related to orders """

    def __init__(self, ordered_by):
        self.id = uuid.uuid1()
        self.ordered_by = ordered_by
        self.date = datetime.now().replace(second=0, microsecond=0)

    def validate_date(self, order_date):
        """ Check if the given date is not the current date """
        date = datetime.strptime(order_date, '%Y-%m-%d').date()
        if date != date.today():
            return False
        return True

    def to_json(self):
        jsonified_order = {
            "id": self.id,
            "ordered_by": self.ordered_by,
            "total_cost": self.total_cost,

        }
        return jsonified_order

    def update_status(self, new_status):
        self.status = new_status

    def set_total_cost(self, cost):
        self.total_cost = cost

    def view_all_orders(self):
        """ A method to return a list of all orders """
        return jsonify({
            "message": "Successful.",
            "Orders": orders}), 200

    @staticmethod
    def get_user_order_by_email(email):
        """ Filter order by a particular user """
        user_orders = [
            order.to_json() for order in orders if order.ordered_by == email]
        return user_orders

    def get_order_by_id(self, order_id):
        """ A method to get order by id """
        for order in orders:
            if order.id == order_id:
                return order
        return False

    def update(self, order_id, ordered_by, address, order_date, total_cost):
        """ Update a specific order with a given id """
        for order in orders:

            if order.id == order_id:
                orders.remove(order)
                if self.validate_date(order_date):
                    return "Order can only have the current date"
                else:
                    self.ordered_by = ordered_by
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
