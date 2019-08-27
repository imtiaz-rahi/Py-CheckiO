# https://py.checkio.org/mission/microwave-ovens/publications/flpo/python-3/make_broken-getattr/?ordering=most_voted&filtering=all
def time_seconds(time):
    return int(time[:-1]) if time.endswith('s') else int(time[:-1]) * 60


class MicrowaveBase(object):
    def __init__(self):
        self.time = 0

    def set_time(self, time):
        m, s = map(int, time.split(':'))
        self.time = min(5400, (m * 60 + s))

    def add_time(self, time):
        self.time = min(5400, self.time + time_seconds(time))

    def del_time(self, time):
        self.time = max(0, self.time - time_seconds(time))

    def show_time(self):
        return '{:02d}:{:02d}'.format(*divmod(self.time, 60))


def make_broken(i):
    class Broken(MicrowaveBase):
        def show_time(self):
            time = super(Broken, self).show_time()
            return time[:i] + '_' + time[i+1:]
    return Broken


Microwave1, Microwave2, Microwave3 = make_broken(0), make_broken(4), MicrowaveBase


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def __getattr__(self, attr):
        return getattr(self.microwave, attr)
