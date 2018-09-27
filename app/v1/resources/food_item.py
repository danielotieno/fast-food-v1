from flask import Flask, request, jsonify
from flask_restful import Resource

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem, food_list


class FoodItemView(Resource):

    def post(self):
        data = request.get_json()
        food_item = FoodItem(data['name'], data['price'])
        food_list.append(food_item)

        for food_item in food_list:
            print(food_item.name)
            print(food_item.price)
