"""Complex list arithmetics.

Results are always complex numbers.
"""

__all__ = ['add', 'sub', 'mul', 'div']

import listmath.math.arithmetics as arith


def add(seq1, seq2):
    """Add two sequences element-wise.

    Returns a list of complex numbers.
    """
    return [complex(x) for x in arith.add(seq1, seq2)]


def sub(seq1, seq2):
    """Subtract two sequences element-wise.

    Returns a list of complex numbers.
    """
    return [complex(x) for x in arith.sub(seq1, seq2)]


def mul(seq1, seq2):
    """Multiply two sequences element-wise.

    Returns a list of complex numbers.
    """
    return [complex(x) for x in arith.mul(seq1, seq2)]


def div(seq1, seq2):
    """Divide two sequences element-wise.

    Returns a list of complex numbers.
    """
    return [complex(x) for x in arith.div(seq1, seq2)]
