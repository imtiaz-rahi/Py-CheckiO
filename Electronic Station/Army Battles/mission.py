# Taken from mission The Warriors


class Warrior:
    is_alive = True

    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    def take_hit(self, other):
        self.health -= other.attack
        self.is_alive = self.health > 0

    def __str__(self):
        return "H: " + str(self.health) + "; A: " + str(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(50, 7)


class Army:
    def __init__(self):
        self.force = {}

    def add_units(self, warrior: Warrior, count: int):
        self.force[warrior] = count


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.take_hit(unit_1)
        if unit_1.is_alive and not unit_2.is_alive:
            return True
        unit_1.take_hit(unit_2)
        if unit_1.is_alive and not unit_2.is_alive:
            return True
    return False


class Battle:

    def fight(self, me: Army, opponent: Army) -> bool:
        keys1 = iter(list(me.force.keys()))
        keys2 = iter(list(opponent.force.keys()))
        while bool(me.force) is True and bool(opponent.force) is True:
            who1 = next(keys1)
            # print(who1)
            in1 = who1()
            # print(in1)
            soldiers = me.force.pop(who1)
            # print(soldiers)
            who2 = next(keys2)
            enemies = opponent.force.pop(who2)
            # print(enemies)
            while soldiers > -1 and enemies > -1:
                no1won = fight(who1(), who2())
                if no1won is True:
                    enemies -= 1
                    if enemies == 0:
                        who2 = next(keys2, None)
                        enemies = -1 if who2 is None else opponent.force.pop(who2)
                else:
                    soldiers -= 1
                    if soldiers == 0:
                        who1 = next(keys1, None)
                        soldiers = -1 if who1 is None else me.force.pop(who1)
                print(soldiers)
                print(enemies)
                print()

        return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
