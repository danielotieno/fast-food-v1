import os
from flask import Flask, request, jsonify
from flask_restful import Resource
import uuid

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem
from app.v1.models.user import User


class FoodOrdersView(Resource):

    def post(self):
        """ Place a new Order method """
        auth_header = request.headers.get('Authorization')
        order_data = request.get_json()
        if auth_header:
            access_token = auth_header.split(" ")[1]
            if access_token:
                res = User.decode_auth_token(access_token,
                                             os.getenv('SECRET_KEY'))
                if 'login' in res:
                    return jsonify({"message": res})
                email = res
                order_details_data = order_data['oderDetails']

                order = FoodOrder(email)
                order_id = order.id

                # loop over orderData and create order details
                total_cost = 0
                for data in order_details_data:
                    price = FoodItem.get_price_by_name(data['food_item'])
                    count = data['count']
                    cost = price * count
                    order_detail = FoodOrderDetail(order_id, data['food_item'], count,
                                                   cost)
                    food_order_details.append(order_detail)
                    total_cost += cost
                order.set_total_cost(total_cost)
                orders.append(order)
                return jsonify({"message": "order placed successful"})
            return jsonify({"message": "please login or register to continue"})
        return jsonify({"message": "please login or register to continue"})

    def get(self):
        "all orders for a particular user"
        auth_header = request.headers.get('Authorization')
        if auth_header:
            access_token = auth_header.split(" ")[1]
            if access_token:
                res = User.decode_auth_token(access_token,
                                             os.getenv('SECRET_KEY'))
                if 'login' in res:
                    return jsonify({"message": res})
                email = res
                user_orders = FoodOrder.get_user_order_by_email(email)
                return jsonify({"orders": user_orders})
            return jsonify({"message": "please login or register to continue"})
        return jsonify({"message": "please login or register to continue"})


class FoodOrderView(Resource):
    def get(self, order_id):
        "all orders for a particular user"
        user_order = FoodOrder.get_order_by_id(uuid.UUID(order_id))
        return user_order.to_json()

    def delete(self, order_id):
        """ Delete a specific from the orders list """
        delete_order = FoodOrder.delete_an_order(uuid.UUID(order_id))
        return delete_order
