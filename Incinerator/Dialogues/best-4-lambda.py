# https://py.checkio.org/mission/dialogues/publications/fed.kz/python-3/first/
VOWELS = 'aeiouAEIOU'
RCHAT = []
HCHAT = []

class Chat:
    RCHAT.clear(); HCHAT.clear()
    connect_human = connect_robot = lambda *_: None
    show_human_dialogue = lambda *_: show(HCHAT)
    show_robot_dialogue = lambda *_: show(RCHAT)

class Human:
    
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        HCHAT.append(f'{self.name} said: {msg}')
        RCHAT.append(f'{self.name} said: {encode(msg)}')
Robot = Human

def show(chat): return '\n'.join(chat)
def encode(msg): return ''.join('0' if char in VOWELS else '1' for char in msg)

