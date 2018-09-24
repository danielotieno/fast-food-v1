from flask import Flask, request, session
from flask_restful import Resource, reqparse

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem


class FoodOrderView(Resource):

    def post(self):
        """ Place a new Order method """
        orderData = request.get_json()
        # orderedby = session['username']
        foodname = orderData['food_name']
        count = orderData['count']
        price = orderData['price']

        order = FoodOrder(foodname, count, price)

        order.create()

        # order_id = order.id
        # # loop over orderData and create order details

        # for order_detail_data in orderData:
        #     food_name = order_detail_data['item']
        #     count = order_detail_data['count']
        #     price = FoodItem.get_price_by_name(food_name)
        #     cost = price * count
        #     order_detail = FoodOrderDetail(
        #         order_id, food_name, count, cost)
        #     food_order_details.append(order_detail)
