"""
This model defines food order details class and it's methods
It also create data structure to store food order details

"""

from flask import jsonify
import re
from datetime import date, datetime
import uuid

# Data structure to hold order details
food_order_details = []


class FoodOrderDetail():
    """ A class to handle actions related to food orders details """

    def __init__(self, order_id, food_item, count, cost):
        """ A method for creating food order details """

        self.id = uuid.uuid1()
        self.order_id = order_id
        self.food_item = food_item
        self.count = count
        self.cost = cost
