"""Complex list trigonometrics.
"""

import cmath


def sin(seq):
    """Calculate sine element-wise.

    Returns a list of complex numbers.
    """
    return [cmath.sin(x) for x in seq]


def cos(seq):
    """Calculate cosine element-wise.

    Returns a list of complex numbers.
    """
    return [cmath.cos(x) for x in seq]


def tan(seq):
    """Calculate tangent element-wise.

    Returns a list of complex numbers.
    """
    return [cmath.tan(x) for x in seq]


def cot(seq):
    """Calculate cotangent element-wise.

    Returns a list of complex numbers.
    """
    return [1 / cmath.tan(x) for x in seq]
