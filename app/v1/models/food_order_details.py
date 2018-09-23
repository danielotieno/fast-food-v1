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


class FoodOrderDetails():
    """ A class to handle actions related to food orders details """
