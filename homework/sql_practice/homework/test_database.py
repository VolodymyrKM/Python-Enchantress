import unittest
import datetime
from psycopg2 import DatabaseError
from unittest import TestCase

from dict_info_for_test import users_dict_1, users_dict_2, users_dict_3, users_dict_4, update_users_dict_1, \
    update_users_dict_2, update_users_dict_4, update_users_dict_3, empty_users_dict, empty_users_dict_2, \
    empty_users_dict_4, empty_users_dict_3
from utils.database import DataBaseParser


class TestDataBaseParserPositive(TestCase):

    def setUp(self):
        self.database = DataBaseParser()
        """creation of db"""
        self.database._setup()

        self.message_create_1 = ('Volodymyr', 'Volodymyr@gmail.com', datetime.datetime(2021, 2, 5, 7, 21, 37))
        self.message_create_2 = ('Antonina', 'Antonina@gmail.com', datetime.datetime(2021, 2, 6, 10, 20, 30))
        self.message_create_3 = ('Bogdan', 'Bogdan@gmail.com', datetime.datetime(2021, 2, 7, 10, 10, 10))
        self.message_create_4 = ('Sophia', 'Sophia@gmail.com', datetime.datetime(2021, 2, 8, 11, 15, 15))

        self.message_update_1 = ('Olga', 'Olga@gmail.com', datetime.datetime(2021, 2, 5, 10, 21, 37))
        self.message_update_2 = ('Michela', 'Michela@gmail.com', datetime.datetime(2021, 2, 11, 11, 11, 11))
        self.message_update_3 = ('Galina', 'Galina@gmail.com', datetime.datetime(2021, 2, 12, 14, 13, 13))
        self.message_update_4 = ('Solomia', 'Solomia@gmail.com', datetime.datetime(2021, 4, 5, 13, 25, 25))

        self.message_create_cart_details_1 = (1, 25, 'chocolate')
        self.message_create_cart_details_2 = (2, 30, 'cheese')
        self.message_create_cart_details_3 = (3, 35, 'bread')
        self.message_create_cart_details_4 = (4, 40, 'meat')

        self.message_update_cart_details_1 = (1, 44, 'potato')
        self.message_update_cart_details_2 = (2, 50, 'corn')
        self.message_update_cart_details_3 = (3, 60, 'meat')
        self.message_update_cart_details_4 = (4, 60, 'batter')

    def tearDown(self):
        """delete db"""
        self.database._cleaned_up()

    def test_create_user(self):
        self.database.create_user(users_dict_1)
        self.assertEqual(self.message_create_1, self.database.read_user_info(1))

        self.database.create_user(users_dict_2)
        self.assertEqual(self.message_create_2, self.database.read_user_info(2))

        self.database.create_user(users_dict_3)
        self.assertEqual(self.message_create_3, self.database.read_user_info(3))

        self.database.create_user(users_dict_4)
        self.assertEqual(self.message_create_4, self.database.read_user_info(4))

    def test_update_user(self):
        self.database.create_user(users_dict_1)
        self.database.update_user(user_info=update_users_dict_1)
        self.assertEqual(self.message_update_1, self.database.read_user_info(1))

        self.database.create_user(users_dict_2)
        self.database.update_user(user_info=update_users_dict_2)
        self.assertEqual(self.message_update_2, self.database.read_user_info(2))

        self.database.create_user(users_dict_3)
        self.database.update_user(user_info=update_users_dict_3)
        self.assertEqual(self.message_update_3, self.database.read_user_info(3))

        self.database.create_user(users_dict_4)
        self.database.update_user(user_info=update_users_dict_4)
        self.assertEqual(self.message_update_4, self.database.read_user_info(4))

    def test_delete_user(self):
        self.database.create_user(users_dict_1)
        self.database.delete_user(1)
        self.assertEqual(None, self.database.read_user_info(1))

        self.database.create_user(users_dict_2)
        self.database.delete_user(2)
        self.assertEqual(None, self.database.read_user_info(2))

        self.database.create_user(users_dict_3)
        self.database.delete_user(3)
        self.assertEqual(None, self.database.read_user_info(3))

        self.database.create_user(users_dict_4)
        self.database.delete_user(4)
        self.assertEqual(None, self.database.read_user_info(4))

    def test_create_card(self):
        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        self.assertEqual(self.message_create_cart_details_1, self.database.read_cart(1))

        self.database.create_user(users_dict_2)
        self.database.create_cart(users_dict_2)
        self.assertEqual(self.message_create_cart_details_2, self.database.read_cart(2))

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        self.assertEqual(self.message_create_cart_details_3, self.database.read_cart(3))

        self.database.create_user(users_dict_4)
        self.database.create_cart(users_dict_4)
        self.assertEqual(self.message_create_cart_details_4, self.database.read_cart(4))

    def test_update_card(self):
        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        self.database.update_cart(update_users_dict_1)
        self.assertEqual(self.message_update_cart_details_1, self.database.read_cart(1))

        self.database.create_user(users_dict_2)
        self.database.create_cart(users_dict_2)
        self.database.update_cart(update_users_dict_2)
        self.assertEqual(self.message_update_cart_details_2, self.database.read_cart(2))

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        self.database.update_cart(update_users_dict_3)
        self.assertEqual(self.message_update_cart_details_3, self.database.read_cart(3))

        self.database.create_user(users_dict_4)
        self.database.create_cart(users_dict_4)
        self.database.update_cart(update_users_dict_4)
        self.assertEqual(self.message_update_cart_details_4, self.database.read_cart(4))

    def test_delete_card(self):
        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        self.database.delete_cart(1)

        self.database.create_user(users_dict_2)
        self.database.create_cart(users_dict_2)
        self.database.delete_cart(2)

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        self.database.delete_cart(3)

        self.database.create_user(users_dict_4)
        self.database.create_cart(users_dict_4)
        self.database.delete_cart(4)


class TestDataBaseParserNegative(TestCase):
    def setUp(self):
        self.database = DataBaseParser()
        """creation of db"""
        self.database._setup()

        self.message_negative_result = (
            ('Dmutro', 'Volodymyr@gmail.com', datetime.datetime(2021, 2, 5, 7, 21, 37)),
            ('Volodymyr', 'Dmutro@gmail.com', datetime.datetime(2021, 2, 5, 7, 21, 37)),
            ('Volodymyr', 'Dmutro@gmail.com', datetime.datetime(2021, 2, 5, 7, 51, 37)),
        )

        self.message_update_cart_details_1 = (1, 44, 'potato')
        self.message_update_cart_details_2 = (1, 50, 'corn')
        self.message_update_cart_details_3 = (1, 60, 'meat')
        self.message_update_cart_details_4 = (1, 60, 'batter')

        self.message_update_1 = ('Olga', 'Olga@gmail.com', datetime.datetime(2021, 2, 5, 10, 21, 37))
        self.message_update_2 = ('Michela', 'Michela@gmail.com', datetime.datetime(2021, 2, 11, 11, 11, 11))
        self.message_update_3 = ('Galina', 'Galina@gmail.com', datetime.datetime(2021, 2, 12, 14, 13, 13))
        self.message_update_4 = ('Solomia', 'Solomia@gmail.com', datetime.datetime(2021, 4, 5, 13, 25, 25))

        self.empty_users_dict = [
            {'user_id': "", 'name': '', 'email': '', 'registration_time': '2020'},
            {'user_id': "23", 'name': '', 'email': '', 'registration_time': ''},
            {'user_id': "", 'name': '', 'email': 'qwe@qwe', 'registration_time': ''},
        ]

        self.cart_list = (
            (2, 34, 'milk'),
            (5, 32, 'bread'),
            (1, 12, 'corn'),
        )

    def tearDown(self):
        """delete db"""
        self.database._cleaned_up()

    def test_create_user_negative(self):
        for i, test_info in enumerate(self.empty_users_dict):
            with self.subTest(test_name=f'Test # {i}'):
                with self.assertRaises(DatabaseError):
                    self.database.create_user(test_info)

    def test_read_user_negative(self):
        self.database.create_user(users_dict_1)
        for i, mess_neg in enumerate(self.message_negative_result):
            with self.subTest(test_name=f'Test #{i}'):
                self.assertNotEqual(self.database.read_user_info(1), mess_neg)

        self.database.create_user(users_dict_3)
        self.database.update_user(user_info=update_users_dict_1)
        for i, mess_neg in enumerate(self.message_negative_result):
            with self.subTest(test_name=f'Test #{i}'):
                self.assertNotEqual(self.database.read_user_info(1), mess_neg)

    def test_delete_user_negative(self):
        self.database.create_user(users_dict_2)
        self.database.delete_user(1)

        for i, mess_neg in enumerate(self.message_negative_result):
            with self.subTest(test_name=f'Test #{i}'):
                self.assertNotEqual(self.database.read_user_info(1), mess_neg)

    def test_update_user_negative(self):
        self.database.create_user(users_dict_1)
        self.database.update_user(user_info=update_users_dict_1)
        self.assertNotEqual(None, self.message_update_1)

        self.database.create_user(users_dict_2)
        self.database.update_user(user_info=update_users_dict_2)
        self.assertNotEqual(None, self.message_update_2)

        self.database.create_user(users_dict_3)
        self.database.update_user(user_info=update_users_dict_3)
        self.assertNotEqual(None, self.message_update_3)

        self.database.create_user(users_dict_4)
        self.database.update_user(user_info=update_users_dict_4)
        self.assertNotEqual(None, self.message_update_4)

    def test_create_card_negative(self):
        with self.assertRaises(DatabaseError):
            self.database.create_cart(users_dict_1)

        self.database.create_user(users_dict_1)
        with self.assertRaises(DatabaseError):
            self.database.create_cart(empty_users_dict)

    def test_update_cart_negative(self):
        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        with self.assertRaises(DatabaseError):
            self.database.update_cart(empty_users_dict)

        self.database.create_user(users_dict_2)
        self.database.create_cart(users_dict_2)
        with self.assertRaises(DatabaseError):
            self.database.update_cart(empty_users_dict_2)

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        with self.assertRaises(DatabaseError):
            self.database.update_cart(empty_users_dict_3)

        self.database.create_user(users_dict_4)
        self.database.create_cart(users_dict_4)
        with self.assertRaises(DatabaseError):
            self.database.update_cart(empty_users_dict_4)

    def test_read_cart_negative(self):
        self.assertEqual(None, self.database.read_cart(1))
        self.assertEqual(None, self.database.read_cart(2))
        self.assertEqual(None, self.database.read_cart(3))
        self.assertEqual(None, self.database.read_cart(4))

        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        for i, cart in enumerate(self.cart_list):
            with self.subTest(test_name=f'TEst # {i}'):
                self.assertNotEqual(cart, self.database.read_cart(i))

    def test_delete_cart_negative(self):
        self.database.create_user(users_dict_1)
        self.database.create_cart(users_dict_1)
        self.database.delete_cart(1)
        self.assertNotEqual(self.message_update_1, self.database.read_cart(1))

        self.database.create_user(users_dict_2)
        self.database.create_cart(users_dict_2)
        self.database.delete_cart(2)
        self.assertNotEqual(self.message_update_2, self.database.read_cart(2))

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        self.database.delete_cart(3)
        self.assertNotEqual(self.message_update_3, self.database.read_cart(3))

        self.database.create_user(users_dict_3)
        self.database.create_cart(users_dict_3)
        self.database.delete_cart(3)
        self.assertNotEqual(self.message_update_1, self.database.read_cart(3))


if __name__ == '__main__':
    unittest.main()
