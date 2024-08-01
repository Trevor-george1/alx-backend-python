#!/usr/bin/env python3
"""Write a type-annotated function to_kv that
    takes a string k and an int OR float v
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns atuple of the string"""
    return (k, float(v * v))
