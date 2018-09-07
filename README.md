# Fast-Food-v1

[![Build Status](https://travis-ci.com/danielotieno/fast-food-v1.svg?branch=api)](https://travis-ci.com/danielotieno/fast-food-v1)
[![Coverage Status](https://coveralls.io/repos/github/danielotieno/fast-food-v1/badge.svg?branch=api)](https://coveralls.io/github/danielotieno/fast-food-v1?branch=api)
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