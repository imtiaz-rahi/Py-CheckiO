def lesser(v1, v2):
    return v1 < v2


def greater(v1, v2):
    return v1 > v2


def find_min_max(comparator, *args, **kwargs):
    args = list(args[0]) if len(args) == 1 else args
    key = kwargs.get("key", lambda x: x)
    res = None
    for item in args:
        if res is None or comparator(key(item), key(res)):
            res = item
    return res


min = lambda *args, **kwargs: find_min_max(lesser, *args, **kwargs)
max = lambda *args, **kwargs: find_min_max(greater, *args, **kwargs)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
