from flask import Blueprint, request
from datetime import datetime
from custom_exceptions import UserNotFound, CartNotFound
from flask_restful import Resource, Api

amazon_killer = Blueprint('amazon_killer', __name__)
api = Api(amazon_killer)

USER_DATABASE = dict()
user_counter = 1
CART_DATABASE = dict()
cart_counter = 1


@amazon_killer.errorhandler(UserNotFound)
def user_not_found(error):
    return {"error": f"no such user with id {error.user_id}"}, 404


class UserRestfulApi(Resource):
    def post(self):
        global user_counter
        user = request.json

        user['user_id'] = user_counter
        dt = datetime.now().isoformat()

        user['registration_timestamp'] = dt
        USER_DATABASE[user_counter] = user

        response = {"registration_timestamp": dt, "user_id": user_counter}
        user_counter += 1
        status_code = 201

        return response, status_code

    def put(self, user_id):
        if user_id not in USER_DATABASE:
            raise UserNotFound(user_id)

        update_data_user = request.json

        USER_DATABASE[user_id]["name"] = update_data_user["name"]
        USER_DATABASE[user_id]["name"] = update_data_user["name"]
        response = {
            "status": "success"
        }
        return response, 200

    def get(self, user_id):
        user = USER_DATABASE.get(user_id)
        if user is None:
            raise UserNotFound(user_id)
        return user

    def delete(self, user_id):
        if user_id not in USER_DATABASE:
            raise UserNotFound(user_id)

        USER_DATABASE.pop(user_id)
        response = {"status": "success"}

        return response


@amazon_killer.errorhandler(CartNotFound)
def cart_not_found(error):
    return {"error": f"no such cart with id {error.cart_id}"}, 404


class UserCartRestfullApi(Resource):
    def post(self):
        global cart_counter
        USER_DATABASE[1] = dict()
        cart = request.json
        user_id = cart.get("user_id")

        if user_id not in USER_DATABASE:
            raise UserNotFound(user_id)

        dt = datetime.now().isoformat()
        response = {"cart_id": cart_counter,
                    "creation_time": dt}
        cart["creation_time"] = response["creation_time"]
        CART_DATABASE[cart_counter] = cart

        cart_counter += 1
        status_code = 201

        return response, status_code

    def get(self, cart_id):
        cart = CART_DATABASE.get(cart_id)

        if cart is None:
            raise CartNotFound(cart_id)
        return cart

    def put(self, cart_id):
        cart_data = CART_DATABASE.get(cart_id)

        if cart_data is None:
            raise CartNotFound(cart_id)

        new_list_products = request.json.get("products")
        for key, value in CART_DATABASE.items():
            if key == "products":
                value.append(new_list_products)

        response = {"status": "success"}

        return response

    def delete(self, cart_id):
        cart = CART_DATABASE.get(cart_id)

        if cart is None:
            raise CartNotFound(cart_id)

        CART_DATABASE.pop(cart_id)
        response = {"status": "success"}

        return response


api.add_resource(UserRestfulApi, '/users', '/users/<int:user_id>')
api.add_resource(UserCartRestfullApi, '/cart', '/cart/<int:cart_id>')
