#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a
    float multiplier
    argument and returns a function that multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """return a function that multiplies a float"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
