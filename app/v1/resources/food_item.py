from flask import Flask, request
from flask_restful import Resource

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem, Food_list


class FoodItemView(Resource):

    def post(self):
        data = request.get_json()
        food_item = FoodItem(data['name'], data['price'])
        Food_list.append(food_item)

        for food_item in Food_list:
            print(food_item.name)
            print(food_item.price)
