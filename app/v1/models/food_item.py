"""
This model defines a Food class and it's methods
It also create data structure to store Food Items

"""
from flask import jsonify
from datetime import date, datetime
import re
import uuid

# Data structure list to hold food details
Food_list = []


class FoodItem():
    """ A class to handle activities related to a Food Items """

    def create_food(self, food_name, food_price):
        """ A method for creating food Items """

        self.id = uuid.uuid1()
        self.name = food_name
        self.price = food_price
        self.date = datetime.now().replace(second=0, microsecond=0)

    def get_all_foods(self):
        """ A method to return a list of all food items  """
        return jsonify({
            "message": "Successful.",
            "Food": Food_list}), 200

    def get_food_item_by_id(self, food_id):
        """ A method to get fooditem by id """
        for food in Food_list:
            if food.id == food_id:
                return jsonify({
                    "message": "Successful.",
                    "Food": food}), 200
        return False
