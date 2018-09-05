import pytest
import json

from app import create_app


from app.resources.orders import Order, Orders


ADD_ENTRY_URL = '/api/v1/orders/1'
GET_SINGLE_URL = '/api/v1/orders/1'
GET_ALL_URL = '/api/v1/orders'
DELETE_URL = '/api/v1/orders/1'
MODIFY_URL = '/api/v1/orders/1'
