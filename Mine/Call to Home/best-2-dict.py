# https://py.checkio.org/mission/calls-home/publications/saklar13/python-3/first/
def total_cost(calls):
    days = {}
    for call in calls:
        day, _, duration = call.split()
        duration = (int(duration) + 59) // 60
        days[day] = days.get(day, 0) + duration
    return sum(max(x, x*2 - 100) for x in days.values())
