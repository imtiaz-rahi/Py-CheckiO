# https://py.checkio.org/mission/min-max/publications/yukirin/python-3/second/?ordering=most_voted&filtering=choice
from functools import reduce


def abs_method(c):
    def f(*args, key=lambda x: x):
        if len(args) == 1: args = args[0]
        return reduce(lambda a, b: b if c(a[1], b[1]) else a, map(lambda x: (x, key(x)), args))[0]
    return f

min = abs_method(lambda a, b: a > b)
max = abs_method(lambda a, b: a < b)

if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
