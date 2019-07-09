def time_converter(time):
    ar = time.split(":")
    hour = 0 if ar[0] == "00" else int(ar[0].lstrip("0"))
    suffix = " a.m." if hour < 12 else " p.m."
    if hour == 0: hour = 12
    if hour > 12: hour %= 12
    return str(hour) + ":" + ar[1] + suffix


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('00:00') == '12:00 a.m.'
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('11:55') == '11:55 a.m.'
    assert time_converter('07:10') == '7:10 a.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
