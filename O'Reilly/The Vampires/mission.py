# Taken from mission The Defenders

class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self):
        return "H: " + str(self.health) + "; A: " + str(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(50, 7, 0)


class Defender(Warrior):
    def __init__(self):
        super().__init__(60, 3, 2)


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, warrior: Warrior, count: int):
        self.soldiers += [warrior() for _ in range(count)]

    @property
    def is_alive(self) -> bool:
        """Does the army have a living warrior?"""
        return self.soldiers != []

    @property
    def soldier(self) -> Warrior:
        """First warrior alive of the army"""
        return self.soldiers[0]

    @property
    def pop(self):
        """Pop a dead warrior out of the list"""
        self.soldiers.pop(0)


def fight(unit_1, unit_2):
    """Duel fight: is unit 1 stronger than unit 2 ?"""
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.attack > unit_2.defense:
            unit_2.health -= unit_1.attack - unit_2.defense
        if unit_2.attack > unit_1.defense:
            unit_1.health -= (unit_2.attack - unit_1.defense) if unit_2.is_alive else 0
    return unit_1.is_alive


class Battle:

    def fight(self, army: Army, enemy: Army) -> bool:
        while army.is_alive and enemy.is_alive:
            if fight(army.soldier, enemy.soldier):
                enemy.soldiers.pop(0)
            else:
                army.soldiers.pop(0)
        return army.is_alive


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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")