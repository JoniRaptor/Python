"""List arithmetics.
"""

__all__ = ['add', 'sub', 'mul', 'div']


def add(seq1, seq2):
    """Add two sequences element-wise.

    Returns a list.
    """
    return [x + y for x, y in zip(seq1, seq2)]


def sub(seq1, seq2):
    """Subtract two sequences element-wise.

    Returns a list.
    """
    return [x - y for x, y in zip(seq1, seq2)]


def mul(seq1, seq2):
    """Multiply two sequences element-wise.

    Returns a list.
    """
    return [x * y for x, y in zip(seq1, seq2)]


def div(seq1, seq2):
    """Divide two sequences element-wise.

    Returns a list.
    """
    return [x / y for x, y in zip(seq1, seq2)]
