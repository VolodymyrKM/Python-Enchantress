class UserNotFound(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class CartNotFound(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id