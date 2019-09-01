VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.messages = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, bot):
        bot.chat = self

    def show_human_dialogue(self):
        return self.show_dialogue(True)

    def show_robot_dialogue(self):
        return self.show_dialogue(False)

    def send(self, user, msg):
        self.messages.append([user.name, msg])

    def show_dialogue(self, is_human):
        result = ""
        for it in self.messages:
            result += f'{it[0]} said: {self.translate(it[1], is_human)}\n'
        return result[:len(result) - 1]

    def translate(self, val: str, is_human: bool) -> str:
        if is_human: return val
        is_vowel = lambda x: '0' if x in VOWELS else '1'
        return ''.join([is_vowel(ch) for ch in val])


class Participant:
    def __init__(self, name):
        self.name = name
        self.chat: Chat = None

    def send(self, msg):
        self.chat.send(self, msg)


class Human(Participant):
    pass


class Robot(Participant):
    pass


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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
