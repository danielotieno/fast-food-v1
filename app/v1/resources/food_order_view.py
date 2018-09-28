import os
from flask import Flask, request, jsonify
from flask_restful import Resource
import uuid

from app.v1.models.food_order import orders, FoodOrder
from app.v1.models.food_order_details import food_order_details, FoodOrderDetail
from app.v1.models.food_item import FoodItem
from app.v1.models.user import User


def is_authenticated(auth_header):
    if auth_header:
        access_token = auth_header.split(" ")[1]
        if access_token:
            res = User.decode_auth_token(access_token,
                                         os.getenv('SECRET_KEY'))
            return res
        return "please login to view the order"
    return "please login or register to continue"


class FoodOrdersView(Resource):
    def post(self):
        """ Place a new Order method """
        auth_header = request.headers.get('Authorization')
        order_data = request.get_json()
        check_token = is_authenticated(auth_header)
        if 'login' in check_token:
            return jsonify({"message": check_token})
        email = check_token
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
        return jsonify({"message": "order placed successful", "order":
                        order.to_json()})

    def get(self):
        "all orders for a particular user"
        auth_header = request.headers.get('Authorization')
        check_token = is_authenticated(auth_header)
        if 'login' in check_token:
            return jsonify({"message": check_token})
        email = check_token
        user_orders = FoodOrder.get_user_order_by_email(email)
        return jsonify({"orders": user_orders})


class FoodOrderView(Resource):
    def get(self, order_id):
        "all orders for a particular user"
        auth_header = request.headers.get('Authorization')
        check_token = is_authenticated(auth_header)
        if 'login' in check_token:
            return jsonify({"message": check_token})
        email = check_token
        user_order = FoodOrder.get_order_by_id(order_id)
        if user_order == "order does not exist":
            return jsonify({"message": user_order})
        if user_order.ordered_by == email:
            return jsonify({"order": user_order.to_json()})
        return jsonify({"message": "you are not allowed to view this order"})

    def put(self, order_id):
        """get one order and update the status"""
        order = FoodOrder.get_order_by_id(order_id)
        data = request.get_json()
        if order:
            order.update_status(data['status'])
            return jsonify({"message": "Order updated Successful", "order":
                            order.to_json()})
        return jsonify({"message": "order not found"})

    def delete(self, order_id):
        """ Delete a specific from the orders list """
        auth_header = request.headers.get('Authorization')
        check_token = is_authenticated(auth_header)
        if 'login' in check_token:
            return jsonify({"message": check_token})
        email = check_token
        order = FoodOrder.get_order_by_id(order_id)
        if order.ordered_by == email:
            order.delete_an_order()
            return jsonify({"message": "delete"})
        return jsonify({"message": "not allowed to delete this order"})
