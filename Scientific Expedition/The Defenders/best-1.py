# https://py.checkio.org/mission/the-defenders/publications/Moff/python-3/first/
class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        other.loss(self.attack)

    def loss(self, attack):
        self.health -= attack


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)


def fight(unit_1, unit_2):
    while 1:
        unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1)
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    @property
    def is_alive(self):
        return self.first_alive_unit is not None


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.first_alive_unit, army_2.first_alive_unit)
        return army_1.is_alive

