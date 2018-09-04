from flask import Flask
from flask_restful import Api

import config


def create_app(config_name):
    '''Function to create a flask app depending on the configuration passed'''

    app = Flask(__name__)
    api = Api(app)

    app.config.from_object('config')
    app.url_map.strict_slashes = False

    from app.resources.orders import Orders

    api.add_resource(Orders, '/api/v1/orders')

    return app
