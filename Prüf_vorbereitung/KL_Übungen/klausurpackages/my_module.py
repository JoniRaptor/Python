"""Fkt aus KL_Aufgaben"""

# Aufgabe 1


def read_file(file_name):
    """Read collums into two lists of floats"""
    xs = []
    ys = []
    with open(file_name) as fobj:
        next(fobj)
        for line in fobj:
            if line.strip():
                x, y = [float(value) for value in line.split(', ')]
                xs.append(x)
                ys.append(y)
        return xs, ys

# Aufgabe 2


def read_file2(file_name):
    """Read collums into dict of floats

    first line represents the keys of the dict
    """
    with open(file_name) as fobj:
        header = next(fobj).strip('\n')
        keys = header.split(', ')
        table = {key: [] for key in keys}
        for line in fobj:
            if line.strip():
                for key, value in zip(keys, line.split(', ')):
                    table[key].append(float(value))
        return table

# Aufgabe 3


def sum_lists(L1, L2):
    """creates Sum of collum of a of two float lists
    returns a tuple"""
    return sum(L1), sum(L2)


def sum_dict(dic):
    """creates sum for numerical List in every key of a dict
    returns a tuple"""
    keys = dic.keys()
    L = []
    zaehler = 0
    for key in keys:
        L.append(0)
        for value in dic[key]:
            L[zaehler] += value
        zaehler += 1
    return tuple(L)


def sum_dict_better(dic):
    """better version of sum_dict"""
    return tuple(sum(value) for value in dic.values())
