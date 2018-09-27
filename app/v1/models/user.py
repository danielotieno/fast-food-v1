"""
This model defines a user class and it's methods
It also create data structure to store user data

"""

import re
import uuid
import jwt
from datetime import date, datetime, timedelta

user_list = []


class User(object):
    """ A class to handle activities related to a user """

    def validate_data(self, username, email, password, confirm_password):
        """ A method to validate username and password details """
        if not re.match("^[a-zA-Z0-9_]*$", username)\
                or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 4:
            return "Your username should be atleast four characters long"
        elif len(password) < 8:
            return "Your password should be atleast eight characters long"
        elif password != confirm_password:
            return "Your passwords must match"
        else:
            return True

    def create_user(self, username, email, password):
        self.id = uuid.uuid1()
        self.username = username
        self.email = email
        self.password = password

    def generate_auth_token(self, secret_key):
        try:
            # prepare payload
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=60),
                'iat': datetime.utcnow(),
                'sub': self.email
            }
            # create the jwt token using the payload and the SECRET key
            jwt_token = jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
            return jwt_token
        except Exception as error:
            return str(error)

    @staticmethod
    def decode_auth_token(token, secret_key):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error message
            return "you were logged out. Please login"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error message
            return "Please register or login"

    @staticmethod
    def find_user_by_email(email):
        for user in user_list:
            if user.email == email:
                return user
        return None

    @staticmethod
    def user_login(email, password):
        """ A method for a user to login with correct details """
        for user in user_list:
            if email == user['email']:
                if password == user['password']:
                    return "Login successful"
                else:
                    return "Invalid password or username"
        return "user does not exist"

    @staticmethod
    def find_user_by_id(user_id):
        """ Get user given user id """
        for user in user_list:
            if user['id'] == user_id:
                return user

    @staticmethod
    def reset_password(email, newpassword):
        """ A method to reset user password """
        for user in user_list:
            if user['email'] == email:
                user['password'] = newpassword
                return "successful"
            return "Incorrect username"
