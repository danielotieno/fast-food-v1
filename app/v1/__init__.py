from flask import Flask
from flask_restful import Api

from config import app_config


def create_app(config_name):
    '''Function to create a flask app depending on the configuration passed'''

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    from app.v1.resources.orders import Order
    from app.v1.resources.orders import Orders
    from app.v1.resources.user_view import SignupView
    from app.v1.resources.user_view import LoginView
    from app.v1.resources.food_order_view import FoodOrderView
    from app.v1.resources.food_item_view import FoodItemView

    api.add_resource(Order, '/api/v1/orders/<int:order_id>')
    api.add_resource(FoodOrderView, '/api/v1/orderss')
    api.add_resource(FoodItemView, '/api/v1/fooditem')
    api.add_resource(Orders, '/api/v1/orders')
    api.add_resource(SignupView, '/api/v1/auth/signup')
    api.add_resource(LoginView, '/api/v1/auth/login')

    return app
