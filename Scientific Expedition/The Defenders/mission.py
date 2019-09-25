class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def loose_health(self, damage):
        self.health -= damage

    def hit(self, victim):
        victim.loose_health(self.attack)

    def __str__(self):
        return "H: " + str(self.health) + "; A: " + str(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def loose_health(self, damage):
        super().loose_health(max(damage - self.defense, 0))


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, warrior: Warrior, count: int):
        self.soldiers += [warrior() for _ in range(count)]

    @property
    def has_live_unit(self) -> bool:
        """Does the army has a living warrior?"""
        return bool(self.next_soldier())

    def next_soldier(self) -> Warrior:
        """Return the first alive soldier"""
        for unit in self.soldiers:
            if unit.is_alive: return unit
        return None


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    bully, victim = unit_1, unit_2
    while True:
        bully.hit(victim)
        if not victim.is_alive: break
        bully, victim = victim, bully
    return unit_1.is_alive


class Battle:
    @staticmethod
    def fight(army1: Army, army2: Army) -> bool:
        while army1.has_live_unit and army2.has_live_unit:
            fight(army1.next_soldier(), army2.next_soldier())
        return army1.has_live_unit


if __name__ == '__main__':
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
