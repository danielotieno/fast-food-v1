"""
This model defines a user class and it's methods
It also create data structure to store user data

"""

import re
import uuid
import jwt
from datetime import date, datetime, timedelta


class User(object):
    """ A class to handle activities related to a user """

    def __init__(self):
        """ Data structure list to hold user details """
        self.users = []

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

    def add_user_to_user_list(self, username, email, password):

        # empty dictionary to hold users details created
        user_details = {}

        user_details['username'] = username
        user_details['email'] = email
        user_details['password'] = password
        user_details['id'] = uuid.uuid1()
        self.users.append(user_details)

    def user_register(self, username, email, password, confirm_password):
        """ A method to register users with correct and valid details """

        # check whether a user with that username exists
        valid_data = self.validate_data(
            username, email, password, confirm_password)
        if valid_data:
            # Register user when details are valid
            if len(self.users) > 0:
                for user in self.users:
                    if username == user['username'] or user['email'] == email:
                        return "Username or email already exists."

                    self.add_user_to_user_list(username, email, password)
                    return "Registration successfull"
                # if the list is empty
            else:
                self.add_user_to_user_list(username, email, password)
                return "Registration successfull"

        # return data  validation  error message
        return valid_data

    def user_login(self, username, password):
        """ A method for a user to login with correct details """
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return "Login successful"
                else:
                    return "Invalid password or username"
        return "user does not exist"

    def find_user_by_id(self, user_id):
        """ Get user given user id """
        for user in self.users:
            if user['id'] == user_id:
                return user

    def find_user_by_username(self, username):
        """ Get user by username """
        for user in self.users:
            if user['username'] == username:
                return user

    def reset_password(self, username, newpassword):
        """ A method to reset user password """
        for user in self.users:
            if user['username'] == username:
                user['password'] = newpassword
                return "successful"
            return "Incorrect username"
