# https://py.checkio.org/mission/the-warriors/publications/xavier-b/python-3/first/?ordering=most_voted&filtering=all
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health >= 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive
