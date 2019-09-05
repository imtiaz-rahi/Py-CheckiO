# https://py.checkio.org/mission/multiplication-table/publications/bryukh/python-3/and-or-xor/
AND = lambda x, y: int(x) and int(y)
OR = lambda x, y: int(x) or int(y)
XOR = lambda x, y: int(x) ^ int(y)

def sum_table(first, second, func):
    """
    Use func for each to each digits, then convert it in the decimal and sum they
    """
    return sum(int("".join(str(func(f, s)) for s in second), 2) for f in first)

def checkio(first, second):
    """
    Weird multiplication
    """
    # convert in the binary form
    f, s = bin(first)[2:], bin(second)[2:]
    # send function as argument
    return sum_table(f, s, AND) + sum_table(f, s, OR) + sum_table(f, s, XOR)
