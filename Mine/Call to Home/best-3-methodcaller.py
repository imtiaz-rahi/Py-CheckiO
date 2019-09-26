# https://py.checkio.org/mission/calls-home/publications/ciel/python-3/defaultdict
from collections import defaultdict
from operator import methodcaller
def total_cost(calls):
    d=defaultdict(int)
    for e in map(methodcaller('split'),calls): d[e[0]]+=(int(e[2])+59)//60
    return sum(e if e<100 else 100+2*(e-100) for e in d.values())
