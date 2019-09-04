# https://py.checkio.org/mission/dialogues/publications/flpo/python-3/human-robot/
from operator import add
from itertools import starmap

def robot_language(text):
    return ''.join('0' if c in 'aeiouAEIOU' else '1' for c in text)

class Chat(list):
    def connect(self, chatter):
        chatter.chat = self

    connect_human = connect_robot = connect

    def show_human_dialogue(self):
        return '\n'.join(starmap(add, self))

    def show_robot_dialogue(self):
        return '\n'.join(chatter + robot_language(text) for chatter, text in self)

class Robot:
    def __init__(self, name):
        self.name, self.chat = name, []
        
    def send(self, text):
        self.chat.append((f'{self.name} said: ', text))

Human = Robot

