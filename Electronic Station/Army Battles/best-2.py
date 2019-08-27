# https://py.checkio.org/mission/army-battles/publications/Phil15/python-3/army-with-3-properties-is_alive-warrior-pop/
class Warrior:
    """Define a warrior."""
    def __init__(self):
        self.health = 50
        self.attack = 5
    @property
    def is_alive(self) -> bool:
        return self.health > 0

class Knight(Warrior):
    """Define a knight, it's a warrior with an increased attack of 7."""
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2) -> bool:
    """Duel fight...
    Is unit_1 stronger than unit_2?"""
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        unit_1.health -= unit_2.attack if unit_2.is_alive else 0
    return unit_1.is_alive

class Army:
    """Define an army."""
    def __init__(self):
        """An empty army for start."""
        self.list = []
    def add_units(self, unit, amount_of_units):
        """Add an amount of specific units to the army."""
        self.list += [unit() for k in range(amount_of_units)]
    @property
    def is_alive(self) -> bool:
        """Does the army have a living warrior?"""
        return self.list != []
    @property
    def warrior(self):
        """First warrior alive of the army."""
        return self.list[0]
    @property
    def pop(self):
        """Pop a dead warrior out of the list."""
        self.list.pop(0)
        
class Battle:
    def fight(self, army_1, army_2) -> bool:
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.warrior, army_2.warrior):
                army_2.pop
            else:
                army_1.pop
        return army_1.is_alive

