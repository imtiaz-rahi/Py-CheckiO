# https://py.checkio.org/mission/min-max/publications/martin_b/python-3/clear/?ordering=most_voted&filtering=choice
import operator


def min_max(c, *args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    i = iter(args if len(args) > 1 else args[0])
    m = next(i)
    for e in i:
        if c(key(e), key(m)):
            m = e
    return m


def min(*args, **kwargs):
    return min_max(operator.lt, *args, **kwargs)


def max(*args, **kwargs):
    return min_max(operator.gt, *args, **kwargs)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
