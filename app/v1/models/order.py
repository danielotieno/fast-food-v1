"""
This model defines a order class and it's methods
It also create data structure to store order data

"""
# Local imports
import re
from datetime import date, datetime
import uuid


class Orders():
    """ A class to handle actions related to orders """

    def __init__(self):
        """ Data structure to hold orders """
        self.orders = []

    def existing_order(self, name, orderedby):
        """A method to check if a user already has already placed the order"""
        for order in self.orders:
            if order['name'] == name and order['orderedby'] == orderedby:
                return True
        else:
            return False

    def validate_date(self, order_date):
        """ Check if the given date is less than the current date """
        date = datetime.strptime(order_date, '%Y-%m-%d').date()
        if date < date.today():
            return False
        return True

    def create(self, name, status, address, order_date, orderedby):
        """A method for placing an order """

        # empty dictionary to hold order details created
        self.order_details = {}

        if self.existing_order(name, orderedby):
            return "order exists"
        else:
            # validate order date
            if not self.validate_date(order_date):
                return "order can only have a future date"
            else:
                self.order_details['name'] == name
                self.order_details['status'] == 'PENDING'
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

    def update(self, order_id, name, status, address, order_date, orderedby):
        """ Update a specific order with a given id """
        for order in self.orders:
            if order['id'] == order_id:
                self.orders.remove(order)
                if self.existing_order(name, orderedby):
                    return "Order cannot be updated, a similar order exists"
                else:
                    if not self.validate_date(order_date):
                        return "Order can only have a future date"
                    else:
                        order['name'] = name
                        order['status'] = 'PENDING'
                        order['address'] = address
                        order['order_date'] = order_date
                        order['date_created'] = date.today().isoformat()
                        order['orderedby'] = orderedby
                        order['id'] = order_id
                        self.orders.append(self.order_details)
                        return "Successfull order updated"
        else:
            return "No order with such id"

    def delete(self, order_id):
        """ A method to delete a specific order from a list """
        for order in self.orders:
            if order['id'] == order_id:
                self.orders.remove(order)
                return "Successfull order deleted"
        else:
            return "Order not found "
