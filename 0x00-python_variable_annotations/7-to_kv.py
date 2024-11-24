#!/usr/bin/env python3
""" Complex annotation type module:
    string and int/float to tuple
"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function to return a tuple of str and int or float
        based on passed arguments
    """
    return (k, (v * v))
