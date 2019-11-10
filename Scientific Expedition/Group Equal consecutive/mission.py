from itertools import groupby
group_equal = lambda data: list(list(it) for _, it in groupby(data))
