# https://py.checkio.org/mission/dialogues/publications/veky/python-3/human-robot-interlocutor/
class Interlocutor(str):
    def send(who, message): who.active_chat.transcript.append((who, message))
Human = Robot = Interlocutor

onezero = lambda char: format(char.casefold() not in 'aeiou', 'b')
class Chat:
    def __init__(chat): chat.transcript = []
    def connect(chat, who): who.active_chat = chat
    connect_human = connect_robot = connect
    def show_human_dialogue(chat): return '\n'.join(chat.show_dialogue())
    def show_robot_dialogue(chat): return '\n'.join(chat.show_dialogue(onezero))
    def show_dialogue(chat, translation=lambda char: char):
        for who, line in chat.transcript:
            yield f"{who} said: " + ''.join(map(translation, line))

