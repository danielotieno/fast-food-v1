"""
This model defines a Food class and it's methods
It also create data structure to store Food Items

"""
from flask import jsonify
from datetime import date, datetime
import re
import uuid

# Data structure list to hold food details
food_list = []


class FoodItem():
    """ A class to handle activities related to a Food Items """

    def __init__(self, food_name, food_price):
        """ A method for creating food Items """

        self.id = uuid.uuid1()
        self.name = food_name
        self.price = food_price
        self.date = datetime.now().replace(second=0, microsecond=0)

    @staticmethod
    def get_price_by_name(food_name):
        """ A method to get order by id """
        for food in food_list:
            if food.name == food_name:
                return food.price
        return False

    def get_all_foods(self):
        """ A method to return a list of all food items  """
        return jsonify({
            "message": "Successful.",
            "Food": food_list}), 200

    def get_food_item_by_id(self, food_id):
        """ A method to get fooditem by id """
        for food in food_list:
            if food.id == food_id:
                return jsonify({
                    "message": "Successful.",
                    "Food": food}), 200
        return False

    def to_json(self):
        """convert a given food item to json"""
        json_food_item = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "date": self.date
        }
        return json_food_item
