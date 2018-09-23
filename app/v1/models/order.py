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
