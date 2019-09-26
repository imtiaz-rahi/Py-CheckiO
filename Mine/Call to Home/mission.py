from math import ceil


def total_cost(calls):
    bill = lambda d: 100 + (d - 100) * 2 if d > 100 else d
    # List of call duration in minutes; [('2014-02-05', 1), ('2014-02-05', 2), ('2014-02-06', 3)]
    data = [(dt, ceil(int(dur) / 60)) for dt, tm, dur in (call.split() for call in calls)]
    # Sum each day call durations and calculate bill
    data = {uk: bill(sum(v for k, v in data if k == uk)) for uk in set(k for k, _ in data)}
    return sum(data.values())


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
    assert total_cost(["2057-01-01 00:00:00 7200",
                       "2057-01-01 03:00:00 7200",
                       "2057-01-01 06:00:00 7200",
                       "2057-01-01 09:00:00 7200",
                       "2057-01-01 12:00:00 7200",
                       "2057-01-01 15:00:00 7200",
                       "2057-01-01 18:00:00 7200",
                       "2057-01-01 21:00:00 7200",
                       "2057-01-01 23:10:00 7200"]) == 2060, "Edge test 5/5"
