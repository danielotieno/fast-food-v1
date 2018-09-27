from flask import Flask, request
from flask_restful import Resource

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem


class FoodOrderView(Resource):

    def post(self):
        """ Place a new Order method """
        order_data = request.get_json()
        username = 'Bucky'
        order_details_data = order_data['oderDetails']

        order = FoodOrder(username)
        order_id = order.id

        # loop over orderData and create order details
        total_cost = 0
        for data in order_details_data:
            price = FoodItem.get_price_by_name(data['food_name'])
            count = data['count']
            cost = price * count
            order_detail = FoodOrderDetail(order_id, data['food_item'], count,
                                           cost)
            food_order_details.append(order_detail)
            total_cost += cost
        order.set_total_cost(total_cost)
        orders.append(order)
