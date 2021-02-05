import unittest
from unittest import TestCase

from utils.database import DataBaseParser
from users_dict import update_user_dict, users_dict, bad_user_dict


class TestDataBaseParserPositive(TestCase):

    def setUp(self):
        self.database = DataBaseParser()
        """creation of db"""
        self.database._setup()

    def tearDown(self):
        """delete db"""
        self.database._cleaned_up()

    def test_create_read_update_delete_user(self):
        message_create = 'user name: Volodymyr, user email: ' \
                         'Volodymyr@gmail.com, ' \
                         'data registration: 2021-02-05 07:21:37'
        self.database.create_user(users_dict)
        self.assertEqual(message_create, self.database.read_user_info(1))

        message_update = f'user name: Olga, user email: Olga@gmail.com, ' \
                         f'data registration: 2021-02-05 10:21:37'
        self.database.update_user(user_info=update_user_dict)
        self.assertEqual(message_update, self.database.read_user_info(1))

        self.database.delete_user(1)
        self.assertEqual(None, self.database.read_user_info(1))

    def test_create_update_read_delete_card(self):
        self.database.create_user(users_dict)
        self.database.create_cart(users_dict)

        message_cart = 'cart id: 1, price: 30, product: milk'
        self.assertEqual(self.database.read_cart(1), message_cart)

        message_cart_update = 'cart id: 1, price: 25, product: chocolate'
        self.database.update_cart(update_user_dict)
        self.assertEqual(message_cart_update, self.database.read_cart(1))

        self.database.delete_cart(1)
        self.assertEqual(None, self.database.read_cart(1))


class TestDataBaseParserNegative(TestCase):
    def setUp(self):
        self.database = DataBaseParser()
        """creation of db"""
        self.database._setup()

    def tearDown(self):
        """delete db"""
        self.database._cleaned_up()

    def test_create_read_update_delete_user_negative_result(self):
        message_create_user = 'user name: Volodymyr, user email: ' \
                              'Volodymyr@gmail.com, ' \
                              'data registration: 2020-00-00 00:00:00'

        self.database.create_user(users_dict)
        self.assertNotEqual(message_create_user, self.database.read_user_info(1))

        self.database.update_user(1, user_info=bad_user_dict)

        message_update_user = f'user name: Olga, user email: Olga@gmail.com, ' \
                              f'data registration: 2021-02-05 10:21:37'
        self.database.update_user(user_info=bad_user_dict)
        self.assertNotEqual(message_update_user, self.database.read_user_info(1))
        self.assertFalse(self.database.read_user_info(2))

    def test_create_read_update_delete_cart_negative_result(self):
        self.database.create_user(users_dict)

        self.assertFalse(self.database.read_cart(1))

        self.database.create_cart(users_dict)
        self.assertTrue(self.database.read_cart(1))

        self.assertFalse(self.database.read_cart(5))
        self.database.update_cart(bad_user_dict)

        message_update_cart = 'cart id: 1, price: 25, product: chocolate'
        self.assertNotEqual(self.database.read_cart(1), message_update_cart)

        self.database.delete_cart(1)
        self.assertFalse(self.database.read_cart(1))


if __name__ == '__main__':
    unittest.main()
