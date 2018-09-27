import os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import re

from app.v1.models.user import user_list, User


class SignupView(Resource):
    def post(self):
        ''''a method to register a user'''''
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        # create a user object
        user_object = User()

        valid_data = user_object.validate_data(username, email, password,
                                               confirm_password)
        if valid_data:
            existing_user = user_object.find_user_by_email(email)
            if existing_user:
                return jsonify({"message": "user with that email already exists"})
            user_object.create_user(username, email, password)
            user_list.append(user_object)
            return jsonify({"message": "registration successful"})
        return jsonify({"message": valid_data})


class LoginView(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        user = User.find_user_by_email(email)
        if user and user.password == password:
            token = user.generate_auth_token(os.getenv('SECRET_KEY'))
            return jsonify({"message": "login successful", "token":
                            token.decode()})
        return jsonify({"message": "wrong email or password"})
