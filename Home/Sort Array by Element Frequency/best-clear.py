# https://py.checkio.org/mission/sort-array-by-element-frequency/publications/flpo/python-3/-itemscountx-itemsindexx/
def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
