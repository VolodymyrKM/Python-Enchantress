from typing import Union


def add(addend_x: Union[int, float], addend_y: Union[int, float]):
    """Add Function"""
    return addend_x + addend_y


def subtract(minuend: Union[int, float], subtrahend: Union[int, float]):
    """Subtract Function"""
    return minuend - subtrahend


def multiply(factor_x: Union[int, float], factor_y: Union[int, float]):
    """Multiply Function"""
    return factor_x * factor_y


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    """Divide Function"""
    if divisor == 0:
        raise ValueError('Can not divide by zero!')
    return dividend / divisor
