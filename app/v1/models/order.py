"""
This model defines a order class and it's methods
It also create data structure to store order data

"""

# Local imports
import re
from datetime import date, datetime
import uuid


class Order():
    """ A class to handle actions related to orders """

    def __init__(self):
        """ Data structure to hold orders """
        self.orders = []

    def validate_date(self, order_date):
        """ Check if the given date is not the current date """
        date = datetime.strptime(order_date, '%Y-%m-%d').date()
        if date != date.today():
            return False
        return True

    def create(self, user_id, food_id, address, order_date, orderedby):
        """A method for placing an order """

        # empty dictionary to hold order details created
        self.order_details = {}

        # validate order date
        if self.validate_date(order_date):
            return "order can only have a future date"
        else:
            self.order_details['user_id'] == user_id
            self.order_details['food_id'] == food_id
            self.order_details['address'] == address
            self.order_details['order_date'] == order_date
            self.order_details['date_created'] = date.today().isoformat()
            self.order_details['orderedby'] == orderedby
            self.order_details['id'] = uuid.uuid1()
            self.orders.append(self.order_details)
            return "Successfull order created"

    def view_all_orders(self):
        """ A method to return a list of all orders """
        return self.orders

    def filter_by_orderedby(self, username):
        """ Filter order by a particular user """
        new_orders = [
            order for order in self.orders if order['orderedby'] == username]
        return new_orders

    def get_order_by_id(self, order_id):
        """ A method to get order by id """
        for order in self.orders:
            if order['id'] == order_id:
                return order
        return False
