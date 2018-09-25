from datetime import datetime
from flask import request
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash


class DATABASE():
    """ Class to create data structure to store user data """

    def __init__(self):
        """ Create a constructor to hold empty user """
        self.users = {}
        self.user_count = 0

    def drop(self):
        """ A constructor to tear down a user """
        self.__init__()


# create a new instance of the class and assigns db
DB = DATABASE()


class Start():
    """ Start class to be inherited by User Class"""

    def update(self, data):
        """ Validate keys before passing to data """
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())
        return self.view()


class User(Start):
    """ This class defines the user data model """

    def __init__(self, username, password, email):
        """ A method constructor for creating an user """
        self.id = None
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()

    def save(self):
        """ Method for saving user registration details """
        setattr(self, 'id', DB.user_count + 1)
        DB.users.update({self.id: self})
        DB.user_count += 1
        return self.view()

    def validate_password(self, password):
        """ Method for validating user password """
        if check_password_hash(self.password, password):
            return True
        return False

    def delete(self):
        """ Method for deleting a user """
        del DB.users[self.id]

    def view(self):
        """ Method to jsonify object user """
        keys = ['username', 'email', 'id']
        return {key: getattr(self, key) for key in keys}

    @classmethod
    def get(cls, id):
        """ Method for getting user by id """
        user = DB.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user

    @classmethod
    def get_user_by_email(cls, email):
        """ Method for getting user by email """
        for id_ in DB.users:
            user = DB.users.get(id_)
            if user.email == email:
                return user
        return None

    @classmethod
    def get_user_by_username(cls, username):
        """ Method for getting user by username """
        for id_ in DB.users:
            user = DB.users.get(id_)
            if user.username == username:
                return user
        return None


def is_blank(var):
    """checks if any required field is blank"""
    if var.strip() == '':
        return 'All fields are required'
    return None


class Order(object):
    """ Create class order to hold order methods """

    def __init__(self):
        """ Initialize empty Order list"""
        self.order_list = []

    def create_order(self, name, status, price, address):
        """Create order_item"""
        self.order_details = {}

        self.orders_id = len(self.order_list)
        self.order_details['order_id'] = self.orders_id + 1
        self.order_details['name'] = name
        self.order_details['status'] = status
        self.order_details['price'] = price
        self.order_details['address'] = address
        self.order_list.append(self.order_details)
        return self.order_list, 201

    def get_orders(self):
        """ A method to get all orders """
        return self.order_list

    def get_order_by_id(self, order_id):
        """ A method to get a single order """
        order = next(
            filter(lambda x: x['order_id'] == order_id, self.order_list), None)
        return {'order': order}, 200 if order else 404

    def update_an_order(self, order_id):
        """ A method to update a specific order """
        data = request.get_json()
        order = next(
            filter(lambda x: x['order_id'] == order_id, self.order_list), None)
        if order is None:
            order = {
                'status': data['status'],
            }
            self.order_list.append(order), 201
        else:
            order.update(data), 200
        return order

    def delete_an_order(self, order_id):
        """ A method to delete a single order using order id """
        self.order_list
        self.order_list = list(
            filter(lambda x: x['order_id'] != order_id, self.order_list))
        return {'message': 'Order deleted'}, 200
