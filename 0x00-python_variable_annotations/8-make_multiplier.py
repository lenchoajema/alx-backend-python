#!/usr/bin/env python3
""" Complex annotations module: functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that returns a function that multiplies
    a float by multiplier
    """

    def multiply(num: float) -> float:
        """ Callback to multiply num with multiplier """
        return num * multiplier

    return multiply
