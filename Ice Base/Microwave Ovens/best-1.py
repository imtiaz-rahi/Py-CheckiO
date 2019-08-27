# https://py.checkio.org/mission/microwave-ovens/publications/veky/python-3/reheated/
import datetime

class MicrowaveBase: pass
class Microwave1(MicrowaveBase): faulty = {0}
class Microwave2(MicrowaveBase): faulty = {4}
class Microwave3(MicrowaveBase): faulty = set()

def clip(seconds): return min(90*60, max(0, seconds))

class RemoteControl:
    def __init__(self, mwave):
        self.faulty = mwave.faulty
        self.time = 0

    def set_time(self, timestr):
        m, s = map(int, timestr.split(':'))
        self.time = clip(60*m + s)
        
    def add_time(self, timestr):
        delta = int(timestr[:~0]) * dict(m=60, s=1)[timestr[~0]]
        self.time = clip(self.time + delta)
    
    def del_time(self, timestr): self.add_time('-' + timestr)
    
    def show_time(self):
        minutes, seconds = divmod(self.time, 60)
        display = list(f'{minutes:02}:{seconds:02}')
        for digit in self.faulty: display[digit] = '_'
        return ''.join(display)

