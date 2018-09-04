from flask import Flask
from flask_restful import Resource

from app.model import orders


class Orders(Resource):
    def get(self):
        return {'orders': orders}
