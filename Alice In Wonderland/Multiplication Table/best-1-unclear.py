# https://py.checkio.org/mission/multiplication-table/publications/pohmelie/python-3/first/
from itertools import repeat
from functools import reduce
from operator import and_, or_, xor


def checkio(f, s):
    res = 0
    while f:
        for op in (and_, or_, xor):
            res += op(s, ((1 << s.bit_length()) - 1) * (f & 1))
        f >>= 1
    return res
