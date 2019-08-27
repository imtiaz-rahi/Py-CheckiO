# https://py.checkio.org/mission/army-battles/publications/martin.pilka/python-3/army_1unitspop0/
class Warrior:
    """
    Class Warrior, the instances of which will have 2 parameters - health (equal to 50 points) and
    attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0)
    or False (in the other case).
    """

    def __init__(self, health: int = 50, attack: int = 5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def fight(self, enemy):
        """
        Every turn one of the warriors will hit another one and the last will lose his health in the same
        value as the attack of the first warrior. After that, the second warrior will do the same to the
        first one. If in the end of the turn the first warrior has > 0 health and the other one doesn’t,
        the function should return True, in the other case it should return False.
        """
        while True:
            # we attack
            enemy.health -= self.attack
            if enemy.health <= 0:
                return True

            # enemy attacks
            self.health -= enemy.attack
            if self.health <= 0:
                return False


class Knight(Warrior):
    """Knight, which should be the subclass of the Warrior but have the increased attack - 7."""

    def __init__(self, health: int = 50, attack: int = 7):
        super().__init__(health, attack)


class Army:
    """
    The new class should be the Army and have the method add_units() - for adding the chosen amount of
    units to the army.
    """

    def __init__(self):
        self.units = []

    def add_units(self, unit, n):
        self.units.extend([unit() for _ in range(n)])


class Battle:
    """
    Also you need to create a Battle() class with a fight() function, which will
    determine the strongest army.
    """

    def fight(self, army_1: Army, army_2: Army) -> bool:
        """
        The battles occur according to the following principles:
        at first, there is a duel between the first warrior of the first army and the first warrior of
        the second army. As soon as one of them dies - the next warrior from the army that lost the
        fighter enters the duel, and the surviving warrior continues to fight with his current health.
        This continues until all the soldiers of one of the armies die. In this case, the battle()
        function should return True, if the first army won, or False, if the second one was stronger.
        Note that army 1 have the advantage to start every fight!
        """
        warrior_1 = army_1.units[0] if len(army_1.units) > 0 else None
        warrior_2 = army_2.units[0] if len(army_2.units) > 0 else None
        while warrior_1 and warrior_2:
            if warrior_1.fight(warrior_2):
                army_2.units.pop(0)
                warrior_2 = army_2.units[0] if len(army_2.units) > 0 else None
            else:
                army_1.units.pop(0)
                warrior_1 = army_1.units[0] if len(army_1.units) > 0 else None

        return warrior_1 is not None


def fight(unit_1: Warrior, unit_2: Warrior):
    return unit_1.fight(unit_2)

