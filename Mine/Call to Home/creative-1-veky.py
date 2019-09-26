# https://py.checkio.org/mission/calls-home/publications/veky/python-3/deceptive/
def total_cost(calls):
    acc = __import__('collections').Counter()
    for d, _, s in map(str.split, calls): acc[d] -= -int(s)//60
    return sum(m + max(m - 100, 0) for m in acc.values())
