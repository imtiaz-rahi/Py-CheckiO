from itertools import groupby

def sum_consecutives(a):
    return [sum(v) for k,v in groupby(a)]
