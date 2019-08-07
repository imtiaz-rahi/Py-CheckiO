import calendar


def strip_leading_zero(val: str) -> str:
    return val[1:] if val.find("0") == 0 else val


def date_time(time: str) -> str:
    dt, tm = time.split(" ")
    day, mon, year = map(strip_leading_zero, dt.split("."))
    h, m = map(strip_leading_zero, tm.split(':'))
    h = h + " " + ("hour" if h == "1" else "hours")
    m = m + " " + ("minute" if m == "1" else "minutes")
    return f'{day} {calendar.month_name[int(mon)]} {year} year {h} {m}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute", "extra s problem"
    print("Coding complete? Click 'Check' to earn cool rewards!")
