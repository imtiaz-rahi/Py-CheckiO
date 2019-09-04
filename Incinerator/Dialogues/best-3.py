# https://py.checkio.org/mission/dialogues/publications/przemyslaw.daniel/python-3/26-liner-robot-human-alter-ego/
class Human:
    def __init__(self, name):
        self.chat, self.name = None, name

    def send(self, message):
        self.chat.history += [(self.name, message)]

Robot = Human

class Chat:
    def __init__(self):
        self.history, self.human, self.robot = [], None, None

    def connect_human(self, human):
        human.chat, self.human = self, human

    def connect_robot(self, robot):
        robot.chat, self.robot = self, robot

    def show_human_dialogue(self):
        return '\n'.join('%s said: %s' % (name, msg) for name, msg in self.history)

    def show_robot_dialogue(self):
        translate = lambda msg: ''.join('10'[c in 'aeiouAEIOU'] for c in msg)
        return '\n'.join('%s said: %s' % (name, translate(msg)) 
                         for name, msg in self.history)

