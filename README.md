# Fast-Food-v1

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.com/danielotieno/fast-food-v1.svg?branch=develop)](https://travis-ci.com/danielotieno/fast-food-v1)
[![Coverage Status](https://coveralls.io/repos/github/danielotieno/fast-food-v1/badge.svg?branch=develop)](https://coveralls.io/github/danielotieno/fast-food-v1?branch=develop)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e23ec45d5b4e814e4310/test_coverage)](https://codeclimate.com/github/danielotieno/fast-food-v1/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/e23ec45d5b4e814e4310/maintainability)](https://codeclimate.com/github/danielotieno/fast-food-v1/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ae2f2e1b9f0439f8e5c3b045aac53d1)](https://www.codacy.com/app/danielotieno/fast-food-v1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=danielotieno/fast-food-v1&amp;utm_campaign=Badge_Grade)

Fast-Food-Fast is a food delivery service app for a restaurant.

## API Endpoints

| EndPoint              | Functionality                    |
| --------------------- | -------------------------------- |
| GET /orders           | Get all the orders.              |
| GET /orders/<orderId> | Fetch a specific order           |
| POST /orders          | Place a new order.               |
| PUT /orders/<orderId> | Update the status of an order.   |
| DEL /orders/<orderId> | Delete a specific order.         |
| POST /signup          | Register a new user              |
| POST /login           | Enables registered user to login |

### Technologies used to build the application

[Python 3.6](https://docs.python.org/3.6/)
[Flask](http://flask.pocoo.org/)
[Flask Restful](https://flask-restful.readthedocs.io/en/latest/)

#### How should this be manually tested

Fork the repo here [Fork me](https://github.com/danielotieno/fast-food-v1/tree/develop)

`git clone the forked repo in your machine`

#### Create a virtual environment

`python3 -m venv venv`

#### Activate the virtual environment

`source venv/bin/activate`

#### Install dependencies

`pip install -r requirements.txt`

#### Change directory to develop branch

`cd develop`

#### Then run the command below to start the application

`python run.py`

#### Running Tests

`pytest -v`

### Users

#### User registration

Send a `POST` request to `/api/v1/auth/signup` endpoint with the payload in `JSON`

#### User Login

Send a `POST` request to `/api/v1/auth/login` endpoint with the payload in `JSON`

#### Get list of all orders

Send a `GET` request to `/api/v1/orders`

#### Featch a specific order

Send a `GET` request to `/api/v1/orders/<order_id>`

#### Place/Create an order

Send a `POST` request to `/api/v1/orders/<order_id>` endpoint with the payload in `JSON`

#### Update the order status

Send a `PUT` request to `/api/v1/orders/<order_id>` endpoint with the payload in `JSON`

#### Delete a specific order

Send a `DEL` request to `/api/v1/orders/<order_id>` endpoint with the payload in `JSON`