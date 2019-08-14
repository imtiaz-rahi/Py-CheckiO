# https://py.checkio.org/mission/date-and-time-converter/publications/flpo/python-3/the-art-of-the-metaobject-pluralization
from datetime import datetime

def checkio(dt):
    dt = datetime.strptime(dt, '%d.%m.%Y %H:%M')
    p = lambda attr: attr + 's' * (getattr(dt, attr) != 1)
    return dt.strftime(f'%-d %B %Y year %-H {p("hour")} %-M {p("minute")}')

