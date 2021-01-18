import itertools
import unittest
from unittest.mock import patch
from hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.henhouse = HenHouse(8)

    def test_init_with_less_than_min(self):
        with self.assertRaises(ValueError):
            HenHouse(3)
        self.assertRaises(ValueError, lambda: HenHouse(3))

    def test_season(self):
        with patch('hen_class.datetime') as st_mock:
            st_mock.datetime.today().month = 1
            self.assertEqual(self.henhouse.season, 'winter')

    def test_season_not_equal(self):
        with patch('hen_class.datetime') as st_mock:
            st_mock.datetime.today().month = 3
            self.assertNotEqual(self.henhouse.season, 'winter')

    def test_productivity_index(self):
        with patch.object(HenHouse, 'season', 'winter'):
            self.assertEqual(self.henhouse._productivity_index(), 0.25)

    def test_productivity_index_incorrect_season(self):
        with patch.object(HenHouse, 'season', 'summer'):
            self.assertNotEqual(self.henhouse._productivity_index(), 0.25)

    def test_productivity_index_incorrect_season_message(self):
        with patch.object(HenHouse, 'season', 'BUG'):
            self.assertRaises(ErrorTimesOfYear, lambda: self.henhouse._productivity_index())

    def test_get_eggs_daily_in_winter_seasom_mocked(self):
        with patch.object(HenHouse, 'season', 'autumn'):
            self.assertEqual(self.henhouse.get_eggs_daily(8), 4)

    def test_get_eggs_daily_in_winter_productivity_index_index_mocked(self):
        with patch.object(HenHouse, '_productivity_index', return_value=1):
            self.assertEqual(self.henhouse.get_eggs_daily(8), 8)

    def test_get_max_count_for_soup(self):
        self.assertEqual(self.henhouse.get_eggs_daily(10), 2)

    def test_get_max_count_for_soup_returns_zero(self):
        self.assertNotEqual(self.henhouse.get_eggs_daily(10), 0)

    def test_food_price(self):
        with patch('hen_class.requests.get') as price_mock:
            price_mock.return_value.status_code = 200
            price_mock.return_value.text = list(itertools.islice(itertools.count(10, 0.5), 11))
            self.assertEqual(self.henhouse.food_price(), 15)

    def test_food_price_connection_error(self):
        with patch('hen_class.requests.get') as error_mock:
            bad_get_way = False
            error_mock.return_value.status_code = bad_get_way
            self.assertRaises(ConnectionError, lambda: self.henhouse.food_price())


if __name__ == '__main__':
    unittest.main()
