# https://py.checkio.org/mission/sort-array-by-element-frequency/publications/tokyoamado/python-3/countermost_common
from collections import Counter
from itertools import repeat

def frequency_sort(items):
    return [x for y in (repeat(*x) for x in Counter(items).most_common()) for x in y]

# list(chain.from_iterable(repeat(*x) for x in Counter(items).most_common()))

