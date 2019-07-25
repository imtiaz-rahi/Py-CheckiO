# https://py.checkio.org/mission/the-warriors/publications/s1337/python-3/first/
class Warrior:
    
    def __init__(self):
        self.attack =  5
        self.health = 50

    @property
    def is_alive(self):
        return self.health > 0

    def decrease_health(self, damage):
        self.health -= damage

class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    
    attacker, victim = unit_1, unit_2

    while (attacker.is_alive and victim.is_alive): 
        victim.decrease_health(attacker.attack)
        victim, attacker = attacker, victim
    
    return unit_1.is_alive
