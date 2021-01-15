from unittest import TestCase
from decimal import Decimal
from test_simple_calc import divide, multiply, subtract, add


class TestDivideFunction(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expect = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expect, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expect = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expect, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 3
        expect = 0
        self.assertEqual(divide(dividend, divisor), expect)

    def test_divide_error_on_zero(self):
        # self.assertRaises(ValueError, lambda: divide(25, 0))
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_divide_Decimal_number(self):
        inputs = Decimal('5.8'), Decimal('5.9'),
        expect = Decimal('0.98305')
        self.assertAlmostEqual(divide(*inputs), expect, delta=0.0001)

    def test_multiply_int(self):
        factor_x = 4
        factor_y = 5
        expect = 20
        self.assertEqual(multiply(factor_x, factor_y), expect)

    def test_multiply_float(self):
        factor_x = 5
        factor_y = 4.0
        expect = 20.0
        self.assertAlmostEqual(multiply(factor_x, factor_y), expect, delta=0.0001)

    def test_multiply_factor_zero(self):
        factor_x = 0
        factor_y = 1
        expect = 0
        self.assertEqual(multiply(factor_x, factor_y), expect)

    def test_multiply_negative_value(self):
        inputs = (2, -5)
        expect = -10
        self.assertEqual(multiply(*inputs), expect)

    def test_multiply_Decimal_number(self):
        inputs = (Decimal('3.4'), Decimal('5.9'))
        expect = Decimal('20.06')
        self.assertEqual(multiply(*inputs), expect)

    def test_subtract_integer_numbers(self):
        minuend = 10
        subtrahend = 5
        expect = 5
        self.assertEqual(subtract(minuend, subtrahend), expect)

    def test_subtract_float_numbers(self):
        minuend = 10.0
        subtrahend = 5
        expect = 5.0
        self.assertAlmostEqual(subtract(minuend, subtrahend), expect, delta=0.0001)

    def test_subtract_negative_number(self):
        minuend = -10
        subtrahend = 5
        expect = -15
        self.assertEqual(subtract(minuend, subtrahend), expect)

    def test_subtract_Decimal_numbers(self):
        inputs = Decimal('5.8'), Decimal('5.9'),
        expect = Decimal('-0.1')
        self.assertEqual(subtract(*inputs), expect)

    def test_subtract_minuend_zero(self):
        inputs = (0, 20)
        expect = -20
        self.assertEqual(subtract(*inputs), expect)

    def test_add_integer_number(self):
        addend_x = 4
        addend_y = 30
        expect = 34
        self.assertEqual(add(addend_x, addend_y), expect)

    def test_add_float_number(self):
        addend_x = 4.0
        addend_y = 30
        expect = 34.0
        self.assertAlmostEqual(add(addend_x, addend_y), expect, delta=0.0001)

    def test_add_zero_addend(self):
        addend_x = 0
        addend_y = 30
        expect = 30
        self.assertEqual(add(addend_x, addend_y), expect)

    def test_add_addend_x_negative(self):
        addend_x = -4
        addend_y = 30
        expect = 26
        self.assertEqual(add(addend_x, addend_y), expect)

    def test_add_Decimal_number(self):
        inputs = Decimal('3.4'), Decimal('5.8')
        expect = Decimal('9.2')
        self.assertEqual(add(*inputs), expect)
