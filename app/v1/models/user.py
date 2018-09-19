"""
This model defines a user class and it's methods
It also create data structure to store user data

"""

# local imports
import re
import uuid


class User(object):
    """ A class to handle activities related to a user """

    def __init__(self):
        # Data structure list to hold user details
        self.users = []

    def user_register(self, username, email, password, confirm_password):
        """ A method to register users with correct and valid details """

        # empty dictionary to hold users details created
        user_details = {}

        # check whether a user with that username exists

        for user in self.users:
            if username == user['username'] or user['email'] == email:
                return "Username or email already exists."

        else:
            # validations for username and password
            if not re.match("^[a-zA-Z0-9_]*$", username)\
                    or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return "Username or email can only contain alphanumeric characters"

            elif len(username.strip()) < 4:
                return "username must be more than 4 characters"

            elif password != confirm_password:
                return "passwords does not match"

            elif len(password) < 8:
                return "Password too short to be accepted"

            else:
                # Register user when details are valid
                user_details['username'] = username
                user_details['email'] = email
                user_details['password'] = password
                user_details['id'] = uuid.uuid1()
                self.users.append(user_details)
                return "Registration successfull"

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
