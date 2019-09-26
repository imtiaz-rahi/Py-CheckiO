# https://py.checkio.org/mission/calls-home/publications/Sim0000/python-3/counter/
from collections import Counter

def total_cost(calls):
    db = Counter()
    for call in calls:
        day, time, duration = call.split()
        db[day] += (int(duration) + 59) // 60
    return sum(min if min < 100 else 2*min-100 for min in db.values())
