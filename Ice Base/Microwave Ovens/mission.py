class MicrowaveBase:
    def __init__(self, pos=-99):
        self.problem = pos


class Microwave1(MicrowaveBase):
    def __init__(self):
        super().__init__(0)


class Microwave2(MicrowaveBase):
    def __init__(self):
        super().__init__(-1)


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, microwave: MicrowaveBase):
        self.microwave = microwave
        self.timer = 0

    def set_time(self, time_str: str):
        h, m = map(int, time_str.split(':'))
        self.timer = h * 60 + m

    def add_time(self, time_str):
        m_s, time = (time_str[-1], int(time_str[:-1]))
        self.timer += time if m_s == "s" else time * 60
        if self.timer > 5400: self.timer = 5400

    def del_time(self, time_str):
        if self.timer > 0:
            m_s, time = (time_str[-1], int(time_str[:-1]))
            self.timer -= time if m_s == "s" else time * 60

    def show_time(self):
        rs = f'{self.timer//60:02}:{self.timer%60:02}'
        if self.microwave.problem != -99:
            ar = list(rs)
            ar[self.microwave.problem] = "_"
            rs = ''.join(ar)
        return rs


if __name__ == '__main__':
    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
