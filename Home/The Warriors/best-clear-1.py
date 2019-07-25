# https://py.checkio.org/mission/the-warriors/publications/przemyslaw.daniel/python-3/29-liner-no-looping-with-property
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    my_steps_to_die = unit_1.health // unit_2.attack
    enemy_steps_to_die = unit_2.health // unit_1.attack

    steps = min(my_steps_to_die, enemy_steps_to_die)
    steps -= my_steps_to_die == enemy_steps_to_die
    
    if my_steps_to_die >= enemy_steps_to_die:
        unit_1.health = unit_1.health-steps*unit_2.attack
        unit_2.health = 0
        return True

    unit_2.health = unit_2.health-steps*unit_1.attack
    unit_1.health = 0
    return False
