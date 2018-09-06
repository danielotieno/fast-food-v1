from datetime import datetime
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash

class DATABASE():
    """ Class to create data structure to store user data """
    def __init__(self):
        self.users = {}
        self.user_count = 0

    def drop(self):
        self.__init__()

""" create a new instance of the class and assigns db """
db = DATABASE()

class Start():
    """ Start class to be inherited by User Class"""
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())
        return self.view()

class User(Base):
    """ This class defines the user data model """
    def __init__(self, username, password, email):
        self.id = None
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()

    def save(self):
        """ Method for saving user registration details """
        setattr(self, 'id', db.user_count + 1)
        db.users.update({self.id: self})
        db.user_count += 1
        return self.view()

    def validate_password(self, password):
        """ Method for validating user password """
        if check_password_hash(self.password, password):
            return True
        return False

     def delete(self):
            """ Method for deleting a user """
        del db.users[self.id]



orders = [

    {
        "order_id": 1,
        "name": "Daniel Otieno",
        "type": "Cheese Burger",
        "price": 686.00,
        "address": "Kileleshwa"
    },

    {
        "order_id": 2,
        "name": "Cash Camerine",
        "type": "Chips Masala",
        "price": 400.00,
        "address": "Parklands"
    }

]
