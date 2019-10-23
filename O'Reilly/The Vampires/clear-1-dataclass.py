from dataclasses import dataclass
from collections import deque


@dataclass
class Warrior:
    health: int = 50
    attack: int = 5
    defense: int = int()
    vampirism: float = float()

    @property
    def is_alive(self): return self.health > 0

    def hit(self, other):
        damage = self.attack - other.defense
        if self.is_alive and damage > 0:
            other.health -= damage
            self.health += self.vampirism * damage


@dataclass
class Knight(Warrior):
    attack: int = 7


@dataclass
class Defender(Warrior):
    health: int = 60
    attack: int = 3
    defense: int = 2


@dataclass
class Vampire(Warrior):
    health: int = 40
    attack: int = 4
    vampirism: float = 50 / 100


def fight(first, second):
    while first.is_alive and second.is_alive:
        first.hit(second)
        second.hit(first)
    return first.is_alive


class Army(deque):
    def add_units(self, cls, n): self.extend(cls() for _ in range(n))


class Battle:
    @staticmethod
    def fight(*armies):
        while True:
            field = []
            for i, army in enumerate(armies):
                try:
                    field.append(army[0])
                except IndexError:
                    return i
            armies[fight(*field)].popleft()


if __name__ == '__main__':
    # fight tests
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

    # battle tests
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

    army_1 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)
    army_2 = Army()
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.fight(army_1, army_2) == False
    print("Coding complete? Let's try tests!")
