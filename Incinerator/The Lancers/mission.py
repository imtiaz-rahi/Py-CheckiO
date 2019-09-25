# Taken from mission The Vampires

class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def loose_health(self, damage):
        self.health -= max(damage - self.defense, 0)

    def hit(self, victim):
        victim.loose_health(self.attack)

    @property
    def type(self) -> str:
        return self.__class__.__name__

    def __str__(self):
        return self.type + "; H: " + str(self.health) + "; A: " + str(self.attack) + ";\n"


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.healing = 50

    def hit(self, victim):
        """Vampire gains health (healing value in %) based on damage dealt to his victim"""
        victim.loose_health(self.attack)
        gained_health = self.health + ((self.attack - victim.defense) * self.healing // 100)
        self.health = min(gained_health, 40)


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, warrior, count: int):
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

    def __str__(self):
        return "Total: " + str(len(self.soldiers)) + "\n" + "".join(unit.__str__() for unit in self.soldiers)


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    """Each unit hit each other in turn"""
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
