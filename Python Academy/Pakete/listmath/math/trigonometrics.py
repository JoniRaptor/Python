"""List trigonometrics.
"""

__all__ = ['sin', 'cos', 'tan', 'cot']

import math


def sin(seq):
    """Calculate sine element-wise.

    Returns a list.
    """
    return [math.sin(x) for x in seq]


def cos(seq):
    """Calculate cosine element-wise.

    Returns a list.
    """
    return [math.cos(x) for x in seq]


def tan(seq):
    """Calculate tangent element-wise.

    Returns a list.
    """
    return [math.tan(x) for x in seq]


def cot(seq):
    """Calculate cotangent element-wise.

    Returns a list.
    """
    return [1 / math.tan(x) for x in seq]
