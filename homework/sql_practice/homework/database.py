from datetime import datetime
from databaseconnection import DatabaseConnection
from setup import set_table

from users_dict import users_dict, update_user_dict


class DataBaseParser:
    DT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def _cleaned_up():
        with DatabaseConnection() as cursor:
            cursor.execute('DROP TABLE cart_details')
            cursor.execute('DROP TABLE cart')
            cursor.execute('DROP TABLE users')

    @staticmethod
    def _setup():
        with DatabaseConnection() as cursor:
            cursor.execute(set_table)

    @staticmethod
    def create_user(user_info):
        """Creation user in db 'users' with values 'name', 'email', 'registration time' """
        with DatabaseConnection() as cursor:
            cursor.execute("""INSERT INTO users (name, email, registration_time)
                 VALUES (%(name)s, %(email)s, %(registration_time)s)""", user_info)

    @staticmethod
    def read_user_info(user_id):
        """read user info by user id """
        with DatabaseConnection() as cursor:
            cursor.execute("""SELECT name, email, registration_time
             FROM users WHERE id = %s""", (user_id,))
            data_info = cursor.fetchone()
        return data_info

    @staticmethod
    def update_user(user_id=None, *, user_info: dict):
        """update db users : 'name', 'email', uses id"""
        if user_id:
            user_info['user_id'] = user_id  # This parameter used to set user_id in dict info_user for updating
        with DatabaseConnection() as cursor:
            cursor.execute("""UPDATE users
                SET name = %(name)s,
                email = %(email)s,
                registration_time = %(registration_time)s
                WHERE id = %(user_id)s""", user_info)

    @staticmethod
    def delete_user(_id: int):
        with DatabaseConnection() as cursor:
            cursor.execute("""DELETE FROM users WHERE id = %s""", (_id,))

    @staticmethod
    def create_cart(user_info: dict):
        """Creation cart for user and card details whit setting products and price for each product"""
        with DatabaseConnection() as cursor:
            cursor.execute('INSERT INTO cart (creation_time, user_id) VALUES (%s, %s)',
                           (DataBaseParser.DT, user_info['user_id'],))  # creation card
            cursor.execute('SELECT id FROM cart ORDER BY id DESC LIMIT 1')  # select card id for cart details
            id_cart = cursor.fetchall()[0][0]  # id for cart_details
            cart_details = user_info.get('cart_details')  # list with dicts witch will be set as cart details
            for cart_detail in cart_details:
                cart_detail['cart_id'] = id_cart  # setting each card id in dict and set into cart details
                cursor.execute("""INSERT INTO cart_details (cart_id, price, product)
                     VALUES (%(cart_id)s, %(price)s, %(product)s)""", cart_detail)

    @staticmethod
    def update_cart(update_user_dict):
        with DatabaseConnection() as cursor:
            users_update_cards = update_user_dict.get('cart_details')  # take list with dict from update_dict
            cursor.execute("""SELECT id from cart_details
                            WHERE cart_id = %(cart_id)s""", users_update_cards[0], )  # take id from cart_details
            cart_ids = cursor.fetchall()  # id from cart_details
            for card_id, update_card in zip(cart_ids, users_update_cards):
                update_card['id'] = card_id
                cursor.execute("""UPDATE cart_details
                     SET price = %(price)s, product = %(product)s
                      WHERE id = %(id)s""", update_card)

    @staticmethod
    def read_cart(cart_id: int):
        """Output to the user info from all the card details"""
        with DatabaseConnection() as cursor:
            cursor.execute("""SELECT cart_id, price, product
                              FROM cart_details
                              WHERE cart_id = %s""", (cart_id,))
            read_data = cursor.fetchone()  # select on product from product list
            return read_data

    @staticmethod
    def delete_cart(id_cart: int):
        with DatabaseConnection() as cursor:
            cursor.execute('DELETE FROM cart WHERE id = %s', (id_cart,))


if __name__ == '__main__':
    dbp = DataBaseParser()
    dbp._setup()
    dbp.create_user(users_dict)
    print(dbp.read_user_info(1))
    dbp.update_user(5, user_info=update_user_dict)
    dbp.delete_user(1)
    dbp.update_user(1, user_info=update_user_dict)
    dbp.create_cart(users_dict)
    print(dbp.update_cart(update_user_dict))
    print(dbp.read_cart(1))
    dbp.delete_cart(1)
    print(dbp.read_cart(1))
    dbp._cleaned_up()
