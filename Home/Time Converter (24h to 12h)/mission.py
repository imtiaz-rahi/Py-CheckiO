def time_converter(time):
    h, m = map(int, time.split(":"))
    suffix = "p.m." if h > 11 else "a.m."
    return f'{(h-1)%12+1}:{m:02d} {suffix}'
