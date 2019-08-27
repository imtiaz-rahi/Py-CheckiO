class MicrowaveBase:
    def __init__(self):
        self.seconds = 0


class Microwave1(MicrowaveBase):
    pass


class Microwave2(MicrowaveBase):
    pass


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave
    
    def set_time(self, time):
        mm, ss = map(int, time.split(':'))
        self.microwave.seconds = 60 * mm + ss
    
    def add_time(self, time):
        seconds, token = int(time[:-1]), time[-1]
        if token == 'm':
            seconds *= 60
        self.microwave.seconds = min(5400, self.microwave.seconds + seconds)
    
    def del_time(self, time):
        seconds, token = int(time[:-1]), time[-1]
        if token == 'm':
            seconds *= 60
        self.microwave.seconds = max(0, self.microwave.seconds - seconds)
    
    def show_time(self):
        mm, ss = divmod(self.microwave.seconds, 60)
        time = f'{mm:02d}:{ss:02d}'
        if isinstance(self.microwave, Microwave1):
            return '_' + time[1:]
        if isinstance(self.microwave, Microwave2):
            return time[:-1] + '_'
        return time

