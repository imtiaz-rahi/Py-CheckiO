# https://py.checkio.org/mission/dialogues/publications/sinclair2k/python-3/1001011/
from abc import ABCMeta, abstractmethod

VOWELS = "aeiou"


class Member(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.chat = None

    def setchat(self, chat):
        self.chat = chat

    def send(self, message):
        self.chat.recieve(self, message)

    @staticmethod
    @abstractmethod
    def encode(message):
        pass


class Chat:
    def __init__(self):
        self.messages = []

    def connect_human(self, member):
        member.setchat(self)

    def connect_robot(self, member):
        member.setchat(self)

    def recieve(self, sender, message):
        self.messages.append((sender.name, message))

    def show_dialogue(self, encoder):
        return '\n'.join([f'{name} said: {encoder(message)}' for name, message in self.messages])

    def show_robot_dialogue(self):
        return self.show_dialogue(Robot.encode)

    def show_human_dialogue(self):
        return self.show_dialogue(Human.encode)


class Human(Member):
    @staticmethod
    def encode(message):
        return message


class Robot(Member):
    @staticmethod
    def encode(message):
        return ''.join(['0' if c in VOWELS else '1' for c in message])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
