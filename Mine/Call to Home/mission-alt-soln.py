# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
def total_cost(calls):
    data = {}
    for call in calls:
        dt, _, dur = call.split()
        # Python integers division ceil when one of the operands is negative
        data[dt] = data.get(dt, 0) + abs(int(dur)//-60)
    return sum(max(d * 2 - 100, d) for d in data.values())


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
